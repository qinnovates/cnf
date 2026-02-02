# Brand Strategy: QInnovate, Mindloft, and QIF

> **Status:** DRAFT v0.2
> **Created:** 2026-02-02
> **Purpose:** Define the relationship between QInnovate, Mindloft, and QIF. Establish mission, positioning, and separation of concerns.

---

## The Three-Entity Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         QINNOVATE                                   │
│              The Organization / Parent Brand                        │
│         "Securing the Neural Frontier"                              │
│                                                                     │
│    ┌────────────────────────────────────────────────────────────┐   │
│    │                      MINDLOFT                              │   │
│    │           The Open-Source Research Home                     │   │
│    │         github.com/qinnovates/mindloft                     │   │
│    │                                                            │   │
│    │    ┌────────────────────────────────────┐                  │   │
│    │    │              QIF                   │   Autodidact     │   │
│    │    │   The Security Framework           │   TARA           │   │
│    │    │   (neurosecurity/qif/)             │   Docs / Tools   │   │
│    │    └────────────────────────────────────┘                  │   │
│    └────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

QIF is the flagship research contribution *within* Mindloft. Mindloft is the open-source home *under* QInnovate. The nesting matters — QIF doesn't exist outside Mindloft, and Mindloft doesn't exist outside QInnovate.

### Quick Reference

| Entity | What It Is | Audience | URL |
|--------|-----------|----------|-----|
| **QInnovate** | Organization / parent brand | General public, funders, media | qinnovates.github.io |
| **Mindloft** | GitHub repo / open-source home | Developers, researchers, contributors | github.com/qinnovates/mindloft |
| **QIF** | Security framework (the science) | Academics, BCI industry, standards bodies | mindloft/neurosecurity/qif/ |

### The "QI" Root

All three brands share the "QI" root, which carries a double meaning:

| Usage | Meaning |
|-------|---------|
| **QI** (collaboration) | Quantum Intelligence — Kevin Qi + Claude, thinking together |
| **QI** (variable) | Quantum Indeterminacy — the core variable in the QIF equation |
| **QInnovate** | QI + Innovate — the organization |
| **QIF** | QI + Framework — the framework |

The "QI" in QInnovate is intentionally ambiguous: it is both Kevin's surname and the scientific concept at the heart of the work. This is a feature, not an accident.

---

## 1. QInnovate — The Organization

### What It Is

QInnovate is the parent brand and public identity. It is the organization that houses all research, tools, and publications. Think of it as the "lab" or "institute."

### Mission Statement

> **QInnovate exists to ensure that brain-computer interfaces are as secure as they are powerful.** We build open security standards, frameworks, and tools for the neural frontier — because the mind should never be an attack surface.

### Vision

A world where neural interfaces are protected by open standards, where neural data is a recognized human right, and where the security gap between what we can build and what we can protect is closed before it becomes a crisis.

### Core Values

1. **Open by default.** Research, code, and standards are open-source. Security through obscurity does not work for the mind.
2. **Honest about uncertainty.** We label speculation as speculation. We don't overclaim. The framework is future-proof because it treats unknowns as parameters, not assumptions.
3. **Ethics are architecture, not afterthought.** Neuroethics is embedded at the framework level, not bolted on as a compliance checklist.
4. **Anticipatory, not reactive.** We build security for the BCI that will exist in 10 years, not just the one that exists today.

### Current Structure

QInnovate is currently a research initiative led by Kevin Qi. It is not a registered entity. All output is open-source under Apache 2.0. The organizational structure can evolve as the work matures (see Section 6.2).

---

## 2. Mindloft — The Repository

### What It Is

Mindloft is the GitHub repository (github.com/qinnovates/mindloft) and the project home for all QInnovate research output. It is the codebase, the documentation, the interactive tools, and the publications — all in one place.

### Tagline

> **"Projects for the mind — from neurosecurity to cognitive science."**

### What Lives in Mindloft

| Pillar | Contents | Status |
|--------|----------|--------|
| **Neurosecurity** | QIF framework, legacy ONI research, 31 publications, Python packages | Active |
| **Autodidact** | ONI Academy, learning visualizations, BCI fundamentals | Active |
| **Docs** | GitHub Pages website, interactive visualizations, whitepaper | Active |
| **Video** | Demo videos, motion graphics | Maintenance |

