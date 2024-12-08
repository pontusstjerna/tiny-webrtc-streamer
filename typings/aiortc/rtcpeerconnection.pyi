"""
This type stub file was generated by pyright.
"""

from typing import List, Optional, Set, Union
from pyee.asyncio import AsyncIOEventEmitter
from . import sdp
from .mediastreams import MediaStreamTrack
from .rtcconfiguration import RTCConfiguration
from .rtcdtlstransport import RTCDtlsTransport
from .rtcicetransport import RTCIceCandidate, RTCIceTransport
from .rtcrtpparameters import RTCRtpCodecCapability, RTCRtpCodecParameters, RTCRtpHeaderExtensionParameters
from .rtcrtpreceiver import RTCRtpReceiver
from .rtcrtpsender import RTCRtpSender
from .rtcrtptransceiver import RTCRtpTransceiver
from .rtcsctptransport import RTCSctpTransport
from .rtcsessiondescription import RTCSessionDescription
from .stats import RTCStatsReport

DISCARD_HOST = ...
DISCARD_PORT = ...
MEDIA_KINDS = ...
logger = ...
def filter_preferred_codecs(codecs: List[RTCRtpCodecParameters], preferred: List[RTCRtpCodecCapability]) -> List[RTCRtpCodecParameters]:
    ...

def find_common_codecs(local_codecs: List[RTCRtpCodecParameters], remote_codecs: List[RTCRtpCodecParameters]) -> List[RTCRtpCodecParameters]:
    ...

def find_common_header_extensions(local_extensions: List[RTCRtpHeaderExtensionParameters], remote_extensions: List[RTCRtpHeaderExtensionParameters]) -> List[RTCRtpHeaderExtensionParameters]:
    ...

def is_codec_compatible(a: RTCRtpCodecParameters, b: RTCRtpCodecParameters) -> bool:
    ...

def add_transport_description(media: sdp.MediaDescription, dtlsTransport: RTCDtlsTransport) -> None:
    ...

async def add_remote_candidates(iceTransport: RTCIceTransport, media: sdp.MediaDescription) -> None:
    ...

def allocate_mid(mids: Set[str]) -> str:
    """
    Allocate a MID which has not been used yet.
    """
    ...

def create_media_description_for_sctp(sctp: RTCSctpTransport, legacy: bool, mid: str) -> sdp.MediaDescription:
    ...

def create_media_description_for_transceiver(transceiver: RTCRtpTransceiver, cname: str, direction: str, mid: str) -> sdp.MediaDescription:
    ...

def and_direction(a: str, b: str) -> str:
    ...

def or_direction(a: str, b: str) -> str:
    ...

def reverse_direction(direction: str) -> str:
    ...

def wrap_session_description(session_description: Optional[sdp.SessionDescription]) -> Optional[RTCSessionDescription]:
    ...

