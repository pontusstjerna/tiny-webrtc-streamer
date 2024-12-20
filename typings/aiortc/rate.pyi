"""
This type stub file was generated by pyright.
"""

from enum import Enum
from typing import List, Optional, Tuple

BURST_DELTA_THRESHOLD_MS = ...
MAX_ADAPT_OFFSET_MS = ...
MIN_NUM_DELTAS = ...
DELTA_COUNTER_MAX = ...
MIN_FRAME_PERIOD_HISTORY_LENGTH = ...
INTER_ARRIVAL_SHIFT = ...
TIMESTAMP_GROUP_LENGTH_MS = ...
TIMESTAMP_TO_MS = ...
class BandwidthUsage(Enum):
    NORMAL = ...
    UNDERUSING = ...
    OVERUSING = ...


class RateControlState(Enum):
    HOLD = ...
    INCREASE = ...
    DECREASE = ...


class AimdRateControl:
    def __init__(self) -> None:
        ...
    
    def feedback_interval(self) -> int:
        ...
    
    def set_estimate(self, bitrate: int, now_ms: int) -> None:
        """
        For testing purposes.
        """
        ...
    
    def update(self, bandwidth_usage: BandwidthUsage, estimated_throughput: Optional[int], now_ms: int) -> Optional[int]:
        ...
    


class TimestampGroup:
    def __init__(self, timestamp: Optional[int] = ...) -> None:
        ...
    


class InterArrivalDelta:
    def __init__(self, timestamp: int, arrival_time: int, size: int) -> None:
        ...
    


class InterArrival:
    """
    Inter-arrival time and size filter.

    Adapted from the webrtc.org codebase.
    """
    def __init__(self, group_length: int, timestamp_to_ms: float) -> None:
        ...
    
    def compute_deltas(self, timestamp: int, arrival_time: int, packet_size: int) -> Optional[InterArrivalDelta]:
        ...
    
    def belongs_to_burst(self, timestamp: int, arrival_time: int) -> bool:
        ...
    
    def new_timestamp_group(self, timestamp: int, arrival_time: int) -> bool:
        ...
    
    def packet_out_of_order(self, timestamp: int) -> bool:
        ...
    


class OveruseDetector:
    """
    Bandwidth overuse detector.

    Adapted from the webrtc.org codebase.
    """
    def __init__(self) -> None:
        ...
    
    def detect(self, offset: float, timestamp_delta_ms: float, num_of_deltas: int, now_ms: int) -> BandwidthUsage:
        ...
    
    def state(self) -> BandwidthUsage:
        ...
    
    def update_threshold(self, modified_offset: float, now_ms: int) -> None:
        ...
    


class OveruseEstimator:
    """
    Bandwidth overuse estimator.

    Adapted from the webrtc.org codebase.
    """
    def __init__(self) -> None:
        ...
    
    def num_of_deltas(self) -> int:
        ...
    
    def offset(self) -> float:
        ...
    
    def update(self, time_delta_ms: int, timestamp_delta_ms: float, size_delta: int, current_hypothesis: BandwidthUsage, now_ms: int): # -> None:
        ...
    
    def update_min_frame_period(self, ts_delta: float) -> float:
        ...
    
    def update_noise_estimate(self, residual: float, ts_delta: float) -> None:
        ...
    


class RateBucket:
    def __init__(self, count: int = ..., value: int = ...) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    


class RateCounter:
    """
    Rate counter, which stores the amount received in 1ms buckets.
    """
    def __init__(self, window_size: int, scale: int = ...) -> None:
        ...
    
    def add(self, value: int, now_ms: int) -> None:
        ...
    
    def rate(self, now_ms: int) -> Optional[int]:
        ...
    
    def reset(self) -> None:
        ...
    


class RemoteBitrateEstimator:
    def __init__(self) -> None:
        ...
    
    def add(self, arrival_time_ms: int, abs_send_time: int, payload_size: int, ssrc: int) -> Optional[Tuple[int, List[int]]]:
        ...
    


