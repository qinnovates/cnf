<div align="center">
  <img src="docs/images/mindloft-hearts.png" alt="Mindloft" width="420">

  # M I N D L O F T

  **Security Engineering meets Neuroethics**

  *Safeguarding BCIs on the road to Web 5.0*

  **Qinnovate** — the engine. **Mindloft** — the workshop.

  > *"The most important connections require the most thought."*

  [![Tests](https://github.com/qinnovates/mindloft/actions/workflows/tests.yml/badge.svg)](https://github.com/qinnovates/mindloft/actions/workflows/tests.yml)
  [![Security](https://github.com/qinnovates/mindloft/actions/workflows/security.yml/badge.svg)](https://github.com/qinnovates/mindloft/actions/workflows/security.yml)

  [qinnovate.com/mindloft](https://qinnovate.com/mindloft/) · *"Let's Mind Our Way."*

</div>

## Table of Contents

- [Two Models. One Mission.](#two-models-one-mission)
  - [Classical Model — Securing Today](#classical-model--securing-today)
  - [Quantum Model — Securing Tomorrow](#quantum-model--securing-tomorrow)
  - [Neuroethics — The Bridge](#neuroethics--the-bridge)
- [NIST CSF Functions — How This Project Is Organized](#nist-csf-functions--how-this-project-is-organized)
  - [Identify — Map the Attack Surface](#identify--map-the-attack-surface)
  - [Protect — Build the Defenses](#protect--build-the-defenses)
  - [Detect — See What Others Miss](#detect--see-what-others-miss)
  - [Govern — Neuroethics as Foundation](#govern--neuroethics-as-foundation)
  - [Respond — Teach + Equip](#respond--teach--equip)
  - [Recover — Future Work](#recover--future-work)
- [Repository Structure](#repository-structure)
- [Project Evolution](#project-evolution)
- [Live Site — qinnovate.com/mindloft](#live-site--qinnovatecommindloft)
  - [Main Pages](#main-pages)
  - [Legacy Archive](#legacy-archive)
- [About](#about)

---

## Two Models. One Mission.

| | Classical | Quantum |
|---|---|---|
| **Framework** | ONI 14-Layer Model | QIF 7-Band Hourglass |
| **Focus** | Securing today | Securing tomorrow |
| **Foundation** | OSI extension into biology | Quantum physics at neural boundary |
| **Status** | Established | Active research |
| **Site** | [Classical Model](https://qinnovate.com/mindloft/classical/) | [Quantum Model](https://qinnovate.com/mindloft/quantum/) |
| **Bridge** | ← Neuroethics & Security by Design → |

### [Classical Model](MAIN/legacy-core/) — Securing Today

The ONI 14-layer model extends the OSI networking stack into the biological domain, providing the first comprehensive reference architecture for BCI security.

- 14-layer OSI extension (L1-L14: Silicon → Gateway → Cognitive Sovereignty)
- 31 research publications across 8 topics
- Python packages: `oni-framework`, `oni-tara`
- Threat taxonomy: 10 tactics, 46 techniques
- Neural Firewall architecture at Layer 8

### [Quantum Model](MAIN/qif/) — Securing Tomorrow

The QIF (Quantum Indeterministic Framework, pronounced "CHIEF") rebuilds BCI security from neuroscience constraints, incorporating quantum biology at the electrode-neuron interface.

- 7-band hourglass architecture (N3/N2/N1 | I0 | S1/S2/S3)
- QI Equation (under development) — two complementary formulations
- Hamiltonian formulation of electrode-neuron interface
- 9 governance documents (neuroethics, regulatory compliance, consent)
- Interactive whitepaper with AI voiceover

### [Neuroethics](MAIN/governance/) — The Bridge

Without neuroethics as the foundation, both models risk enabling the very threats they aim to prevent. Just as ethical hackers protect classical systems against nation-state threats, neuroethics must be the architectural foundation for both approaches.

---

## NIST CSF Functions — How This Project Is Organized

> Structured around the [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) functions, applied to the neural security domain.

### [Identify](MAIN/) — Map the Attack Surface

Understand the neural threat landscape before building defenses. BCIs are being implanted in humans today — with no universal security standard. This function creates the science to change that.

| Component | Model | Description |
|-----------|-------|-------------|
| [QIF Framework](MAIN/qif/) | Quantum | 7-band hourglass architecture, 9 architectural docs |
| [QIF Whitepaper](MAIN/qif/QIF-WHITEPAPER.md) | Quantum | Comprehensive working paper — v3.1 with Hamiltonian, Nobel Prize context |
| [Threat Taxonomy](MAIN/legacy-core/publications/) | Classical | 10 tactics, 46 techniques across the 14-layer model |
| [Field Journal](MAIN/qif/QIF-FIELD-JOURNAL.md) | Quantum | First-person research observations |

### [Protect](MAIN/legacy-core/) — Build the Defenses

Implement safeguards — from Python packages to architectural standards — that limit or contain the impact of neural security events.

| Component | Model | Description |
|-----------|-------|-------------|
| [oni-framework](MAIN/legacy-core/oni-framework/) | Classical | `pip install oni-framework` — 14-layer model, coherence metric, neural firewall |
| [oni-tara](MAIN/legacy-core/tara-nsec-platform/) | Classical | `pip install oni-tara` — real-time BCI security monitoring |
| [QI Equation](MAIN/qif/QIF-WHITEPAPER.md) | Quantum | Two complementary formulations — unified security metric |
| [Legacy Core (ONI)](MAIN/legacy-core/) | Classical | 31 publications, foundational research |

### [Detect](docs/visualizations/) — See What Others Miss

Find and analyze what classical security cannot see — quantum-scale anomalies at the electrode-tissue interface.

| Component | Model | Description |
|-----------|-------|-------------|
| [Coherence Metric](MAIN/legacy-core/publications/coherence-metric/) | Classical | Cₛ = e^(−(σ²ᵩ + σ²τ + σ²ᵧ)) — signal trust scoring |
| [QI Equation](MAIN/qif/QIF-WHITEPAPER.md) | Quantum | Quantum indeterminacy as a detection signal |
| [Visualizations](docs/visualizations/) | Both | 13+ interactive tools for exploring framework behavior |

### [Govern](MAIN/governance/) — Neuroethics as Foundation

Establish the ethical and regulatory context that makes both models trustworthy. Without governance, security is just capability without conscience.

| Component | Description |
|-----------|-------------|
| [Governance (9 docs)](MAIN/governance/) | Neuroethics, regulatory compliance, consent, UNESCO alignment |
| [Transparency](MAIN/governance/TRANSPARENCY.md) | Human-AI collaboration audit trail |
| [Neuroethics Alignment](MAIN/governance/NEUROETHICS_ALIGNMENT.md) | Framework-to-ethics principle mapping |

### [Respond](autodidactive/) — Teach + Equip

Take action — not just against incidents, but against ignorance. Making neuroscience and BCI security accessible so the field can respond collectively.

| Component | Description |
|-----------|-------------|
| [Autodidactive](autodidactive/oni-academy/) | Educational modules — `pip install oni-academy` |
| [Neuroscience](autodidactive/neuroscience/) | BCI fundamentals and neuroscience learning |
| [Media](autodidactive/) | BCI zoom animations, motion graphics, workflow tools |
| [Blog](https://qinnovate.com/mindloft/blog/) | Public-facing research communication |

### Recover — *Future Work*

Incident response and recovery for neural security breaches. What happens after a BCI is compromised? This function is not yet built — and that honesty is part of the research.

### Future Work

| Initiative | Description |
|-----------|-------------|
| **Multi-AI CI/CD Validation** | Incorporate cross-AI review (Gemini, Claude, others) into CI/CD pipeline as automated consistency checks — validating that changes to one model propagate correctly to both Classical and Quantum frameworks. A feedback cycle that also surfaces the work to external AI systems for broader review. |
| ~~**STRIDE Threat Matrix**~~ | ✅ **Done.** All 34 techniques in `shared/threat-matrix.json` mapped to STRIDE categories. Coverage: Information Disclosure (12), Tampering (22), Spoofing (10), Elevation of Privilege (13), Denial of Service (3), Repudiation (2). |
| ~~**Classical-Quantum Bridge**~~ | ✅ **Done.** `MAIN/shared/threat-matrix.json` + `bridge.py` — 9 tactics, 34 techniques, 6 defenses, 4 neurorights mapped to both models. `config.py` loads from shared source. |
| **Recover Function** | Incident response and recovery playbooks for neural security breaches. |
| **Human-in-the-Loop Validation** | This framework is pre-peer-review independent research. Before any claim moves from hypothesis to assertion, it requires HITL validation through: academic peer review, IEEE standards alignment (IEEE 2794, Neuroethics Framework), NIST CSF 2.0 compliance audit, and engagement with BCI security researchers (Kohno, Bonaci, Schroder). No equation, threshold, or architectural decision is finalized without external human expert review. AI assists — humans decide. |
| **Live BCI Testing** | Validate the framework against real hardware. Test coherence metric thresholds, signal injection detection, and anomaly classification using consumer-grade BCIs (OpenBCI, EMOTIV, Muse, BrainFlow-compatible devices). Move from synthetic data to empirical validation — every equation in `qif_equations.py` tested against live neural signals. |
| **BCI-Enhanced Website** | Build mindloft.org from the ground up as a BCI-aware web experience. Adaptive UI that responds to neural input — attention-driven navigation, cognitive load detection that adjusts content density, coherence-based authentication demos, and real-time signal visualization. Not a website with BCI bolted on, but a website architectured for neural interaction from the first line of code. |

**Python packages:**
```bash
pip install oni-framework   # 14-layer model, coherence metric, neural firewall
pip install oni-tara        # TARA — real-time BCI security monitoring
pip install oni-academy     # Autodidactive — self-adaptive learning
```

---

## Repository Structure

```
mindloft/
├── MAIN/                              # IDENTIFY + PROTECT: Map & build defenses
│   ├── governance/                    # 9 neuroethics + compliance docs (GOVERN)
│   ├── shared/                        # BRIDGE: Classical-Quantum shared data
│   │   ├── threat-matrix.json         # Single source of truth for threats (both models)
│   │   ├── bridge.py                  # Validation + consistency checker
│   │   └── README.md                  # Bridge documentation
│   ├── qif/                           # QUANTUM: QIF Framework (active, v3.1)
│   │   ├── framework/                 # 9 architectural documents (IDENTIFY)
│   │   ├── qif-lab/                   # Equation code, tests, Quarto whitepaper
│   │   └── images/                    # QIF model diagrams
│   └── legacy-core/                   # CLASSICAL: ONI Foundation (established)
│       ├── publications/              # 31 papers across 8 topics (IDENTIFY)
│       ├── oni-framework/             # Python: pip install oni-framework (PROTECT)
│       ├── tara-nsec-platform/        # Python: pip install oni-tara (PROTECT)
│       ├── resources/                 # Brand, templates, pipeline, editor
│       └── archive/                   # Website evolution (v1-v6)
│
├── autodidactive/                     # RESPOND: Teach + equip
│   ├── oni-academy/                   # Python: pip install oni-academy
│   ├── neuroscience/                  # Neuroscience fundamentals
│   ├── bci-zoom/                      # BCI zoom animation
│   ├── motion/                        # Motion graphics
│   └── workflow/                      # Workflow tools
│
├── docs/                              # GitHub Pages website
│   ├── index.html                     # Venn diagram landing (Classical | Quantum)
│   ├── classical/                     # Classical model site (ONI 14-layer)
│   ├── quantum/                       # Quantum model site (QIF hourglass)
│   ├── visualizations/                # 13+ interactive tools (DETECT)
│   ├── documentation/                 # Documentation hub
│   └── whitepaper/                    # Published whitepaper
```

---

## Project Evolution

Every version of this project is preserved. The journey from initial concept to the current dual-model framework is part of the research itself.

| Version | Date | What It Was | Live Link |
|---------|------|-------------|-----------|
| **v1** | Jan 18, 2026 | First public page. ONI 14-layer model introduced. | [View v1](https://qinnovates.github.io/mindloft/legacy/v1/) |
| **v2** | Jan 22, 2026 | Expanded documentation. Interactive layer visualization. | [View v2](https://qinnovates.github.io/mindloft/legacy/v2/) |
| **v3** | Jan 24, 2026 | Visual storytelling shift. Three.js and scroll-driven animations. | [View v3](https://qinnovates.github.io/mindloft/legacy/v3/) |
| **v4** | Jan 26, 2026 | Architecture refinement. GSAP ScrollTrigger. | [View v4](https://qinnovates.github.io/mindloft/legacy/v4/) |
| **v5** | Jan 28, 2026 | Final ONI iteration. Full interactive layer explorer. | [View v5](https://qinnovates.github.io/mindloft/legacy/v5/) |
| **ONI Whitepaper** | Jan 30, 2026 | Complete technical whitepaper. Coherence metric, scale-frequency, TARA. | [View whitepaper](https://qinnovates.github.io/mindloft/legacy/whitepaper-oni/) |
| **v6 (QIF)** | Feb 2, 2026 | Paradigm shift. QIF hourglass, AI voiceover, immersive whitepaper. | [View v6](https://qinnovates.github.io/mindloft/legacy/v6/) |
| **Current (Venn)** | Feb 3, 2026 | Classical/Quantum dual-model portal. Neuroethics at the center. | [View current](https://qinnovates.github.io/mindloft/) |

---

## Live Site — [qinnovate.com/mindloft](https://qinnovate.com/mindloft/)

### Main Pages

| Page | URL |
|------|-----|
| Landing (Venn Portal) | [/mindloft/](https://qinnovate.com/mindloft/) |
| Classical Model | [/mindloft/classical/](https://qinnovate.com/mindloft/classical/) |
| Quantum Model | [/mindloft/quantum/](https://qinnovate.com/mindloft/quantum/) |
| Whitepaper | [/mindloft/whitepaper/](https://qinnovate.com/mindloft/whitepaper/) |
| Documentation Hub | [/mindloft/documentation/](https://qinnovate.com/mindloft/documentation/) |
| Research | [/mindloft/research/](https://qinnovate.com/mindloft/research/) |
| About | [/mindloft/about/](https://qinnovate.com/mindloft/about/) |
| Blog | [/mindloft/blog/](https://qinnovate.com/mindloft/blog/) |

### Legacy Archive

| Page | URL |
|------|-----|
| Site Archive | [/mindloft/legacy/](https://qinnovate.com/mindloft/legacy/) |

---

## About

Kevin Qi — researching at the intersection of neuroscience, quantum security, and AI ethics.

[Full bio →](ABOUT.md) | [Contributing →](MAIN/legacy-core/CONTRIBUTING.md) | [License →](LICENSE) (Apache 2.0)

---

*Last update: 2026-02-03*
*Classical: 14 layers, 31 publications, 46 threats | Quantum: 7 bands, 9 framework docs, 9 governance docs | Packages: 3 | Visualizations: 13+*
