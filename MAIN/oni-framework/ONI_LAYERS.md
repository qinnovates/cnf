# ONI Layer Model Reference

> **ONI**: Organic Neurocomputing Interface — A 14-layer framework extending OSI for brain-computer interface (BCI) security.

---

## Table of Contents

- [Executive Summary](#executive-summary)
- [Privacy & Ethics Statement](#privacy--ethics-statement)
- [Complete 14-Layer Model](#complete-14-layer-model)
  - [OSI Stack — Classical Networking (L1-L7)](#osi-stack--classical-networking-l1-l7)
  - [ONI Extension Stack — Neural & Cognitive Systems (L8-L14)](#oni-extension-stack--neural--cognitive-systems-l8-l14)
- [Visual Summary](#visual-summary)
- [Why This Architecture Works](#why-this-architecture-works)
- [Threat Landscape by Layer](#threat-landscape-by-layer)
- [External Physical Threats](#external-physical-threats)
- [Coherence Score (Cₛ) Across Layers](#coherence-score-cₛ-across-layers)
- [Scale-Frequency Invariant](#scale-frequency-invariant)
- [Implementation Guide](#implementation-guide)
  - [For BCI Developers](#for-bci-developers)
  - [For Security Researchers](#for-security-researchers)
  - [For Neuroethicists](#for-neuroethicists)
- [References](#references)
- [Changelog](#changelog)

---

## Executive Summary

The ONI Framework extends the classical OSI 7-layer networking model with 7 additional layers (L8-L14) specifically designed for neural and cognitive systems. This creates a complete security model for brain-computer interfaces.

**Key Principle:**
- **OSI (L1-L7)** answers: *How does data move?*
- **ONI (L8-L14)** answers: *Should it move, can it be trusted, and what does it mean—especially when the endpoint is a human brain?*

**L8 (Neural Gateway) is the critical boundary:**
- No neural data crosses without policy, trust, and security validation
- This is where the ONI Firewall operates
- Most attacked, least standardized, most dangerous layer

---

## Privacy & Ethics Statement

**ONI is NOT a surveillance framework.**

The ONI Framework exists to **protect** neural privacy and ensure the **integrity** of brain-computer interfaces. Its purpose is:

- **Defense** against malicious attacks (nation-state actors, cybercriminals)
- **Protection** from accidental risks (MRI exposure, electromagnetic interference, device malfunction)
- **Privacy preservation** ensuring neural data remains confidential
- **Availability** maintaining BCI functionality when users depend on it
- **Human sovereignty** keeping humans in control of their own neural interfaces

The framework provides security without requiring surveillance. Signal integrity can be validated without reading thoughts. Attacks can be detected without decoding intent.

---

## Complete 14-Layer Model

<p align="center">
  <img src="../resources/images/oni-14-layer-hourglass.png" alt="ONI Framework 14-Layer Model" width="700">
</p>

### OSI Stack — Classical Networking (L1-L7)

These layers handle data movement. They do not know or care about brains.

| Layer | Name | Domain | Function | Examples |
|-------|------|--------|----------|----------|
| **L1** | Physical | OSI | Transmission of raw bits over a medium | Copper, fiber optics, RF |
| **L2** | Data Link | OSI | Framing, MAC addressing, local delivery | Ethernet, Wi-Fi, Bluetooth |
| **L3** | Network | OSI | Logical addressing and routing | IP, ICMP, BGP |
| **L4** | Transport | OSI | End-to-end delivery, flow control | TCP, UDP, QUIC |
| **L5** | Session | OSI | Connection lifecycle management | TLS sessions, RPC |
| **L6** | Presentation | OSI | Encoding, encryption, compression | TLS, JSON, ASN.1 |
| **L7** | Application | OSI | User-facing network services | HTTP, REST APIs |

**Stop here for traditional networking.** No neurons. No spikes. No cognition. This discipline is what gives ONI legitimacy.

---

### ONI Extension Stack — Neural & Cognitive Systems (L8-L14)

This is where the brain enters the network.

#### L8 — Neural Gateway (Hard Boundary Layer)

| Attribute | Value |
|-----------|-------|
| **Domain** | Bridge (Biology ↔ Silicon) |
| **Function** | Physical and logical interface between neural tissue and computation |
| **Signals** | Action potentials, local field potentials |
| **Frequency** | ~1–500 Hz |
| **Scale** | μm–mm |
| **Examples** | Utah arrays, Neuralink threads, ECoG grids, cochlear implants |

**This is the firewall layer.** All security policy enforcement happens here:
- Read/write access control
- Signal validation and provenance
- Trust establishment
- Isolation enforcement

#### L9 — Signal Processing

| Attribute | Value |
|-----------|-------|
| **Domain** | Biology |
| **Function** | Filtering, amplification, denoising, digitization |
| **Signals** | Sampled neural waveforms, spike trains |
| **Frequency** | 1–500 Hz (sampled at kHz rates) |
| **Scale** | Embedded systems, edge compute |
| **Examples** | Spike sorting, FFT analysis, adaptive filters |

#### L10 — Neural Protocol

| Attribute | Value |
|-----------|-------|
| **Domain** | Biology |
| **Function** | Mapping neural signals to machine-readable formats |
| **Signals** | Encoded spike patterns, feature vectors |
| **Frequency** | Event-driven |
| **Scale** | Device ↔ compute node |
| **Examples** | Neural codecs, BCI data schemas, protocol buffers |

#### L11 — Cognitive Transport

| Attribute | Value |
|-----------|-------|
| **Domain** | Biology |
| **Function** | Reliable transmission of neural/cognitive state |
| **Signals** | Structured cognitive packets |
| **Frequency** | Seconds → minutes |
| **Scale** | Distributed systems |
| **Examples** | Cognitive state streaming, redundancy checks, integrity validation |

#### L12 — Cognitive Session

| Attribute | Value |
|-----------|-------|
| **Domain** | Cognitive Systems |
| **Function** | Context persistence, working memory windows |
| **Signals** | Sustained activation patterns |
| **Frequency** | Seconds → minutes |
| **Scale** | Distributed cortical networks |
| **Examples** | Attention windows, task context, session state |

#### L13 — Semantic Layer

| Attribute | Value |
|-----------|-------|
| **Domain** | Cognitive / Executive |
| **Function** | Meaning construction, goal formation, agency |
| **Signals** | Distributed semantic representations |
| **Frequency** | Minutes → hours |
| **Scale** | Association cortex, PFC loops |
| **Examples** | Concept binding, decision policies, action planning, intent decoding |

#### L14 — Identity Layer

| Attribute | Value |
|-----------|-------|
| **Domain** | Human |
| **Function** | Self-model, moral reasoning, long-term coherence |
| **Signals** | Integrated whole-brain patterns |
| **Frequency** | Days → lifetime |
| **Scale** | Whole brain |
| **Examples** | Personal identity, values, ethical constraints, continuity of self |

---

## Visual Summary

```
┌─────────────────────────────────────────────────────────────┐
│                    L14: Identity Layer                       │
│              Self-model, ethics, continuity                  │
├─────────────────────────────────────────────────────────────┤
│                   L13: Semantic Layer                        │
│              Meaning, intent, goals                          │
├─────────────────────────────────────────────────────────────┤
│                 L12: Cognitive Session                       │
│              Context, attention, working memory              │
├─────────────────────────────────────────────────────────────┤
│                L11: Cognitive Transport                      │
│              Reliable neural data delivery                   │
├─────────────────────────────────────────────────────────────┤
│                  L10: Neural Protocol                        │
│              Neural data formatting                          │
├─────────────────────────────────────────────────────────────┤
│                L9: Signal Processing                         │
│              Filtering, digitization                         │
╠═════════════════════════════════════════════════════════════╣
│           ████  L8: NEURAL GATEWAY  ████                     │
│           ████    ONI FIREWALL      ████                     │
│              Trust, Policy, Security                         │
╠═════════════════════════════════════════════════════════════╣
│                  L7: Application (OSI)                       │
│              HTTP, APIs, user services                       │
├─────────────────────────────────────────────────────────────┤
│                 L6: Presentation (OSI)                       │
│              Encoding, encryption                            │
├─────────────────────────────────────────────────────────────┤
│                   L5: Session (OSI)                          │
│              Connection management                           │
├─────────────────────────────────────────────────────────────┤
│                  L4: Transport (OSI)                         │
│              TCP/UDP, flow control                           │
├─────────────────────────────────────────────────────────────┤
│                   L3: Network (OSI)                          │
│              IP routing, addressing                          │
├─────────────────────────────────────────────────────────────┤
│                  L2: Data Link (OSI)                         │
│              Framing, MAC addresses                          │
├─────────────────────────────────────────────────────────────┤
│                  L1: Physical (OSI)                          │
│              Bits on wire, electrical signals                │
└─────────────────────────────────────────────────────────────┘
```

---

## Why This Architecture Works

### 1. OSI Remains Untouched
L1-L7 are exactly what network engineers expect. No biological concepts leak into networking layers.

### 2. Clean Separation of Concerns
- **L1-L7:** Data movement (networking)
- **L8:** Trust boundary (security)
- **L9-L14:** Meaning and cognition (neural)

### 3. L8 as True Choke Point
All data crossing between silicon and biology must pass through L8. This is not a metaphor—it's an enforcement point.

### 4. Standards Alignment
ONI can adopt existing standards:
- L1-L7: IEEE, IETF standards
- L8-L10: Medical device standards (IEC 62443, FDA guidance)
- L11-L14: Emerging neuroethics frameworks

> **⚠️ Future Work (L11-L14):** Unlike the mature standards for L1-L10, no established international standards currently exist for cognitive and identity-layer security. Standards development for L11-L14 requires collaboration with subject matter experts (neuroethicists, cognitive scientists, BCI researchers) and governing agencies (FDA, EU MDR, IEEE, UNESCO, OECD). See `MAIN/governance/POST_DEPLOYMENT_ETHICS.md` and `prd.json` item `future-l11-l14-standards-development` for tracking.

### 5. Scalability
The model works for:
- Current BCIs (cochlear implants, deep brain stimulators)
- Near-term BCIs (Neuralink, Synchron)
- Future neural networks and brain-to-brain interfaces

---

## Threat Landscape by Layer

| Layer | Primary Threats | Defense Strategy |
|-------|-----------------|------------------|
| **L1-L4** | Network attacks, MitM, DDoS | Standard network security |
| **L5-L7** | Application exploits, injection | Input validation, encryption |
| **L8** | Bypass attacks, unauthorized access | ONI Firewall, coherence validation |
| **L9** | Signal injection, jamming | Anomaly detection, hardware validation |
| **L10** | Protocol manipulation | Schema validation, checksums |
| **L11-L12** | Session hijacking, state corruption | Session tokens, integrity checks |
| **L13** | Intent manipulation, semantic attacks | Context validation, anomaly detection |
| **L14** | Identity attacks, long-term manipulation | Behavioral baselines, ethics filters |

---

## External Physical Threats

BCIs face unique threats from the physical environment:

| Threat | Description | Detection | Mitigation |
|--------|-------------|-----------|------------|
| **MRI Exposure** | Strong magnetic fields can damage implants or cause heating | Pre-scan protocols | MRI-conditional designs |
| **Electromagnetic Interference** | RF, power lines, industrial equipment | EMI signature detection | Shielding, filtering |
| **Physical Trauma** | Impact to head affecting implant | Accelerometer data, signal disruption | Ruggedized designs |
| **Intentional Jamming** | Deliberate RF interference | Signal quality monitoring | Frequency hopping |
| **Proximity Attacks** | ProxMark-style RFID/NFC attacks | Unexpected command sequences | Authentication, encryption |
| **ESD/Lightning** | Electrostatic discharge | Transient detection | Surge protection |

---

## Coherence Score (Cₛ) Across Layers

The Coherence Score measures signal integrity and trustworthiness:

```
Cₛ = e^-(σ²ᵩ + σ²τ + σ²γ)

Where:
  σ²ᵩ = Phase variance (timing jitter)
  σ²τ = Transport variance (pathway reliability)
  σ²γ = Gain variance (amplitude stability)
```

| Layer | Coherence Role |
|-------|----------------|
| **L8** | Primary validation point—signals with Cₛ < threshold are blocked |
| **L9** | Hardware-level coherence (SNR, impedance) |
| **L10-L11** | Protocol-level coherence (packet integrity) |
| **L12-L14** | Cognitive coherence (semantic consistency) |

---

## Scale-Frequency Invariant

A fundamental constraint observed across neural systems:

```
f × S ≈ k

Where:
  f = Frequency (Hz)
  S = Spatial scale
  k = Constant (~20-25 for neural systems)
```

This invariant helps validate signals: violations may indicate attacks or malfunctions.

| Scale | Typical Frequency | f × S |
|-------|-------------------|-------|
| Synapse (μm) | ~1000 Hz | ~1 |
| Microcircuit (mm) | ~100 Hz | ~100 |
| Region (cm) | ~10 Hz | ~100 |
| Whole brain | ~1 Hz | ~100 |

---

## Implementation Guide

### For BCI Developers

1. **Implement L8 first** — This is your security foundation
2. **Use Cₛ validation** — Block signals below coherence threshold
3. **Monitor L9 metrics** — Impedance, SNR, signal quality
4. **Log all boundary crossings** — Audit trail for L8 events

### For Security Researchers

1. **Focus on L8 attacks** — Most impactful, least standardized
2. **Study coherence manipulation** — Can attackers fake Cₛ?
3. **Cross-layer attacks** — How do L1-L7 attacks propagate to L8+?
4. **Develop detection signatures** — For NSAM integration

### For Neuroethicists

1. **L14 is the identity layer** — What protections are needed?
2. **Consent at L8** — How is read/write permission granted?
3. **L13 intent privacy** — Can intent be validated without being read?

---

## References

- OSI Model: ISO/IEC 7498-1
- Medical Device Cybersecurity: FDA Guidance 2023
- BCI Security: [ONI Framework Publications](../publications/0-oni-framework/)
- Coherence Metric: [Technical Document](../publications/coherence-metric/)
- Neural Firewall: [Technical Document](../publications/neural-firewall/)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 2.1 | 2026-01-24 | Fixed L9-L11 domain labels: Silicon → Biology (L9+ is neural side of bridge) |
| 2.0 | 2026-01-22 | Major revision: L1-L7 now pure OSI, L8-L14 neural extension |
| 1.0 | 2026-01 | Initial release with biological L1-L7 (deprecated) |

---

*This document is the authoritative reference for ONI layer definitions. All other documentation should reference this file.*

*Last Updated: 2026-01-24*
