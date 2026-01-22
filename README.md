# 🛡️ Welcome To The ONI Project 🛡️

# ONI Framework

> An extensible framework for monitoring and securing neural communications, designed for transparency and interoperability across brain-computer interfaces (BCIs).

---

## Table of Contents

- [Navigation](#navigation)
- [Python Library](#python-library)
- [Repository Structure](#repository-structure)
- [Objective](#objective)
- [Key Components](#key-components)
  - [The 14-Layer ONI Model](#the-14-layer-oni-model)
  - [The Coherence Metric](#the-coherence-metric)
  - [Neural Signal Assurance Model (NSAM)](#neural-signal-assurance-model-nsam)
- [Quick Reference](#quick-reference)
  - [Attack Surfaces by Layer](#attack-surfaces-by-layer)
  - [Hardware Constraints](#hardware-constraints-neuralink-n1-reference)
- [Topics & Documents](#topics--documents)
  - [Coherence Metric](#-coherence-metric)
  - [Neural Firewall](#️-neural-firewall)
  - [Neural Ransomware](#-neural-ransomware)
  - [ONI Framework (Base)](#️-oni-framework-base)
  - [Quantum Encryption](#-quantum-encryption)
  - [Scale-Frequency](#-scale-frequency)
- [About the Author](#about-the-author)
- [Contributing](#contributing)
- [License](#license)

---

## Navigation

| Start Here | Purpose |
|------------|---------|
| **[MAIN/](MAIN/)** | All research content — publications, visualizations, resources |
| **[INDEX.md](MAIN/INDEX.md)** | Central hub — navigation, dependencies, cross-references, roadmap |
| **This README** | Public overview — key concepts, quick reference |

**For deep exploration:** Each topic folder contains an `INDEX.md` with summaries, dependencies, and related topics.

---

## Python Library

[![PyPI version](https://badge.fury.io/py/oni-framework.svg)](https://badge.fury.io/py/oni-framework)
[![Tests](https://github.com/qikevinl/ONI/actions/workflows/tests.yml/badge.svg)](https://github.com/qikevinl/ONI/actions/workflows/tests.yml)

The ONI Framework is available as a Python package for researchers and developers.

### Installation

```bash
pip install oni-framework
```

### Quick Start

```python
from oni import CoherenceMetric, NeuralFirewall, ONIStack

# Calculate signal coherence (Cₛ)
metric = CoherenceMetric(reference_freq=40.0)  # 40 Hz gamma band
cs = metric.calculate(
    arrival_times=[0.0, 0.025, 0.050, 0.075],
    amplitudes=[100, 98, 102, 99]
)
print(f"Coherence Score: {cs:.3f}")  # 0 = untrusted, 1 = fully coherent

# Use the Neural Firewall
firewall = NeuralFirewall(threshold_high=0.6, threshold_low=0.3)
from oni.firewall import Signal
signal = Signal(arrival_times=[0.0, 0.025], amplitudes=[100, 102], authenticated=True)
result = firewall.filter(signal)
print(f"Decision: {result.decision.name}")  # ACCEPT, ACCEPT_FLAG, or REJECT

# Explore the 14-layer model
stack = ONIStack()
print(stack.layer(8).name)  # "Neural Gateway" - the firewall layer
print(stack.ascii_diagram())  # Visual representation
```

**Full documentation:** [MAIN/oni-framework/README.md](MAIN/oni-framework/README.md)

---

## Repository Structure

All research, publications, and supporting infrastructure live in the `MAIN/` directory. Navigate there to explore the full body of work.

```
ONI/
├── README.md                    # Public overview (you are here)
├── CLAUDE.md                    # Claude AI instructions
├── ABOUT.md                     # Author bio
├── CONTRIBUTING.md              # Contribution guidelines
├── LICENSE                      # Apache 2.0
│
└── MAIN/
    ├── INDEX.md                 # Central hub — navigation, dependencies, cross-references
    │
    ├── oni-framework/           # Python library (pip install oni-framework)
    │   ├── oni/                 # Source code
    │   │   ├── coherence.py     # Cₛ calculation
    │   │   ├── layers.py        # 14-layer model
    │   │   ├── firewall.py      # Neural Firewall
    │   │   └── scale_freq.py    # f × S ≈ k invariant
    │   └── tests/               # Unit tests
    │
    ├── publications/            # Research content
    │   ├── 0-oni-framework/     # Base/foundational content
    │   ├── coherence-metric/
    │   ├── neural-firewall/
    │   ├── neural-ransomware/
    │   ├── quantum-encryption/
    │   └── scale-frequency/
    │
    └── resources/               # Infrastructure
        ├── templates/           # Formatting templates
        ├── processes/           # Workflow documentation
        └── pipeline/            # Research pipeline
```

---

## Objective

Brain-computer interfaces are being implanted in humans today, yet we lack standardized security frameworks for protecting neural communications. This project aims to:

1. **Establish shared vocabulary** — Define the attack surfaces, threat models, and defense mechanisms for neural interfaces before exploits emerge in the wild

2. **Bridge disciplines** — Translate cybersecurity principles into neuroscience contexts and vice versa, creating a common language for cross-domain collaboration

3. **Build proactively** — Develop security primitives (like the Coherence Metric) that can be implemented in hardware before BCIs reach mainstream adoption

4. **Invite scrutiny** — This framework is intentionally public and open. I want neuroscientists to challenge the biological assumptions, security researchers to find holes, and ethicists to identify governance gaps

**This is a living research project.** If you see flaws, have ideas, or want to collaborate — open an issue, submit a PR, or reach out directly. The goal isn't to be right; it's to build something robust enough to protect the most sensitive interface humanity will ever create: the one between technology and the mind.

---

## Key Components

### The 14-Layer ONI Model

Extends the traditional OSI model into biological territory:

| Layers | Domain | Description |
|--------|--------|-------------|
| 1-7 | Traditional OSI | Physical → Application (standard networking) |
| 8-10 | Neural Interface | Electrodes, local field potentials, oscillatory patterns |
| 11-14 | Cognitive | Working memory, attention, executive function, identity |

### The Coherence Metric

Mathematical framework for validating neural signal trustworthiness:

```
Cₛ = e^(−(σ²φ + σ²τ + σ²γ))
```

| Component | Variable | Measures | Security Function |
|-----------|----------|----------|-------------------|
| **Phase** | σ²φ | Timing jitter | Detects out-of-sync signal injections |
| **Transport** | σ²τ | Pathway reliability | Flags signals bypassing biological routes |
| **Gain** | σ²γ | Amplitude stability | Catches over/under-powered attacks |

**Interpretation:** Cₛ ranges from 0 (untrusted) to 1 (fully coherent). Signals below threshold are rejected before reaching neural tissue.

### Neural Signal Assurance Model (NSAM)

Physiology-first defense framework with checkpoints:

1. **Signal Existence** — Should this signal exist at all?
2. **Signal Integrity** — Is it biologically plausible?
3. **Intent & Context** — Does it make sense right now?
4. **Outcome Monitoring** — What effect is it causing?
5. **Human Sovereignty** — Does the human retain agency?

---

## Quick Reference

### Attack Surfaces by Layer

| Layer | Attack Surface | Example Threat |
|-------|---------------|----------------|
| L1-2 | RF/Bluetooth | BlueBorne-style exploits |
| L3-4 | Protocol | Packet injection, replay attacks |
| L8 | Electrode | Signal injection at hardware |
| L9-10 | Neural | Phase-locked malicious stimulation |
| L11-14 | Cognitive | Memory manipulation, identity attacks |

### Hardware Constraints (Neuralink N1 Reference)

| Constraint | Value | Security Implication |
|------------|-------|---------------------|
| Power budget | 25mW total | Firewall gets ~3-5mW max |
| Latency | <1ms required | Real-time validation needed |
| Electrodes | 1,024 channels | High-bandwidth monitoring |
| Form factor | ~1mm² | Minimal silicon for security |

---

## Topics & Documents

> **Tip:** For dependency maps and reading order, see [INDEX.md](MAIN/INDEX.md). Each topic below also has an INDEX.md with detailed summaries.

### 📊 Coherence Metric — [INDEX](MAIN/publications/coherence-metric/INDEX.md)

Signal validation mathematics, trust scoring algorithms, and biological plausibility checks.

| Document | Summary |
|----------|----------|
| [Blog-Coherence_Metric](MAIN/publications/coherence-metric/Blog-Coherence_Metric.md) | *Inside the math that could protect your mind from neural hackers.* |
| [TechDoc-Coherence_Metric_Detailed](MAIN/publications/coherence-metric/TechDoc-Coherence_Metric_Detailed.md) | *A Mathematical Framework for Quantifying Trustworthiness.* |

### 🛡️ Neural Firewall — [INDEX](MAIN/publications/neural-firewall/INDEX.md)

Hardware and software firewall design for neural interfaces, signal filtering, and real-time protection.

| Document | Summary |
|----------|----------|
| [Blog-Neural_Firewall](MAIN/publications/neural-firewall/Blog-Neural_Firewall.md) | *The same security principles that protect your computer will soon need to protect your mind.* |
| [TechDoc-Neural_Firewall_Architecture](MAIN/publications/neural-firewall/TechDoc-Neural_Firewall_Architecture.md) | *A Zero-Trust Security Model for Neural Interfaces.* |

### 🔓 Neural Ransomware — [INDEX](MAIN/publications/neural-ransomware/INDEX.md)

Threat analysis, attack vectors, kill chains, and defensive architectures.

| Document | Summary |
|----------|----------|
| [Blog-Neural_Ransomware](MAIN/publications/neural-ransomware/Blog-Neural_Ransomware.md) | *The technical threat model for holding a brain implant hostage.* |
| [TechDoc-Neural_Ransomware](MAIN/publications/neural-ransomware/TechDoc-Neural_Ransomware.md) | *Attack Vectors and Defensive Architectures for Brain-Computer Interfaces.* |

### 🏗️ ONI Framework (Base) — [INDEX](MAIN/publications/0-oni-framework/INDEX.md)

Core ONI architecture, 14-layer model extending OSI into biological territory. **This is the foundational content for all other publications.**

| Document | Summary |
|----------|----------|
| [Blog-ONI_Framework](MAIN/publications/0-oni-framework/Blog-ONI_Framework.md) | *If you've worked in IT, you know the OSI model.* |
| [TechDoc-ONI_Framework](MAIN/publications/0-oni-framework/TechDoc-ONI_Framework.md) | *A Unified Neuro-Computational Stack for Secure Bio-Digital Integration.* |

### ⚛️ Quantum Encryption — [INDEX](MAIN/publications/quantum-encryption/INDEX.md)

Comprehensive coverage of quantum computing threats, quantum key distribution (QKD), tunneling traversal time, and quantum-enhanced security for brain-computer interfaces.

| Document | Summary |
|----------|----------|
| [Blog-Quantum_Security](MAIN/publications/quantum-encryption/Blog-Quantum_Security.md) | *The real quantum threat isn't about transcending spacetime—it's about transcending computational complexity.* |
| [Blog-Quantum_Keys](MAIN/publications/quantum-encryption/Blog-Quantum_Keys.md) | *From Macroscopic Quantum Tunneling to Quantum Keys: How the Nobel Prize Will Secure BCIs.* |
| [Blog-Tunneling_Traversal_Time](MAIN/publications/quantum-encryption/Blog-Tunneling_Traversal_Time.md) | *The Liminal Phase: How Quantum Tunneling Time Could Secure Your Brain.* |
| [TechDoc-Quantum_Encryption](MAIN/publications/quantum-encryption/TechDoc-Quantum_Encryption.md) | *A Framework for Post-Quantum BCI Protection.* |
| [TechDoc-Tunneling_Traversal_Time](MAIN/publications/quantum-encryption/TechDoc-Tunneling_Traversal_Time.md) | *Tunneling Traversal Time as a Security Primitive for Brain-Computer Interfaces.* |

### 🔬 Scale-Frequency — [INDEX](MAIN/publications/scale-frequency/INDEX.md)

Cross-scale neural patterns, frequency invariants, and information compression.

| Document | Summary |
|----------|----------|
| [Blog-Scale_Frequency](MAIN/publications/scale-frequency/Blog-Scale_Frequency.md) | *From millisecond spikes to lifetime memories.* |
| [TechDoc-Scale_Frequency](MAIN/publications/scale-frequency/TechDoc-Scale_Frequency.md) | *Mathematical Foundations for Hierarchical Neural Processing in the ONI Framework.* |

---

## About the Author

See [ABOUT.md](ABOUT.md) to learn more about the researcher behind this project.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Seeking input from:**
- **Neuroscientists** — Validate biological assumptions
- **Security Engineers** — Identify attack vectors
- **Hardware Engineers** — Assess implementation constraints
- **Ethicists** — Address governance gaps

---

## License

Apache License 2.0 - See [LICENSE](LICENSE)

*This license is subject to change as the ONI project evolves to support agile development and implementation.*

---

*Auto-published from research pipeline*
*Last update: 2026-01-22*
*Documents: 14 | Topics: 6 | Python Package: v0.1.0*
