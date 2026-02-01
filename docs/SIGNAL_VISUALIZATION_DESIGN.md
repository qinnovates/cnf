# ONI Signal Visualization: Design Rationale & Physical Basis

> Why wavefront propagation was chosen as a pedagogical model to depict BCI signal traversal through the ONI 14-layer model.
>
> **Accuracy Note:** The wavefront visualization is a pedagogical model, not literal electromagnetic wave propagation. At BCI frequencies, electric fields are quasi-static (volume conduction). See the [Mathematical Audit](../MAIN/publications/mathematical-foundations/TechDoc-Mathematical_Audit.md) for the rigorous physical analysis.

---

## Why Wavefronts (Not Beams or Particles)

### What We Rejected

| Approach | Why Not |
|----------|---------|
| **Laser beams** | Lasers are coherent, collimated light — a single focused beam punching through layers. This is not how BCI signals work. Neural signals are diffuse, not directional beams. |
| **Particle streams** | Particles imply discrete units traveling in a line. Real electromagnetic and ionic signals propagate as fields, not projectiles. |
| **Static arrows** | No animation means no representation of propagation speed, attenuation, or frequency-dependent behavior. |

### What We Chose: Wavefront Propagation (as Pedagogical Model)

A **wavefront** is a surface of constant phase in a propagating wave. We chose this as a visualization metaphor because it best captures the concept of a signal's influence spreading outward through layers — even though the literal physics is different at BCI frequencies.

**What each BCI modality actually does:**

| BCI Modality | Actual Physical Mechanism | Wave Model Accuracy |
|-------------|--------------------------|---------------------|
| **Electrode arrays** (Neuralink, Utah) | Volume conduction: quasi-static electric field (∇·(σ∇V) = Iₛ). Field established instantaneously at neural timescales. | **Metaphor** — no wavefront propagation at <10 kHz |
| **EEG/MEG** | Volume-conducted potentials through skull/scalp (quasi-static) | **Metaphor** — quasi-static fields, not propagating waves |
| **TMS** | Time-varying magnetic field induces electric field via Faraday's law (quasi-static at 1-10 kHz) | **Metaphor** — induction, not wave propagation |
| **Optogenetics** | Light at visible/near-IR frequencies (~10¹⁴ Hz). This IS wave propagation, but highly scattered in tissue (Beer-Lambert, Monte Carlo photon transport) | **Closest to accurate** — but scattering prevents clean wavefronts |
| **Action potentials** | Ionic current along axon membrane (Hodgkin-Huxley cable equation) | **Metaphor** — 1D propagation along axon, not spherical |

**Why we still chose wavefronts:** Despite not being literal physics, the expanding-ring metaphor is the best available visualization for three reasons:
1. It communicates **diffuse influence** (vs. beams which imply directionality)
2. It shows **layer-by-layer interaction** as the signal crosses each shell
3. It is **intuitively graspable** — everyone has seen ripples in water

The alternative — animating quasi-static volume conduction with anisotropic conductivity tensors — would be physically accurate but visually incomprehensible to non-specialists.

> **For the physically accurate model**, see [TechDoc-Mathematical_Foundations](../MAIN/publications/mathematical-foundations/TechDoc-Mathematical_Foundations.md), Section 2.

---

## Why Circles: The Fourier Foundation

### Circular Motion and Neural Signals

Every neural oscillation — from a 40 Hz gamma burst to a 1 Hz delta wave — is a sinusoidal waveform. Sinusoids are projections of circular motion, formalized by Euler's formula:

**e^(iθ) = cos θ + i·sin θ**

The expanding rings in the 3D visualization represent this directly: each wavefront is a circular propagation of an oscillatory signal through the ONI layer stack.

### Fourier Decomposition for Security

A **Fourier Transform** decomposes any neural signal into a sum of these circular components, each defined by three measurable properties:

| Property | Circle Analogy | ONI Coherence Component |
|----------|---------------|------------------------|
| **Frequency** (f) | How fast the circle spins | σ²τ (Transport variance) |
| **Amplitude** (A) | The circle's radius | σ²γ (Gain variance) |
| **Phase** (φ) | The circle's starting angle | σ²φ (Phase variance) |

The ONI Coherence Metric (Cₛ) measures the stability of these Fourier components across consecutive time windows. An injected signal must simultaneously match *all three properties* across *all frequency components* of the patient's neural baseline — and the exponential form means even small mismatches compound into rapid coherence collapse.

