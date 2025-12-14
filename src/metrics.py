"""
Metrics stubs for Entropy Folding experiments.
License: AGPLv3 (see LICENSE).

- Stall detection
- Burst detection
- ΔM estimation hooks
"""

from typing import List, Sequence


def detect_stall(history: Sequence[float], window: int = 3, epsilon: float = 1e-3) -> bool:
    """
    Simple stall detector: checks last `window` deltas for near-zero change.
    Replace with domain metrics (skill scores, loss curves).
    """
    if len(history) < window + 1:
        return False
    deltas = [abs(history[i] - history[i - 1]) for i in range(-1, -window - 1, -1)]
    return all(d < epsilon for d in deltas)


def detect_burst(timestamps: List[float], min_gap: float) -> List[int]:
    """
    Identify burst boundaries given a minimum gap.
    Returns indices where a new burst starts.
    """
    if not timestamps:
        return []
    bursts = [0]
    for i in range(1, len(timestamps)):
        if timestamps[i] - timestamps[i - 1] > min_gap:
            bursts.append(i)
    return bursts
