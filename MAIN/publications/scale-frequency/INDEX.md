# Scale-Frequency — Index

> **Mathematical relationship between spatial scale and temporal frequency across neural processing layers (f × S ≈ k).**

**Status:** Published
**Last Updated:** 2026-01-21
**ONI Layers:** L1-L7 (biological layers)

---

## Summary

Scale-Frequency analysis reveals a fundamental invariant in neural information processing: the product of spatial scale and temporal frequency remains approximately constant across biological layers. This relationship (f × S ≈ 10⁶ m·Hz) emerges from the physics of neural computation and has direct implications for BCI design.

At molecular scales (L1), processes operate at microsecond timescales with frequencies in the MHz range. At whole-brain scales (L6), oscillations occur at Hz frequencies but coordinate across centimeters of tissue. The scale-frequency constant provides a unifying principle for understanding how information compresses and expands as it traverses the neural hierarchy.

For BCI security, this invariant establishes expectations for legitimate signals at each layer — deviations from the expected scale-frequency relationship can indicate signal manipulation or injection attempts.

---

## Dependencies

**This topic builds on:**

| Topic | Relationship |
|-------|--------------|
| [ONI Framework](../0-oni-framework/INDEX.md) | Layer definitions for scale-frequency mapping |

**Topics that build on this:**

| Topic | Relationship |
|-------|--------------|
| [Coherence Metric](../coherence-metric/INDEX.md) | Frequency expectations inform coherence validation |

---

## Documents

| Type | Document | Description |
|------|----------|-------------|
| Blog | [Blog-Scale_Frequency.md](Blog-Scale_Frequency.md) | Accessible introduction to neural scaling laws ([Original on Medium](https://medium.com/@qikevinl/the-hidden-equation-your-brain-runs-on-and-why-it-matters-5be5598eac1f)) |
| TechDoc | [TechDoc-Scale_Frequency.md](TechDoc-Scale_Frequency.md) | Mathematical derivation and empirical validation |

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| Scale-Frequency Constant | f × S ≈ 10⁶ m·Hz across neural layers |
| Spatial Scale (S) | Physical extent of neural structures at each layer |
| Temporal Frequency (f) | Characteristic oscillation rates at each layer |
| Information Compression | How signals transform across scale boundaries |
| Cross-Scale Coherence | Synchronization patterns linking layer frequencies |

---

## Related Topics

| Topic | Connection |
|-------|------------|
| [Coherence Metric](../coherence-metric/INDEX.md) | Uses frequency expectations for validation |
| [ONI Framework](../0-oni-framework/INDEX.md) | Provides layer structure for scale mapping |

---

## Keywords

**Primary:** scale-frequency, neural scaling, frequency invariants, cross-scale patterns
**Technical:** spectral analysis, spatial frequency, temporal dynamics, oscillations
**Biological:** neural oscillations, cortical columns, brain rhythms, synaptic timing
**Security:** signal validation, anomaly detection, frequency fingerprinting

---

## Future Work

- [ ] Empirical validation across BCI modalities
- [ ] Individual variation in scale-frequency constant
- [ ] Real-time frequency monitoring at L8
- [ ] Integration with coherence metric calculations

---

← Back to [Index](../../INDEX.md)
