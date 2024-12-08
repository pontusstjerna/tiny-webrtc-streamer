"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import Any, List, Optional, Tuple, Union
from av import AudioFrame
from .rtcrtpparameters import RTCRtpParameters

RTP_HISTORY_SIZE = ...
FORBIDDEN_PAYLOAD_TYPES = ...
DYNAMIC_PAYLOAD_TYPES = ...
RTP_HEADER_LENGTH = ...
RTCP_HEADER_LENGTH = ...
PACKETS_LOST_MIN = ...
PACKETS_LOST_MAX = ...
RTCP_SR = ...
RTCP_RR = ...
RTCP_SDES = ...
RTCP_BYE = ...
RTCP_RTPFB = ...
RTCP_PSFB = ...
RTCP_RTPFB_NACK = ...
RTCP_PSFB_PLI = ...
RTCP_PSFB_SLI = ...
RTCP_PSFB_RPSI = ...
RTCP_PSFB_APP = ...
@dataclass
class HeaderExtensions:
    abs_send_time: Optional[int] = ...
    audio_level: Any = ...
    mid: Any = ...
    repaired_rtp_stream_id: Any = ...
    rtp_stream_id: Any = ...
    transmission_offset: Optional[int] = ...
    transport_sequence_number: Optional[int] = ...


class HeaderExtensionsMap:
    def __init__(self) -> None:
        ...
    
    def configure(self, parameters: RTCRtpParameters) -> None:
        ...
    
    def get(self, extension_profile: int, extension_value: bytes) -> HeaderExtensions:
        ...
    
    def set(self, values: HeaderExtensions): # -> Tuple[int, bytes]:
        ...
    


def clamp_packets_lost(count: int) -> int:
    ...

def pack_packets_lost(count: int) -> bytes:
    ...

def unpack_packets_lost(d: bytes) -> int:
    ...

def pack_rtcp_packet(packet_type: int, count: int, payload: bytes) -> bytes:
    ...

def pack_remb_fci(bitrate: int, ssrcs: List[int]) -> bytes:
    """
    Pack the FCI for a Receiver Estimated Maximum Bitrate report.

    https://tools.ietf.org/html/draft-alvestrand-rmcat-remb-03
    """
    ...

def unpack_remb_fci(data: bytes) -> Tuple[int, List[int]]:
    """
    Unpack the FCI for a Receiver Estimated Maximum Bitrate report.

    https://tools.ietf.org/html/draft-alvestrand-rmcat-remb-03
    """
    ...

def is_rtcp(msg: bytes) -> bool:
    ...

def padl(length: int) -> int:
    """
    Return amount of padding needed for a 4-byte multiple.
    """
    ...

def unpack_header_extensions(extension_profile: int, extension_value: bytes) -> List[Tuple[int, bytes]]:
    """
    Parse header extensions according to RFC 5285.
    """
    ...

def pack_header_extensions(extensions: List[Tuple[int, bytes]]) -> Tuple[int, bytes]:
    """
    Serialize header extensions according to RFC 5285.
    """
    ...

def compute_audio_level_dbov(frame: AudioFrame): # -> int:
    """
    Compute the energy level as spelled out in RFC 6465, Appendix A.
    """
    ...

@dataclass
class RtcpReceiverInfo:
    ssrc: int
    fraction_lost: int
    packets_lost: int
    highest_sequence: int
    jitter: int
    lsr: int
    dlsr: int
    def __bytes__(self) -> bytes:
        ...
    
    @classmethod
    def parse(cls, data: bytes): # -> Self:
        ...
    


@dataclass
class RtcpSenderInfo:
    ntp_timestamp: int
    rtp_timestamp: int
    packet_count: int
    octet_count: int
    def __bytes__(self) -> bytes:
        ...
    
    @classmethod
    def parse(cls, data: bytes): # -> Self:
        ...
    


@dataclass
class RtcpSourceInfo:
    ssrc: int
    items: List[Tuple[Any, bytes]]
    ...


@dataclass
class RtcpByePacket:
    sources: List[int]
    def __bytes__(self) -> bytes:
        ...
    
    @classmethod
    def parse(cls, data: bytes, count: int): # -> Self:
        ...
    


@dataclass
class RtcpPsfbPacket:
    """
    Payload-Specific Feedback Message (RFC 4585).
    """
    fmt: int
    ssrc: int
    media_ssrc: int
    fci: bytes = ...
    def __bytes__(self) -> bytes:
        ...
    
    @classmethod
    def parse(cls, data: bytes, fmt: int): # -> Self:
        ...
    


@dataclass
class RtcpRrPacket:
    ssrc: int
    reports: List[RtcpReceiverInfo] = ...
    def __bytes__(self) -> bytes:
        ...
    
    @classmethod
    def parse(cls, data: bytes, count: int): # -> Self:
        ...
    


@dataclass
class RtcpRtpfbPacket:
    """
    Generic RTP Feedback Message (RFC 4585).
    """
    fmt: int
    ssrc: int
    media_ssrc: int
    lost: List[int] = ...
    def __bytes__(self) -> bytes:
        ...
    
    @classmethod
    def parse(cls, data: bytes, fmt: int): # -> Self:
        ...
    


@dataclass
class RtcpSdesPacket:
    chunks: List[RtcpSourceInfo] = ...
    def __bytes__(self) -> bytes:
        ...
    
    @classmethod
    def parse(cls, data: bytes, count: int): # -> Self:
        ...
    


@dataclass
class RtcpSrPacket:
    ssrc: int
    sender_info: RtcpSenderInfo
    reports: List[RtcpReceiverInfo] = ...
    def __bytes__(self) -> bytes:
        ...
    
    @classmethod
    def parse(cls, data: bytes, count: int): # -> RtcpSrPacket:
        ...
    


AnyRtcpPacket = Union[RtcpByePacket, RtcpPsfbPacket, RtcpRrPacket, RtcpRtpfbPacket, RtcpSdesPacket, RtcpSrPacket,]
class RtcpPacket:
    @classmethod
    def parse(cls, data: bytes) -> List[AnyRtcpPacket]:
        ...
    


class RtpPacket:
    def __init__(self, payload_type: int = ..., marker: int = ..., sequence_number: int = ..., timestamp: int = ..., ssrc: int = ..., payload: bytes = ...) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    @classmethod
    def parse(cls, data: bytes, extensions_map=...): # -> Self:
        ...
    
    def serialize(self, extensions_map=...) -> bytes:
        ...
    


def unwrap_rtx(rtx: RtpPacket, payload_type: int, ssrc: int) -> RtpPacket:
    """
    Recover initial packet from a retransmission packet.
    """
    ...

def wrap_rtx(packet: RtpPacket, payload_type: int, sequence_number: int, ssrc: int) -> RtpPacket:
    """
    Create a retransmission packet from a lost packet.
    """
    ...

