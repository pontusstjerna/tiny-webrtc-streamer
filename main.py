import paho.mqtt.client as mqtt
from typing import Any
from paho.mqtt.reasoncodes import ReasonCode
from paho.mqtt.properties import Properties
import os
from dotenv import load_dotenv
from aiortc.rtcpeerconnection import RTCPeerConnection
from aiortc.mediastreams import MediaStreamTrack
import requests
import json
from utils import (
    create_webcam_video_track,
    get_size,
    PiCameraTrack,
)
import asyncio

load_dotenv()

MQTT_BROKER_URL: str = os.getenv("MQTT_BROKER_URL") or ""
MQTT_USER: str = os.getenv("MQTT_USER") or ""
MQTT_PASSWORD: str = os.getenv("MQTT_PASSWORD") or ""
VIDEO_SOURCE: str = os.getenv("VIDEO_SOURCE") or "anynomous_camera"
BACKEND_BASE_URL: str = os.getenv("BACKEND_BASE_URL") or "https://nocroft.se/api"
VIDEO_ANSWER_ENDPOINT: str = f"{BACKEND_BASE_URL}/video_answer/{VIDEO_SOURCE}"
VIDEO_ANSWER_SECRET: str = os.getenv("VIDEO_ANSWER_SECRET") or ""

has_picamera2 = False
active_track: MediaStreamTrack | None = None


try:
    from picamera2 import Picamera2  # type: ignore
    from picamera2.encoders import H264Encoder, Quality  # type: ignore
    from picamera2.outputs import FfmpegOutput  # type: ignore

    has_picamera2 = True
except ModuleNotFoundError:
    print("Could not find picamera2 library, will use webcam instead!")

if has_picamera2:
    cam: Picamera2  # type: ignore
    encoder: H264Encoder  # type: ignore
recording = False


def setup_and_start_picamera():
    print("Setting up Picamera")
    global cam, encoder
    cam = Picamera2()  # type: ignore
    encoder = H264Encoder(1000000)  # type: ignore
    size = get_size()

    config: Any = cam.create_video_configuration(  # type: ignore
        main={"size": (1920, 1080)},
        lores={"size": size, "format": "YUV420"},
        encode="lores",
    )
    cam.configure(config)  # type: ignore
    cam.start()  # type: ignore


def on_connect(
    client: mqtt.Client,
    userdata: Any,
    flags: mqtt.ConnectFlags,
    reason_code: ReasonCode,
    properties: Properties | None,
):
    print(f"Subscribed to MQTT at {MQTT_BROKER_URL}")
    client.subscribe("$$SYS/#")
    client.subscribe(f"/video/client_offers/{VIDEO_SOURCE}")


def on_message(
    client: mqtt.Client, userdata: dict[str, Any], message: mqtt.MQTTMessage
):
    str_message = str(message.payload, "utf-8")
    if message.topic == f"/video/client_offers/{VIDEO_SOURCE}":
        print(f"Got video offer!")
        offer = json.loads(str_message)
        answer = asyncio.run(create_answer(offer))
        print(f"Returning video answer for source '{VIDEO_SOURCE}'")
        post_answer(answer)


async def create_answer(offer: Any) -> dict[str, Any]:
    peer_connection: Any = RTCPeerConnection()

    @peer_connection.on("connectionstatechange")
    async def _():
        print(f"Connection state is {peer_connection.connectionState}")
        if peer_connection.connectionState == "failed":
            await peer_connection.close()

    global active_track, cam
    if has_picamera2:
        active_track = PiCameraTrack(cam)  # type: ignore
    else:
        active_track = create_webcam_video_track()

    peer_connection.addTrack(active_track)

    await peer_connection.setRemoteDescription(offer)
    answer = await peer_connection.createAnswer()
    await peer_connection.setLocalDescription(answer)
    return {
        "sdp": peer_connection.localDescription.sdp,
        "type": peer_connection.localDescription.type,
    }


def post_answer(answer: dict[str, Any]):
    requests.post(
        VIDEO_ANSWER_ENDPOINT,
        json.dumps({"secret": VIDEO_ANSWER_SECRET, "answer": answer}),
    )


mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)  # type: ignore
mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
mqtt_client.connect(MQTT_BROKER_URL)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

try:
    print(f"Registering video source {VIDEO_SOURCE} to {BACKEND_BASE_URL}")
    response = requests.post(
        f"{BACKEND_BASE_URL}/register_video_source",
        json.dumps({"secret": VIDEO_ANSWER_SECRET, "source": VIDEO_SOURCE}),
    )
    if not response.ok:
        raise Exception(f"{response.status_code}")
except Exception as e:
    print(f"Failed to register video source: {e}")
    exit(-1)

mqtt_client.loop_forever()
