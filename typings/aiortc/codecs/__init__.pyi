"""
This type stub file was generated by pyright.
"""

from typing import Dict, List, Optional, Union
from ..rtcrtpparameters import ParametersDict, RTCRtcpFeedback, RTCRtpCapabilities, RTCRtpCodecCapability, RTCRtpCodecParameters, RTCRtpHeaderExtensionCapability, RTCRtpHeaderExtensionParameters
from .base import Decoder, Encoder
from .g711 import PcmaDecoder, PcmaEncoder, PcmuDecoder, PcmuEncoder
from .h264 import H264Decoder, H264Encoder, h264_depayload
from .opus import OpusDecoder, OpusEncoder
from .vpx import Vp8Decoder, Vp8Encoder, vp8_depayload

PCMU_CODEC = ...
PCMA_CODEC = ...
CODECS: Dict[str, List[RTCRtpCodecParameters]] = ...
HEADER_EXTENSIONS: Dict[str, List[RTCRtpHeaderExtensionParameters]] = ...
def init_codecs() -> None:
    ...

def depayload(codec: RTCRtpCodecParameters, payload: bytes) -> bytes:
    ...

def get_capabilities(kind: str) -> RTCRtpCapabilities:
    ...

def get_decoder(codec: RTCRtpCodecParameters) -> Decoder:
    ...

def get_encoder(codec: RTCRtpCodecParameters) -> Encoder:
    ...

def is_rtx(codec: Union[RTCRtpCodecCapability, RTCRtpCodecParameters]) -> bool:
    ...

