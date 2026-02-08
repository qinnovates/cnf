"""
QIF Model — v4.0 Hourglass Architecture (11-band, 7-1-3).

The QIFModel class provides access to the full band architecture,
zone navigation, and ASCII visualization of the hourglass.
"""

from typing import List, Optional

from .bands import Band, Zone, BANDS, BANDS_BY_ID


class QIFModel:
    """
    The QIF v4.0 hourglass model.

    11 bands across 3 zones: Neural (N7-N1), Interface (I0), Silicon (S1-S3).
    Numbers increase away from the interface in both directions.
    The hourglass narrows at I0 (the electrode-tissue boundary).

    Example:
        >>> model = QIFModel()
        >>> print(model.version)
        '4.0'
        >>> print(len(model.bands))
        11
        >>> n7 = model.band("N7")
        >>> print(n7.name)
        'Neocortex'
    """

    VERSION = "4.0"
    ARCHITECTURE = "Hourglass (11-band, 7-1-3)"

    def __init__(self):
        self._bands = list(BANDS)
        self._by_id = dict(BANDS_BY_ID)

    @property
    def version(self) -> str:
        return self.VERSION

    @property
    def architecture(self) -> str:
        return self.ARCHITECTURE

    @property
    def bands(self) -> List[Band]:
        """All 11 bands in hourglass order (N7 → N1 → I0 → S1 → S3)."""
        return list(self._bands)

    def band(self, band_id: str) -> Band:
        """Look up a band by ID (e.g. 'N7', 'I0', 'S2')."""
        b = self._by_id.get(band_id)
        if b is None:
            raise KeyError(f"Unknown band ID: {band_id!r}. Valid: {list(self._by_id.keys())}")
        return b

    def neural_bands(self) -> List[Band]:
        """Neural domain bands (N7-N1), outermost to innermost."""
        return [b for b in self._bands if b.zone == Zone.NEURAL]

    def silicon_bands(self) -> List[Band]:
        """Silicon domain bands (S1-S3), innermost to outermost."""
        return [b for b in self._bands if b.zone == Zone.SILICON]

    def interface(self) -> Band:
        """The interface band (I0)."""
        return self._by_id["I0"]

    def bands_by_zone(self, zone: Zone) -> List[Band]:
        """All bands in a given zone."""
        return [b for b in self._bands if b.zone == zone]

    def ascii_diagram(self) -> str:
        """
        ASCII art of the hourglass model.

        Width proportional to hourglass_width field.
        """
        max_label_width = max(len(f"{b.id} {b.name}") for b in self._bands)
        max_bar = 40
        lines = [
            f"QIF v{self.VERSION} Hourglass Model ({self.ARCHITECTURE})",
            "=" * 60,
            "",
        ]

        zone_labels = {
            Zone.NEURAL: "NEURAL DOMAIN",
            Zone.INTERFACE: "INTERFACE",
            Zone.SILICON: "SILICON DOMAIN",
        }
        current_zone = None

        for b in self._bands:
            if b.zone != current_zone:
                current_zone = b.zone
                lines.append(f"  --- {zone_labels[current_zone]} ---")

            bar_width = int(b.hourglass_width * max_bar)
            padding = (max_bar - bar_width) // 2
            label = f"{b.id} {b.name}"
            bar = " " * padding + "#" * bar_width
            lines.append(f"  {label:<{max_label_width}}  |{bar}|")

        lines.append("")
        lines.append(f"  Bands: {len(self._bands)} | Zones: 3 | Waist: I0 (Neural Interface)")
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"QIFModel(version={self.VERSION!r}, bands={len(self._bands)})"

    def __len__(self) -> int:
        return len(self._bands)
