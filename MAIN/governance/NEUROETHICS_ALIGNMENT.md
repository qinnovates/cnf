# ONI Framework: Neuroethics Alignment

> How the ONI Framework addresses core principles of neuroethics and cognitive liberty.

**Last Updated:** 2026-01-22
**Version:** 1.0

---

## Overview

The ONI Framework was designed with neuroethical principles as foundational constraints, not afterthoughts. This document maps each framework component to the ethical principles it protects and explains the design decisions through a neuroethics lens.

---

## Privacy & Ethics Statement

**ONI is NOT a surveillance framework.**

The ONI Framework exists to **protect** neural privacy and ensure the **integrity** of brain-computer interfaces. Its purpose is:

- **Defense** against malicious attacks (nation-state actors, cybercriminals, ransomware)
- **Protection** from accidental risks (MRI exposure, electromagnetic interference, device malfunction)
- **Privacy preservation** ensuring neural data remains confidential
- **Availability** maintaining BCI functionality when users depend on it
- **Human sovereignty** keeping humans in control of their own neural interfaces

The framework provides security without requiring surveillance. Signal integrity can be validated without reading thoughts. Attacks can be detected without decoding intent. The goal is to implement BCI security that preserves confidentiality, integrity, and availability — the same principles that protect all other computing systems.

---

## Core Neuroethics Principles

The following principles are widely recognized in neuroethics literature (Ienca & Andorno, 2017; Yuste et al., 2017; UNESCO, 2021):

| Principle | Definition | Threat Without Protection |
|-----------|------------|---------------------------|
| **Cognitive Liberty** | Right to mental self-determination; freedom from unauthorized interference | External control of thoughts, forced neural modification |
| **Mental Privacy** | Right to keep neural data and mental states confidential | Unauthorized brain reading, thought surveillance |
| **Mental Integrity** | Right to protection from unauthorized alteration of neural function | Neural hacking, cognitive manipulation, "brain malware" |
| **Psychological Continuity** | Right to maintain personal identity and sense of self | Identity manipulation, memory tampering, personality modification |
| **Cognitive Authenticity** | Right to know which thoughts/intentions are genuinely one's own | Implanted thoughts, covert influence, confusion of agency |

---

## Framework-to-Ethics Mapping

### 1. Coherence Metric (Cₛ) → Cognitive Authenticity

**The Problem**: How does a person (or their BCI) know if a neural signal is genuinely from their own brain versus injected by an attacker?

**ONI Solution**: The coherence metric quantifies signal trustworthiness across three dimensions:

| Component | What It Measures | Authenticity Protection |
|-----------|------------------|------------------------|
| Phase variance (σ²φ) | Timing consistency | Detects out-of-sync injections that don't match brain rhythms |
| Transport variance (σ²τ) | Pathway integrity | Flags signals bypassing biological routes |
| Gain variance (σ²γ) | Amplitude stability | Catches artificially over/under-powered signals |

**Ethical Reasoning**: A signal that doesn't match expected biological patterns may not be authentic to the user. By scoring coherence, the system provides a *quantitative basis* for authenticity assessment.

**Design Decision**: The formula `Cₛ = e^(−(σ²φ + σ²τ + σ²γ))` was chosen because:
- Exponential decay ensures high sensitivity to small variances
- Multiplicative combination means *any* anomaly reduces trust
- Score range [0,1] enables threshold-based decisions

---

### 2. Neural Firewall (L8) → Cognitive Liberty & Mental Integrity

**The Problem**: How do you prevent unauthorized neural signals from reaching the brain (input attacks) or unauthorized reading of neural signals (output attacks)?

**ONI Solution**: Zero-trust security at the Neural Gateway (Layer 8), where electrodes meet neurons.

| Firewall Feature | Liberty/Integrity Protection |
|------------------|------------------------------|
| Coherence threshold | Blocks signals that don't "belong" |
| Authentication requirement | Ensures signal source is verified |
| Amplitude bounds | Prevents dangerously strong stimulation |
| Rate limiting | Stops flooding/DoS attacks on neural tissue |
| ACCEPT_FLAG state | Allows human review of borderline cases |

**Ethical Reasoning**:
- **Cognitive Liberty**: The firewall enforces the user's right to choose what enters their neural space. Unauthenticated signals are rejected regardless of coherence—you must have permission.
- **Mental Integrity**: Hardware bounds and rate limiting protect against physical harm from overstimulation.

**Design Decision**: The decision matrix requires *both* high coherence AND valid authentication for unconditional acceptance. This embodies the principle that even "good-looking" signals need permission—benevolent paternalism without consent is still a violation.

```
High Coherence + No Auth = REJECT (consent required)
Low Coherence + Valid Auth = REJECT (harm prevention)
```

---

### 3. 14-Layer Model → Comprehensive Threat Mapping

**The Problem**: Where can attacks occur? Where should defenses be placed?

**ONI Solution**: A complete architectural model from molecules to applications, with attack surfaces and defenses catalogued at each layer.

| Layer Range | Ethical Concern | ONI Contribution |
|-------------|-----------------|------------------|
| L1-L3 (Molecular→Microcircuit) | Biological manipulation at cellular level | Identifies attack surfaces; notes biological defenses |
| L4-L7 (Regional→Behavioral) | Higher-order cognitive manipulation | Maps system-level vulnerabilities |
| L8 (Neural Gateway) | The critical boundary | Places firewall at bio-digital interface |
| L9-L14 (Silicon) | Digital attack vectors | Standard cybersecurity applies |

**Ethical Reasoning**: You cannot protect what you cannot name. The 14-layer model provides *vocabulary* for discussing neural security across disciplines (neuroscience, security, ethics, law).

