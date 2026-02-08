"""Tests for coherence metric."""

import math
import pytest
from qif import CoherenceMetric, VarianceComponents, calculate_cs, quick_coherence


class TestVarianceComponents:
    def test_total(self):
        vc = VarianceComponents(phase=0.1, transport=0.2, gain=0.3)
        assert abs(vc.total - 0.6) < 1e-10

    def test_zero_total(self):
        vc = VarianceComponents(phase=0.0, transport=0.0, gain=0.0)
        assert vc.total == 0.0


class TestCoherenceMetric:
    def setup_method(self):
        self.metric = CoherenceMetric(reference_freq=40.0)

    def test_perfect_coherence(self):
        """Perfectly regular signal should have high coherence."""
        times = [i * 0.025 for i in range(10)]  # exact 40 Hz intervals
        amps = [100.0] * 10
        cs = self.metric.calculate(times, amps)
        assert cs > 0.5

    def test_random_signal_low_coherence(self):
        """Highly irregular signal should have low coherence."""
        import random
        random.seed(42)
        times = sorted([random.random() for _ in range(20)])
        amps = [random.random() * 200 for _ in range(20)]
        cs = self.metric.calculate(times, amps)
        assert cs < 0.6

    def test_coherence_range(self):
        """Cs should always be in [0, 1]."""
        times = [0.0, 0.025, 0.050, 0.075, 0.100]
        amps = [100, 98, 102, 99, 101]
        cs = self.metric.calculate(times, amps)
        assert 0 <= cs <= 1

    def test_single_point_returns_high(self):
        """Single data point should return high coherence (low phase/gain variance).
        Transport variance is still nonzero from default pathway factors."""
        cs = self.metric.calculate([0.0], [100.0])
        assert cs > 0.5

    def test_interpret_high(self):
        level, _ = self.metric.interpret(0.8)
        assert level == "HIGH"

    def test_interpret_medium(self):
        level, _ = self.metric.interpret(0.45)
        assert level == "MEDIUM"

    def test_interpret_low(self):
        level, _ = self.metric.interpret(0.1)
        assert level == "LOW"

    def test_get_band_gamma(self):
        metric = CoherenceMetric(reference_freq=40.0)
        assert metric.get_band() == "gamma"

    def test_get_band_theta(self):
        metric = CoherenceMetric(reference_freq=6.0)
        assert metric.get_band() == "theta"

    def test_get_band_out_of_range(self):
        metric = CoherenceMetric(reference_freq=200.0)
        assert metric.get_band() is None

    def test_transport_invalid_factor(self):
        with pytest.raises(ValueError):
            self.metric.calculate([0, 0.025], [100, 100],
                                  transport_factors={"bad": 0.0})


class TestCalculateCs:
    def test_zero_variance(self):
        vc = VarianceComponents(phase=0, transport=0, gain=0)
        assert calculate_cs(vc) == 1.0

    def test_infinite_variance(self):
        vc = VarianceComponents(phase=0, transport=0, gain=float('inf'))
        assert calculate_cs(vc) == 0.0

    def test_negative_variance_raises(self):
        vc = VarianceComponents(phase=-1, transport=0, gain=0)
        with pytest.raises(ValueError):
            calculate_cs(vc)

    def test_known_value(self):
        vc = VarianceComponents(phase=0.1, transport=0.1, gain=0.1)
        expected = math.exp(-0.3)
        assert abs(calculate_cs(vc) - expected) < 1e-10


class TestQuickCoherence:
    def test_returns_float(self):
        cs = quick_coherence([0.0, 0.025, 0.050], [100, 102, 98])
        assert isinstance(cs, float)
        assert 0 <= cs <= 1