class RTCPeerConnection(AsyncIOEventEmitter):
    """
    The :class:`RTCPeerConnection` interface represents a WebRTC connection
    between the local computer and a remote peer.

    :param configuration: An optional :class:`RTCConfiguration`.
    """
    def __init__(self, configuration: Optional[RTCConfiguration] = ...) -> None:
        ...
    
    @property
    def connectionState(self) -> str:
        """
        The current connection state.

        Possible values: `"connected"`, `"connecting"`, `"closed"`, `"failed"`, `"new`".

        When the state changes, the `"connectionstatechange"` event is fired.
        """
        ...
    
    @property
    def iceConnectionState(self) -> str:
        """
        The current ICE connection state.

        Possible values: `"checking"`, `"completed"`, `"closed"`, `"failed"`, `"new`".

        When the state changes, the `"iceconnectionstatechange"` event is fired.
        """
        ...
    
    @property
    def iceGatheringState(self) -> str:
        """
        The current ICE gathering state.

        Possible values: `"complete"`, `"gathering"`, `"new`".

        When the state changes, the `"icegatheringstatechange"` event is fired.
        """
        ...
    
    @property
    def localDescription(self) -> RTCSessionDescription:
        """
        An :class:`RTCSessionDescription` describing the session for
        the local end of the connection.
        """
        ...
    
    @property
    def remoteDescription(self) -> RTCSessionDescription:
        """
        An :class:`RTCSessionDescription` describing the session for
        the remote end of the connection.
        """
        ...
    
    @property
    def sctp(self) -> Optional[RTCSctpTransport]:
        """
        An :class:`RTCSctpTransport` describing the SCTP transport being used
        for datachannels or `None`.
        """
        ...
    
    @property
    def signalingState(self): # -> str:
        """
        The current signaling state.

        Possible values: `"closed"`, `"have-local-offer"`, `"have-remote-offer`",
        `"stable"`.

        When the state changes, the `"signalingstatechange"` event is fired.
        """
        ...
    
    async def addIceCandidate(self, candidate: RTCIceCandidate) -> None:
        """
        Add a new :class:`RTCIceCandidate` received from the remote peer.

        The specified candidate must have a value for either `sdpMid` or
        `sdpMLineIndex`.

        :param candidate: The new remote candidate.
        """
        ...
    
    def addTrack(self, track: MediaStreamTrack) -> RTCRtpSender:
        """
        Add a :class:`MediaStreamTrack` to the set of media tracks which
        will be transmitted to the remote peer.
        """
        ...
    
    def addTransceiver(self, trackOrKind: Union[str, MediaStreamTrack], direction: str = ...) -> RTCRtpTransceiver:
        """
        Add a new :class:`RTCRtpTransceiver`.
        """
        ...
    
    async def close(self): # -> None:
        """
        Terminate the ICE agent, ending ICE processing and streams.
        """
        ...
    
    async def createAnswer(self): # -> RTCSessionDescription | None:
        """
        Create an SDP answer to an offer received from a remote peer during
        the offer/answer negotiation of a WebRTC connection.

        :rtype: :class:`RTCSessionDescription`
        """
        ...
    
    def createDataChannel(self, label, maxPacketLifeTime=..., maxRetransmits=..., ordered=..., protocol=..., negotiated=..., id=...): # -> RTCDataChannel:
        """
        Create a data channel with the given label.

        :rtype: :class:`RTCDataChannel`
        """
        ...
    
    async def createOffer(self) -> RTCSessionDescription:
        """
        Create an SDP offer for the purpose of starting a new WebRTC
        connection to a remote peer.

        :rtype: :class:`RTCSessionDescription`
        """
        ...
    
    def getReceivers(self) -> List[RTCRtpReceiver]:
        """
        Returns the list of :class:`RTCRtpReceiver` objects that are currently
        attached to the connection.
        """
        ...
    
    def getSenders(self) -> List[RTCRtpSender]:
        """
        Returns the list of :class:`RTCRtpSender` objects that are currently
        attached to the connection.
        """
        ...
    
    async def getStats(self) -> RTCStatsReport:
        """
        Returns statistics for the connection.

        :rtype: :class:`RTCStatsReport`
        """
        ...
    
    def getTransceivers(self) -> List[RTCRtpTransceiver]:
        """
        Returns the list of :class:`RTCRtpTransceiver` objects that are currently
        attached to the connection.
        """
        ...
    
    async def setLocalDescription(self, sessionDescription: RTCSessionDescription) -> None:
        """
        Change the local description associated with the connection.

        :param sessionDescription: An :class:`RTCSessionDescription` generated
                                    by :meth:`createOffer` or :meth:`createAnswer()`.
        """
        ...
    
    async def setRemoteDescription(self, sessionDescription: RTCSessionDescription) -> None:
        """
        Changes the remote description associated with the connection.

        :param sessionDescription: An :class:`RTCSessionDescription` created from
                                    information received over the signaling channel.
        """
        ...
    

