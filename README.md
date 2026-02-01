# The Convergent Neurosecurity Framework

### A Model for Quantum Neural Interfaces

*Life's most important connections deserve the most thought.*

[![Tests](https://github.com/qinnovates/qinnovate/actions/workflows/tests.yml/badge.svg)](https://github.com/qinnovates/qinnovate/actions/workflows/tests.yml)
[![Security](https://github.com/qinnovates/qinnovate/actions/workflows/security.yml/badge.svg)](https://github.com/qinnovates/qinnovate/actions/workflows/security.yml)

---

## Start Here

| You are... | Start with... | What you'll find |
|------------|---------------|------------------|
| **Professor / Admissions** | [The Framework](#the-framework) → [Governance](#governance) | Strongest work: architectural redesign, neuroethics, quantum neurosecurity |
| **Researcher / Technical** | [Publications](#publications) → [Python Packages](#python-packages) → [Visualizations](#interactive-visualizations) | 31 papers, 2 pip-installable packages, 11 interactive tools |
| **Curious Visitor** | [Why This Exists](#why-this-exists) → [About](#about-the-author) | Context, motivation, the person behind the project |

---

## The Framework (v2 — February 2026)

> A ground-up architectural redesign of BCI security, built from neuroscience constraints rather than retrofitted IT models.

The original model placed the Neural Gateway at Layer 8 (middle of a 14-layer stack). BCIs are physical hardware — they belong adjacent to OSI Layer 1. Everything needed to be rebuilt from that realization.

**9 documents, designed to be read in order:**

| # | Document | What It Covers |
|---|----------|---------------|
| 01 | [WHY-REVAMP](neurosecurity-framework/framework/01-WHY-REVAMP.md) | Why the original model was fundamentally flawed |
| 02 | [KNOWNS-AND-UNKNOWNS](neurosecurity-framework/framework/02-KNOWNS-AND-UNKNOWNS.md) | What neuroscience has confirmed vs. what remains open |
| 03 | [BCI-CAPABILITIES](neurosecurity-framework/framework/03-BCI-CAPABILITIES.md) | Every proven BCI READ/WRITE/CLOSED-LOOP today |
| 04 | [FRAMEWORKS-ANALYSIS](neurosecurity-framework/framework/04-FRAMEWORKS-ANALYSIS.md) | OSI, Kandel, biological organization — the math and patterns |
| 05 | [PROPOSED-MODEL](neurosecurity-framework/framework/05-PROPOSED-MODEL.md) | The funnel model and quantum tunneling thought experiment |
| 06 | [GAP-ANALYSIS](neurosecurity-framework/framework/06-GAP-ANALYSIS.md) | Known limits vs. open questions |
| 07 | [QUANTUM-BIOLOGY](neurosecurity-framework/framework/07-QUANTUM-BIOLOGY.md) | What's proven, what's not, and the measurement wall |
| 08 | [QUANTUM-INTEGER](neurosecurity-framework/framework/08-QUANTUM-INTEGER.md) | Q — the labeled gap for quantum unknowns at each ring |
| 09 | [QUANTUM-NEUROSECURITY](neurosecurity-framework/framework/09-QUANTUM-NEUROSECURITY.md) | Quantum bridges, DSKE, defense-in-depth rings, NIST CSF lifecycle |

[Read the full framework introduction →](neurosecurity-framework/)

---

## Governance

> The foundation isn't faster tools. It's defining the rules those tools must follow.

| Document | Focus |
|----------|-------|
| [Transparency](neurosecurity-framework/governance/TRANSPARENCY.md) | Human-AI collaboration audit trail |
| [Neuroethics Alignment](neurosecurity-framework/governance/NEUROETHICS_ALIGNMENT.md) | Framework-to-ethics principle mapping |
| [UNESCO Alignment](neurosecurity-framework/governance/UNESCO_ALIGNMENT.md) | 15 of 17 UNESCO Recommendation elements implemented |
| [Regulatory Compliance](neurosecurity-framework/governance/REGULATORY_COMPLIANCE.md) | FDA, state laws, MIND Act, EU alignment |
| [Informed Consent](neurosecurity-framework/governance/INFORMED_CONSENT_FRAMEWORK.md) | Consent requirements (Lazaro-Munoz framework) |
| [Post-Deployment Ethics](neurosecurity-framework/governance/POST_DEPLOYMENT_ETHICS.md) | Device lifecycle and abandonment prevention |
| [Pediatric Considerations](neurosecurity-framework/governance/PEDIATRIC_CONSIDERATIONS.md) | Minors and limited capacity guidelines |
| [Data Policy FAQ](neurosecurity-framework/governance/DATA_POLICY_FAQ.md) | Privacy FAQ and user rights |
| [Accessibility](neurosecurity-framework/governance/ACCESSIBILITY.md) | Accessibility standards and compliance |

---

## Publications

31 research documents across 8 topic areas:

| Topic | Key Documents |
|-------|--------------|
| [Framework Foundation](neurosec-research/publications/0-oni-framework/) | Whitepaper, blog post, technical document |
| [Coherence Metric](neurosec-research/publications/coherence-metric/) | Signal integrity measurement (Cs = e^(-(sigma^2))) |
| [Detection Theory](neurosec-research/publications/detection-theory/) | Privacy-preserving ML for neural signals |
| [Mathematical Foundations](neurosec-research/publications/mathematical-foundations/) | Equations reference and audit |
| [Neural Firewall](neurosec-research/publications/neural-firewall/) | Layer 8 security architecture |
| [Neural Ransomware](neurosec-research/publications/neural-ransomware/) | Threat modeling for BCIs |
| [Quantum Encryption](neurosec-research/publications/quantum-encryption/) | QKD, tunneling traversal time |
| [Scale-Frequency](neurosec-research/publications/scale-frequency/) | The f x S ~ k invariant |

[Browse all publications →](neurosec-research/publications/)

---

## Python Packages

### oni-framework (v0.2.0)

```bash
pip install oni-framework
```

14-layer model, coherence metric, scale-frequency invariant, neural firewall primitives.
[Documentation →](neurosec-research/oni-framework/)

### oni-tara (v0.8.0)

```bash
pip install oni-tara
```

Telemetry Analysis & Response Automation — real-time BCI security monitoring, attack simulation, Streamlit dashboard.
[Documentation →](neurosec-research/tara-nsec-platform/)

---

## Interactive Visualizations

11 web-based tools demonstrating framework concepts:

| Tool | What It Does |
|------|-------------|
| [Coherence Metric Playground](docs/visualizations/01-coherence-metric-playground.html) | Interactive Cs calculation |
| [Layer Explorer](docs/visualizations/02-oni-layer-explorer.html) | 14-layer model browser |
| [Academic Alignment](docs/visualizations/03-academic-alignment.html) | Research landscape mapping |
| [Neural Kill Chain](docs/visualizations/03-neural-killchain-visualizer.html) | Attack sequence visualization |
| [NSAM Checkpoint Simulator](docs/visualizations/04-nsam-checkpoint-simulator.html) | Security monitoring simulation |
| [Scale-Frequency Navigator](docs/visualizations/05-scale-frequency-navigator.html) | f x S ~ k explorer |
| [Attack Matrix](docs/visualizations/06-oni-attack-matrix.html) | Threat-layer mapping |
| [Threat Matrix](docs/visualizations/06-oni-threat-matrix.html) | Comprehensive threat taxonomy |
| [Privacy-Preserving Monitoring](docs/visualizations/07-privacy-preserving-monitoring.html) | Privacy vs. security tradeoffs |
| [Framework Visualization](docs/visualizations/08-oni-framework-viz.html) | Full 14-layer interactive diagram |
| [Governance Stack](docs/visualizations/09-governance-stack.html) | Ethics-to-implementation mapping |

[Explore all visualizations →](docs/visualizations/)

**Published whitepaper:** [docs/whitepaper/](docs/whitepaper/)

---

## Educational Resources

**ONI Academy** — Python package for learning BCI security concepts:

```bash
pip install oni-academy
```

[Course curriculum →](autodidact/oni-academy/)

---

## Why This Exists

Brain-computer interfaces are being implanted in humans today. Neuralink, BrainGate, and dozens of clinical trials are creating direct connections between silicon and neural tissue — yet no universal security standard exists to protect the people who depend on them.

This framework translates neuroethical principles — cognitive liberty, mental privacy, mental integrity, psychological continuity — into testable, implementable security controls.

### The Priority Stack

```
DONE     Understand the brain (neuroscience, BCI capabilities, quantum biology)
DONE     Build the model (funnel, gap analysis, Q integer)
NOW      Ethics & governance — who owns neural data? consent? post-deployment?
NEXT     Classical security tools (TARA with measurable signals)
LATER    Quantum security tools (when quantum measurement advances)
```

### Why Governance First

The original v1 model relied on concepts of self, consciousness, and identity (L13-L14) — things we cannot measure, model, or define with math or science. Building security on unmeasurable abstractions is the wrong order. Start with what we can measure: ethical constraints and testable controls.

The more I learn, the more I realize how much I don't know. A framework built on that humility — one that labels its gaps instead of hiding them — is more trustworthy than one that claims to have all the answers.

---

## Repository Structure

```
qinnovate/
├── neurosecurity-framework/     # The Convergent Neurosecurity Framework
│   ├── framework/               # 9 architectural documents (v2)
│   └── governance/              # 9 neuroethics and compliance documents
│
├── neurosec-research/           # Foundational research (formerly ONI)
│   ├── publications/            # 31 research papers across 8 topics
│   ├── oni-framework/           # Python package (pip install oni-framework)
│   ├── tara-nsec-platform/      # TARA package (pip install oni-tara)
│   ├── resources/               # Templates, brand, pipeline, editor
│   └── archive/                 # Website evolution (v1-v5), old snapshots
│
├── docs/                        # GitHub Pages website
│   ├── index.html               # Landing page
│   ├── visualizations/          # 11 interactive tools
│   └── whitepaper/              # Published whitepaper
│
├── autodidact/                  # Educational content
│   ├── oni-academy/             # Python learning package
│   └── neuroscience-bci/        # Personal neuroscience notes
│
└── video/                       # Video production (Remotion)
```

---

## About the Author

Kevin Qi — researching at the intersection of neuroscience, quantum security, and AI ethics.

[Full bio →](ABOUT.md)

---

## Contributing

Contributions welcome. See [CONTRIBUTING.md](neurosec-research/CONTRIBUTING.md) for guidelines.

---

## License

Apache 2.0 — see [LICENSE](LICENSE).

---

*Last update: 2026-02-01*
*Framework v2: 9 docs | Governance: 9 docs | Publications: 31 | Python Packages: 2 | Visualizations: 11*
