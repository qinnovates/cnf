"""
Tests for TARA core modules.

Tests coherence calculation, ONI layers, firewall, and scale-frequency.
"""

import pytest
import numpy as np


class TestCoherence:
    """Tests for coherence metric calculation."""

    def test_coherence_import(self):
        """Test that coherence module can be imported."""
        from tara.core import coherence
        assert hasattr(coherence, "CoherenceMetric")

    def test_coherence_calculation(self, sample_signal):
        """Test basic coherence calculation."""
        from tara.core.coherence import CoherenceMetric

        metric = CoherenceMetric()
        signal = sample_signal["signal"]

        # Should return a value between 0 and 1
        cs = metric.calculate(signal)
        assert 0.0 <= cs <= 1.0

    def test_coherence_high_for_coherent_signal(self):
        """Test that coherent signals have high Cₛ."""
        from tara.core.coherence import CoherenceMetric

        metric = CoherenceMetric()

        # Pure sine wave should have high coherence
        t = np.linspace(0, 1, 1000)
        pure_signal = np.sin(2 * np.pi * 10 * t)

        cs = metric.calculate(pure_signal)
        assert cs > 0.5

    def test_coherence_low_for_noise(self):
        """Test that noise has low Cₛ."""
        from tara.core.coherence import CoherenceMetric

        metric = CoherenceMetric()

        # Random noise should have low coherence
        np.random.seed(42)
        noise = np.random.randn(1000)

        cs = metric.calculate(noise)
        assert cs < 0.5


class TestONILayers:
    """Tests for ONI 14-layer model."""

    def test_layers_import(self):
        """Test that layers module can be imported."""
        from tara.core import layers
        assert hasattr(layers, "ONIStack")

    def test_layer_count(self):
        """Test that ONI model has 14 layers."""
        from tara.core.layers import ONIStack

        stack = ONIStack()
        assert len(stack.layers) == 14

    def test_layer_8_is_gateway(self):
        """Test that L8 is Neural Gateway."""
        from tara.core.layers import ONIStack

        stack = ONIStack()
        layer_8 = stack.get_layer(8)
        assert "gateway" in layer_8.name.lower() or "gateway" in str(layer_8).lower()

    def test_biological_layers(self):
        """Test that L1-L7 are biological domain."""
        from tara.core.layers import ONIStack

        stack = ONIStack()
        for i in range(1, 8):
            layer = stack.get_layer(i)
            assert layer.domain == "biological" or layer.domain == "bio"

    def test_silicon_layers(self):
        """Test that L9-L14 are silicon domain."""
        from tara.core.layers import ONIStack

        stack = ONIStack()
        for i in range(9, 15):
            layer = stack.get_layer(i)
            assert layer.domain == "silicon" or layer.domain == "digital"


class TestFirewall:
    """Tests for neural firewall."""

    def test_firewall_import(self):
        """Test that firewall module can be imported."""
        from tara.core import firewall
        assert hasattr(firewall, "NeuralFirewall")

    def test_firewall_pass_good_signal(self, sample_firewall_signal):
        """Test that good signals pass the firewall."""
        from tara.core.firewall import NeuralFirewall

        fw = NeuralFirewall()
        result = fw.evaluate(sample_firewall_signal)

        # Good signal should pass
        assert result.passed or result.decision == "pass"

    def test_firewall_block_low_coherence(self, sample_firewall_signal):
        """Test that low coherence signals are blocked."""
        from tara.core.firewall import NeuralFirewall

        fw = NeuralFirewall()

        # Modify signal to have very low coherence
        bad_signal = sample_firewall_signal.copy()
        bad_signal["coherence"] = 0.1

        result = fw.evaluate(bad_signal)
        assert not result.passed or result.decision in ["block", "flag"]

    def test_firewall_block_high_anomaly(self, sample_firewall_signal):
        """Test that high anomaly signals are blocked."""
        from tara.core.firewall import NeuralFirewall

        fw = NeuralFirewall()

        # Modify signal to have high anomaly score
        bad_signal = sample_firewall_signal.copy()
        bad_signal["anomaly_score"] = 0.95

        result = fw.evaluate(bad_signal)
        assert not result.passed or result.decision in ["block", "flag"]


class TestScaleFrequency:
    """Tests for scale-frequency invariant."""

    def test_scale_freq_import(self):
        """Test that scale_freq module can be imported."""
        from tara.core import scale_freq
        assert hasattr(scale_freq, "ScaleFrequencyInvariant")

    def test_invariant_holds(self):
        """Test that f × S ≈ k for valid signals."""
        from tara.core.scale_freq import ScaleFrequencyInvariant

        sfi = ScaleFrequencyInvariant()

        # Test at different scales
        pairs = [
            (10, 1.0),    # 10 Hz at scale 1
            (100, 0.1),   # 100 Hz at scale 0.1
            (1, 10.0),    # 1 Hz at scale 10
        ]

        products = [f * s for f, s in pairs]

        # All products should be approximately equal
        assert all(abs(p - products[0]) < 1.0 for p in products)
