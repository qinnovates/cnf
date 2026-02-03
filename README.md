# Mindloft

> Projects for the mind — from neurosecurity to cognitive science.

[![Tests](https://github.com/qinnovates/mindloft/actions/workflows/tests.yml/badge.svg)](https://github.com/qinnovates/mindloft/actions/workflows/tests.yml)
[![Security](https://github.com/qinnovates/mindloft/actions/workflows/security.yml/badge.svg)](https://github.com/qinnovates/mindloft/actions/workflows/security.yml)

<div align="center">

https://github.com/qinnovates/mindloft/releases/download/v1.0.0-demo/ONIDemoVideo.mp4

</div>

---

## Pillars

### [Neurosecurity](neurosecurity/) — BCI Security Research

Brain-computer interfaces are being implanted in humans today. This pillar builds the security frameworks to protect them.

| Component | Description |
|-----------|-------------|
| [QIF Framework](neurosecurity/qif/) | Quantum Indeterminacy Framework — 9 architectural docs + 9 governance docs |
| [Legacy Core (ONI)](neurosecurity/legacy-core/) | 31 publications, Python packages, TARA platform |
| [Autodidact](autodidact/) | ONI Academy, learning visualizations, BCI fundamentals |

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
│
├── autodidact/                        # Educational content
│   ├── oni-academy/                   # Python: pip install oni-academy
│   └── neuroscience-bci/              # BCI fundamentals
│
├── docs/                              # GitHub Pages website
│   ├── index.html                     # Landing page
│   ├── visualizations/                # 13+ interactive tools
│   ├── documentation/                 # Documentation hub
│   └── whitepaper/                    # Published whitepaper
│
├── content/videos/                     # Video production
│
└── [future pillars]                   # Room to grow
```

---

## Project Evolution

Every version of this project is preserved. The journey from initial concept to the current QIF framework is part of the research itself — it shows how the problem was identified, how the thinking evolved, and why a quantum-informed approach became necessary.

| Version | Date | What It Was | Live Link |
|---------|------|-------------|-----------|
| **v1** | Jan 18, 2026 | First public page. "BCIs are being implanted in humans today — with no security standard." Introduced the ONI 14-layer model as "The OSI of Mind." | [View v1](https://qinnovate.com/mindloft/legacy/v1/) |
| **v2** | Jan 22, 2026 | Expanded documentation. Refined the 14-layer presentation and added interactive layer visualization. | [View v2](https://qinnovate.com/mindloft/legacy/v2/) |
| **v3** | Jan 24, 2026 | Visual storytelling shift. Added Three.js and scroll-driven animations. "No standards. No ethics. No security. Until now." | [View v3](https://qinnovate.com/mindloft/legacy/v3/) |
| **v4** | Jan 26, 2026 | Architecture refinement. Stabilized the immersive visual direction with GSAP ScrollTrigger. | [View v4](https://qinnovate.com/mindloft/legacy/v4/) |
| **v5** | Jan 28, 2026 | Final ONI iteration. Full interactive layer explorer, governance sections, polished narrative. | [View v5](https://qinnovate.com/mindloft/legacy/v5/) |
| **ONI Whitepaper** | Jan 30, 2026 | Complete technical whitepaper. Coherence metric, scale-frequency invariant, neural firewall, TARA platform. The culmination of the ONI framework. | [View whitepaper](https://qinnovate.com/mindloft/legacy/whitepaper-oni/) |
| **Current (QIF)** | Feb 2, 2026 | Paradigm shift. ONI becomes legacy. QIF (Quantum Indeterministic Framework) rebuilds from neuroscience constraints with quantum-informed security. BCI-adaptive mode, AI voiceover, immersive whitepaper. | [View current](https://qinnovate.com/mindloft/) |

> **Why preserve all versions?** The original v1 identified the right problem — BCIs have no security standard. Each iteration refined the approach. The transition from ONI to QIF wasn't abandoning that vision, it was deepening it: moving from a network-security analogy to a framework grounded in the actual physics and neuroscience of the bio-digital boundary.

---

## About

Kevin Qi — researching at the intersection of neuroscience, quantum security, and AI ethics.

[Full bio →](ABOUT.md) | [Contributing →](neurosecurity/legacy-core/CONTRIBUTING.md) | [License →](LICENSE) (Apache 2.0)

---

*Last update: 2026-02-02*
*QIF: 9 docs | Governance: 9 docs | Publications: 31 | Python Packages: 3 | Visualizations: 13+*
