"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class RTCIceServer:
    """
    The :class:`RTCIceServer` dictionary defines how to connect to a single
    STUN or TURN server. It includes both the URL and the necessary credentials,
    if any, to connect to the server.
    """
    urls: str
    username: Optional[str] = ...
    credential: Optional[str] = ...
    credentialType: str = ...


@dataclass
class RTCConfiguration:
    """
    The :class:`RTCConfiguration` dictionary is used to provide configuration
    options for an :class:`RTCPeerConnection`.
    """
    iceServers: Optional[List[RTCIceServer]] = ...


