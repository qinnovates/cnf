"""Tests for QIFModel — v4.0 Hourglass Architecture."""

import pytest
from qif import QIFModel, Band, Zone, BANDS, BANDS_BY_ID


class TestQIFModel:
    def setup_method(self):
        self.model = QIFModel()

    def test_version(self):
        assert self.model.version == "4.0"

    def test_architecture(self):
        assert "11-band" in self.model.architecture
        assert "7-1-3" in self.model.architecture

    def test_total_bands(self):
        assert len(self.model.bands) == 11
        assert len(self.model) == 11

    def test_neural_bands_count(self):
        neural = self.model.neural_bands()
        assert len(neural) == 7

    def test_silicon_bands_count(self):
        silicon = self.model.silicon_bands()
        assert len(silicon) == 3

    def test_interface_band(self):
        i0 = self.model.interface()
        assert i0.id == "I0"
        assert i0.zone == Zone.INTERFACE

    def test_band_ids_order(self):
        """Bands should be in hourglass order: N7 -> N1 -> I0 -> S1 -> S3."""
        ids = [b.id for b in self.model.bands]
        assert ids == ["N7", "N6", "N5", "N4", "N3", "N2", "N1", "I0", "S1", "S2", "S3"]

    def test_neural_band_ids(self):
        ids = [b.id for b in self.model.neural_bands()]
        assert ids == ["N7", "N6", "N5", "N4", "N3", "N2", "N1"]

    def test_silicon_band_ids(self):
        ids = [b.id for b in self.model.silicon_bands()]
        assert ids == ["S1", "S2", "S3"]

    def test_band_lookup(self):
        n7 = self.model.band("N7")
        assert n7.name == "Neocortex"
        assert n7.zone == Zone.NEURAL

    def test_band_lookup_invalid(self):
        with pytest.raises(KeyError):
            self.model.band("X99")

    def test_all_bands_have_required_fields(self):
        for band in self.model.bands:
            assert band.id
            assert band.name
            assert isinstance(band.zone, Zone)
            assert band.description
            assert isinstance(band.qi_range, tuple)
            assert len(band.qi_range) == 2
            assert isinstance(band.hourglass_width, float)
            assert 0 < band.hourglass_width <= 1.0

    def test_neural_zones_all_neural(self):
        for band in self.model.neural_bands():
            assert band.zone == Zone.NEURAL

    def test_silicon_zones_all_silicon(self):
        for band in self.model.silicon_bands():
            assert band.zone == Zone.SILICON

    def test_hourglass_narrows_at_i0(self):
        """I0 should have the smallest hourglass_width."""
        i0 = self.model.interface()
        for band in self.model.bands:
            if band.id != "I0":
                assert band.hourglass_width >= i0.hourglass_width

    def test_bands_by_zone(self):
        neural = self.model.bands_by_zone(Zone.NEURAL)
        interface = self.model.bands_by_zone(Zone.INTERFACE)
        silicon = self.model.bands_by_zone(Zone.SILICON)
        assert len(neural) == 7
        assert len(interface) == 1
        assert len(silicon) == 3

    def test_ascii_diagram(self):
        diagram = self.model.ascii_diagram()
        assert "QIF v4.0" in diagram
        assert "N7" in diagram
        assert "I0" in diagram
        assert "S3" in diagram

    def test_repr(self):
        r = repr(self.model)
        assert "4.0" in r
        assert "11" in r

    def test_n2_brainstem_severity(self):
        """N2 Brainstem should be LETHAL severity."""
        n2 = self.model.band("N2")
        assert n2.severity == "LETHAL"

    def test_n4_diencephalon_severity(self):
        """N4 Diencephalon should be CRITICAL severity."""
        n4 = self.model.band("N4")
        assert n4.severity == "CRITICAL"

    def test_silicon_bands_deterministic(self):
        """S2 and S3 should be deterministic."""
        assert self.model.band("S2").determinacy == "Deterministic"
        assert self.model.band("S3").determinacy == "Deterministic"


class TestBandConstants:
    def test_bands_list_length(self):
        assert len(BANDS) == 11

    def test_bands_by_id_lookup(self):
        assert BANDS_BY_ID["N7"].name == "Neocortex"
        assert BANDS_BY_ID["I0"].name == "Neural Interface"
        assert BANDS_BY_ID["S3"].name == "Radio / Wireless / DE"

    def test_band_frozen(self):
        """Band dataclass should be frozen (immutable)."""
        band = BANDS_BY_ID["N7"]
        with pytest.raises(AttributeError):
            band.name = "Changed"
