# Neurosecurity

> Brain-Computer Interface security research — from quantum indeterminacy theory to practical threat detection.

This pillar contains all neurosecurity research under the Mindloft umbrella.

---

## Table of Contents

- [Structure](#structure)
- [Key Resources](#key-resources)
- [Evolution](#evolution)

---

## Structure

```
MAIN/
├── governance/       Ethics, compliance, accessibility (9 docs)
│
├── qif/              Quantum Indeterminacy Framework (current)
│   ├── framework/    Core research (9 papers)
│   └── images/       QIF model diagrams
│
├── legacy-core/      ONI Framework legacy (v1)
│   ├── publications/ Published research papers
│   ├── oni-framework/ Python detection library
│   ├── tara-nsec-platform/ Threat assessment platform
│   ├── resources/    Brand, templates, workflows
│   ├── project/      Project management
│   └── archive/      Historical website versions
│
See also: [autodidact/](../autodidact/) — Educational content (oni-academy, learnviz, BCI fundamentals)
```

## Key Resources

| Resource | Path | Description |
|----------|------|-------------|
| QIF Framework | `qif/framework/` | Quantum indeterminacy bounds for neural signal authentication |
| Coherence Metric | `legacy-core/publications/coherence-metric/` | Core detection equation: Cs = e^(-(s2_phi + s2_tau + s2_gamma)) |
| 14-Layer Model | `legacy-core/publications/0-oni-framework/` | Full BCI security architecture |
| Threat Taxonomy | `legacy-core/publications/threat-taxonomy/` | 46 attack techniques against BCI systems |
| Neural Firewall | `legacy-core/publications/neural-firewall/` | Layer 8 enforcement of validity bands |
| TARA Platform | `legacy-core/tara-nsec-platform/` | Threat Assessment & Risk Analysis MVP |
| ONI Python Lib | `legacy-core/oni-framework/` | `pip install oni-framework` |

## Evolution

```
ONI (v1) → CNF (v2) → QIF (current)
```

- **ONI** (Open Neurosecurity Interoperability): Original 14-layer framework
- **CNF** (Cognitive Neurosecurity Framework): Restructured with governance
- **QIF** (Quantum Indeterminacy Framework): Grounded in quantum physics — the "unknowns" in biological neural signals are the security feature
