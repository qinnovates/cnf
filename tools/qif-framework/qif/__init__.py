"""
QIF — Quantum Indeterministic Framework for Neural Security

v4.0 Hourglass Model: 11 bands, 3 zones (7-1-3 asymmetric).

Usage:
    >>> from qif import QIFModel
    >>> model = QIFModel()
    >>> print(model.band("N7").name)
    'Neocortex'
"""

__version__ = "4.0.0"

from .bands import Band, Zone, BANDS, BANDS_BY_ID
from .model import QIFModel
from .coherence import (
    CoherenceMetric,
    VarianceComponents,
    calculate_cs,
    quick_coherence,
)
from .scale_freq import (
    ScaleFrequencyInvariant,
    ScaleLevel,
    NEURAL_HIERARCHY,
    validate_signal_scale,
)
from .firewall import (
    NeuralFirewall,
    Signal,
    FilterResult,
    Decision,
    AlertLevel,
)

__all__ = [
    # Model
    "QIFModel",
    "Band",
    "Zone",
    "BANDS",
    "BANDS_BY_ID",
    # Coherence
    "CoherenceMetric",
    "VarianceComponents",
    "calculate_cs",
    "quick_coherence",
    # Scale-Frequency
    "ScaleFrequencyInvariant",
    "ScaleLevel",
    "NEURAL_HIERARCHY",
    "validate_signal_scale",
    # Firewall
    "NeuralFirewall",
    "Signal",
    "FilterResult",
    "Decision",
    "AlertLevel",
]
