# ONI Framework — Index

> **The central navigation hub for all ONI Framework research, publications, and development.**

**Version:** 1.9
**Last Updated:** 2026-01-24
**Status:** Active Development

---

## Overview

The **Organic Neurocomputing Interface (ONI) Framework** extends the classical OSI networking model (L1-L7) with 7 additional layers (L8-L14) for neural and cognitive systems, creating a unified architecture for brain-computer interface security.

**Key Distinction:**
- **L1-L7 (OSI):** Standard networking — how data moves
- **L8 (Neural Gateway):** The critical boundary — THE FIREWALL (most attacked, least standardized)
- **L9-L14 (Neural/Cognitive):** Neural signal processing, cognition, identity — what data means

This index connects all research topics, maps dependencies, and provides navigation paths for readers and contributors.

---

## Quick Navigation

| Topic | Description | Documents |
|-------|-------------|-----------|
| [ONI Framework](publications/0-oni-framework/) | Foundational 14-layer model | [Blog](publications/0-oni-framework/Blog-ONI_Framework.md) · [TechDoc](publications/0-oni-framework/TechDoc-ONI_Framework.md) |
| [Coherence Metric](publications/coherence-metric/) | Signal trust scoring (Cₛ formula) | [Blog](publications/coherence-metric/Blog-Coherence_Metric.md) · [TechDoc](publications/coherence-metric/TechDoc-Coherence_Metric_Detailed.md) |
| [Scale-Frequency](publications/scale-frequency/) | Cross-scale invariants (f × S ≈ k) | [Blog](publications/scale-frequency/Blog-Scale_Frequency.md) · [TechDoc](publications/scale-frequency/TechDoc-Scale_Frequency.md) |
| [Neural Firewall](publications/neural-firewall/) | Zero-trust security at L8 | [Blog](publications/neural-firewall/Blog-Neural_Firewall.md) · [TechDoc](publications/neural-firewall/TechDoc-Neural_Firewall_Architecture.md) |
| [Neural Ransomware](publications/neural-ransomware/) | Threat analysis & defense | [Blog](publications/neural-ransomware/Blog-Neural_Ransomware.md) · [TechDoc](publications/neural-ransomware/TechDoc-Neural_Ransomware.md) |
| [Quantum Encryption](publications/quantum-encryption/) | Quantum threats, QKD, TTT, QPUFs | [Blog-QSec](publications/quantum-encryption/Blog-Quantum_Security.md) · [Blog-QKeys](publications/quantum-encryption/Blog-Quantum_Keys.md) · [Blog-TTT](publications/quantum-encryption/Blog-Tunneling_Traversal_Time.md) · [TechDoc-QEnc](publications/quantum-encryption/TechDoc-Quantum_Encryption.md) · [TechDoc-TTT](publications/quantum-encryption/TechDoc-Tunneling_Traversal_Time.md) |

---

## Python Packages

The ONI Framework is implemented in two pip-installable Python packages.

### oni-framework (Core Library)

```bash
pip install oni-framework
```

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| [oni.coherence](oni-framework/oni/coherence.py) | Cₛ calculation | `CoherenceMetric`, `calculate_cs()` |
| [oni.layers](oni-framework/oni/layers.py) | 14-layer model | `ONIStack`, `Layer` |
| [oni.firewall](oni-framework/oni/firewall.py) | Signal filtering | `NeuralFirewall`, `Signal` |
| [oni.scale_freq](oni-framework/oni/scale_freq.py) | f × S ≈ k invariant | `ScaleFrequencyInvariant` |
| [oni.neurosecurity](oni-framework/oni/neurosecurity/) | Kohno CIA + BCI Anonymizer | `NeurosecurityFirewall`, `BCIAnonymizer` |

**Documentation:** [oni-framework/README.md](oni-framework/README.md)

### oni-tara (Security Operations Platform)