### Why "Mindloft"

The name evokes an elevated space for thinking — a loft where ideas about the mind are developed. It is warm, creative, and accessible. It signals that the work is about the mind (neuro) but isn't clinical or intimidating.

### Relationship to QInnovate

Mindloft is QInnovate's primary public repository. QInnovate is the identity; Mindloft is where the work lives. When someone finds the research, they land in Mindloft. When someone asks "who made this," the answer is QInnovate.

---

## 3. QIF — The Framework

### What It Is

QIF (Quantum Indeterministic Framework for Neural Security, pronounced "CHIEF") is the core academic and technical contribution. It is a 14-layer security architecture for brain-computer interfaces that accounts for quantum effects at the electrode-tissue boundary.

### Tagline

> **"Life's most important connections deserve the most thought."**

### What QIF Contains

| Component | Description |
|-----------|-------------|
| 14-layer architecture | OSI extended with 7 neural security layers (L8-L14) |
| Coherence metric (Cs) | Signal trustworthiness score, implementable today |
| QI equation (2 candidates) | Quantum-aware security scoring |
| Threat taxonomy | 7 attack types across classical and quantum domains |
| Governance framework | 9 neuroethics and compliance documents |
| 5 experimental predictions | Testable hypotheses that advance the field |

### Why QIF Is Separate from Mindloft

QIF is the intellectual contribution — the framework, the equations, the science. Mindloft is the container that holds QIF alongside other projects (Autodidact, TARA, educational content). Separating them means:

1. **QIF can be cited independently.** Academic papers cite "QIF (Qi, 2026)" not "the mindloft repository."
2. **Mindloft can grow beyond QIF.** If Kevin pursues cognitive science, AI safety, or other neuro-adjacent research, it lives in Mindloft alongside QIF.
3. **QIF has its own versioning.** QIF v2.0 doesn't mean Mindloft v2.0.

### Relationship to Legacy ONI

QIF is the successor to the ONI Framework. ONI (Open Neurosecurity Interoperability) was the v1 research — 31 publications, Python packages, and the original 14-layer model. QIF is the v2 redesign that adds quantum security layers, the QI equation, and formal governance.

ONI content is preserved in `neurosecurity/legacy-core/` for continuity. The Python packages still use `oni-framework` and `oni-tara` for backwards compatibility.

---

## 4. How They Relate — The Hierarchy

```
QInnovate (organization — qinnovates.github.io)
│
└── Mindloft (repository — github.com/qinnovates/mindloft)
    │
    ├── neurosecurity/
    │   ├── qif/              ← QIF Framework (the core contribution)
    │   └── legacy-core/      ← ONI v1 research (31 publications, packages)
    │
    ├── autodidact/           ← Educational content (ONI Academy)
    │
    ├── docs/                 ← GitHub Pages site + interactive tools
    │   ├── visualizations/   ← 13+ web-based demos
    │   └── whitepaper/       ← Published whitepaper
    │
    └── video/                ← Demo videos, motion graphics
```

### Brand Usage Rules

| Context | Use | Example |
|---------|-----|---------|
| Public website, social media | **QInnovate** | "QInnovate — Securing the Neural Frontier" |
| GitHub repository, code | **Mindloft** | "github.com/qinnovates/mindloft" |
| Academic citations | **QIF** | "QIF (Qi, 2026)" |
| Python packages | **ONI / TARA** (legacy) | `pip install oni-framework` |
| Blog posts about the research | **QIF** (framework) under **QInnovate** (byline) | "QInnovate Blog: Understanding the QIF Coherence Metric" |
| Grants, partnerships, pitches | **QInnovate** (the initiative) developing **QIF** (the framework) | "QInnovate develops QIF, an open security standard for BCIs" |

### What Each Brand Owns

| Decision | Owner |
|----------|-------|
| Mission, vision, values | QInnovate |
| Visual identity (logo, colors, fonts) | QInnovate |
| Repository structure, code architecture | Mindloft |
| Scientific claims, equations, layer model | QIF |
| Neuroethics positions, governance docs | QIF |
| Blog content, social media | QInnovate |
| Educational content | Mindloft / Autodidact |
| Python package branding | ONI / TARA (legacy, kept for compatibility) |

---

## 5. Identity Separation from Personal Brands

