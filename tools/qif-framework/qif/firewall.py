"""
Neural Firewall Module

Signal filtering based on coherence scores at the Neural Interface (I0).
Zero-trust security validation for brain-computer interface signals.

Decision matrix:
  High Cs (>0.6) + authenticated   -> ACCEPT
  High Cs (>0.6) + not auth        -> REJECT (alert)
  Medium Cs (0.3-0.6) + auth       -> ACCEPT_FLAG
  Medium Cs + not auth              -> REJECT (alert)
  Low Cs (<0.3) + any              -> REJECT (critical)
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto
from typing import List, Optional, Callable, Dict, Any

from .coherence import CoherenceMetric, VarianceComponents


class Decision(Enum):
    ACCEPT = auto()
    ACCEPT_FLAG = auto()
    REJECT = auto()


class AlertLevel(Enum):
    NONE = auto()
    ROUTINE = auto()
    ENHANCED = auto()
    ALERT = auto()
    CRITICAL = auto()


@dataclass
class Signal:
    """A signal to be validated by the firewall."""
    arrival_times: List[float]
    amplitudes: List[float]
    authenticated: bool = False
    source_id: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class FilterResult:
    """Result of firewall signal filtering."""
    decision: Decision
    coherence: float
    variances: VarianceComponents
    alert_level: AlertLevel
    reason: str
    timestamp: datetime = field(default_factory=datetime.now)

    @property
    def accepted(self) -> bool:
        return self.decision in (Decision.ACCEPT, Decision.ACCEPT_FLAG)

    @property
    def rejected(self) -> bool:
        return self.decision == Decision.REJECT

    @property
    def flagged(self) -> bool:
        return self.decision == Decision.ACCEPT_FLAG


class NeuralFirewall:
    """
    Zero-trust neural signal firewall operating at QIF band I0.

    Example:
        >>> firewall = NeuralFirewall()
        >>> signal = Signal([0.0, 0.025, 0.050], [100, 98, 102], authenticated=True)
        >>> result = firewall.filter(signal)
        >>> print(f"{result.decision.name}, Cs={result.coherence:.3f}")
    """

    def __init__(
        self,
        threshold_high: float = 0.6,
        threshold_low: float = 0.3,
        reference_freq: float = 40.0,
        amplitude_bounds: Optional[tuple] = None,
        rate_limit: Optional[int] = None,
    ):
        if threshold_low >= threshold_high:
            raise ValueError("threshold_low must be less than threshold_high")
        if not (0 < threshold_low < 1 and 0 < threshold_high < 1):
            raise ValueError("Thresholds must be between 0 and 1")

        self.threshold_high = threshold_high
        self.threshold_low = threshold_low
        self.amplitude_bounds = amplitude_bounds
        self.rate_limit = rate_limit
        self._coherence_metric = CoherenceMetric(reference_freq=reference_freq)
        self._signal_log: List[FilterResult] = []
        self._callbacks: Dict[AlertLevel, List[Callable]] = {
            level: [] for level in AlertLevel
        }

    def filter(self, signal: Signal) -> FilterResult:
        """Filter a signal through the firewall."""
        if self.amplitude_bounds:
            min_amp, max_amp = self.amplitude_bounds
            if any(a < min_amp or a > max_amp for a in signal.amplitudes):
                result = FilterResult(
                    decision=Decision.REJECT,
                    coherence=0.0,
                    variances=VarianceComponents(phase=0, transport=0, gain=float('inf')),
                    alert_level=AlertLevel.CRITICAL,
                    reason=f"Amplitude outside hardware bounds [{min_amp}, {max_amp}]",
                )
                self._log_and_alert(result)
                return result

        variances = self._coherence_metric.calculate_variances(
            signal.arrival_times, signal.amplitudes,
        )
        coherence = self._coherence_metric.calculate(
            signal.arrival_times, signal.amplitudes,
        )
        decision, alert_level, reason = self._apply_decision_matrix(
            coherence, signal.authenticated
        )
        result = FilterResult(
            decision=decision, coherence=coherence, variances=variances,
            alert_level=alert_level, reason=reason,
        )
        self._log_and_alert(result)
        return result

    def _apply_decision_matrix(self, coherence: float, authenticated: bool) -> tuple:
        if coherence > self.threshold_high:
            if authenticated:
                return (Decision.ACCEPT, AlertLevel.ROUTINE,
                        f"High coherence ({coherence:.3f}) with valid authentication")
            else:
                return (Decision.REJECT, AlertLevel.ALERT,
                        f"High coherence ({coherence:.3f}) but missing authentication")
        elif coherence > self.threshold_low:
            if authenticated:
                return (Decision.ACCEPT_FLAG, AlertLevel.ENHANCED,
                        f"Medium coherence ({coherence:.3f}), flagged for review")
            else:
                return (Decision.REJECT, AlertLevel.ALERT,
                        f"Medium coherence ({coherence:.3f}) without authentication")
        else:
            return (Decision.REJECT, AlertLevel.CRITICAL,
                    f"Low coherence ({coherence:.3f}), signal incoherent")

    def _log_and_alert(self, result: FilterResult):
        self._signal_log.append(result)
        for level in AlertLevel:
            if level.value >= result.alert_level.value:
                for callback in self._callbacks.get(level, []):
                    callback(result)

    def register_callback(self, alert_level: AlertLevel, callback: Callable[[FilterResult], None]):
        self._callbacks[alert_level].append(callback)

    def filter_batch(self, signals: List[Signal]) -> List[FilterResult]:
        return [self.filter(signal) for signal in signals]

    def get_stats(self) -> Dict[str, Any]:
        if not self._signal_log:
            return {"total": 0, "accepted": 0, "rejected": 0, "flagged": 0, "avg_coherence": 0.0}
        accepted = sum(1 for r in self._signal_log if r.accepted)
        rejected = sum(1 for r in self._signal_log if r.rejected)
        flagged = sum(1 for r in self._signal_log if r.flagged)
        avg_coherence = sum(r.coherence for r in self._signal_log) / len(self._signal_log)
        return {
            "total": len(self._signal_log),
            "accepted": accepted, "rejected": rejected, "flagged": flagged,
            "accept_rate": accepted / len(self._signal_log),
            "reject_rate": rejected / len(self._signal_log),
            "avg_coherence": avg_coherence,
            "alerts": {
                level.name: sum(1 for r in self._signal_log if r.alert_level == level)
                for level in AlertLevel
            },
        }

    def clear_log(self):
        self._signal_log.clear()

    @property
    def log(self) -> List[FilterResult]:
        return list(self._signal_log)
