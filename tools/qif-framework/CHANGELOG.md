# Changelog

## v4.0.0 (2026-02-07)

Initial release of the QIF Framework package.

- 11-band hourglass architecture (7-1-3 asymmetric)
- 3 zones: Neural (N7-N1), Interface (I0), Silicon (S1-S3)
- QIFModel class with band lookup, zone navigation, ASCII visualization
- Coherence metric (Cs = e^(-(s2_phi + s2_tau + s2_gamma)))
- Scale-frequency invariant (f x S ~ k)
- Neural firewall with decision matrix
- Zero external dependencies
- Replaces legacy ONI Framework (14-layer model)
