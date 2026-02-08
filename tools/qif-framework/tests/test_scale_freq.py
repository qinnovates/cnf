"""Tests for scale-frequency invariant."""

import math
import pytest
from qif import ScaleFrequencyInvariant, ScaleLevel, NEURAL_HIERARCHY, validate_signal_scale


class TestScaleLevel:
    def test_center_frequency(self):
        level = ScaleLevel("Test", 1e-4, (30, 100), "test")
        expected = math.sqrt(30 * 100)
        assert abs(level.center_frequency - expected) < 1e-10

    def test_k_value(self):
        level = ScaleLevel("Test", 1e-4, (30, 100), "test")
        expected = level.center_frequency * 1e-4
        assert abs(level.k_value - expected) < 1e-15


class TestNeuralHierarchy:
    def test_hierarchy_length(self):
        assert len(NEURAL_HIERARCHY) == 7

    def test_scales_decrease(self):
        """Spatial scales should decrease from Molecular to Whole-Brain (small to large)."""
        # Actually they increase (nm to 10 cm)
        for i in range(len(NEURAL_HIERARCHY) - 1):
            assert NEURAL_HIERARCHY[i].spatial_scale < NEURAL_HIERARCHY[i + 1].spatial_scale

    def test_frequencies_decrease(self):
        """Center frequencies should decrease as spatial scale increases."""
        for i in range(len(NEURAL_HIERARCHY) - 1):
            assert NEURAL_HIERARCHY[i].center_frequency > NEURAL_HIERARCHY[i + 1].center_frequency


class TestScaleFrequencyInvariant:
    def setup_method(self):
        self.sfi = ScaleFrequencyInvariant()

    def test_k_is_positive(self):
        assert self.sfi.k > 0

    def test_validate_exact_k(self):
        """f*S == k should always validate."""
        freq = self.sfi.k / 1e-3  # exact k at 1mm scale
        assert self.sfi.validate(freq, 1e-3)

    def test_validate_within_tolerance(self):
        """f*S within 50% of k should validate."""
        freq = self.sfi.k / 1e-3 * 1.3  # 30% above expected
        assert self.sfi.validate(freq, 1e-3)

    def test_expected_frequency_positive(self):
        freq = self.sfi.expected_frequency(1e-3)
        assert freq > 0

    def test_expected_scale_positive(self):
        scale = self.sfi.expected_scale(40)
        assert scale > 0

    def test_expected_frequency_zero_raises(self):
        with pytest.raises(ValueError):
            self.sfi.expected_frequency(0)

    def test_expected_scale_zero_raises(self):
        with pytest.raises(ValueError):
            self.sfi.expected_scale(0)

    def test_deviation_zero_for_exact_k(self):
        """deviation should be ~0 when f*S == k."""
        freq = self.sfi.k / 1e-3
        dev = self.sfi.deviation(freq, 1e-3)
        assert dev < 1e-10

    def test_anomaly_score_range(self):
        score = self.sfi.anomaly_score(40, 1e-4)
        assert 0 <= score <= 1

    def test_anomaly_score_high_for_mismatch(self):
        """Very mismatched f and S should give high anomaly score."""
        score = self.sfi.anomaly_score(1e6, 1)  # 1 MHz at 1 meter
        assert score > 0.9

    def test_find_level_gamma(self):
        level = self.sfi.find_level(50)
        assert level is not None
        assert level.name == "Microcircuit"

    def test_find_level_delta(self):
        level = self.sfi.find_level(2)
        assert level is not None
        assert level.name == "Whole-Brain"

    def test_find_level_out_of_range(self):
        level = self.sfi.find_level(0.001)
        assert level is None

    def test_hierarchy_report(self):
        report = self.sfi.hierarchy_report()
        assert "Molecular" in report
        assert "Whole-Brain" in report

    def test_custom_k(self):
        sfi = ScaleFrequencyInvariant(k_constant=1.0)
        assert sfi.k == 1.0


class TestValidateSignalScale:
    def test_returns_tuple(self):
        result = validate_signal_scale(40, 1e-4)
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_valid_signal(self):
        valid, dev = validate_signal_scale(40, 1e-4)
        assert isinstance(valid, bool)
        assert isinstance(dev, float)
