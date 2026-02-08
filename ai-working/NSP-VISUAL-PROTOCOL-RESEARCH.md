# Neural Sensory Protocol — Visual Rendering Research

> **Status:** Early research / concept development
> **Author:** Kevin Qi
> **Created:** 2026-02-06
> **Location:** Mindloft drafts (research playground)
> **Related:** QIF-FIELD-NOTES.md Entry 2, Qinnovate NSP Use-Case

---

## 1. Vision

Create a lightweight, post-quantum secure protocol for encoding and rendering visual data to the visual cortex via a BCI — enabling blind individuals to "see" through a secure, on-device processing pipeline. No cloud dependency. Real-time. Secure from day one.

---

## 2. The Problem

No protocol exists for how a BCI should encode, transmit, and render sensory data to the brain. Current BCIs use proprietary, ad hoc signal processing. This is the equivalent of the pre-TCP/IP internet — every system speaks its own language, security is an afterthought, and interoperability is nonexistent.

**Historical parallel:**
| Internet era | BCI equivalent today |
|---|---|
| Pre-TCP/IP: every network proprietary | Every BCI uses proprietary encoding |
| HTTP without encryption | Neural data transmitted without quantum-secure encryption |
| IPv4 address exhaustion | No forward-planning for scale or key space |
| Security bolted on after deployment | No security standard exists yet |

The opportunity: build it right the first time.

---

## 3. Concept: "Neural HTML"

A lightweight encoding protocol — inspired by HTML's simplicity — that wraps sensory data for delivery to the visual cortex.

### Why HTML as inspiration?

- Simple, easy to learn, widely understood
- Lightweight — minimal compute overhead
- Declarative — describes WHAT to render, not HOW (the brain handles the "how")
- Extensible — can add new sensory modalities (audio, haptic) without redesigning the core
- Open standard — anyone can implement it

### What "Neural HTML" would encode:

- Object identity (what is it?)
- Spatial position (where is it relative to the user?)
- Depth / distance
- Motion vectors
- Brightness / contrast gradients
- Color information (if the cortical implant supports it)
- Temporal sequencing (animation, movement)

### What it would NOT encode:

