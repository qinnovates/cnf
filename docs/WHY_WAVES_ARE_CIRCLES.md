# Why Waves Are Circles: The Mathematics Behind ONI's Signal Visualization

> From right triangles to Fourier transforms — and why it all matters for brain-computer interface security.

*A visual mathematics primer for the ONI Neuroassurance Stack*

---

## The Chain

```
Right Triangle → Unit Circle → Sine Wave → Circular Wavefront → Fourier Transform → ONI Coherence
```

Every link in this chain is the same math, viewed from a different angle. By the end of this document, you'll see why we represent neural signals as expanding circular wavefronts in the ONI visualization — and how the underlying trigonometry connects directly to the ONI coherence metric and scale-frequency invariant.

> **Accuracy Note:** This document is a pedagogical primer. The circular wavefront visualization is a teaching model — not literal BCI physics. At BCI-relevant frequencies, electric fields are quasi-static (volume conduction), not propagating waves. See the [Mathematical Audit](../neurosecurity/legacy-core/publications/mathematical-foundations/TechDoc-Mathematical_Audit.md) for the full rigorous analysis and the [Corrected Foundations](../neurosecurity/legacy-core/publications/mathematical-foundations/TechDoc-Mathematical_Foundations.md) for empirically accurate physics.

---

## 1. It Starts with a Triangle

Take a right triangle. The kind you drew in geometry class.

```
        /|
       / |
    1 /  | sin(θ)
     /   |
    / θ  |
   /_____|
    cos(θ)
```

The ratios of the sides have names:

| Ratio | Name | Value |
|-------|------|-------|
| opposite / hypotenuse | **sin(θ)** | Height of the triangle |
| adjacent / hypotenuse | **cos(θ)** | Width of the triangle |

If the hypotenuse is 1 (a **unit** triangle), then:
- **sin(θ)** is literally the height
- **cos(θ)** is literally the width

That's all sine and cosine are. Ratios of triangle sides. Nothing more mysterious than that.

---

## 2. Put the Triangle in a Circle

Now take that triangle and pin the hypotenuse to the center of a circle with radius 1 (the **unit circle**). Let the angle θ sweep around.

```
           sin(θ)
            ↑
            |  ╱ ← hypotenuse = 1 (radius)
            | ╱
            |╱ θ
   ─────────┼──────── → cos(θ)
            |
            |
```

As θ rotates from 0° to 360°:
- The **x-coordinate** of the point on the circle = cos(θ)
- The **y-coordinate** of the point on the circle = sin(θ)

This is why the equation of a circle is **x² + y² = 1**, which is the same as **cos²(θ) + sin²(θ) = 1**. The Pythagorean theorem and the equation of a circle are the same statement.

**The triangle doesn't just live inside the circle. The triangle *defines* the circle.**

---

## 3. Unroll the Circle into a Wave

Here's where it gets beautiful.

Watch the y-coordinate (sin θ) as the point travels around the circle. If you plot that height over time — as the angle increases steadily — you get a **sine wave**:

```
Circle (side view)          Unrolled over time

    ●                        1 ╭─╮     ╭─╮
   ╱                           │   │     │   │
  ╱                        0 ──╯   ╰──╯   ╰──  → time
 ●───
  ╲                       -1         ╰─╯     ╰─╯
   ╲
    ●
```

**A wave IS circular motion viewed from the side.**

This isn't an analogy. It's a mathematical identity:

```
sin(θ) = sin(ωt)

where:
  θ = angle around circle
  ω = angular velocity (how fast you go around)
  t = time
```

Every sine wave is a circle spinning in time. Every circle is a wave frozen in space.

---

## 4. Why Wavefronts Are Circular

Now imagine dropping a stone in still water. Ripples expand outward. Why are they circles?

Because the wave travels at the same speed in every direction in a uniform medium. After time *t*, the wave has traveled distance *r = v × t* in all directions. The set of all points at distance *r* from the center is... a circle.