> **Design note:** Cₛ = e^(−(σ²φ + σ²τ + σ²γ)) is *designed using* Fourier analysis — it is not mathematically *derived from* it. The exponential form is one of several valid choices. See [Mathematical Audit, Finding 5](../MAIN/publications/mathematical-foundations/TechDoc-Mathematical_Audit.md).

### Destructive Interference: Active Signal Cancellation

The same Fourier decomposition that enables detection also enables **active defense** through destructive interference. By identifying a malicious injection's frequency components and generating an anti-phase counterpart (shifted by π radians), the injected signal can be neutralized through superposition — the peaks of the malicious signal align with troughs of the cancellation signal, producing zero net effect.

This principle is well-established across multiple domains:

| Domain | Application | Mechanism | Reference |
|--------|------------|-----------|-----------|
| **Consumer audio** | Active noise cancellation (ANC) | Microphones capture ambient sound; DSP decomposes via FFT; speakers emit anti-phase signal | Kuo & Morgan, 1999 |
| **Neural prosthetics** | Cochlear implant artifact rejection | Stimulation artifacts are identified and removed from neural recordings using template subtraction in the frequency domain | Wichmann, 2000 |
| **Clinical EEG** | Line noise removal | 50/60 Hz power line interference is cancelled via adaptive notch filtering, preserving underlying neural signals | Mitra & Bhatt, 2021 |
| **Telecommunications** | 5G OFDM | Orthogonal Frequency Division Multiplexing uses inverse FFT to encode data onto non-interfering frequency subcarriers; receiver uses FFT to separate them | 3GPP TS 38.211 |
| **MRI** | Gradient artifact cancellation | EEG recorded during fMRI contains scanner artifacts at known frequencies; template subtraction removes them while preserving neural data | Allen et al., 2000 |

### Application to Neural Defense

In the ONI framework, destructive interference extends naturally to neurosecurity:

1. **Baseline establishment** — A patient's authentic neural signature is decomposed into its Fourier components, establishing per-channel frequency, amplitude, and phase baselines
2. **Injection detection** — Incoming signals are decomposed via Short-Time FFT; components deviating from baseline are flagged as potential injections
3. **Active cancellation** — For WRITE-path attacks (malicious stimulation), the firewall can generate a counter-stimulation signal with anti-phase components to neutralize the injection before it reaches neural tissue
4. **Residual monitoring** — Post-cancellation signal is re-evaluated; any remaining anomalous components trigger escalation

This is the same mathematics that makes noise-cancelling headphones work — applied to the most critical interface of all.

---

## Physical Mapping to ONI Layers

### How Real Signals Traverse the Stack

```
Signal Source (e.g., electrode, TMS coil, neural spike)
    │
    ▼ wavefront propagates outward
    │
┌───────────────────────────────────────────────┐
│ L1-L7: Silicon Layers                         │
│                                               │
│ The wavefront encounters:                     │
│ - L1 Physical Carrier: impedance matching     │
│ - L2 Signal Processing: ADC sampling, filters │
│ - L3 Protocol: packet framing                 │
│ - L4 Transport: error correction, checksums   │
│ - L5 Session: temporal synchronization        │
│ - L6 Presentation: data normalization         │
│ - L7 Application: API-level signal delivery   │
│                                               │
│ Each layer attenuates, filters, or transforms │
│ the wavefront based on its function.          │
└───────────────────────────────────────────────┘
    │
    ▼ wavefront reaches the bridge
    │
┌───────────────────────────────────────────────┐
│ L8: Neural Gateway (Firewall)                 │
│                                               │
│ The critical checkpoint. The wavefront is     │
│ analyzed for:                                 │
│ - Coherence score (Cₛ) — does the signal     │
│   match expected statistical baselines?       │
│ - Frequency content — is it within the        │
│   expected band for this neural pathway?      │
│ - Temporal pattern — does timing match known  │
│   biological rhythms?                         │
│                                               │
│ If Cₛ < threshold → BLOCKED (threat)          │
│ If Cₛ ≥ threshold → PASSED (verified)         │
└───────────────────────────────────────────────┘
    │
    ▼ wavefront enters biology
    │
┌───────────────────────────────────────────────┐
│ L9-L14: Biology Layers                        │
│                                               │
│ The verified wavefront interacts with:        │
│ - L9 Bio Signal Processing: filtering         │
│ - L10 Neural Protocol: encoding format        │
│ - L11 Cognitive Transport: delivery pathway   │
│ - L12 Cognitive Session: contextual binding   │
│ - L13 Semantic Layer: meaning/intent          │
│ - L14 Identity Layer: self-model integration  │
└───────────────────────────────────────────────┘
```

### Why Signals Can Be Injected at Any Layer