```bash
pip install oni-tara
```

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| [tara.core](tara-neural-security-platform/tara/core/) | ONI security primitives | `CoherenceMetric`, `ONIStack`, `NeuralFirewall` |
| [tara.simulation](tara-neural-security-platform/tara/simulation/) | Neural network simulation | `LIFNeuron`, `IzhikevichNeuron`, networks |
| [tara.attacks](tara-neural-security-platform/tara/attacks/) | Attack testing & scenarios | `AttackSimulator`, `AttackScenario` |
| [tara.nsam](tara-neural-security-platform/tara/nsam/) | Neural Signal Assurance Monitoring | `NSAMMonitor`, `RuleEngine`, `AlertManager` |
| [tara.neurosecurity](tara-neural-security-platform/tara/neurosecurity/) | Kohno rules integration | `NeurosecurityMonitor` |
| [tara.data](tara-neural-security-platform/tara/data/) | Data models & external datasets | `MOABBAdapter`, `BrainRegion`, `BCINode` |
| [tara.ui](tara-neural-security-platform/tara/ui/) | Streamlit web interface | `tara ui` command |
| [visualizations/](tara-neural-security-platform/visualizations/) | Interactive HTML apps | ONI Visualization Suite |

**Documentation:** [tara-neural-security-platform/README.md](tara-neural-security-platform/README.md) | **CLI:** `tara --help`

#### ONI Visualization Suite

Five interactive HTML applications for education and demonstration:

| App | Purpose | Research Alignment |
|-----|---------|-------------------|
| [Coherence Playground](tara-neural-security-platform/visualizations/01-coherence-metric-playground.html) | Real-time Cₛ calculation | Signal integrity (Kohno 2009) |
| [Layer Explorer](tara-neural-security-platform/visualizations/02-oni-layer-explorer.html) | Interactive 14-layer navigation | ONI Framework model |
| [Kill Chain Visualizer](tara-neural-security-platform/visualizations/03-neural-killchain-visualizer.html) | Attack propagation animation | Attack patterns (Bonaci 2015) |
| [NSAM Checkpoint Sim](tara-neural-security-platform/visualizations/04-nsam-checkpoint-simulator.html) | Gamified signal validation | NSAM pipeline |
| [Scale-Frequency Nav](tara-neural-security-platform/visualizations/05-scale-frequency-navigator.html) | Temporal scale exploration | f × S ≈ k invariant |

**Quick Start:** Open `tara-neural-security-platform/visualizations/index.html` in a browser.

#### MOABB Integration (External Datasets)

