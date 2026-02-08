"""
Coherence Metric Module

Calculates the coherence score (Cs) for neural signal validation.

Formula: Cs = e^(-(s2_phi + s2_tau + s2_gamma))

Where:
- s2_phi = phase variance (timing jitter relative to reference oscillations)
- s2_tau = transport variance (pathway integrity)
- s2_gamma = gain variance (amplitude stability)

This module is framework-agnostic: it operates on signal data regardless
of which band model is in use.
"""

import math
import warnings
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class VarianceComponents:
    """Container for the three variance components of coherence."""
    phase: float      # s2_phi - timing jitter
    transport: float  # s2_tau - pathway integrity
    gain: float       # s2_gamma - amplitude stability

    @property
    def total(self) -> float:
        """Total variance."""
        return self.phase + self.transport + self.gain


class CoherenceMetric:
    """
    Calculator for neural signal coherence scores.

    Example:
        >>> metric = CoherenceMetric(reference_freq=40.0)
        >>> cs = metric.calculate([0.0, 0.025, 0.050], [100, 98, 102])
        >>> print(f"Cs = {cs:.3f}")
    """

    BANDS = {
        'delta': (0.5, 4),
        'theta': (4, 8),
        'alpha': (8, 12),
        'beta': (13, 30),
        'gamma': (30, 100),
    }

    DEFAULT_TRANSPORT_FACTORS = {
        'myelinated_axon': 0.999,
        'unmyelinated_axon': 0.97,
        'synaptic_transmission': 0.85,
        'dendritic_integration': 0.90,
    }

    def __init__(
        self,
        reference_freq: float = 40.0,
        transport_factors: Optional[dict] = None,
        expected_amplitude: Optional[float] = None,
    ):
        self.reference_freq = reference_freq
        self.transport_factors = transport_factors or self.DEFAULT_TRANSPORT_FACTORS
        self.expected_amplitude = expected_amplitude

    def calculate(
        self,
        arrival_times: List[float],
        amplitudes: List[float],
        transport_factors: Optional[dict] = None,
    ) -> float:
        """Calculate Cs for a signal. Returns value in [0, 1]."""
        variances = self.calculate_variances(arrival_times, amplitudes, transport_factors)
        return calculate_cs(variances)

    def calculate_variances(
        self,
        arrival_times: List[float],
        amplitudes: List[float],
        transport_factors: Optional[dict] = None,
    ) -> VarianceComponents:
        """Calculate individual variance components."""
        return VarianceComponents(
            phase=self._calculate_phase_variance(arrival_times),
            transport=self._calculate_transport_variance(transport_factors),
            gain=self._calculate_gain_variance(amplitudes),
        )

    def _calculate_phase_variance(self, arrival_times: List[float]) -> float:
        if len(arrival_times) < 2:
            return 0.0
        phases = [
            (2 * math.pi * self.reference_freq * t) % (2 * math.pi)
            for t in arrival_times
        ]
        n = len(phases)
        sin_sum = sum(math.sin(p) for p in phases)
        cos_sum = sum(math.cos(p) for p in phases)
        R = math.sqrt((sin_sum / n) ** 2 + (cos_sum / n) ** 2)
        circular_variance = 1 - R
        return circular_variance * (math.pi ** 2)

    def _calculate_transport_variance(self, transport_factors: Optional[dict] = None) -> float:
        factors = transport_factors or self.transport_factors
        if not factors:
            return 0.0
        total = 0.0
        for name, reliability in factors.items():
            if reliability <= 0 or reliability > 1:
                raise ValueError(f"Transport factor '{name}' must be in (0, 1], got {reliability}")
            total += -math.log(reliability)
        return total

    def _calculate_gain_variance(self, amplitudes: List[float]) -> float:
        if len(amplitudes) < 2:
            return 0.0
        baseline = self.expected_amplitude or (sum(amplitudes) / len(amplitudes))
        if baseline == 0:
            warnings.warn("Zero baseline amplitude, returning infinite gain variance")
            return float('inf')
        squared_devs = [((a - baseline) / baseline) ** 2 for a in amplitudes]
        return sum(squared_devs) / len(squared_devs)

    def get_band(self) -> Optional[str]:
        """Return the neural oscillation band for the reference frequency."""
        for band, (low, high) in self.BANDS.items():
            if low <= self.reference_freq <= high:
                return band
        return None

    def interpret(self, cs: float) -> Tuple[str, str]:
        """Interpret a coherence score. Returns (level, description)."""
        if cs > 0.6:
            return ("HIGH", "Signal is coherent and trustworthy")
        elif cs > 0.3:
            return ("MEDIUM", "Signal shows moderate variance, verify context")
        else:
            return ("LOW", "Signal is incoherent, reject or investigate")


def calculate_cs(variances: VarianceComponents) -> float:
    """Calculate Cs = e^(-(total_variance))."""
    total_variance = variances.total
    if total_variance < 0:
        raise ValueError(f"Total variance cannot be negative: {total_variance}")
    if total_variance == float('inf'):
        return 0.0
    return math.exp(-total_variance)


def quick_coherence(
    arrival_times: List[float],
    amplitudes: List[float],
    reference_freq: float = 40.0,
) -> float:
    """Convenience function for quick coherence calculation."""
    metric = CoherenceMetric(reference_freq=reference_freq)
    return metric.calculate(arrival_times, amplitudes)