```
        ╭─────╮           The wave equation:
      ╱    ●    ╲
    ╱    (source)  ╲       r = v × t
   │                │
    ╲              ╱       All points at distance r
      ╲          ╱         from the source form a circle.
        ╰─────╯           In 3D, they form a sphere.
```

This is why:
- Sound waves from a speaker expand as spheres (in uniform air)
- Light from a bulb expands as spheres (in vacuum/uniform medium)
- Ripples in water expand as circles (in still, uniform water)

> **Important physics note:** BCI electrodes operate at low frequencies (0.5 Hz – 10 kHz) where the electromagnetic wavelength in tissue is ~hundreds of meters — far larger than the brain. At this scale, electric fields don't propagate as waves. They are **quasi-static**: governed by volume conduction (Laplace's equation ∇·(σ∇V) = Iₛ), not the wave equation. The field establishes effectively instantaneously and falls off with distance according to the tissue's anisotropic conductivity tensor.
>
> Additionally, neural tissue is **anisotropic** — conductivity differs by direction (~10:1 ratio along vs. across white matter fibers). Even in a volume conduction model, equipotential surfaces are ellipsoidal or irregular, not spherical.
>
> **The circular wavefront in the ONI visualization is a pedagogical model** representing how a signal's influence spreads through the ONI layer stack. It is not literal electromagnetic wave propagation. The mathematical chain (triangle → circle → wave → Fourier) is exact; the application to BCI electrode fields as "wavefronts" is a useful simplification. See the [Mathematical Audit](../neurosecurity/legacy-core/publications/mathematical-foundations/TechDoc-Mathematical_Audit.md) for full details.

Despite this distinction, the wavefront visualization captures a correct intuition: a signal originating at one point influences surrounding tissue, and each ONI layer it encounters (L14 biology → L13 → ... → L8 gateway → ... → L1 silicon) interacts with the signal differently — filtering, transforming, or blocking it.

---

## 5. Fourier: Every Signal Is Made of Circles

This is where it all connects.

