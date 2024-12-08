"""
This type stub file was generated by pyright.
"""

from typing import List, Tuple
from av.frame import Frame
from av.packet import Packet
from ..jitterbuffer import JitterFrame
from .base import Decoder, Encoder

CHANNELS = ...
SAMPLE_RATE = ...
SAMPLE_WIDTH = ...
SAMPLES_PER_FRAME = ...
TIME_BASE = ...
class OpusDecoder(Decoder):
    def __init__(self) -> None:
        ...
    
    def __del__(self) -> None:
        ...
    
    def decode(self, encoded_frame: JitterFrame) -> List[Frame]:
        ...
    


class OpusEncoder(Encoder):
    def __init__(self) -> None:
        ...
    
    def __del__(self) -> None:
        ...
    
    def encode(self, frame: Frame, force_keyframe: bool = ...) -> Tuple[List[bytes], int]:
        ...
    
    def pack(self, packet: Packet) -> Tuple[List[bytes], int]:
        ...
    