- Pixel-level rendering (the brain doesn't process pixels — it processes features)
- Full video streams (too much data for current BCI bandwidth)
- Anything requiring cloud round-trip

---

## 4. The Processing Pipeline

```
SENSE INPUT                    ON-DEVICE AI                NEURAL ENCODING              SECURE DELIVERY           CORTICAL RENDERING
─────────────                  ────────────                ───────────────              ───────────────           ──────────────────
Camera / Lidar / Mic     →    Object recognition     →    "Neural HTML"           →    Post-quantum         →    BCI stimulates
on body (non-invasive)        Spatial mapping              encodes scene                encryption                visual cortex
                              Depth estimation             as structured data           (on-chip)                 Brain reconstructs
                              OCR for text                                                                        the scene
                              Local LLM inference
```

**All on-device. No cloud. Post-quantum secure from day one.**

---

## 5. Why Lightweight Matters

### The power budget constraint

| Device | Total Power | Available for Compute | Available for Stimulation |
|---|---|---|---|
| Neuralink N1 | 24.7 mW | TBD | TBD |
| BrainGate (Utah array) | ~30 mW (estimated) | TBD | TBD |
| Cochlear implant (reference) | ~1-5 mW | TBD | TBD |
| *(More devices to be added from research)* | | | |

If the protocol is lightweight enough:
- The entire OS + AI + encryption fits on a small chip
- Processing stays local (no cloud = no latency = real-time)
- More power budget available for actual neural stimulation
- Smaller device = less invasive = better biocompatibility

### The Moore's Law question

Kevin's hypothesis: Moore's Law can predict when BCI chips will have enough onboard compute for real-time neural rendering. At the quantum limit, Moore's Law breaks — but quantum computing provides the next curve. The QI equation may contain the bridge between these two scaling regimes.

---

## 6. Security Architecture

### Post-quantum from day one

The protocol must be encrypted with post-quantum algorithms before NIST's migration deadline. Rationale:
- Neural data is the most sensitive data possible (thoughts, perceptions, memories)
- "Harvest now, decrypt later" attacks mean data captured TODAY could be decrypted by future quantum computers
- Building classical encryption first and upgrading later repeats every mistake the internet made

### Threat model (from QIF)

| Attack | Protocol defense |
|---|---|
| Replay attack (inject previously seen image) | Temporal nonce / freshness token in every frame |
| Eavesdropping (intercept neural data) | End-to-end post-quantum encryption |
| Signal injection (inject false visual data) | Coherence metric Cₛ validation |
| Man-in-the-middle | QKD or post-quantum key exchange at I0 |
| Data exfiltration | All processing local, no cloud transmission |

---

## 7. The "Fixing Blindness" Use Case

### Phase 1: Audio (proving ground)
- Cochlear implants already encode audio for the brain
- Create a standardized, secure version of the encoding protocol
- Prove the protocol architecture works for one sense

### Phase 2: Visual (the goal)
- Encode visual scene data from camera/lidar/sensors
- Local AI processes scene into structured representation
- "Neural HTML" encodes the representation
- BCI delivers to visual cortex via electrical stimulation
- User perceives a reconstructed scene

### What existing technology can do NOW:
- Object recognition: state of the art (YOLO, SAM, etc.)
- Spatial mapping: lidar on smartphones already does this
- OCR: mature technology
- Real-time rendering from recognition data: Unreal Engine, NVIDIA Omniverse
- Visual cortex stimulation: Orion (Second Sight), Gennaris (Monash), cortical BCI research

### What's missing:
- A standard protocol connecting these pieces
- Post-quantum security at every layer
- A lightweight enough implementation to run on a BCI chip
- Understanding of how much data the visual cortex needs (minimum viable image)

---

## 8. Comparison to Web Rendering

Kevin's insight: if we can calculate the energy to render a webpage client-side, we have a baseline for neural rendering requirements.

| Metric | Web browser | Neural rendering (estimated) |
|---|---|---|
| Power to render | ~500 mW - 2W (mobile browser) | Must fit in ~5-10 mW budget |
| Data rate | ~1-50 Mbps (typical page) | ~10-100 kbps (BCI bandwidth limit) |
| Latency tolerance | ~100-300 ms acceptable | <50 ms for real-time perception |
| Rendering model | Pixel-based (GPU rasterization) | Feature-based (brain does the rendering) |
| Protocol | HTML/CSS/JS over HTTPS | "Neural HTML" over post-quantum encryption |

The key difference: the brain does the rendering. The protocol only needs to deliver FEATURES (edges, objects, spatial relationships), not pixels. This dramatically reduces bandwidth and compute requirements.

---

## 9. Open Research Questions

1. What is the minimum data rate needed for useful visual perception via BCI?
2. How does the visual cortex encode spatial relationships — and can we reverse-engineer a protocol from that encoding?
3. What is the energy per electrode needed for reliable visual cortex stimulation?
4. Can post-quantum encryption (lattice-based, hash-based) run within a 5-10 mW power budget?
5. Is there a compression algorithm optimized for neural feature encoding (not pixel encoding)?
6. How does the "neural HTML" concept relate to existing work on phosphene mapping in visual prostheses?
7. Can the same protocol framework extend to other senses (haptic, proprioceptive, olfactory)?

---

## 10. References and Inspiration

- **MKBHD + Epic Spaceman:** Apple chip architecture breakdown — "what's next?" → quantum
- **Jensen Huang / NVIDIA:** Investment in real-time rendering from recognition data (Omniverse, digital twins)
- **Unreal Engine:** Scene rendering from object recognition — the game engine as neural rendering prototype
- **Second Sight Orion:** Visual cortical prosthesis — direct cortical stimulation for blindness
- **Monash Gennaris:** 9-tile cortical implant for visual prosthesis research
- **QIF Threat Model:** `config.py THREAT_MODEL` — maps attacks to bands and detection methods
- **ONI 14-Layer Model:** Classical layer-by-layer security analysis framework

---

*Document version: 0.1 (concept stage)*
*Next steps: Claude classical analysis, Gemini quantum review, energy calculations, BCI power budget table*
