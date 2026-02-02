# Mindloft

> Projects for the mind — from neurosecurity to cognitive science.

[![Tests](https://github.com/qinnovates/mindloft/actions/workflows/tests.yml/badge.svg)](https://github.com/qinnovates/mindloft/actions/workflows/tests.yml)
[![Security](https://github.com/qinnovates/mindloft/actions/workflows/security.yml/badge.svg)](https://github.com/qinnovates/mindloft/actions/workflows/security.yml)

---

## Pillars

### [Neurosecurity](neurosecurity/) — BCI Security Research

Brain-computer interfaces are being implanted in humans today. This pillar builds the security frameworks to protect them.

| Component | Description |
|-----------|-------------|
| [QIF Framework](neurosecurity/qif/) | Quantum Indeterminacy Framework — 9 architectural docs + 9 governance docs |
| [Legacy Core (ONI)](neurosecurity/legacy-core/) | 31 publications, Python packages, TARA platform |
| [Autodidact](neurosecurity/autodidact/) | ONI Academy, learning visualizations, BCI fundamentals |

**Key resources:**
- [QIF Framework (9 docs)](neurosecurity/qif/framework/) — read in order, 01 through 09
- [Governance (9 docs)](neurosecurity/qif/governance/) — neuroethics, regulatory compliance, consent
- [Publications (31 papers)](neurosecurity/legacy-core/publications/) — coherence metric, neural firewall, quantum encryption
- [Interactive Visualizations (13+ tools)](docs/visualizations/) — web-based framework demos
- [Whitepaper](docs/whitepaper/)

**Python packages:**
```bash
pip install oni-framework   # 14-layer model, coherence metric, neural firewall
pip install oni-tara        # TARA — real-time BCI security monitoring
pip install oni-academy     # Educational modules
```

---

## Repository Structure

```
mindloft/
├── neurosecurity/                     # PILLAR 1: BCI/Neural Security
│   ├── qif/                           # Quantum Indeterminacy Framework
│   │   ├── framework/                 # 9 architectural documents (v2)
│   │   ├── governance/                # 9 neuroethics + compliance docs
│   │   └── images/                    # QIF model diagrams
│   ├── legacy-core/                   # ONI Foundation (v1)
│   │   ├── publications/              # 31 papers across 8 topics
│   │   ├── oni-framework/             # Python: pip install oni-framework
│   │   ├── tara-nsec-platform/        # Python: pip install oni-tara
│   │   ├── resources/                 # Brand, templates, pipeline, editor
│   │   └── archive/                   # Website evolution (v1-v5)
│   └── autodidact/                    # Educational content
│       ├── oni-academy/               # Python: pip install oni-academy
│       └── neuroscience-bci/          # BCI fundamentals
│
├── docs/                              # GitHub Pages website
│   ├── index.html                     # Landing page
│   ├── visualizations/                # 13+ interactive tools
│   ├── documentation/                 # Documentation hub
│   └── whitepaper/                    # Published whitepaper
│
├── video/                             # Video production
│
└── [future pillars]                   # Room to grow
```

---

## About

Kevin Qi — researching at the intersection of neuroscience, quantum security, and AI ethics.

[Full bio →](ABOUT.md) | [Contributing →](neurosecurity/legacy-core/CONTRIBUTING.md) | [License →](LICENSE) (Apache 2.0)

---

*Last update: 2026-02-02*
*QIF: 9 docs | Governance: 9 docs | Publications: 31 | Python Packages: 3 | Visualizations: 13+*
