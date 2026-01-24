# ONI Framework
*"The OSI of Mind"*

> **ONI**: Organic Neurocomputing Interface — A 14-layer framework extending OSI for brain-computer interface (BCI) security.

An extensible framework for monitoring and securing neural communications, designed for transparency and interoperability across brain-computer interfaces (BCIs).

---

## Privacy & Ethics Statement

**ONI is NOT a surveillance framework.** It exists to **protect** neural privacy, not compromise it. Signal integrity can be validated without reading thoughts. Attacks can be detected without decoding intent.

**Full statement:** [NEUROETHICS_ALIGNMENT.md](MAIN/governance/NEUROETHICS_ALIGNMENT.md)

---

## Table of Contents

- [Privacy & Ethics Statement](#privacy--ethics-statement)
- [Navigation](#navigation)
  - [Transparency & Ethics](#transparency--ethics)
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
| **[INDEX.md](MAIN/INDEX.md)** | **Main Wiki** — central hub for navigation, dependencies, cross-references, roadmap |
| **This README** | Public overview — key concepts, quick reference |

### Governance & Ethics

| Document | Purpose |
|----------|---------|
| **[TRANSPARENCY.md](MAIN/governance/TRANSPARENCY.md)** | Human-AI collaboration audit trail — documents cognitive boundary, HITL methodology |
| **[NEUROETHICS_ALIGNMENT.md](MAIN/governance/NEUROETHICS_ALIGNMENT.md)** | Maps framework components to neuroethics principles |
| **[RELATED_WORK.md](MAIN/RELATED_WORK.md)** | Prior BCI security research — acknowledges foundational work, positions ONI contribution |

### Naming Convention

| File | Location | Purpose |
|------|----------|---------|
| `INDEX.md` | `MAIN/` only | **Main wiki hub** — the single source of truth for navigation |
| `README.md` | Each topic folder | **Topic overview** — auto-rendered by GitHub when browsing folders |

**For deep exploration:** Each topic folder contains a `README.md` with summaries, dependencies, and related topics.

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

# Neurosecurity: Kohno's CIA triad + BCI Anonymizer (NEW)
from oni.neurosecurity import NeurosecurityFirewall, BCIAnonymizer, ThreatType

# Validate signals against Kohno's threat model
ns_firewall = NeurosecurityFirewall()
# decision = ns_firewall.validate(signal)  # ALLOW, BLOCK, or EMERGENCY_SHUTOFF

# Filter privacy-sensitive information (BCI Anonymizer)
anonymizer = BCIAnonymizer()
# result = anonymizer.anonymize(signal_data)
# print(f"Privacy Score: {result.metrics.privacy_score}")  # Lower = more private
```

**Full documentation:** [MAIN/oni-framework/README.md](MAIN/oni-framework/README.md)

**Neurosecurity Integration:** Based on [Kohno et al. (2009)](https://doi.org/10.3171/2009.4.FOCUS0985) and [BCI Anonymizer patent](https://patents.google.com/patent/US20140228701A1). See [NEUROSECURITY_IMPLEMENTATION.md](MAIN/oni-framework/NEUROSECURITY_IMPLEMENTATION.md).

### TARA - Neural Security Platform

[![PyPI version](https://badge.fury.io/py/oni-tara.svg)](https://badge.fury.io/py/oni-tara)

**TARA** (Telemetry Awareness and Response Analyzer) is a neural security platform for BCI monitoring, simulation, and attack testing. Named after the Buddhist goddess of protection, TARA provides real-time security analysis aligned with the ONI 14-layer model.

**Features:** Neural network simulation, attack pattern testing, Neural Signal Assurance Monitoring (NSAM), 3D brain topology visualization, and a Streamlit web dashboard.

```bash
# Installation
pip install oni-tara[full]  # Full installation with UI and simulation

# Launch the dashboard
tara ui
```

**Note:** TARA is a research and development tool for BCI security analysis. It requires `oni-framework` as a dependency and is intended for security researchers, not production BCI systems.

**Full documentation:** [MAIN/tara/README.md](MAIN/tara/README.md)

---

## Repository Structure

All research, publications, and supporting infrastructure live in the `MAIN/` directory. Navigate there to explore the full body of work.

```
ONI/
├── README.md                    # Public overview (you are here)
├── CLAUDE.md                    # Claude AI instructions
├── AGENTS.md                    # Ralph Loop learnings (knowledge compounding)
├── ABOUT.md                     # Author bio
├── LICENSE                      # Apache 2.0
│
├── .github/
│   ├── .gitignore               # Git ignore rules
│   ├── workflows/               # CI/CD pipelines
│   └── security-audit/          # Security scanning tools
│
└── MAIN/
    ├── INDEX.md                 # Central hub — navigation, dependencies, cross-references
    ├── CONTRIBUTING.md          # Contribution guidelines
    ├── RELATED_WORK.md          # Prior BCI security research
    │
    ├── governance/              # Ethics & transparency
    │   ├── TRANSPARENCY.md      # Human-AI collaboration audit trail
    │   └── NEUROETHICS_ALIGNMENT.md # Framework-to-ethics principle mapping
    │
    ├── project/                 # Project management
    │   ├── prd.json             # Task tracker with exit conditions
    │   └── processes/           # Workflow documentation
    │
    ├── oni-framework/           # Python library (pip install oni-framework)
    │   ├── ONI_LAYERS.md        # **Authoritative 14-layer reference**
    │   ├── NEUROSECURITY_IMPLEMENTATION.md  # Kohno/BCI integration guide
    │   ├── oni/                 # Source code
    │   │   ├── coherence.py     # Cₛ calculation
    │   │   ├── layers.py        # 14-layer model
    │   │   ├── firewall.py      # Neural Firewall
    │   │   ├── scale_freq.py    # f × S ≈ k invariant
    │   │   └── neurosecurity/   # Kohno threat model + BCI Anonymizer
    │   └── tests/               # Unit tests
    │
    ├── tara/                    # Neural Security Platform (pip install oni-tara)
    │   ├── tara/                # Source modules (nested package)
    │   │   ├── core/            # ONI security primitives
    │   │   ├── simulation/      # Neural network simulation
    │   │   ├── attacks/         # Attack testing & scenarios
    │   │   ├── nsam/            # Neural Signal Assurance Monitoring
    │   │   ├── neurosecurity/   # Kohno rules integration
    │   │   ├── visualization/   # Real-time dashboards
    │   │   └── ui/              # Streamlit web interface
    │   └── tests/               # Unit tests
    │
    ├── visualizations/          # Interactive web visualizations
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
        ├── agents/              # PM Agent instructions
        ├── editor/              # Editor Agent (quality & sync)
        ├── images/              # ONI diagrams and visualizations
        ├── templates/           # Formatting templates
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

<p align="center">
  <img src="MAIN/resources/images/oni-14-layer-hourglass.png" alt="ONI Framework 14-Layer Model" width="700">
</p>

Extends the classical OSI networking model with 7 additional layers for neural and cognitive systems:

| Layers | Domain | Description |
|--------|--------|-------------|
| **L1-L7** | Classical OSI Networking | Physical → Application (standard networking) |
| **L8** | Neural Gateway | **THE FIREWALL** — Bridge between silicon and biology |
| **L9-L10** | Signal Processing | Neural filtering, digitization, protocol encoding |
| **L11-L12** | Cognitive Transport | Session management, state tracking, reliable delivery |
| **L13-L14** | Semantic/Identity | Intent interpretation, ethics, continuity of self |

**Key Principle:**
- **OSI (L1-L7)** answers: *How does data move?*
- **ONI (L8-L14)** answers: *Should it move, can it be trusted, and what does it mean — especially when the endpoint is a human brain?*

**L8 (Neural Gateway) is the critical boundary** — most attacked, least standardized, most dangerous layer.

For complete layer definitions, see [ONI_LAYERS.md](MAIN/oni-framework/ONI_LAYERS.md) — the authoritative reference.

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

| Layer | Domain | Attack Surface | Example Threat |
|-------|--------|---------------|----------------|
| L1-L4 | OSI | Network infrastructure | MitM, DDoS, BlueBorne-style exploits |
| L5-L7 | OSI | Application protocols | Packet injection, API exploits |
| **L8** | **Gateway** | **Neural boundary** | **Bypass attacks, unauthorized write access** |
| L9 | Signal | Hardware/DSP | Signal injection, jamming, impedance manipulation |
| L10-L11 | Protocol | Neural encoding | Protocol manipulation, session hijacking |
| L12-L13 | Cognitive | State/Intent | Context corruption, semantic attacks |
| L14 | Identity | Self-model | Long-term manipulation, identity attacks |

**External Physical Threats** (documented in [ONI_LAYERS.md](MAIN/oni-framework/ONI_LAYERS.md)):
- MRI exposure, electromagnetic interference, physical trauma, intentional jamming, proximity attacks (ProxMark-style)

### Hardware Constraints (Neuralink N1 Reference)

| Constraint | Value | Security Implication |
|------------|-------|---------------------|
| Power budget | 25mW total | Firewall gets ~3-5mW max |
| Latency | <1ms required | Real-time validation needed |
| Electrodes | 1,024 channels | High-bandwidth monitoring |
| Form factor | ~1mm² | Minimal silicon for security |

---

## Topics & Documents

> **Tip:** For dependency maps and reading order, see [INDEX.md](MAIN/INDEX.md) (the main wiki). Each topic folder below has a `README.md` with detailed summaries (auto-rendered by GitHub).

### 📊 Coherence Metric — [Overview](MAIN/publications/coherence-metric/)

Signal validation mathematics, trust scoring algorithms, and biological plausibility checks.

| Document | Summary |
|----------|----------|
| [Blog-Coherence_Metric](MAIN/publications/coherence-metric/Blog-Coherence_Metric.md) | *Inside the math that could protect your mind from neural hackers.* |
| [TechDoc-Coherence_Metric_Detailed](MAIN/publications/coherence-metric/TechDoc-Coherence_Metric_Detailed.md) | *A Mathematical Framework for Quantifying Trustworthiness.* |

### 🛡️ Neural Firewall — [Overview](MAIN/publications/neural-firewall/)

Hardware and software firewall design for neural interfaces, signal filtering, and real-time protection.

| Document | Summary |
|----------|----------|
| [Blog-Neural_Firewall](MAIN/publications/neural-firewall/Blog-Neural_Firewall.md) | *The same security principles that protect your computer will soon need to protect your mind.* |
| [TechDoc-Neural_Firewall_Architecture](MAIN/publications/neural-firewall/TechDoc-Neural_Firewall_Architecture.md) | *A Zero-Trust Security Model for Neural Interfaces.* |

### 🔓 Neural Ransomware — [Overview](MAIN/publications/neural-ransomware/)

Threat analysis, attack vectors, kill chains, and defensive architectures.

| Document | Summary |
|----------|----------|
| [Blog-Neural_Ransomware](MAIN/publications/neural-ransomware/Blog-Neural_Ransomware.md) | *The technical threat model for holding a brain implant hostage.* |
| [TechDoc-Neural_Ransomware](MAIN/publications/neural-ransomware/TechDoc-Neural_Ransomware.md) | *Attack Vectors and Defensive Architectures for Brain-Computer Interfaces.* |

### 🏗️ ONI Framework (Base) — [Overview](MAIN/publications/0-oni-framework/)

Core ONI architecture, 14-layer model extending OSI into biological territory. **This is the foundational content for all other publications.**

| Document | Summary |
|----------|----------|
| [Blog-ONI_Framework](MAIN/publications/0-oni-framework/Blog-ONI_Framework.md) | *If you've worked in IT, you know the OSI model.* |
| [TechDoc-ONI_Framework](MAIN/publications/0-oni-framework/TechDoc-ONI_Framework.md) | *A Unified Neuro-Computational Stack for Secure Bio-Digital Integration.* |

### ⚛️ Quantum Encryption — [Overview](MAIN/publications/quantum-encryption/)

Comprehensive coverage of quantum computing threats, quantum key distribution (QKD), tunneling traversal time, and quantum-enhanced security for brain-computer interfaces.

| Document | Summary |
|----------|----------|
| [Blog-Quantum_Security](MAIN/publications/quantum-encryption/Blog-Quantum_Security.md) | *The real quantum threat isn't about transcending spacetime—it's about transcending computational complexity.* |
| [Blog-Quantum_Keys](MAIN/publications/quantum-encryption/Blog-Quantum_Keys.md) | *From Macroscopic Quantum Tunneling to Quantum Keys: How the Nobel Prize Will Secure BCIs.* |
| [Blog-Tunneling_Traversal_Time](MAIN/publications/quantum-encryption/Blog-Tunneling_Traversal_Time.md) | *The Liminal Phase: How Quantum Tunneling Time Could Secure Your Brain.* |
| [TechDoc-Quantum_Encryption](MAIN/publications/quantum-encryption/TechDoc-Quantum_Encryption.md) | *A Framework for Post-Quantum BCI Protection.* |
| [TechDoc-Tunneling_Traversal_Time](MAIN/publications/quantum-encryption/TechDoc-Tunneling_Traversal_Time.md) | *Tunneling Traversal Time as a Security Primitive for Brain-Computer Interfaces.* |

### 🔬 Scale-Frequency — [Overview](MAIN/publications/scale-frequency/)

Cross-scale neural patterns, frequency invariants, and information compression.

| Document | Summary |
|----------|----------|
| [Blog-Scale_Frequency](MAIN/publications/scale-frequency/Blog-Scale_Frequency.md) | *From millisecond spikes to lifetime memories.* |
| [TechDoc-Scale_Frequency](MAIN/publications/scale-frequency/TechDoc-Scale_Frequency.md) | *Mathematical Foundations for Hierarchical Neural Processing in the ONI Framework.* |

---

## About the Author

See [ABOUT.md](ABOUT.md) to learn more about the researcher behind this project.

---

## Partnerships & Future Directions

The ONI Framework is actively seeking partnerships to move from research to real-world implementation.

| Partnership Tier | Goal | Target |
|------------------|------|--------|
| **Open-Source Hardware** | Validate on real BCIs | OpenBCI, BrainFlow |
| **Academic Research** | Peer review, validation | UW Kohno Lab, Rice SIMS |
| **Industry Engagement** | Commercial adoption | BCI companies |
| **Standards Integration** | Shape BCI security standards | IEEE, FDA, ISO |

### Priority: OpenBCI Integration

We're building `oni-openbci` — a hardware adapter to demonstrate ONI concepts on accessible, open-source EEG hardware. This includes:
- Real-time Coherence Metric (Cₛ) on live EEG streams
- TARA dashboard with OpenBCI hardware
- Validation reports and tutorials

**Full roadmap:** [PARTNERSHIPS.md](MAIN/PARTNERSHIPS.md)

### Get Involved

| Role | How to Help |
|------|-------------|
| **Researchers** | Use ONI, validate assumptions, co-author papers |
| **Engineers** | Contribute code, build hardware adapters |
| **Industry** | Pilot programs, integration, sponsorship |
| **Standards Bodies** | Review, invite participation, reference |

---

## Contributing

See [CONTRIBUTING.md](MAIN/CONTRIBUTING.md) for guidelines.

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
*Last update: 2026-01-23*
*Documents: 16 | Topics: 6 | Python Packages: oni-framework v0.2.0, oni-tara v0.4.0*