In 1822, Joseph Fourier claimed something remarkable — later rigorously proven by Dirichlet (1829) and Carleson (1966): **any finite-energy signal can be decomposed into a sum of simple sine waves.** Each sine wave has a frequency, an amplitude, and a phase. (All real BCI recordings are finite-energy, so this applies to every neural signal we'd encounter.)

Since each sine wave is circular motion (Section 3), this means:

**Any signal is a sum of spinning circles.**

```
Complex neural signal = circle₁ + circle₂ + circle₃ + ...
                      = A₁·sin(f₁t + φ₁) + A₂·sin(f₂t + φ₂) + A₃·sin(f₃t + φ₃) + ...

where:
  Aₙ = amplitude (size of circle)
  fₙ = frequency (speed of rotation)
  φₙ = phase (starting angle)
```

Visually, imagine stacking circles on top of circles, each spinning at a different speed. The combined motion of all these spinning circles traces out the complex signal:

```
Slow circle (low frequency):      ○ ← large, slow
                                   │
Fast circle (high frequency):      ◌ ← small, fast
                                   │
Combined tip traces:            ~~∿~~ ← complex waveform
```

This is literally how an EEG signal works. Your brain produces:
- **Delta waves** (0.5–4 Hz) — large, slow circles
- **Theta waves** (4–8 Hz) — medium circles
- **Alpha waves** (8–13 Hz) — medium-fast circles
- **Beta waves** (13–30 Hz) — fast circles
- **Gamma waves** (30–100 Hz) — very fast, small circles

An EEG recording is the sum of all of these. The Fourier transform decomposes the recording back into its constituent circles.

---

## 6. The Fourier Transform: Seeing Inside the Signal

The Fourier Transform takes a signal in **time** and reveals its **frequencies**:

```
Time domain                    Frequency domain
(what you record)              (what Fourier reveals)

~~∿∿~∿~~∿∿~    ──────→      │
                   FFT         │  ▌
                               │  ▌ ▌
                               │  ▌ ▌   ▌
                               └──────────── → frequency
                                δ θ α β γ
```

**Left side:** The messy, complex signal as recorded from an electrode.
**Right side:** The clean frequency spectrum — how much energy is at each frequency (each circle size).

This is the basis for the ONI coherence metric. The metric is **designed** (not mathematically derived) to measure the stability of a signal's Fourier components over time:

```
Cₛ = e^(−(σ²φ + σ²τ + σ²γ))
```

Where:
- **σ²φ** = variance in **phase** (how much the circle's starting angles jitter across time windows)
- **σ²τ** = variance in **timing** (how much the circle's speeds fluctuate across time windows)
- **σ²γ** = variance in **amplitude** (how much the circle's sizes change across time windows)

The exponential form is a design choice that produces sharp threshold behavior: coherence stays high when variances are small, then collapses rapidly as they increase — similar to how biological neurons gate signals with all-or-nothing firing. (Note: computing variance requires comparing Fourier decompositions across multiple consecutive time windows, not just a single snapshot.)

If a signal's Fourier components (its circles) are stable — consistent phase, timing, and amplitude — the coherence score is high (Cₛ → 1). The signal is trustworthy.

If an attacker injects a foreign signal, its Fourier components won't match the expected pattern. The circles will be wrong — wrong sizes, wrong speeds, wrong starting angles. The coherence score drops (Cₛ → 0). The gateway blocks it.

**Fourier analysis is the mathematical tool L8 uses to decompose signals and check their components against baseline expectations.**

---

## 7. The ONI Scale-Frequency Invariant

One more connection. The ONI framework identifies that:

**f × S ≈ k** (frequency × spatial scale ≈ constant)

This means:
- High-frequency signals (fast-spinning circles) operate at small spatial scales
- Low-frequency signals (slow-spinning circles) operate at large spatial scales
- The product is approximately constant for a given neural pathway

The intuition comes from wave physics. A wave's wavelength λ relates to its frequency f by:

```
v = f × λ

where v = propagation speed
```

If v were constant, then f × λ = constant, and since spatial scale S relates to wavelength: f × S ≈ k.

> **Accuracy note:** In neural tissue, v is **not** constant across frequencies — tissue is dispersive, with frequency-dependent dielectric properties described by the Cole-Cole model (Cole & Cole, 1941; Gabriel et al., 1996). This means f × S is not strictly constant. However, the **qualitative** relationship holds well: higher-frequency neural oscillations (gamma, >30 Hz) involve smaller neural circuits (cortical columns, ~1mm), while lower-frequency oscillations (delta, <4 Hz) involve larger brain regions. This is empirically well-documented (Buzsáki & Draguhn, 2004) and follows from neural circuit anatomy — larger circuits have longer conduction delays and thus slower oscillation frequencies. The invariant should be understood as an approximate scaling law, not an exact constant. See the [Mathematical Audit](../neurosecurity/legacy-core/publications/mathematical-foundations/TechDoc-Mathematical_Audit.md) for details.

This is why:
- **Outer shells (L1–L7 silicon)** handle high-frequency digital signals — small, fast circles
- **Inner shells (L9–L14 biology)** handle low-frequency neural oscillations — large, slow circles
- **L8 gateway** sits at the transition point where the frequency-scale relationship shifts from digital to biological

---

## 8. Full Circle: Why the Visualization Works

Now you can see the complete chain:

| Mathematical Concept | What It Means | How It Appears in ONI |
|----------------------|---------------|----------------------|
| **Right triangle ratios** | sin(θ), cos(θ) | The foundation of all wave math |
| **Unit circle** | sin²+cos²=1 | The geometric foundation of wave math |
| **Sine wave** | Circular motion over time | The shape of neural oscillations |
| **Fourier Transform** | Signal = sum of circles | How L8 decomposes signals to check coherence |
| **Coherence metric Cₛ** | Stability of the circles | How L8 decides: pass or block (design choice, not derivation) |
| **f × S ≈ k** | Frequency-scale relationship | Why different layers handle different frequencies (approximate) |
| **Visualization** | Expanding rings | Pedagogical model of signal influence spreading through layers |

When you see a circular wavefront expanding through the ONI layers in the visualization, you're watching a **pedagogical model** of:

1. A signal (sum of spinning circles) originating at an injection point
2. The signal's influence spreading outward through the layer structure (simplified as circular for clarity; real tissue is anisotropic)
3. Each layer interacting with the signal's frequency components differently
4. At L8, the Fourier components are analyzed — are the circles what we expect?
5. If yes → pass. If no → block.

**The triangle, the circle, the wave, and the Fourier transform are all the same mathematics viewed from different perspectives. The coherence metric and scale-frequency relationship are *designed using* this mathematics to protect the brain — they are engineering applications of these foundations, not direct derivations from them.**

---

## Summary

```
A right triangle's side ratios
        │
        ▼
define sine and cosine
        │
        ▼
which trace a circle
        │
        ▼
which unrolled over time creates a wave
        │
        ▼
and Fourier proved any finite-energy signal = sum of these waves (circles)
        │
        ▼
so the coherence metric is DESIGNED to check if the circles match expectations
        │
        ▼
and the gateway blocks signals whose circles are wrong
```

From a triangle drawn in sand to a firewall protecting your thoughts. Same foundational math, applied as engineering to defend the brain.

> **What's proven math vs. what's ONI design:**
> - Triangle → circle → sine wave → Fourier decomposition: **established mathematics**
> - Cₛ formula and f × S ≈ k: **ONI design choices** that use this math but are not derived from it
> - Circular wavefront visualization: **pedagogical model**, not literal BCI physics
> - For the full rigorous analysis, see [Mathematical Audit](../neurosecurity/legacy-core/publications/mathematical-foundations/TechDoc-Mathematical_Audit.md)

---

## Further Reading

- [Mathematical Audit](../neurosecurity/legacy-core/publications/mathematical-foundations/TechDoc-Mathematical_Audit.md) — Rigorous audit of every mathematical claim in this document
- [Corrected Mathematical Foundations](../neurosecurity/legacy-core/publications/mathematical-foundations/TechDoc-Mathematical_Foundations.md) — Empirically accurate physics with expansion stubs
- [ONI Signal Visualization Design Rationale](SIGNAL_VISUALIZATION_DESIGN.md) — Why wavefronts were chosen and the physical basis
- [ONI 14-Layer Model](https://github.com/qinnovates/mindloft/blob/main/neurosecurity/legacy-core/oni-framework/ONI_LAYERS.md) — The full layer specification
- [Coherence Metric](https://github.com/qinnovates/mindloft/blob/main/neurosecurity/legacy-core/publications/coherence-metric/) — The variance-based anomaly detection system
- [Scale-Frequency Invariant](https://github.com/qinnovates/mindloft/blob/main/neurosecurity/legacy-core/publications/scale-frequency/) — f × S ≈ k in neural signal processing
- Fourier, J. (1822). *Theorie analytique de la chaleur* — The original work decomposing functions into sine series
- [From Stars to Waves — Underground Mathematics](https://undergroundmathematics.org/trigonometry-triangles-to-functions/from-stars-to-waves) — Triangles to trigonometric functions
- [Wave Mathematics — Visionlearning](https://www.visionlearning.com/en/library/Math-in-Science/62/Wave-Mathematics/131) — Mathematical foundations of waves
- Inspired by: [youtube.com/watch?v=ZU-cIz8dvqU](https://www.youtube.com/watch?v=ZU-cIz8dvqU)

---

*Document created: 2026-01-29*
*Author: Kevin Qi + Claude (QI Collaboration)*
*For: ONI Framework — qinnovates/mindloft*
*Location: docs/WHY_WAVES_ARE_CIRCLES.md*
