# ONI Framework

*The OSI of Mind*
Life's most important connections deserve the best thought.

---

**ONI** (Open Neurosecurity Interoperability) — a unified 14-layer model extending OSI into the biological domain.

One framework to understand, build, and secure brain-computer interfaces. Open. Accessible. Universal.

> **Brand Reference:** [`MAIN/resources/brand.json`](MAIN/resources/brand.json) — Single source of truth for project naming and identity

---

## Table of Contents

- [Navigation](#navigation)
- [Privacy & Ethics Statement](#privacy--ethics-statement)
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
| **[Live Demo](https://qikevinl.github.io/ONI/)** | **Interactive visualizations** — animated, dynamic exploration of the framework |
| **[MAIN/](MAIN/)** | All research content — publications, visualizations, resources |
| **[INDEX.md](MAIN/INDEX.md)** | **Main Wiki** — central hub for navigation, dependencies, cross-references, roadmap |
| **This README** | Public overview — key concepts, quick reference |

### Security & Maintenance

| Feature | Description |
|---------|-------------|
| **Dependabot** | Automated weekly security updates for all dependencies |
| **CI/CD** | GitHub Actions for tests (Python 3.9-3.12) and security scanning |
| **CDN Libraries** | GitHub Pages uses CDN-hosted AOS.js — auto-updated, no maintenance |

### Governance & Ethics

| Document | Purpose |
|----------|---------|
| **[DATA_POLICY_FAQ.md](MAIN/governance/DATA_POLICY_FAQ.md)** | **FAQ & Data Policy** — privacy, anonymization, user rights, known vulnerabilities |
| **[TRANSPARENCY.md](MAIN/governance/TRANSPARENCY.md)** | Human-AI collaboration audit trail — documents cognitive boundary, HITL methodology |
| **[NEUROETHICS_ALIGNMENT.md](MAIN/governance/NEUROETHICS_ALIGNMENT.md)** | Maps framework components to neuroethics principles |
| **[INFORMED_CONSENT_FRAMEWORK.md](MAIN/governance/INFORMED_CONSENT_FRAMEWORK.md)** | Consent architecture for BCIs — continuous consent, pediatric considerations |
| **[RELATED_WORK.md](MAIN/RELATED_WORK.md)** | Prior BCI security research — acknowledges foundational work, positions ONI contribution |
| **[ACADEMIC_LANDSCAPE.md](MAIN/ACADEMIC_LANDSCAPE.md)** | Research landscape — top universities, key researchers, collaboration opportunities |

### Naming Convention

| File | Location | Purpose |
|------|----------|---------|
| `INDEX.md` | `MAIN/` only | **Main wiki hub** — the single source of truth for navigation |
| `README.md` | Each topic folder | **Topic overview** — auto-rendered by GitHub when browsing folders |

**For deep exploration:** Each topic folder contains a `README.md` with summaries, dependencies, and related topics.

---

## Privacy & Ethics Statement

**ONI is NOT a surveillance framework.** It exists to **protect** neural privacy, not compromise it. Signal integrity can be validated without reading thoughts. Attacks can be detected without decoding intent.

**Key Resources:**
- **[DATA_POLICY_FAQ.md](MAIN/governance/DATA_POLICY_FAQ.md)** — FAQ, data handling, anonymization, known vulnerabilities
- **[NEUROETHICS_ALIGNMENT.md](MAIN/governance/NEUROETHICS_ALIGNMENT.md)** — Full ethics statement and principle mapping

---

## Python Library

[![PyPI version](https://badge.fury.io/py/oni-framework.svg)](https://badge.fury.io/py/oni-framework)
[![Tests](https://github.com/qikevinl/ONI/actions/workflows/tests.yml/badge.svg)](https://github.com/qikevinl/ONI/actions/workflows/tests.yml)
[![Security](https://github.com/qikevinl/ONI/actions/workflows/security.yml/badge.svg)](https://github.com/qikevinl/ONI/actions/workflows/security.yml)

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

### Foundational Research Integration

ONI builds directly on pioneering research from leading institutions in BCI security and neuroethics:

#### Core Technical Foundation (Directly Implemented)

| Institution | Researchers | Research | ONI Implementation |
|-------------|-------------|----------|-------------------|
| **[University of Washington](https://seclab.cs.washington.edu/)** | [Tadayoshi Kohno](https://homes.cs.washington.edu/~yoshi/), [Tamara Bonaci](https://www.researchgate.net/profile/Tamara-Bonaci), [Howard Chizeck](https://people.ece.uw.edu/chizeck/) | [Neurosecurity (2009)](https://doi.org/10.3171/2009.4.FOCUS0985) — Coined the term, defined CIA threat model | `NeurosecurityFirewall` |
| **[UW BioRobotics Lab](https://wp.ece.uw.edu/brl/)** | Bonaci, Chizeck | [BCI Anonymizer Patent](https://patents.google.com/patent/US20140228701A1) — Privacy-preserving signal filtering | `BCIAnonymizer` |

#### Neuroethics & Policy Foundation

| Institution | Researchers | Contribution | ONI Alignment |
|-------------|-------------|--------------|---------------|
| **[Columbia University](https://www.neurorightsfoundation.org/)** | [Rafael Yuste](https://magazine.columbia.edu/article/need-protect-data-our-brains) | [Five Neurorights](https://www.frontiersin.org/articles/10.3389/fnhum.2021.701258) — Mental privacy, identity, free will | Framework-wide design principles |
| **[Yale Digital Ethics Center](https://dec.yale.edu/)** | [Luciano Floridi](https://dec.yale.edu/profile/luciano-floridi), [Tyler Schroder](https://dec.yale.edu/tyler-schroder) | [Cyber Risks to Next-Gen BCIs (2025)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5138265) — BCI threat modeling, regulatory recommendations | Threat model methodology, L8 design |
| **[ETH Zurich / TU Munich](https://ethz.ch/en/news-and-events/eth-news/news/2021/10/marcello-ienca-we-must-expand-human-rights-to-cover-neurotechnology.html)** | [Marcello Ienca](https://www.professoren.tum.de/en/ienca-marcello) | [Four Neurorights (2017)](https://link.springer.com/article/10.1007/s12152-022-09498-8) — Cognitive liberty, mental integrity | L14 Identity layer design |
| **[UW Neuroethics Group](https://phil.washington.edu/neuroethics-research-group)** | [Sara Goering](https://phil.washington.edu/people/sara-goering), [Eran Klein](https://phil.washington.edu/ethical-considerations-and-neurotechnology) | [Agency in BCI users](https://pmc.ncbi.nlm.nih.gov/articles/PMC8443241/) — Relational agency, user autonomy | User consent models |
| **[Harvard Bioethics](https://bioethics.hms.harvard.edu/faculty-staff/gabriel-lazaro-munoz)** | [Gabriel Lázaro-Muñoz](https://brain.harvard.edu/?people=gabriel-lazaro-munoz) | [DBS ethics, neural data privacy](https://www.frontiersin.org/articles/10.3389/fnhum.2024.1332451) | Privacy scoring, vulnerable populations |
| **[Oxford Uehiro Centre](https://www.practicalethics.ox.ac.uk/people/dr-hannah-maslen)** | [Hannah Maslen](https://www.nature.com/articles/d41586-019-02214-2) | [Autonomy in closed-loop BCIs](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3002899) | Adaptive system safeguards |

#### Neural Engineering (Security-Relevant)

| Institution | Lab/Program | Security Relevance |
|-------------|-------------|-------------------|
| **[Brown University](https://www.brown.edu/news/2021-03-31/braingate-wireless)** | [BrainGate Consortium](https://www.braingate.org/) | Wireless BCI security, 17-year safety data |
| **[Stanford University](https://nptl.stanford.edu/)** | Neural Prosthetics Translational Lab | Clinical trial protocols, multi-site security |
| **[Carnegie Mellon](https://www.cmu.edu/bme/helab/)** | [Bin He Lab](https://engineering.cmu.edu/directory/bios/he-bin.html) | Bidirectional BCI, ML decoder security |
| **[Johns Hopkins APL](https://www.hopkinsmedicine.org/physical-medicine-rehabilitation/research/tetraplegia-brain-study)** | [Celnik Lab](https://celniklab.johnshopkins.edu/) | Bilateral implants, multi-array sync |
| **[Caltech](https://www.vis.caltech.edu/)** | [Andersen Lab](https://www.vis.caltech.edu/Chen_Center) | Intent decoding, stimulation safety |

**Full academic landscape:** [ACADEMIC_LANDSCAPE.md](MAIN/ACADEMIC_LANDSCAPE.md)
**Implementation details:** [NEUROSECURITY_IMPLEMENTATION.md](MAIN/oni-framework/NEUROSECURITY_IMPLEMENTATION.md)

#### Research Gaps ONI Addresses

| Gap in Current Research | ONI's Contribution |
|-------------------------|-------------------|
| No unified security model across BCI types | 14-layer model applicable to invasive, non-invasive, and hybrid BCIs |
| Privacy concepts remain theoretical | `BCIAnonymizer` provides executable implementation |
| No standard threat taxonomy | Kohno CIA model + attack pattern library in TARA |
| Layer-by-layer attack surface undefined | ONI explicitly maps attacks to layers L1-L14 |
| Coherence/integrity unmeasured | Cₛ metric provides quantifiable signal trust |
| Neurorights lack technical enforcement | Framework translates rights to technical controls |

🎯 **[Explore Interactive Gap Analysis →](https://qikevinl.github.io/ONI/visualizations/03-academic-alignment.html)**

### TARA - Neural Security Platform

[![PyPI version](https://badge.fury.io/py/oni-tara.svg)](https://badge.fury.io/py/oni-tara)
[![Tests](https://github.com/qikevinl/ONI/actions/workflows/tests.yml/badge.svg)](https://github.com/qikevinl/ONI/actions/workflows/tests.yml)
[![Security](https://github.com/qikevinl/ONI/actions/workflows/security.yml/badge.svg)](https://github.com/qikevinl/ONI/actions/workflows/security.yml)

**TARA** (Telemetry Analysis & Response Automation) is a neural security platform for BCI monitoring, simulation, and attack testing. Named after the Buddhist goddess of protection, TARA provides real-time security analysis aligned with the ONI 14-layer model.

**Features:** Neural network simulation, attack pattern testing, Neural Signal Assurance Monitoring (NSAM), 3D brain topology visualization, and a Streamlit web dashboard.

```bash
# Installation
pip install oni-tara[full]  # Full installation with UI and simulation

# Launch the dashboard
tara ui
```

**Note:** TARA is a research and development tool for BCI security analysis. It requires `oni-framework` as a dependency and is intended for security researchers, not production BCI systems.

**Full documentation:** [MAIN/tara-nsec-platform/README.md](MAIN/tara-nsec-platform/README.md)

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
    ├── ACADEMIC_LANDSCAPE.md    # Universities, researchers, collaboration
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
    │   ├── ONI_THREAT_MATRIX.md # **7 tactics, 21 techniques (MITRE-inspired)**
    │   ├── NEUROSECURITY_IMPLEMENTATION.md  # Kohno/BCI integration guide
    │   ├── oni/                 # Source code
    │   │   ├── coherence.py     # Cₛ calculation
    │   │   ├── layers.py        # 14-layer model
    │   │   ├── firewall.py      # Neural Firewall
    │   │   ├── scale_freq.py    # f × S ≈ k invariant
    │   │   └── neurosecurity/   # Kohno threat model + BCI Anonymizer
    │   └── tests/               # Unit tests
    │
    ├── tara-nsec-platform/  # TARA package (pip install oni-tara)
    │   ├── pyproject.toml       # Package configuration
    │   ├── README.md            # Platform documentation
    │   ├── LICENSE              # Apache 2.0
    │   ├── tara_mvp/             # Source modules (MVP)
    │   │   ├── core/            # ONI security primitives
    │   │   ├── simulation/      # Neural network simulation
    │   │   ├── attacks/         # Attack testing & scenarios
    │   │   ├── nsam/            # Neural Signal Assurance Monitoring
    │   │   ├── neurosecurity/   # Kohno rules integration
    │   │   ├── data/            # Data models & adapters
    │   │   ├── visualization/   # Real-time dashboards
    │   │   └── ui/              # Streamlit web interface
    │   ├── tests/               # Unit tests
    │   └── visualizations/      # Interactive HTML demos (6 apps)
    │
    ├── publications/            # Research content
    │   ├── 0-oni-framework/     # Base/foundational content
    │   ├── coherence-metric/
    │   ├── detection-theory/    # Detection algorithms, privacy-preserving ML
    │   ├── neural-firewall/
    │   ├── neural-ransomware/
    │   ├── quantum-encryption/
    │   └── scale-frequency/
    │
    └── resources/               # Infrastructure
        ├── agents/              # PM Agent instructions
        ├── editor/              # Editor Agent (quality & sync)
        ├── images/              # ONI diagrams
        ├── templates/           # Formatting templates
        ├── pipeline/            # Research pipeline + researcher tracking
        └── workflows/           # Research integration, Visualization as Code
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

Mathematical framework for validating neural signal trustworthiness using entropy-based anomaly detection:

```
Cₛ = e^(−(σ²φ + σ²τ + σ²γ))
```

| Component | Variable | Measures | Security Function |
|-----------|----------|----------|-------------------|
| **Phase** | σ²φ | Timing jitter | Detects out-of-sync signal injections |
| **Transport** | σ²τ | Pathway reliability | Flags signals bypassing biological routes |
| **Gain** | σ²γ | Amplitude stability | Catches over/under-powered attacks |

**Why Exponential Decay?** The formula models biological threshold behaviors from information theory. Total variance (σ²φ + σ²τ + σ²γ) represents Shannon entropy—the uncertainty across all signal dimensions. The exponential form creates sharp transitions: coherence remains high at low variance but collapses rapidly as variance increases, mirroring how neural systems gate signals for downstream propagation.

**Anomaly Detection Approach:**
1. **Baseline Establishment** — ML models trained on authentic neural signatures establish per-user variance thresholds for phase, transport, and gain
2. **Statistical Monitoring** — Incoming signals are continuously evaluated against learned baselines
3. **Deviation Flagging** — Signals exceeding standard deviation bounds trigger coherence score degradation
4. **Threshold Enforcement** — Cₛ below configurable threshold (default: 0.6) triggers rejection or enhanced scrutiny

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

**For comprehensive threat documentation, see [ONI_THREAT_MATRIX.md](MAIN/oni-framework/ONI_THREAT_MATRIX.md):**
- 7 tactics, 21 techniques mapped to ONI layers
- Methodology inspired by [MITRE ATT&CK](https://attack.mitre.org/)® (not affiliated)
- Integrated with Kohno (2009) and Yale (2025) threat models
- CIA impact ratings, mitigations, and detection methods

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

### 🎯 Detection Theory — [Overview](MAIN/publications/detection-theory/)

Mathematical frameworks for threat detection in neural systems, including signature-based, anomaly-based, and behavioral detection with privacy-preserving implementations.

| Document | Summary |
|----------|----------|
| [TechDoc-Detection_Theory](MAIN/publications/detection-theory/TechDoc-Detection_Theory.md) | *Mathematical Framework for Neural Signal Threat Detection with differential privacy, federated learning, and secure multi-party computation.* |

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
*Last update: 2026-01-26*
*Documents: 17 | Topics: 7 | Python Packages: oni-framework v0.2.0, oni-tara v0.8.0*
