# ONI Framework — Index

> **The central navigation hub for all ONI Framework research, publications, and development.**

**Version:** 1.2
**Last Updated:** 2026-01-22
**Status:** Active Development

---

## Overview

The **Organic Neural Interface (ONI) Framework** extends the OSI networking model into biological neural systems, creating a unified architecture for brain-computer interface security. This index connects all research topics, maps dependencies, and provides navigation paths for readers and contributors.

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

## Python Library

The ONI Framework concepts are implemented in a pip-installable Python package.

```bash
pip install oni-framework
```

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| [oni.coherence](oni-framework/oni/coherence.py) | Cₛ calculation | `CoherenceMetric`, `calculate_cs()` |
| [oni.layers](oni-framework/oni/layers.py) | 14-layer model | `ONIStack`, `Layer` |
| [oni.firewall](oni-framework/oni/firewall.py) | Signal filtering | `NeuralFirewall`, `Signal` |
| [oni.scale_freq](oni-framework/oni/scale_freq.py) | f × S ≈ k invariant | `ScaleFrequencyInvariant` |

**Full documentation:** [oni-framework/README.md](oni-framework/README.md)

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
   └─────────────────────────┘    └─────────────────────┘
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

The ONI Framework extends OSI's 7 layers to 14, bridging silicon and biology:

| Layer | Name | Domain | Function |
|:-----:|------|--------|----------|
| L1 | Molecular | Biology | Ion channels, neurotransmitters |
| L2 | Cellular | Biology | Action potentials, synaptic transmission |
| L3 | Microcircuit | Biology | Local neural computation |
| L4 | Regional | Biology | Brain region specialization |
| L5 | Systems | Biology | Distributed neural networks |
| L6 | Whole-Brain | Biology | Global integration patterns |
| L7 | Behavioral | Biology | Observable outputs, motor commands |
| **L8** | **Neural Gateway** | **Bridge** | **BCI hardware boundary (Firewall lives here)** |
| L9 | Signal Processing | Silicon | Filtering, amplification, digitization |
| L10 | Protocol | Silicon | Data formatting, transmission rules |
| L11 | Transport | Silicon | Reliable data delivery |
| L12 | Session | Silicon | Connection management |
| L13 | Presentation | Silicon | Data interpretation |
| L14 | Application | Silicon | End-user interfaces |

---

## Visualizations

| Project | Description |
|---------|-------------|
| [ONI Visualizations](oni-visualizations/README.md) | Interactive web apps for ONI concepts |

---

## Transparency & Ethics

The ONI Framework maintains Responsible AI standards and documents alignment with neuroethics principles.

| Document | Purpose |
|----------|---------|
| [TRANSPARENCY.md](../TRANSPARENCY.md) | Human-AI collaboration audit trail — cognitive boundary documentation, HITL methodology |
| [NEUROETHICS_ALIGNMENT.md](NEUROETHICS_ALIGNMENT.md) | Maps framework components to cognitive liberty, mental privacy, mental integrity principles |

---

## Resources

### Templates

| Template | Purpose |
|----------|---------|
| [BLOG_TEMPLATE.md](resources/templates/BLOG_TEMPLATE.md) | Blog post formatting guide |
| [TECHDOC_TEMPLATE_APA.md](resources/templates/TECHDOC_TEMPLATE_APA.md) | Technical document (APA format) |
| [README_TEMPLATE.md](resources/templates/README_TEMPLATE.md) | Topic README template (for folder overviews) |

### Processes

| Document | Purpose |
|----------|---------|
| [PUBLISHING_INSTRUCTIONS.md](resources/processes/PUBLISHING_INSTRUCTIONS.md) | Step-by-step publishing workflow |
| [PROCESS_IMPROVEMENTS.md](resources/processes/PROCESS_IMPROVEMENTS.md) | Workflow enhancement tracking |

### Research Pipeline

| Resource | Purpose |
|----------|---------|
| [research_monitor.py](resources/pipeline/scripts/research_monitor.py) | Automated academic paper discovery |
| [keywords.json](resources/pipeline/scripts/keywords.json) | Research search terms database |
| [incoming/](resources/pipeline/incoming/) | New research discoveries |
| [processed/](resources/pipeline/processed/) | Reviewed and integrated research |

### Editor Agent (Quality & Sync)

| Resource | Purpose |
|----------|---------|
| [EDITOR_AGENT.md](resources/editor/EDITOR_AGENT.md) | **Main instructions — run before commits** |
| [AGENTS.md](../AGENTS.md) | **Ralph Loop learnings — read at session start** |
| [prd.json](../prd.json) | **Task tracker with exit conditions** |
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
| 2 | Adversarial Stimulation | Attack vectors through neural feedback | Ransomware, Firewall | Planned |
| 3 | Cross-Device Protocol | Multi-BCI communication standards | ONI L10-L12 | Conceptual |
| 4 | Neural Privacy Framework | Data minimization for neural signals | Coherence, Firewall | Conceptual |
| 5 | Regulatory Mapping | FDA/EU compliance for ONI architecture | All topics | Conceptual |

---

## Folder Structure

```
MAIN/
├── INDEX.md                    # This file (central hub)
├── NEUROETHICS_ALIGNMENT.md    # Framework-to-ethics principle mapping
│
├── oni-framework/              # Python library (pip install oni-framework)
│   ├── oni/                    # Source modules
│   │   ├── coherence.py        # Cₛ calculation
│   │   ├── layers.py           # 14-layer model
│   │   ├── firewall.py         # Neural Firewall
│   │   └── scale_freq.py       # f × S ≈ k
│   ├── tests/                  # Unit tests (77 tests)
│   └── pyproject.toml          # Package config
│
├── publications/               # Research content
│   ├── 0-oni-framework/
│   ├── coherence-metric/
│   ├── neural-firewall/
│   ├── neural-ransomware/
│   ├── quantum-encryption/
│   └── scale-frequency/
│
└── resources/                  # Templates, processes, tools
    ├── templates/
    ├── processes/
    └── pipeline/
```

---

## Metrics

| Metric | Count |
|--------|-------|
| Total Topics | 6 |
| Published Documents | 14 |
| Blog Posts | 8 |
| Technical Documents | 6 |
| Python Package | v0.1.0 |
| Unit Tests | 77 |
| Planned Topics | 5 |

---

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for collaboration guidelines. The ONI Framework welcomes contributions from neuroscience, security, hardware, and ethics disciplines.

---

## License

Apache 2.0 — See [LICENSE](../LICENSE)

---

← Back to [Repository Root](../README.md)

*This index is a living document. It evolves as the framework grows.*
