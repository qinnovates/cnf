# ONI Visualizations

Programmatic video generation for the ONI Neuroassurance Framework using [Remotion](https://remotion.dev/).

## Purpose

Generate investor-ready, scientifically accurate visualizations that communicate:
- The 14-layer neural stack architecture
- The Coherence Metric (Cₛ) trust calculation
- Attack detection capabilities
- Zero-trust authentication flow

## Available Compositions

| Composition | Duration | Description |
|-------------|----------|-------------|
| `CoherenceMetric` | 30s | Animates Cₛ = e^(−(σ²φ + σ²τ + σ²γ)) with real-time trust scoring |
| `LayerStack` | 45s | Signal flow from L1 Physical to L14 Identity (placeholder) |
| `AttackDetection` | 60s | Legitimate vs attack signal comparison (placeholder) |

## Quick Start

```bash
# Install dependencies
npm install

# Start Remotion Studio (development)
npm start

# Render a video
npm run build:coherence

# Render all videos
npm run build:all
```

## Project Structure

```
oni-visualizations/
├── src/
│   ├── components/          # Reusable visual primitives
│   ├── compositions/        # Complete video compositions
│   │   └── CoherenceMetric.tsx
│   ├── data/
│   │   └── oni-constants.ts # Scientific values from ONI Framework
│   ├── Root.tsx             # Composition registry
│   └── index.ts             # Entry point
├── public/
│   └── assets/              # Static images, fonts
├── out/                     # Rendered videos
├── package.json
└── tsconfig.json
```

## Scientific Accuracy

All visualizations are constrained by documented research values:

- **Phase Variance (σ²φ):** 0.05 - 0.2
- **Transport Variance (σ²τ):** 0.1 - 0.4 (dominates)
- **Gain Variance (σ²γ):** 0.02 - 0.1
- **Thresholds:** Accept > 0.75, Flag 0.5-0.75, Reject ≤ 0.5

See `neurosecurity/legacy-core/publications/coherence-metric/TechDoc-Coherence_Metric_Detailed.md` for derivations.

## Animation Principles

1. **No linear motion** — Biological systems don't move linearly
2. **Physics-based easing** — `spring()` for organic feel
3. **Entropy visualization** — Show variance, not just means
4. **Scientific precision** — Every parameter maps to real data

## Brand Colors

| Color | Hex | Usage |
|-------|-----|-------|
| Cyan | `#00d4ff` | OSI layers, phase variance |
| Purple | `#8b5cf6` | Biology layers |
| Pink | `#ec4899` | Cognitive layers |
| Yellow | `#f59e0b` | Bridge layer (L8), transport variance |
| Green | `#10b981` | Accept, success, gain variance |
| Red | `#ef4444` | Reject, threats |

## Output Formats

```bash
# MP4 (default)
remotion render src/index.ts CoherenceMetric out/coherence.mp4

# GIF (for web)
remotion render src/index.ts CoherenceMetric out/coherence.gif --image-format=png

# PNG sequence
remotion render src/index.ts CoherenceMetric out/frames --image-sequence
```

## Integration with GitHub Pages

Rendered videos can be embedded in the ONI documentation:

```html
<video controls width="100%">
  <source src="oni-visualizations/out/coherence-metric.mp4" type="video/mp4">
</video>
```

## References

- [Remotion Documentation](https://remotion.dev/docs)
- [ONI VISUALIZATION_AS_CODE_STRATEGY.md](../../neurosecurity/legacy-core/resources/workflows/VISUALIZATION_AS_CODE_STRATEGY.md)
- [ONI Coherence Metric TechDoc](../../neurosecurity/legacy-core/publications/coherence-metric/)

---

*Part of the ONI Neuroassurance Framework*