| Identity | GitHub | Purpose | Relationship to QInnovate |
|----------|--------|---------|---------------------------|
| **qinnovates** | github.com/qinnovates | QInnovate organization | IS QInnovate |
| **qikevinl** | github.com/qikevinl | Kevin Qi — research identity | Kevin is QInnovate's founder/lead researcher |
| **kevinqicode** | github.com/kevinqicode | Kevin Qi — personal brand | Separate. Content creation, not research |

### Rules

- QInnovate content lives under `qinnovates`. Research papers credit "Kevin Qi" as author, QInnovate as affiliation.
- `qikevinl` is the private development identity. Drafts, working documents, and the QIF truth document live here.
- `kevinqicode` is completely separate. YouTube, TikTok, personal brand content. May reference QInnovate research for educational videos but doesn't own it.

---

## 6. Open Questions (For Kevin to Decide)

### 6.1 Domain Strategy

| Option | Domain | Status |
|--------|--------|--------|
| A | qinnovate.com → qinnovates.github.io | Not yet purchased |
| B | mindloft.org → mindloft docs site | Not yet purchased |
| C | Both (qinnovate.com as org, mindloft.org as project) | Recommended |

**Recommendation:** Purchase both. `qinnovate.com` is the front door for the organization. `mindloft.org` is the technical/developer audience landing page. They can link to each other.

### 6.2 Nonprofit Status

QInnovate could be structured as:
- **Personal project** (current) — simplest, no legal overhead
- **Nonprofit / 501(c)(3)** — enables grant funding, tax-deductible donations, academic legitimacy
- **LLC** — if commercial products emerge (consulting, enterprise tools)

The .org domain does NOT require nonprofit status. But if Kevin plans to seek grants (NSF, NIH, DARPA) or academic partnerships, nonprofit status strengthens the application.

### 6.3 Scope Expansion

Mindloft is currently neurosecurity-focused. The architecture supports additional research areas (they would get their own folders alongside `neurosecurity/`), but there is no pressure to expand. QIF alone is substantial enough to justify the entire brand. Scope expansion should only happen when a new research area has real substance behind it, not as speculative brand-building.

### 6.4 Package Rebranding

The Python packages still use `oni-framework`, `oni-tara`, `oni-academy`. Should they be renamed to `qif-*` or `mindloft-*`?

**Recommendation:** Keep `oni-*` for now. Package renames break existing users. Add deprecation notices when ready to migrate. The packages are implementation details — the brand hierarchy doesn't depend on them.

---

## 7. Elevator Pitches

### 10 seconds (QInnovate)
> "We build open security standards for brain-computer interfaces."

### 30 seconds (QInnovate + QIF)
> "Brain-computer interfaces are being implanted in humans today, and there is no universal security standard for them. QInnovate is building QIF — an open framework that extends the internet's security model to the brain, with quantum-aware protections built in from the start."

### 2 minutes (Full story)
> "Right now, companies are implanting chips in human brains. Neuralink has patients. The BCI market is projected to reach $6 billion by 2030. But there is no universal security standard for these devices. No equivalent of what HTTPS did for the web, or what the OSI model did for networking.
>
> QInnovate is building that standard. Our framework, QIF, defines 14 security layers — the same 7 that protect the internet, plus 7 new layers for the biology side. It covers everything from the raw electrode signal all the way up to identity and cognitive agency.
>
> What makes QIF unusual is how it handles the unknown. At the boundary between silicon and brain tissue, there are open questions in quantum physics that nobody has resolved yet. Most frameworks either ignore this or bet on one answer. We built ours to work regardless of which answer turns out to be correct. The unknowns are parameters in the equation, not assumptions.
>
> Everything is open-source — the model, the math, the tools, the Python packages. We think the mind deserves security standards as rigorous as the ones we built for the internet."

---

*Draft v0.2*
*Revisions: Fixed hierarchy (QIF nested inside Mindloft, not parallel). Added QI root etymology. Removed speculative future pillars. Rewrote 2-minute pitch for general audience. Removed private infrastructure from public-facing diagrams.*

**Next steps for Kevin:**
1. Review and refine the mission statement and vision (Section 1) — make it your voice
2. Decide on domain strategy (Section 6.1)
3. Decide on organizational structure (Section 6.2)
4. Decide on package rebranding (Section 6.4)
