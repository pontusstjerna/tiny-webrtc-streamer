"""
This type stub file was generated by pyright.
"""

import datetime
from dataclasses import dataclass
from typing import List, Optional
from av.frame import Frame
from .mediastreams import MediaStreamTrack
from .rtcdtlstransport import RTCDtlsTransport
from .rtcrtpparameters import RTCRtpCapabilities, RTCRtpReceiveParameters
from .rtp import RtpPacket
from .stats import RTCStatsReport

logger = ...
def decoder_worker(loop, input_q, output_q): # -> None:
    ...

class NackGenerator:
    def __init__(self) -> None:
        ...
    
    def add(self, packet: RtpPacket) -> bool:
        """
        Mark a new packet as received, and deduce missing packets.
        """
        ...
    
    def truncate(self) -> None:
        """
        Limit the number of missing packets we track.

        Otherwise, the size of RTCP FB messages grows indefinitely.
        """
        ...
    


class StreamStatistics:
    def __init__(self, clockrate: int) -> None:
        ...
    
    def add(self, packet: RtpPacket) -> None:
        ...
    
    @property
    def fraction_lost(self) -> int:
        ...
    
    @property
    def jitter(self) -> int:
        ...
    
    @property
    def packets_expected(self) -> int:
        ...
    
    @property
    def packets_lost(self) -> int:
        ...
    


class RemoteStreamTrack(MediaStreamTrack):
    def __init__(self, kind: str, id: Optional[str] = ...) -> None:
        ...
    
    async def recv(self) -> Frame:
        """
        Receive the next frame.
        """
        ...
    


class TimestampMapper:
    def __init__(self) -> None:
        ...
    
    def map(self, timestamp: int) -> int:
        ...
    


@dataclass
class RTCRtpContributingSource:
    """
    The :class:`RTCRtpContributingSource` dictionary contains information about
    a contributing source (CSRC).
    """
    timestamp: datetime.datetime
    source: int
    ...


@dataclass
class RTCRtpSynchronizationSource:
    """
    The :class:`RTCRtpSynchronizationSource` dictionary contains information about
    a synchronization source (SSRC).
    """
    timestamp: datetime.datetime
    source: int
    ...


class RTCRtpReceiver:
    """
    The :class:`RTCRtpReceiver` interface manages the reception and decoding
    of data for a :class:`MediaStreamTrack`.

    :param kind: The kind of media (`'audio'` or `'video'`).
    :param transport: An :class:`RTCDtlsTransport`.
    """
    def __init__(self, kind: str, transport: RTCDtlsTransport) -> None:
        ...
    
    @property
    def track(self) -> MediaStreamTrack:
        """
        The :class:`MediaStreamTrack` which is being handled by the receiver.
        """
        ...
    
    @property
    def transport(self) -> RTCDtlsTransport:
        """
        The :class:`RTCDtlsTransport` over which the media for the receiver's
        track is received.
        """
        ...
    
    @classmethod
    def getCapabilities(self, kind) -> Optional[RTCRtpCapabilities]:
        """
        Returns the most optimistic view of the system's capabilities for
        receiving media of the given `kind`.

        :rtype: :class:`RTCRtpCapabilities`
        """
        ...
    
    async def getStats(self) -> RTCStatsReport:
        """
        Returns statistics about the RTP receiver.

        :rtype: :class:`RTCStatsReport`
        """
        ...
    
    def getSynchronizationSources(self) -> List[RTCRtpSynchronizationSource]:
        """
        Returns a :class:`RTCRtpSynchronizationSource` for each unique SSRC identifier
        received in the last 10 seconds.
        """
        ...
    
    async def receive(self, parameters: RTCRtpReceiveParameters) -> None:
        """
        Attempt to set the parameters controlling the receiving of media.

        :param parameters: The :class:`RTCRtpParameters` for the receiver.
        """
        ...
    
    def setTransport(self, transport: RTCDtlsTransport) -> None:
        ...
    
    async def stop(self) -> None:
        """
        Irreversibly stop the receiver.
        """
        ...
    


