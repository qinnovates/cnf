"""
Scale-Frequency Invariant Module

Validates biological plausibility of neural signals using the f x S ~ k invariant.
Small brain structures oscillate fast. Large brain structures oscillate slowly.
Violations may indicate anomalous (potentially malicious) signals.

This module is framework-agnostic.
"""

import math
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class ScaleLevel:
    """A level in the neural processing hierarchy."""
    name: str
    spatial_scale: float  # meters
    frequency_range: Tuple[float, float]  # Hz
    description: str

    @property
    def center_frequency(self) -> float:
        return math.sqrt(self.frequency_range[0] * self.frequency_range[1])

    @property
    def k_value(self) -> float:
        return self.center_frequency * self.spatial_scale


NEURAL_HIERARCHY: List[ScaleLevel] = [
    ScaleLevel("Molecular", 1e-9, (1e6, 1e9), "Ion channel dynamics, neurotransmitter binding"),
    ScaleLevel("Synaptic", 1e-6, (1e3, 1e5), "Synaptic transmission, vesicle release"),
    ScaleLevel("Cellular", 1e-5, (100, 1000), "Action potentials, spike patterns"),
    ScaleLevel("Microcircuit", 1e-4, (30, 100), "Local field potentials, gamma oscillations"),
    ScaleLevel("Macrocolumn", 1e-3, (8, 30), "Cortical columns, regional processing"),
    ScaleLevel("Regional", 1e-2, (4, 8), "Brain region activity, hippocampal theta"),
    ScaleLevel("Whole-Brain", 1e-1, (0.5, 4), "Global integration, slow oscillations"),
]


class ScaleFrequencyInvariant:
    """
    Calculator and validator for the f x S ~ k invariant.

    Example:
        >>> sfi = ScaleFrequencyInvariant()
        >>> is_valid = sfi.validate(frequency=40, spatial_scale=1e-4)
    """

    def __init__(self, k_constant: Optional[float] = None, tolerance: float = 0.5):
        self.hierarchy = NEURAL_HIERARCHY
        self._k_constant = k_constant or self._compute_k()
        self.tolerance = tolerance

    def _compute_k(self) -> float:
        k_values = [level.k_value for level in self.hierarchy]
        log_mean = sum(math.log(k) for k in k_values) / len(k_values)
        return math.exp(log_mean)

    @property
    def k(self) -> float:
        return self._k_constant

    def calculate_k(self, frequency: float, spatial_scale: float) -> float:
        return frequency * spatial_scale

    def validate(self, frequency: float, spatial_scale: float, tolerance: Optional[float] = None) -> bool:
        tol = tolerance if tolerance is not None else self.tolerance
        calculated_k = self.calculate_k(frequency, spatial_scale)
        lower = self.k * (1 - tol)
        upper = self.k * (1 + tol)
        return lower <= calculated_k <= upper

    def deviation(self, frequency: float, spatial_scale: float) -> float:
        calculated_k = self.calculate_k(frequency, spatial_scale)
        return abs(calculated_k - self.k) / self.k

    def expected_frequency(self, spatial_scale: float) -> float:
        if spatial_scale <= 0:
            raise ValueError("Spatial scale must be positive")
        return self.k / spatial_scale

    def expected_scale(self, frequency: float) -> float:
        if frequency <= 0:
            raise ValueError("Frequency must be positive")
        return self.k / frequency

    def find_level(self, frequency: float) -> Optional[ScaleLevel]:
        for level in self.hierarchy:
            low, high = level.frequency_range
            if low <= frequency <= high:
                return level
        return None

    def anomaly_score(self, frequency: float, spatial_scale: float) -> float:
        deviation = self.deviation(frequency, spatial_scale)
        return 1 - math.exp(-deviation)

    def hierarchy_report(self) -> str:
        lines = [
            "Neural Processing Hierarchy (f x S ~ k)",
            "=" * 60,
            f"{'Level':<15} {'Scale':>12} {'Freq Range':>15} {'k':>10}",
            "-" * 60,
        ]
        for level in self.hierarchy:
            scale_str = f"{level.spatial_scale:.0e} m"
            freq_str = f"{level.frequency_range[0]:.0f}-{level.frequency_range[1]:.0f} Hz"
            k_str = f"{level.k_value:.2e}"
            lines.append(f"{level.name:<15} {scale_str:>12} {freq_str:>15} {k_str:>10}")
        lines.append("-" * 60)
        lines.append(f"{'Computed k:':<15} {self.k:.2e}")
        lines.append(f"{'Tolerance:':<15} {self.tolerance * 100:.0f}%")
        return "\n".join(lines)


def validate_signal_scale(
    frequency: float, spatial_scale: float, tolerance: float = 0.5
) -> Tuple[bool, float]:
    """Quick validation. Returns (is_valid, deviation_fraction)."""
    sfi = ScaleFrequencyInvariant(tolerance=tolerance)
    return sfi.validate(frequency, spatial_scale), sfi.deviation(frequency, spatial_scale)
