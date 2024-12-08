from aiortc.contrib.media import MediaRecorder, MediaPlayer
from aiortc.mediastreams import MediaStreamTrack
import platform
import time
import av
import sys
from fractions import Fraction
from typing import Any

time_base = Fraction(1, 1000000)


def get_size():
    if "--res=1080p" in sys.argv:
        return (1920, 1080)
    elif "--res=720p" in sys.argv:
        return (1280, 720)
    elif "--res=270p" in sys.argv:
        return (480, 270)

    return (640, 360)


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
        return MediaPlayer("/dev/video0", format="v4l2", options=options).video


class PiCameraTrack(MediaStreamTrack):
    kind = "video"
    cam: Any

    def __init__(self, cam: Any):
        super().__init__()
        self.cam = cam

    async def recv(self):

        img = self.cam.capture_array("lores")  # type: ignore

        pts = time.time() * 1000000
        new_frame = av.VideoFrame.from_ndarray(img, format="yuv420p")  # type: ignore
        new_frame.pts = int(pts)
        new_frame.time_base = time_base
        return new_frame