This is the key security insight that the visualization demonstrates:

| Injection Point | Real-World Attack Vector | Example |
|-----------------|--------------------------|---------|
| **L1 (Physical)** | Hardware tampering, electrode manipulation | Physically modifying implant electrodes |
| **L2 (Signal Processing)** | ADC overflow, filter bypass | Injecting signals that exceed ADC dynamic range |
| **L3 (Protocol)** | Protocol spoofing | Crafting packets that mimic legitimate BCI protocol |
| **L4 (Transport)** | Man-in-the-middle | Intercepting and modifying data in transit |
| **L5 (Session)** | Session hijacking | Replaying captured neural session data |
| **L6 (Presentation)** | Data injection | Injecting normalized-looking data into the stream |
| **L7 (Application)** | API exploitation | Sending malformed commands through the BCI API |
| **L8 (Gateway)** | Firewall bypass | Crafting signals that pass coherence checks |
| **L9-L14 (Biology)** | Direct neural manipulation | Stimulating neurons directly (bypasses all silicon layers) |

This is identical to network security: an attacker doesn't have to start at Layer 1. They find the weakest layer and inject there.

---

## The ONI Scale-Frequency Relationship

The visualization relates to the scale-frequency relationship: **f × S ≈ k**

Where:
- **f** = frequency of the signal
- **S** = scale (spatial extent in the neural substrate)
- **k** = approximately constant for a given neural pathway

This qualitative relationship is empirically well-documented in neuroscience (Buzsáki & Draguhn, 2004):
- High-frequency signals (gamma, >30 Hz) involve small spatial scales (cortical columns, ~1mm)
- Low-frequency signals (delta, <4 Hz) involve large spatial scales (whole-brain regions)
- This follows from neural circuit anatomy: larger circuits have longer conduction delays and thus slower oscillation frequencies

> **Accuracy note:** The original claim derived f × S ≈ k from the wave equation v = fλ with constant v. However, neural tissue is **dispersive** — dielectric properties are frequency-dependent (Cole-Cole model), so v(f) varies with frequency and f × S is not strictly constant. The qualitative scaling holds, but the quantitative invariant requires a dispersion-corrected formulation. See [Mathematical Audit, Finding 4](../MAIN/publications/mathematical-foundations/TechDoc-Mathematical_Audit.md).

In the visualization, this manifests as:
- **Outer shells (silicon)**: Process high-frequency, small-scale digital signals
- **Inner shells (biology)**: Process low-frequency, large-scale neural oscillations
- **L8 (gateway)**: The transition point where frequency-scale characteristics shift

A threat signal might have the wrong frequency profile for the layer it's targeting — this is exactly what the **Layer-Aware Coherence Metric** Cₛ(S) formalizes.

### The Unified Layer-Aware Coherence Metric

The visualization directly maps to the proposed unified metric:

**Cₛ(S) = e^(−Σ_f w(f, S) · (σ²φ(f) + σ²τ(f) + σ²γ(f)))**

Each concentric shell in the 3D model represents a different spatial scale S. The weighting function w(f, S) — derived from f × S ≈ k — adjusts scrutiny based on whether a frequency component belongs at that shell's spatial scale. In the visualization:

| Visual Element | Mathematical Meaning |
|---------------|---------------------|
| Outer shells (small S) | High expected frequency — w(f, S) peaks at high f |
| Inner shells (large S) | Low expected frequency — w(f, S) peaks at low f |
| L8 gateway flash | Cₛ(S) evaluation — green if above threshold, red if below |
| Shell brightness on crossing | Per-layer w(f, S) contribution to the total score |
| Signal color (blue/red/green) | Signal type determines variance profile (σ²φ, σ²τ, σ²γ) |

The physical chain underpinning this metric — Maxwell (quasi-static) → Boltzmann → Nernst-Planck → Einstein diffusion → Hodgkin-Huxley → Cole-Cole → Fourier → Cₛ(S) — is documented in [TechDoc-Equations_Reference](../MAIN/publications/mathematical-foundations/TechDoc-Equations_Reference.md).

> **Note:** Cₛ(S) is a proposed theoretical framework. The base components are established; the unification is the contribution. See the [ONI Whitepaper, Section 8](../MAIN/publications/0-oni-framework/ONI_Whitepaper.md) for the full formulation.

---

## Visualization Technical Implementation

### Technologies Used