**Design Decision**: Layer 8 is explicitly marked as the "firewall layer" because:
- It's the boundary between biological autonomy and digital control
- Attacks at L8 can propagate in both directions
- Defense-in-depth requires strongest protection at the interface

---

### 4. Scale-Frequency Invariant → Anomaly Detection for Mental Integrity

**The Problem**: How do you detect signals that are technically "correct" but biologically implausible?

**ONI Solution**: The f × S ≈ k invariant validates that signal frequencies match the spatial scale they claim to originate from.

| Check | What It Catches | Integrity Protection |
|-------|-----------------|---------------------|
| Frequency vs. scale | Signals with wrong frequency for claimed origin | Attacker using 100Hz to target whole-brain (should be ~1Hz) |
| Deviation scoring | How "wrong" a signal is | Graduated response based on anomaly severity |
| Hierarchy validation | Does signal fit known neural processing levels? | Flags signals that don't match any biological scale |

**Ethical Reasoning**: An attacker might craft a signal that passes coherence checks but targets the wrong level of neural processing. Scale-frequency validation provides a *biological plausibility check* independent of signal quality.

---

### 5. Transport Variance → Mental Privacy Protection

**The Problem**: How do you detect if someone is accessing neural signals through unauthorized pathways?

**ONI Solution**: Transport variance (σ²τ) measures pathway integrity based on expected reliability of biological signal routes.

**Ethical Reasoning**: If a signal arrives via an unexpected pathway (bypassing normal synaptic routes), it may indicate:
- Unauthorized access point
- Compromised electrode
- Side-channel attack

By modeling expected pathway reliability, the system can flag signals that "took the wrong route"—a potential privacy breach.

---

### 6. Signal Rejection → Cognitive Sovereignty

**The Problem**: Who has final say over what enters or exits the neural space?

**ONI Solution**: The firewall's REJECT decision is absolute. Rejected signals do not reach neural tissue.

**Ethical Design Principles**:

1. **Default Deny**: Unknown signals are rejected, not accepted
2. **User Override**: System should support user-configurable thresholds (future work)
3. **Transparency**: Every rejection includes a reason (`result.reason`)
4. **Logging**: All decisions logged for audit (`firewall.log`)

**Ethical Reasoning**: Cognitive sovereignty means the human retains ultimate authority. The firewall is a *tool* that implements the user's policy, not an autonomous gatekeeper making independent judgments about what's "good" for the user.

---

## Ethical Design Decisions Summary

| Decision | Alternatives Considered | Ethical Reasoning for Choice |
|----------|------------------------|------------------------------|
| Exponential coherence decay | Linear scoring | Higher sensitivity to anomalies protects integrity |
| Authentication required even for high-coherence signals | Coherence-only acceptance | Consent is non-negotiable; quality doesn't imply permission |
| ACCEPT_FLAG intermediate state | Binary accept/reject | Allows human review; preserves user agency in edge cases |
| Open-source framework | Proprietary/closed | Transparency enables scrutiny; security through obscurity fails |
| Explicit documentation of limitations | Marketing-style claims | Honesty about research status enables informed adoption |

---

## Gaps and Future Work

### Currently Unaddressed

| Ethical Concern | Status | Notes |
|-----------------|--------|-------|
| **Informed Consent Mechanisms** | Not implemented | Framework validates signals but doesn't manage consent workflows |
| **User Override Interface** | Designed, not built | Users should be able to adjust thresholds based on risk tolerance |
| **Long-term Identity Protection** | Theoretical only | Psychological continuity requires longitudinal monitoring not in scope |
| **Pediatric/Incapacity Considerations** | Not addressed | Surrogate decision-making adds complexity |
| **Dual-Use Concerns** | Acknowledged | Security tools can inform attacks; mitigated by open publication |

### Planned Additions

1. **Neural Authentication Module** — Identity verification via neural signatures
2. **Consent Protocol Integration** — Hooks for consent management systems
3. **Adversarial Testing Framework** — Validate defenses against known attack patterns
4. **Regulatory Compliance Mapping** — FDA, EU AI Act, UNESCO recommendations

---

## Alignment with Regulatory Frameworks

| Framework | ONI Alignment |
|-----------|---------------|
| **UNESCO Recommendation on Neuroethics (2021)** | Cognitive liberty, mental privacy, mental integrity explicitly addressed |
| **EU AI Act (2024)** | High-risk AI system transparency requirements met via documentation |
| **FDA Neural Device Guidance (2023)** | Security-by-design principles implemented |
| **IEEE Neuroethics Framework (2020)** | Human agency and oversight emphasized |

---

## For Academic Review

This document demonstrates:

1. **Ethical Grounding**: Technical decisions traced to ethical principles
2. **Comprehensive Coverage**: All major neuroethics concerns addressed or explicitly noted as gaps
3. **Design Transparency**: Alternatives considered and reasoning documented
4. **Intellectual Honesty**: Limitations acknowledged; framework positioned as research, not solution

---

## References

Ienca, M., & Andorno, R. (2017). Towards new human rights in the age of neuroscience and neurotechnology. *Life Sciences, Society and Policy*, 13(1), 5.

Yuste, R., Goering, S., Arcas, B. A. Y., et al. (2017). Four ethical priorities for neurotechnologies and AI. *Nature*, 551(7679), 159-163.

UNESCO. (2021). *Recommendation on the Ethics of Artificial Intelligence*.

---

← Back to [INDEX.md](../INDEX.md) | [TRANSPARENCY.md](TRANSPARENCY.md)
