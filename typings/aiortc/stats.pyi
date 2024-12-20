"""
This type stub file was generated by pyright.
"""

import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class RTCStats:
    """
    Base class for statistics.
    """
    timestamp: datetime.datetime
    type: str
    id: str
    ...


@dataclass
class RTCRtpStreamStats(RTCStats):
    ssrc: int
    kind: str
    transportId: str
    ...


@dataclass
class RTCReceivedRtpStreamStats(RTCRtpStreamStats):
    packetsReceived: int
    packetsLost: int
    jitter: int
    ...


@dataclass
class RTCSentRtpStreamStats(RTCRtpStreamStats):
    packetsSent: int
    bytesSent: int
    ...


@dataclass
class RTCInboundRtpStreamStats(RTCReceivedRtpStreamStats):
    """
    The :class:`RTCInboundRtpStreamStats` dictionary represents the measurement
    metrics for the incoming RTP media stream.
    """
    ...


@dataclass
class RTCRemoteInboundRtpStreamStats(RTCReceivedRtpStreamStats):
    """
    The :class:`RTCRemoteInboundRtpStreamStats` dictionary represents the remote
    endpoint's measurement metrics for a particular incoming RTP stream.
    """
    roundTripTime: float
    fractionLost: float
    ...


@dataclass
class RTCOutboundRtpStreamStats(RTCSentRtpStreamStats):
    """
    The :class:`RTCOutboundRtpStreamStats` dictionary represents the measurement
    metrics for the outgoing RTP stream.
    """
    trackId: str
    ...


@dataclass
class RTCRemoteOutboundRtpStreamStats(RTCSentRtpStreamStats):
    """
    The :class:`RTCRemoteOutboundRtpStreamStats` dictionary represents the remote
    endpoint's measurement metrics for its outgoing RTP stream.
    """
    remoteTimestamp: Optional[datetime.datetime] = ...


@dataclass
class RTCTransportStats(RTCStats):
    packetsSent: int
    packetsReceived: int
    bytesSent: int
    bytesReceived: int
    iceRole: str
    dtlsState: str
    ...


class RTCStatsReport(dict):
    """
    Provides statistics data about WebRTC connections as returned by the
    :meth:`RTCPeerConnection.getStats()`, :meth:`RTCRtpReceiver.getStats()`
    and :meth:`RTCRtpSender.getStats()` coroutines.

    This object consists of a mapping of string identifiers to objects which
    are instances of:

    - :class:`RTCInboundRtpStreamStats`
    - :class:`RTCOutboundRtpStreamStats`
    - :class:`RTCRemoteInboundRtpStreamStats`
    - :class:`RTCRemoteOutboundRtpStreamStats`
    - :class:`RTCTransportStats`
    """
    def add(self, stats: RTCStats) -> None:
        ...
    