| Component | Technology | Purpose |
|-----------|-----------|---------|
| 3D Rendering | Three.js (WebGL) | GPU-accelerated 3D graphics |
| Shell Materials | Custom GLSL Fresnel Shaders | Physically-based rim glow on translucent shells |
| Gateway Effect | Custom GLSL Energy Shader | Pulsing scan-line energy field |
| Brain Core | GLSL Subsurface Scattering | Simulates light passing through tissue |
| Signal Wavefronts | GLSL Ring Shaders + Raycasting | Expanding ring wavefronts with propagation physics |
| Neural Nodes | GLSL Point Sprites | Flickering synaptic activity |
| Tone Mapping | ACES Filmic | Cinematic lighting with HDR feel |
| Interaction | Three.js Raycaster | Click-to-inject signals at any layer |

### Signal Behavior

1. **Normal signals** (blue): Propagate at standard speed, pass L8 gateway check, reach brain core
2. **Threat signals** (red): Propagate faster (aggressive injection), blocked at L8 gateway, coherence score fails
3. **Stimulation signals** (green): Propagate slower (therapeutic), pass L8 gateway, reach neural core

### Visual Feedback

- **Shell flash**: When a wavefront crosses a layer, that shell briefly brightens
- **Gateway checkpoint**: L8 flashes green (passed) or red (blocked) when a signal reaches it
- **Brain core flash**: Core glows when a verified signal arrives
- **Event log**: Real-time terminal-style log shows signal path and gateway decisions

---

## Physical Implementation Feasibility

### How This Could Be Physically Built

The ONI layer model could be physically implemented using existing and near-term technologies:

**Silicon Layers (L1-L7):**
- Already exist in current BCI systems (Neuralink, Blackrock Microsystems)
- Hardware: electrode arrays, ADCs, signal processors, wireless transmitters
- Software: firmware, protocols, encryption, APIs

**L8 Neural Gateway:**
- Requires real-time coherence scoring hardware
- Could be implemented as:
  - FPGA-based anomaly detection at the hardware level
  - Neural network classifier running on edge compute (e.g., embedded GPU)
  - Statistical baseline comparison engine (comparing incoming signals to trained Cₛ baselines)
- Latency requirement: < 1ms for real-time blocking

**Biology Layers (L9-L14):**
- These are descriptive/organizational — they represent how the brain itself processes signals
- "Implementation" means understanding and modeling these layers, not building them
- The gateway (L8) protects the biology layers by filtering what reaches them

### Signal Detection Methods

| Method | Layer | How It Works |
|--------|-------|-------------|
| **Impedance monitoring** | L1 | Detect physical electrode tampering by measuring impedance changes |
| **Statistical baseline** | L2-L7 | Compare signal statistics to trained baselines (Cₛ metric) |
| **Coherence scoring** | L8 | Real-time Cₛ = e^(−(σ²φ + σ²τ + σ²γ)) calculation |
| **Frequency analysis** | L9-L14 | Verify f × S ≈ k invariant for the targeted neural pathway |
| **Temporal pattern matching** | L5, L11 | Compare timing patterns to known biological rhythms |

---

## References

- Qi, K. (2026). *ONI Framework: Open Neurosecurity Interoperability*. https://github.com/qinnovates/qinnovate
- Qi, K. (2026). *Mathematical Audit of the ONI Framework*. ONI Publications. [TechDoc-Mathematical_Audit](../MAIN/publications/mathematical-foundations/TechDoc-Mathematical_Audit.md)
- Qi, K. (2026). *Corrected Mathematical Foundations*. ONI Publications. [TechDoc-Mathematical_Foundations](../MAIN/publications/mathematical-foundations/TechDoc-Mathematical_Foundations.md)
- Qi, K. (2026). *The Coherence Metric: Variance-Based Neural Signal Verification*. ONI Publications.
- Qi, K. (2026). *Scale-Frequency Relationship: f × S ≈ k in Neural Signal Processing*. ONI Publications.
- Buzsáki, G., & Draguhn, A. (2004). Neuronal oscillations in cortical networks. *Science*, 304(5679), 1926–1929.
- Gabriel, S., Lau, R. W., & Gabriel, C. (1996). The dielectric properties of biological tissues. *Physics in Medicine & Biology*, 41(11), 2251.
- Nunez, P. L., & Srinivasan, R. (2006). *Electric Fields of the Brain* (2nd ed.). Oxford University Press.
- Kohno, T., & Johnson, B. (2009). *Analysis of Proposed Attack Models for Brain-Computer Interfaces*.
- Denning, T., et al. (2009). *Neurosecurity: Security and Privacy for Neural Devices*.

---

*Document created: 2026-01-29*
*Author: Kevin Qi + Claude (QI Collaboration)*
*For: ONI Framework — qinnovates/qinnovate*
