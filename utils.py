from aiortc.contrib.media import MediaRecorder, MediaPlayer
from aiortc.mediastreams import MediaStreamTrack
import platform
import time
import av
from av.video.frame import VideoFrame
import sys
from fractions import Fraction
from typing import Any, Iterator
import asyncio
import av.container


time_base = Fraction(1, 1000000)


def get_size():
    if "--res=1080p" in sys.argv:
        return (1920, 1080)
    elif "--res=720p" in sys.argv:
        return (1280, 720)
    elif "--res=270p" in sys.argv:
        return (480, 270)
    elif "--res=320p" in sys.argv:
        return (320, 240)

    return (640, 480)


def create_webcam_video_track() -> MediaStreamTrack:
    size = get_size()
    options = {"framerate": "30", "video_size": f"{size[0]}x{size[1]}"}

    if platform.system() == "Darwin":
        return MediaPlayer("default:none", format="avfoundation", options=options).video
    elif platform.system() == "Windows":
        return MediaPlayer(
            "video=Integrated Camera", format="dshow", options=options
        ).video
    else:
        return WebcamStreamTrack()


class PiCameraTrack(MediaStreamTrack):
    kind = "video"
    cam: Any

    def __init__(self, cam: Any):
        super().__init__()
        self.cam = cam

    async def recv(self):

        img = self.cam.capture_array("lores")  # type: ignore

        pts = time.time() * 1000000
        new_frame = VideoFrame.from_ndarray(img, format="yuv420p")  # type: ignore
        new_frame.pts = int(pts)
        new_frame.time_base = time_base
        return new_frame


class WebcamStreamTrack(MediaStreamTrack):
    kind = "video"
    frame_iter: Iterator[VideoFrame]
    frame = None
    task = None

    def __init__(self):
        super().__init__()

        size = get_size()

        container = av.container.open(
            "/dev/video0",
            format="v4l2",
            options={
                "framerate": "5",
                "video_size": f"{size[0]}x{size[1]}",
                "hwaccel": "auto",
                "pix_fmt": "yuv420p",
            },
        )
        stream = container.streams.video[0]
        self.frame_iter = container.decode(stream)

    async def get_frame(self):
        for frame in self.frame_iter:
            # frame = frame.reformat(width=160, height=120)
            frame.time_base = time_base
            self.frame = frame
            await asyncio.sleep(0.001)

    async def recv(self):
        if not self.task:
            self.task = asyncio.create_task(self.get_frame())

        while self.frame == None:
            await asyncio.sleep(0.01)

        frame = self.frame
        pts = time.time() * 1000000
        frame.pts = int(pts)
        return frame
