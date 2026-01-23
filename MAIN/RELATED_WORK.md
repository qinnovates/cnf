# Related Work: BCI Security Research Landscape

**ONI Framework Context Document**

This document acknowledges the foundational and concurrent research in brain-computer interface (BCI) security that informs and complements the ONI Framework. The ONI Framework builds upon this body of work rather than claiming to be the first in the field.

---

## Table of Contents

- [Foundational Work](#foundational-work)
- [Standards and Frameworks](#standards-and-frameworks)
- [Privacy and Anonymization](#privacy-and-anonymization)
- [Threat Modeling](#threat-modeling)
- [Hardware Security](#hardware-security)
- [Neuroethics](#neuroethics)
- [How ONI Differs](#how-oni-differs)
- [References](#references)

---

## Foundational Work

### Neurosecurity: The Seminal Paper (2009)

The term "neurosecurity" was coined by **Tadayoshi Kohno** and colleagues at the University of Washington in their 2009 paper:

> Denning, T., Matsuoka, Y., & Kohno, T. (2009). Neurosecurity: Security and privacy for neural devices. *Neurosurgical Focus*, 27(1), E7.

**Key Contributions:**
- First formal application of computer security principles to neural engineering
- Established the CIA triad (Confidentiality, Integrity, Availability) for BCIs:
  - **Confidentiality**: Protection against neural eavesdropping, thought extraction
  - **Integrity**: Prevention of signal hijacking, unauthorized stimulation
  - **Availability**: Ensuring device functionality when needed (life-critical for some users)
- Identified threat actors: malicious individuals, organizations, nation-states
- Proposed defense mechanisms: access control, encryption, anomaly detection
- Anticipated regulatory gaps that still exist today

**ONI Framework Relationship:** The ONI Framework adopts Kohno's CIA triad framing and extends it with specific architectural implementation through the 14-layer model and Coherence Metric.

---

## Standards and Frameworks

### IEEE Brain Initiative (2020-present)

The IEEE has ongoing standardization efforts for brain-machine interfaces:

> IEEE Standards Association. (2020). IEEE Brain Initiative: Standards Roadmap for Brain-Machine Interfaces.

**Key Contributions:**
- Industry collaboration on BMI standards
- Signal quality benchmarks
- Interoperability specifications
- Safety requirements

**ONI Framework Relationship:** ONI provides a complementary security-focused layer model that could interface with IEEE's broader standardization efforts.

### FDA Regulatory Framework

The FDA regulates BCIs as Class II or Class III medical devices:

- **510(k) Pathway**: For devices substantially equivalent to existing products
- **De Novo Pathway**: For novel low-to-moderate risk devices
- **PMA (Premarket Approval)**: For Class III high-risk devices (implantables)

**Key Documents:**
- FDA Guidance on Implanted Brain-Computer Interface Devices (2021)
- Breakthrough Device Designation (granted to Neuralink, Synchron, others)

**ONI Framework Relationship:** ONI is designed to be compatible with FDA regulatory requirements, providing security checkpoints that align with safety validation requirements.

---

## Privacy and Anonymization

### BCI Anonymizer (University of Washington)

Developed by researchers at UW, the BCI Anonymizer addresses neural data privacy:

> Bonaci, T., Calo, R., & Chizeck, H. J. (2015). App stores for the brain: Privacy and security in brain-computer interfaces. *IEEE Technology and Society Magazine*, 34(2), 32-39.

**Key Contributions:**
- Filters sensitive information from EEG data before transmission
- Demonstrates that raw neural signals contain extractable private information
- Proposes privacy-preserving signal processing pipeline

**ONI Framework Relationship:** The ONI Framework's Layer 13 (Semantic) and Layer 14 (Identity) incorporate privacy filtering concepts similar to BCI Anonymizer's approach.

### Neural Privacy Research

> Ienca, M., & Andorno, R. (2017). Towards new human rights in the age of neuroscience and neurotechnology. *Life Sciences, Society and Policy*, 13(1), 5.

**Key Contributions:**
- Proposed "neurorights": cognitive liberty, mental privacy, mental integrity, psychological continuity
- Framework adopted by Chile's constitutional amendment (2021) — first country to protect neurorights

**ONI Framework Relationship:** ONI's Layer 14 (Identity & Ethics) explicitly addresses psychological continuity and mental integrity as security properties.

---

## Threat Modeling

### 6-Layer BCI Threat Model

Several researchers have proposed layered threat models for BCIs:

> Landau, O., Puzis, R., & Nissim, N. (2020). Mind your privacy: Privacy leakage through BCI applications using machine learning. *Knowledge-Based Systems*, 198, 105932.

**Key Contributions:**
- Categorization of BCI attack surfaces
- Machine learning-based privacy attacks
- Demonstration of information leakage through legitimate BCI use

### STRIDE for Medical Devices

Microsoft's STRIDE threat model has been applied to medical devices:

> **S**poofing, **T**ampering, **R**epudiation, **I**nformation disclosure, **D**enial of service, **E**levation of privilege

**ONI Framework Relationship:** The ONI Framework maps specific attack vectors to layers (L8-L14) rather than using abstract threat categories, enabling more targeted defenses.

---

## Hardware Security

### Archimedes Center for Healthcare and Device Security

Founded by **Kevin Fu** at Northeastern University (formerly University of Michigan):

**Key Contributions:**
- Extensive research on medical device security
- Pacemaker/ICD vulnerability research
- EMI attack vectors on implantables
- FDA advisory work

**Relevant Papers:**
> Halperin, D., Heydt-Benjamin, T. S., Ransford, B., Clark, S. S., Defend, B., Morgan, W., ... & Fu, K. (2008). Pacemakers and implantable cardiac defibrillators: Software radio attacks and zero-power defenses. *IEEE Symposium on Security and Privacy*.

**ONI Framework Relationship:** ONI's Layer 8 (Neural Gateway) incorporates hardware security principles from medical device security research.

### SIMS Lab (Rice University)

**Kaiyuan Yang**'s Security of Implantable Medical Systems Lab:

**Key Contributions:**
- Low-power security for implantables
- Side-channel attack mitigation
- Energy-efficient authentication

**ONI Framework Relationship:** ONI's power budget constraints (25mW total, ~3-5mW for firewall) are informed by this research on implantable device limitations.

---

## Neuroethics

### Digital Ethics and Neurotechnology

**Luciano Floridi** (Yale/Oxford) and colleagues have established ethical frameworks for neurotechnology:

> Floridi, L. (2023). The Ethics of Artificial Intelligence: Principles, Challenges, and Opportunities. Oxford University Press.

**Key Contributions:**
- Information ethics applied to neural data
- Agency and autonomy in human-AI systems
- Governance frameworks for emerging technologies

### Neuroethics Societies

- **International Neuroethics Society (INS)**
- **IEEE Brain Initiative Neuroethics Working Group**
- **OECD Neurotechnology Governance Initiative**

**ONI Framework Relationship:** See [NEUROETHICS_ALIGNMENT.md](governance/NEUROETHICS_ALIGNMENT.md) for how ONI maps to established neuroethics principles.

---

## How ONI Differs

While building on this foundational work, the ONI Framework contributes several novel elements:

### 1. OSI Extension Architecture

**Prior Work:** Previous frameworks treat BCI security as a standalone domain.

**ONI Approach:** Extends the established OSI model (L1-L7) with seven additional layers (L8-L14) for neural/cognitive systems. This provides:
- Familiar abstraction for IT security professionals
- Clear mapping between network and neural security concepts
- Interoperability with existing security tools and frameworks

### 2. The Coherence Metric (Cₛ)

**Prior Work:** Anomaly detection based on statistical deviation or ML classifiers.

**ONI Approach:** Introduces a physics-based trust metric:
```
Cₛ = e^(−(σ²φ + σ²τ + σ²γ))
```
Where:
- σ²φ = Phase variance (timing jitter)
- σ²τ = Transport variance (pathway reliability)
- σ²γ = Gain variance (amplitude stability)

This provides a real-time, hardware-implementable trust score independent of training data.

### 3. Scale-Frequency Invariant

**Prior Work:** Frequency analysis at single scales.

**ONI Approach:** Identifies cross-scale relationship:
```
f × S ≈ k
```
This enables anomaly detection across neural scales (molecular to behavioral).

### 4. Layer 8: Neural Gateway

**Prior Work:** Security boundaries described abstractly.

**ONI Approach:** Explicitly defines L8 as THE critical security boundary — the bridge between silicon (L1-L7) and biology (L9-L14). All trust decisions are enforced here.

### 5. Implementation Focus

**Prior Work:** Primarily theoretical frameworks and threat models.

**ONI Approach:** Provides:
- Python reference implementation (`pip install oni-framework`)
- TARA security operations platform
- Specific hardware constraints (25mW power budget, <1ms latency)
- Real-time validation algorithms

### Summary: ONI's Position

| Aspect | Prior Work | ONI Framework |
|--------|------------|---------------|
| **Architecture** | Standalone security | OSI extension (L8-L14) |
| **Trust Metric** | ML-based anomaly detection | Physics-based Coherence Score |
| **Abstraction Level** | Academic/theoretical | Implementation-ready |
| **Target Audience** | Security researchers | Security + engineering teams |
| **Boundary Definition** | Implicit | Explicit Layer 8 gateway |

---

## References

### Foundational Papers

1. Denning, T., Matsuoka, Y., & Kohno, T. (2009). Neurosecurity: Security and privacy for neural devices. *Neurosurgical Focus*, 27(1), E7. https://doi.org/10.3171/2009.4.FOCUS0985

2. Bonaci, T., Calo, R., & Chizeck, H. J. (2015). App stores for the brain: Privacy and security in brain-computer interfaces. *IEEE Technology and Society Magazine*, 34(2), 32-39.

3. Ienca, M., & Andorno, R. (2017). Towards new human rights in the age of neuroscience and neurotechnology. *Life Sciences, Society and Policy*, 13(1), 5.

4. Halperin, D., et al. (2008). Pacemakers and implantable cardiac defibrillators: Software radio attacks and zero-power defenses. *IEEE Symposium on Security and Privacy*.

### Standards and Guidelines

5. IEEE Standards Association. (2020). IEEE Brain Initiative: Standards Roadmap for Brain-Machine Interfaces.

6. U.S. Food and Drug Administration. (2021). Implanted Brain-Computer Interface (BCI) Devices for Patients with Paralysis or Amputation.

### Recent Research

7. Landau, O., Puzis, R., & Nissim, N. (2020). Mind your privacy: Privacy leakage through BCI applications using machine learning. *Knowledge-Based Systems*, 198, 105932.

8. Yuste, R., et al. (2017). Four ethical priorities for neurotechnologies and AI. *Nature*, 551(7679), 159-163.

### Ethics and Governance

9. Floridi, L. (2023). *The Ethics of Artificial Intelligence: Principles, Challenges, and Opportunities*. Oxford University Press.

10. OECD. (2019). Recommendation of the Council on Responsible Innovation in Neurotechnology.

---

## Implementation in ONI Framework

The ONI Framework has integrated the foundational research described above into working code:

### Neurosecurity Module

The `oni.neurosecurity` module implements Kohno's threat model and the BCI Anonymizer architecture:

```python
from oni.neurosecurity import (
    NeurosecurityFirewall,  # Kohno CIA triad validation
    BCIAnonymizer,          # Chizeck & Bonaci patent implementation
    ThreatType,             # ALTERATION, BLOCKING, EAVESDROPPING
    ERPType,                # ERP component classification
    PrivacyScoreCalculator, # Information-criticality metrics
)

# Layer 8 firewall with Kohno's three threat categories
firewall = NeurosecurityFirewall()
decision = firewall.validate(signal)

# BCI Anonymizer for privacy protection
anonymizer = BCIAnonymizer()
result = anonymizer.anonymize(signal_data)
```

### Implementation Details

| Component | Based On | Location |
|-----------|----------|----------|
| `NeurosecurityFirewall` | Kohno (2009) CIA triad | `oni/neurosecurity/firewall.py` |
| `BCIAnonymizer` | Chizeck & Bonaci (2014) patent | `oni/neurosecurity/anonymizer.py` |
| `ThreatType` enum | Kohno threat taxonomy | `oni/neurosecurity/threats.py` |
| `PrivacyScoreCalculator` | Information-criticality metrics | `oni/neurosecurity/privacy_score.py` |

### Full Implementation Guide

For complete implementation details, attack scenarios, and integration strategy, see:

**[NEUROSECURITY_IMPLEMENTATION.md](oni-framework/NEUROSECURITY_IMPLEMENTATION.md)**

---

## Contributing

This document is maintained as part of the ONI Framework. If you know of relevant research that should be included, please:

1. Open an issue or pull request
2. Include full citation in APA format
3. Explain the relationship to ONI Framework

---

*Last Updated: 2026-01-23*
*Part of the [ONI Framework](../README.md)*
