"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass

@dataclass
class RTCSessionDescription:
    """
    The :class:`RTCSessionDescription` dictionary describes one end of a
    connection and how it's configured.
    """
    sdp: str
    type: str
    def __post_init__(self): # -> None:
        ...
    