TARA integrates with [MOABB](https://github.com/NeuroTechX/moabb) (BSD 3-Clause) for testing against real EEG data:

```bash
pip install oni-tara[moabb]
```

```python
from tara.data import MOABBAdapter
adapter = MOABBAdapter()
signals = adapter.get_signals(adapter.load_dataset("BNCI2014_001"), subject=1)
```

See [RELATED_WORK.md](RELATED_WORK.md#moabb-mother-of-all-bci-benchmarks) for citation requirements.

**Neurosecurity Implementation:** [NEUROSECURITY_IMPLEMENTATION.md](oni-framework/NEUROSECURITY_IMPLEMENTATION.md) — Integrates Kohno (2009) and BCI Anonymizer patent

---

## Reading Order

**Recommended path through the framework:**

1. **ONI Framework** → Foundation concepts (14-layer model)
2. **Scale-Frequency** → Mathematical invariants (f × S ≈ k)
3. **Coherence Metric** → Signal validation (Cₛ formula)
4. **Neural Firewall** → Security architecture (zero-trust at L8)
5. **Neural Ransomware** → Threat landscape
6. **Quantum Encryption** → Quantum threats, QKD, liminal phase security, QPUFs

---

## Dependency Map

```
                    ┌─────────────────────────────────────┐
                    │         ONI FRAMEWORK (L1-L14)       │
                    │    The foundational 14-layer model   │
                    └──────────────┬──────────────────────┘
                                   │
            ┌──────────────────────┼──────────────────────┐
            │                      │                      │
            ▼                      ▼                      ▼
   ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
   │ SCALE-FREQUENCY │   │ COHERENCE METRIC│   │  NEURAL FIREWALL│
   │  f × S ≈ k law  │   │ Signal validation│   │  Zero-trust L8  │
   └────────┬────────┘   └────────┬────────┘   └────────┬────────┘
            │                     │                      │
            │                     └──────────┬───────────┘
            │                                │
            ▼                                ▼
   ┌─────────────────────────┐    ┌─────────────────────┐
   │   QUANTUM ENCRYPTION    │    │  NEURAL RANSOMWARE  │
   │ HNDL, QKD, TTT, QPUFs   │    │   Threat modeling   │
   └─────────────────────────┘    └──────────┬──────────┘
                                             │
                    ┌────────────────────────┴────────────────────────┐
                    │                                                  │
                    ▼                                                  ▼
   ┌────────────────────────────────────┐        ┌────────────────────────────┐
   │           oni-framework            │        │          oni-tara          │
   │    Core library (pip install)      │        │  Security Operations (SOC) │
   │ coherence, layers, firewall, etc.  │        │  simulation, attacks, NSAM │
   └────────────────────────────────────┘        └────────────────────────────┘
```

---

## Topics & Publications

### Core Foundation

| Topic | Purpose | Documents | Status |
|-------|---------|-----------|--------|
| [ONI Framework](publications/0-oni-framework/) | 14-layer biological extension of OSI model | [Blog](publications/0-oni-framework/Blog-ONI_Framework.md) · [TechDoc](publications/0-oni-framework/TechDoc-ONI_Framework.md) | Published |

### Signal Processing

| Topic | Purpose | Documents | Status |
|-------|---------|-----------|--------|
| [Coherence Metric](publications/coherence-metric/) | Mathematical framework for signal trust scoring | [Blog](publications/coherence-metric/Blog-Coherence_Metric.md) · [TechDoc](publications/coherence-metric/TechDoc-Coherence_Metric_Detailed.md) | Published |
| [Scale-Frequency](publications/scale-frequency/) | Cross-scale frequency invariants (f × S ≈ k) | [Blog](publications/scale-frequency/Blog-Scale_Frequency.md) · [TechDoc](publications/scale-frequency/TechDoc-Scale_Frequency.md) | Published |

### Security Architecture

| Topic | Purpose | Documents | Status |
|-------|---------|-----------|--------|
| [Neural Firewall](publications/neural-firewall/) | Zero-trust security at the neural gateway (L8) | [Blog](publications/neural-firewall/Blog-Neural_Firewall.md) · [TechDoc](publications/neural-firewall/TechDoc-Neural_Firewall_Architecture.md) | Published |
| [Neural Ransomware](publications/neural-ransomware/) | Threat analysis and defensive architectures | [Blog](publications/neural-ransomware/Blog-Neural_Ransomware.md) · [TechDoc](publications/neural-ransomware/TechDoc-Neural_Ransomware.md) | Published |
| [Quantum Encryption](publications/quantum-encryption/) | Quantum threats, QKD, liminal phase security, QPUFs | [Blog-QSec](publications/quantum-encryption/Blog-Quantum_Security.md) · [Blog-QKeys](publications/quantum-encryption/Blog-Quantum_Keys.md) · [Blog-TTT](publications/quantum-encryption/Blog-Tunneling_Traversal_Time.md) · [TechDoc-QEnc](publications/quantum-encryption/TechDoc-Quantum_Encryption.md) · [TechDoc-TTT](publications/quantum-encryption/TechDoc-Tunneling_Traversal_Time.md) | Published |

---

## Cross-Reference Matrix

Shows which topics reference which. Use this to understand conceptual dependencies.

|                    | ONI Framework | Coherence | Scale-Freq | Firewall | Ransomware | Quantum Enc |
|--------------------|:-------------:|:---------:|:----------:|:--------:|:----------:|:-----------:|
| **ONI Framework**  | —             | ●         | ●          | ●        | ●          | ●           |
| **Coherence**      | ◄             | —         | ○          | ●        | ●          | ●           |
| **Scale-Frequency**| ◄             | ○         | —          | ○        | ○          | ●           |
| **Firewall**       | ◄             | ◄         | ○          | —        | ●          | ○           |
| **Ransomware**     | ◄             | ◄         | ○          | ◄        | —          | ○           |
| **Quantum Enc**    | ◄             | ◄         | ◄          | ○        | ○          | —           |

**Legend:** ● = references this topic | ◄ = referenced by this topic | ○ = related concept

---

## Layer Quick Reference

The ONI Framework extends the classical OSI model with 7 additional layers for neural and cognitive systems:

| Layer | Name | Domain | Function |
|:-----:|------|--------|----------|
| L1 | Physical | OSI | Transmission of raw bits over medium |
| L2 | Data Link | OSI | Framing, MAC addressing, local delivery |
| L3 | Network | OSI | Logical addressing and routing |
| L4 | Transport | OSI | End-to-end delivery, flow control |
| L5 | Session | OSI | Connection lifecycle management |
| L6 | Presentation | OSI | Encoding, encryption, compression |
| L7 | Application | OSI | User-facing network services |
| **L8** | **Neural Gateway** | **Bridge** | **BCI hardware boundary (FIREWALL lives here)** |
| L9 | Signal Processing | Neural | Filtering, amplification, digitization |
| L10 | Neural Protocol | Neural | Neural data formatting, codecs |
| L11 | Cognitive Transport | Neural | Reliable neural data delivery |
| L12 | Cognitive Session | Neural | Context persistence, working memory |
| L13 | Semantic | Cognitive | Meaning construction, intent decoding |
| L14 | Identity | Cognitive | Self-model, ethics, continuity of self |

**Key Principle:**
- **OSI (L1-L7)** answers: *How does data move?*
- **ONI (L8-L14)** answers: *Should it move, can it be trusted, and what does it mean?*

**Authoritative Reference:** [ONI_LAYERS.md](oni-framework/ONI_LAYERS.md)

---

## Visualizations

| Project | Description |
|---------|-------------|
| [Visualizations](tara-neural-security-platform/visualizations/README.md) | Interactive web apps for ONI concepts (5 demos) |

---

## Governance & Ethics

The ONI Framework maintains Responsible AI standards and documents alignment with neuroethics principles.

| Document | Purpose |
|----------|---------|
| [TRANSPARENCY.md](governance/TRANSPARENCY.md) | Human-AI collaboration audit trail — cognitive boundary documentation, HITL methodology |
| [NEUROETHICS_ALIGNMENT.md](governance/NEUROETHICS_ALIGNMENT.md) | Maps framework components to cognitive liberty, mental privacy, mental integrity principles |
| [INFORMED_CONSENT_FRAMEWORK.md](governance/INFORMED_CONSENT_FRAMEWORK.md) | Consent requirements for neural devices (Lázaro-Muñoz framework) |
| [POST_DEPLOYMENT_ETHICS.md](governance/POST_DEPLOYMENT_ETHICS.md) | Device lifecycle, maintenance obligations, abandonment prevention |
| [PEDIATRIC_CONSIDERATIONS.md](governance/PEDIATRIC_CONSIDERATIONS.md) | Guidelines for minors and individuals with limited capacity |
| [RELATED_WORK.md](RELATED_WORK.md) | Prior BCI security research — acknowledges foundational work, positions ONI's contribution |
| [ACADEMIC_LANDSCAPE.md](ACADEMIC_LANDSCAPE.md) | **Research landscape** — top universities, key researchers, collaboration opportunities |
| [PARTNERSHIPS.md](PARTNERSHIPS.md) | Partnership opportunities, implementation roadmap, how to get involved |

---

## Resources

### Templates

| Template | Purpose |
|----------|---------|
| [BLOG_TEMPLATE.md](resources/templates/BLOG_TEMPLATE.md) | Blog post formatting guide |
| [TECHDOC_TEMPLATE_APA.md](resources/templates/TECHDOC_TEMPLATE_APA.md) | Technical document (APA format) |
| [README_TEMPLATE.md](resources/templates/README_TEMPLATE.md) | Topic README template (for folder overviews) |

### Project Management

| Document | Purpose |
|----------|---------|
| [PROJECT_MANAGEMENT.md](project/PROJECT_MANAGEMENT.md) | **Master PM doc — scope, risks, priorities, metrics** |
| [KANBAN.md](project/KANBAN.md) | **Visual Kanban board — task status at a glance** |
| [prd.json](project/prd.json) | Machine-readable task tracker with exit conditions |
| [PUBLISHING_INSTRUCTIONS.md](project/processes/PUBLISHING_INSTRUCTIONS.md) | Step-by-step publishing workflow |
| [PROCESS_IMPROVEMENTS.md](project/processes/PROCESS_IMPROVEMENTS.md) | Workflow enhancement tracking |

### Research Pipeline

| Resource | Purpose |
|----------|---------|
| [research_monitor.py](resources/pipeline/scripts/research_monitor.py) | Automated academic paper discovery |
| [keywords.json](resources/pipeline/scripts/keywords.json) | Research search terms + researcher tracking database |
| [incoming/](resources/pipeline/incoming/) | New research discoveries |
| [processed/](resources/pipeline/processed/) | Reviewed and integrated research |

### Workflows

| Workflow | Purpose |
|----------|---------|
| [RESEARCH_INTEGRATION_WORKFLOW.md](resources/workflows/RESEARCH_INTEGRATION_WORKFLOW.md) | **Academic research → ONI integration pipeline** |
| [VISUALIZATION_AS_CODE_STRATEGY.md](resources/workflows/VISUALIZATION_AS_CODE_STRATEGY.md) | Remotion-based programmatic visualization strategy |

### Editor Agent (Quality & Sync)

| Resource | Purpose |
|----------|---------|
| [EDITOR_AGENT.md](resources/editor/EDITOR_AGENT.md) | **Main instructions — run before commits** |
| [AGENTS.md](../AGENTS.md) | **Ralph Loop learnings — read at session start** |
| [layer_validation.md](resources/editor/checks/layer_validation.md) | 14-layer model accuracy checks |
| [sync_rules.md](resources/editor/checks/sync_rules.md) | Cross-reference cascade rules |
| [naming_rules.md](resources/editor/checks/naming_rules.md) | File/folder naming validation |
| [format_rules.md](resources/editor/checks/format_rules.md) | Template compliance checks |

**Mode:** Hybrid — auto-fixes mechanical issues (dates, counts, links), requires approval for content changes.

---

## Adding New Topics

When expanding the framework, follow this process:

### 1. Create Topic Folder
```bash
mkdir MAIN/publications/[topic-name]/
```

### 2. Create Topic README.md
Use the [README template](resources/templates/README_TEMPLATE.md) with:
- Topic summary
- Dependency list (what this topic builds on)
- Document inventory
- Related topics

> **Note:** Topic folders use `README.md` (auto-rendered by GitHub), while this central index uses `INDEX.md`. This naming convention distinguishes the **main wiki hub** from **topic overviews**.

### 3. Add Publications
- `Blog-[Topic_Name].md` — Accessible narrative (include original URL if applicable)
- `TechDoc-[Topic_Name].md` — Academic depth

### 4. Update This Index
- Add topic to appropriate section table
- Update dependency map if needed
- Add to cross-reference matrix

### 5. Update keywords.json
Add keywords for research monitoring integration.

---

## Roadmap: Future Topics

Planned research areas for framework expansion:

| Priority | Topic | Description | Dependencies | Status |
|:--------:|-------|-------------|--------------|--------|
| 1 | Neural Authentication | Identity verification via neural signatures | Coherence, Firewall | Planned |
| 2 | Neural Consent | Consent architecture for BCIs (Lázaro-Muñoz framework) | Firewall, Governance | In Progress |
| 3 | Adversarial Stimulation | Attack vectors through neural feedback | Ransomware, Firewall | Planned |
| 4 | Cross-Device Protocol | Multi-BCI communication standards | ONI L10-L12 | Conceptual |
| 5 | Neural Privacy Framework | Data minimization for neural signals | Coherence, Firewall | Conceptual |
| 6 | Regulatory Mapping | FDA/EU compliance for ONI architecture | All topics | Conceptual |

---

## Roadmap: Partnership Pathways

To move ONI from research to implementation, we're pursuing four parallel tracks:

### Hardware Validation (Priority 1)

| Target | Platform | Integration | Status |
|--------|----------|-------------|--------|
| **OpenBCI** | Cyton, Ganglion, Ultracortex | `oni-openbci` package | Planned |
| **BrainFlow** | Multi-device abstraction | Native adapter | Planned |
| **Emotiv** | Consumer EEG (EPOC, Insight) | SDK integration | Conceptual |

**Why OpenBCI first:** Open-source hardware, Python-native SDK, active developer community, accessible price point for validation.

### Academic Partnerships (Priority 2)

| Institution | Lab/Group | Focus | Opportunity |
|-------------|-----------|-------|-------------|
| **University of Washington** | Kohno/Chizeck Labs | Neurosecurity founders | Validation, joint papers |
| **Rice University** | SIMS Lab (Yang) | Low-power implantable security | Hardware constraints |
| **Northeastern/Michigan** | Archimedes (Fu) | Medical device security | Threat modeling |

**Goal:** Peer review, empirical validation, conference publications (IEEE S&P, USENIX, NDSS).

### Industry Engagement (Priority 3)

| Company | Device Type | Engagement Path |
|---------|-------------|-----------------|
| **Blackrock Neurotech** | Research arrays | Research partnership |
| **Synchron** | Endovascular | FDA security pathway |
| **Kernel** | Non-invasive | Consumer privacy |
| **Paradromics** | High-bandwidth | Pre-production architecture |

**Approach:** Security consulting, pilot programs, architecture reviews.

### Standards Integration (Priority 4)

| Body | Initiative | ONI Alignment |
|------|------------|---------------|
| **IEEE** | Brain Initiative Standards | Layer model proposal |
| **FDA** | BCI Guidance Documents | Security checkpoint mapping |
| **ISO/IEC** | Medical device security | Framework implementation |
| **OECD** | Neurotechnology Governance | Ethics alignment |

**Full details:** [PARTNERSHIPS.md](PARTNERSHIPS.md)

---

## Folder Structure

```
MAIN/
├── INDEX.md                    # This file (central hub)
├── CONTRIBUTING.md             # Contribution guidelines
├── RELATED_WORK.md             # Prior BCI security research
├── ACADEMIC_LANDSCAPE.md       # Universities, researchers, collaboration opportunities
│
├── governance/                 # Ethics & transparency
│   ├── TRANSPARENCY.md         # Human-AI collaboration audit trail
│   ├── NEUROETHICS_ALIGNMENT.md # Framework-to-ethics principle mapping
│   ├── INFORMED_CONSENT_FRAMEWORK.md # Consent requirements (Lázaro-Muñoz)
│   ├── POST_DEPLOYMENT_ETHICS.md     # Device lifecycle ethics
│   └── PEDIATRIC_CONSIDERATIONS.md   # Minors and incapacity guidelines
│
├── project/                    # Project management
│   ├── PROJECT_MANAGEMENT.md   # Master PM doc (scope, risks, priorities)
│   ├── KANBAN.md               # Visual Kanban board
│   ├── prd.json                # Task tracker with exit conditions
│   └── processes/              # Workflow documentation
│
├── oni-framework/              # Python library (pip install oni-framework)
│   ├── ONI_LAYERS.md           # **Authoritative 14-layer reference**
│   ├── NEUROSECURITY_IMPLEMENTATION.md  # Kohno/BCI integration guide
│   ├── oni/                    # Source modules
│   │   ├── coherence.py        # Cₛ calculation
│   │   ├── layers.py           # 14-layer model
│   │   ├── firewall.py         # Neural Firewall
│   │   ├── scale_freq.py       # f × S ≈ k
│   │   └── neurosecurity/      # Kohno threat model + BCI Anonymizer
│   ├── tests/                  # Unit tests (77 tests)
│   └── pyproject.toml          # Package config (v0.1.0)
│
├── tara-neural-security-platform/  # Security Operations Platform (pip install oni-tara)
│   ├── pyproject.toml          # Package config (v0.4.0)
│   ├── tara/                   # Source modules
│   │   ├── core/               # ONI security primitives
│   │   ├── simulation/         # Neural network simulation
│   │   ├── attacks/            # Attack testing & scenarios
│   │   ├── nsam/               # Neural Signal Assurance Monitoring
│   │   ├── neurosecurity/      # Kohno rules integration
│   │   ├── data/               # Data models & adapters
│   │   ├── visualization/      # Real-time dashboards
│   │   └── ui/                 # Streamlit web interface
│   ├── tests/                  # Unit tests (31 tests)
│   └── visualizations/         # Interactive HTML demos (5 apps)
│
├── publications/               # Research content
│   ├── 0-oni-framework/
│   ├── coherence-metric/
│   ├── neural-firewall/
│   ├── neural-ransomware/
│   ├── quantum-encryption/
│   └── scale-frequency/
│
└── resources/                  # Templates, pipeline, editor
    ├── agents/                 # PM Agent instructions
    ├── editor/                 # Editor Agent checks
    ├── images/                 # ONI diagrams and visualizations
    ├── templates/
    └── pipeline/               # Research monitoring
```

---

## Metrics

| Metric | Count |
|--------|-------|
| Total Topics | 6 |
| Published Documents | 14 |
| Blog Posts | 8 |
| Technical Documents | 6 |
| Python Packages | oni-framework v0.1.0, oni-tara v0.4.0 |
| Unit Tests | 108 (77 + 31) |
| Planned Topics | 5 |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for collaboration guidelines. The ONI Framework welcomes contributions from neuroscience, security, hardware, and ethics disciplines.

---

## License

Apache 2.0 — See [LICENSE](../LICENSE)

---

← Back to [Repository Root](../README.md)

*This index is a living document. It evolves as the framework grows.*
