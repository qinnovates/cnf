# AGENTS.md — Knowledge Compounding for ONI Framework

> **Purpose:** Persistent learnings from Ralph Loop iterations. AI agents read this file at the start of each session to benefit from discovered patterns, gotchas, and conventions.

**Last Updated:** 2026-01-24
**Loop Iterations:** 7

---

## Editor Agent Learnings

### Critical Discoveries

| Date | Learning | Impact |
|------|----------|--------|
| 2026-01-22 | 14-layer table in README.md was completely inverted (Biology/Silicon domains swapped) | Created `layer_validation.md` check — always cross-reference against TechDoc |
| 2026-01-22 | Topic folders use `README.md`, main wiki uses `INDEX.md` | Documented in naming conventions |
| 2026-01-22 | Truth hierarchy: TechDoc > Python code > INDEX.md > README.md | Lower priority files must match higher priority sources |
| 2026-01-23 | BCI Anonymizer patent (US20140228701A1) was ABANDONED, never granted | Academic concepts freely implementable — added notes to neurosecurity module |
| 2026-01-23 | Kohno (2009) threat taxonomy maps perfectly to ONI layers: Alteration→L8-9, Blocking→L8-9, Eavesdropping→L13-14 | Implemented in oni.neurosecurity module with 12 detection rules |
| 2026-01-23 | PyPI trusted publishing via GitHub Actions is more secure than storing tokens | No secrets in config, OIDC-based authentication |
| 2026-01-23 | INDEX.md must be updated when packages/structure change | Created INDEX.md Update Protocol in CLAUDE.md — check versions, folder structure, metrics |
| 2026-01-23 | Repository reorganized: governance/, project/, visualizations/ | prd.json→project/, ethics→governance/, oni-visualizations→visualizations/, processes→project/ |
| 2026-01-24 | Research Verification Protocol adapted from kevinqicode hallucination firewall | Domain-specific verification: SOCRATES (general), GÖDEL (math), FARADAY (physics/neuro) |
| 2026-01-24 | Persona system implemented for research verification | 7 personas: AURORA, SOCRATES, GÖDEL, FARADAY, HYPATIA, ARCHIMEDES, EDITOR |
| 2026-01-24 | Uncertainty tagging system: ✅ ⚠️ 🔍 ❌ 🔬 | All claims must be tagged before publication |
| 2026-01-24 | **L9-L14 domain error found in 6+ files** — labeled as "Silicon" but should be "Biology" | Fixed ONI_LAYERS.md, README.md, NEUROETHICS_ALIGNMENT.md, layer_validation.md, prototype-mvp files |
| 2026-01-24 | **Comprehensive PM system implemented** — KANBAN.md + PROJECT_MANAGEMENT.md | Risk Impact Assessment (L×I matrix), Priority Framework (P0-P3), Scope Change Requests, Milestone roadmap |

### Patterns Established

- **Authoritative Source:** `TechDoc-ONI_Framework.md` is the single source of truth for 14-layer definitions
- **Cascade Sync:** Changes to TechDoc must propagate to README.md, INDEX.md, and verify against Python code
- **Hybrid Validation:** Auto-fix mechanical issues (dates, counts), require approval for content changes

### Gotchas Avoided

- Never trust layer tables in README.md without cross-checking TechDoc
- The old model had L1-L7 as Biology — this is WRONG. Correct: L1-L7 = Silicon
- README.md files don't auto-update when TechDoc changes — Editor Agent sync_rules.md handles this
- **INDEX.md must be updated when moving files or changing packages** — Python Packages, Dependency Map, Folder Structure, and Metrics sections all need updating
- **Folder names in INDEX.md can drift from reality** — e.g., `siem/` vs actual `nsam/`, always verify against filesystem
- **⚠️ CRITICAL: L9-L14 are BIOLOGY, not Silicon** — Even though L9-L10 involve signal processing/protocols, they operate on the BRAIN SIDE of the L8 bridge. This error appeared in 6+ files on 2026-01-24 and was systematically corrected. Memory aid: Below bridge (L1-L7) = computers. Above bridge (L9-L14) = brains.

---

## Persona System Learnings

### The ONI Research Personas

| Persona | Archetype | Domain | Key Question |
|---------|-----------|--------|--------------|
| **AURORA** | Illuminator | Main reasoning | "What's the insight?" |
| **SOCRATES** | Questioner | General verification | "What evidence supports this?" |
| **GÖDEL** | Logician | Math/formulas | "Does this formula hold?" |
| **FARADAY** | Experimentalist | Physics/neuroscience | "What does the science say?" |
| **HYPATIA** | Librarian | Documentation | "Where does this belong?" |
| **ARCHIMEDES** | Pragmatist | Project management | "What's the lever?" |
| **EDITOR** | Validator | Cross-references | "Is this consistent?" |

### Research Verification Protocol

Adapted from kevinqicode anti-hallucination firewall for academic research:

**4-Layer Architecture:**
```
Truth Layer      → Authoritative sources (papers, patents, specs)
Grounding Engine → Extract claims with citations
Firewall         → Domain-specific verification (SOCRATES/GÖDEL/FARADAY)
Publication      → Only verified content
```

**Uncertainty Tags:**
- ✅ VERIFIED — Peer-reviewed source, safe to use
- ⚠️ INFERRED — Logical inference, must label
- 🔍 UNVERIFIED — No source, do NOT use
- ❌ CONTRADICTED — Evidence against, do NOT use
- 🔬 HYPOTHESIS — Novel ONI contribution, label clearly

### Folder Structure for Verification

```
MAIN/resources/pipeline/
├── sources/                    # Authoritative documents
│   ├── papers/                 # Peer-reviewed
│   ├── patents/                # Patents
│   ├── specs/                  # Standards
│   └── data/                   # Datasets
├── verified/                   # Verified claims with citations
└── ...
```

### Key Patterns

| Pattern | Why |
|---------|-----|
| Domain personas prevent cross-domain errors | FARADAY catches physics errors GÖDEL misses |
| Tension between personas is valuable | SOCRATES questions what AURORA proposes |
| Uncertainty tags force explicit epistemic states | No more confident hallucinations |
| Verified claims file creates audit trail | Academic credibility requires traceability |

### Common Errors Caught

| Error Type | Persona | Example |
|------------|---------|---------|
| Timescale confusion | FARADAY | "10 ms" instead of "100 fs" quantum coherence |
| Uniform reliability | FARADAY | AI suggesting 0.95 instead of biological 0.85 |
| Formula mismatch | GÖDEL | TechDoc formula differs from Python code |
| Missing citation | SOCRATES | Confident claim with no source |

---

## Neurosecurity Implementation Learnings

### Key Discoveries

| Date | Discovery | Implementation |
|------|-----------|----------------|
| 2026-01-23 | Kohno (2009) defines 3 threat categories: Alteration, Blocking, Eavesdropping | Maps to CIA triad: Integrity, Availability, Confidentiality |
| 2026-01-23 | Bonaci (2015) BCI privacy filtering uses ERP component stripping | Implemented P300, N170, N400, ERN, LRP, CNV filters with sensitivity levels |
| 2026-01-23 | Privacy Score = weighted ERP sensitivity across signal components | PrivacyScoreCalculator with configurable weights |

### Module Structure

```
oni-framework/oni/neurosecurity/
├── __init__.py       # Exports, patent status note
├── firewall.py       # NeurosecurityFirewall (Kohno CIA triad)
├── anonymizer.py     # BCIAnonymizer (ERP filtering)
├── threats.py        # ThreatType enum, KohnoThreatModel
└── privacy_score.py  # PrivacyScoreCalculator
```

### TARA Integration

Created `tara/neurosecurity/integration.py` with 12 Kohno-based detection rules:
- Signal injection, neural DoS, cognitive leakage (base threats)
- Amplitude bounds, frequency analysis, spatial filtering (validation)
- Cross-layer correlation, behavioral deviation, cognitive fingerprinting (advanced)

---

## PyPI Publishing Learnings

### GitHub Actions Trusted Publishing

| Step | Action | Notes |
|------|--------|-------|
| 1 | Create PyPI project (or pending publisher) | Project name must match pyproject.toml |
| 2 | Configure trusted publisher on PyPI | Repository, workflow file, environment name |
| 3 | Use `pypa/gh-action-pypi-publish` action | `id-token: write` permission required |
| 4 | Configure environment in workflow | `environment: name: pypi` |

### Package Naming

- `oni-framework` — Core library (PyPI)
- `oni-tara` — TARA neural security platform (PyPI)
- Renamed from `tara-neural` to `oni-tara` for brand consistency

### Workflow Configuration

```yaml
permissions:
  id-token: write  # Required for trusted publishing
environment:
  name: pypi
  url: https://pypi.org/p/package-name
```

---

## Publishing Learnings

### Content Rules

| Rule | Why |
|------|-----|
| Keywords must be extracted to `keywords.json` | Research monitor depends on it |
| APA tables: numbers **BOLD**, titles *ITALIC* | Template compliance |
| Blog front-matter requires RFC 2822 date format | Medium compatibility |
| Sub-Tags footer required on all blog posts | Consistency |

### File Placement

| Content Type | Location | Wrong Location |
|--------------|----------|----------------|
| Blog posts | `publications/[topic]/` | `resources/` |
| TechDocs | `publications/[topic]/` | Root |
| Templates | `resources/templates/` | `publications/` |
| Editor checks | `resources/editor/checks/` | Anywhere else |

### Naming Conventions

```
Folders:   lowercase-hyphenated     (neural-firewall)
Blogs:     Blog-Topic_Name.md       (Blog-Neural_Firewall.md)
TechDocs:  TechDoc-Topic_Name.md    (TechDoc-Neural_Firewall.md)
```

---

## Cross-Reference Learnings

### Dependency Chain

```
ONI Framework (base)
    ├── Coherence Metric
    │   ├── Neural Firewall
    │   │   └── Neural Ransomware
    │   └── Scale-Frequency
    │       └── Quantum Encryption
    └── All other topics
```

### Common Sync Failures

| Symptom | Cause | Fix |
|---------|-------|-----|
| Layer names don't match | README not updated after TechDoc change | Run Editor Agent layer_validation |
| Broken internal links | File renamed without link update | Run Editor Agent sync_rules |
| Stale dates in footer | Manual process skipped | Auto-fix via Editor Agent |
| Wrong document count | New file added, footer not updated | Auto-fix via Editor Agent |
| INDEX.md shows wrong folder names | File/folder moved without updating INDEX.md | Follow INDEX.md Update Protocol |
| INDEX.md shows outdated versions | Package version changed without updating metrics | Update Python Packages and Metrics sections |
| INDEX.md dependency map stale | New package/component added without diagram update | Redraw dependency map in INDEX.md |

---

## Session Patterns

### What Works

1. **Read CLAUDE.md first** — Contains all conventions and workflows
2. **Run Editor Agent before commits** — Catches inconsistencies early
3. **Cross-reference TechDocs** — They are the authoritative source
4. **Update AGENTS.md after discoveries** — Knowledge compounds for next session

### What Doesn't Work

1. **Trusting derived files** — README.md, INDEX.md can drift from TechDoc
2. **Manual date/count updates** — Error-prone, let Editor Agent handle
3. **Assuming consistency** — Always validate with Editor Agent
4. **Skipping layer validation** — The 14-layer inversion bug proves this

---

## Technical Specifications

### The 14 ONI Layers (Canonical)

```
L1:  Physical Carrier          (Silicon)
L2:  Link Framing              (Silicon)
L3:  Network Routing           (Silicon)
L4:  Transport Flow            (Silicon)
L5:  Session State             (Silicon)
L6:  Data Encoding             (Silicon)
L7:  Application Interface     (Silicon)
L8:  Neural Gateway            (Bridge)
L9:  Ion Channel Encoding      (Biology)
L10: Oscillatory Synchrontic   (Biology)
L11: Cognitive Session         (Biology)
L12: Semantic Assembly         (Biology)
L13: Intent & Agency           (Biology)
L14: Identity & Ethics         (Biology)
```

### Key Formulas

| Name | Formula | Source |
|------|---------|--------|
| Coherence Score | Cₛ = Σᵢ wᵢ × Φᵢ(Δtᵢ) × Θᵢ(fᵢ, Aᵢ) | TechDoc-Coherence_Metric |
| Scale-Frequency | f × S ≈ k | TechDoc-Scale_Frequency |

---

## Project Management Learnings

### PM System Architecture

| Component | File | Purpose |
|-----------|------|---------|
| **PROJECT_MANAGEMENT.md** | `MAIN/project/` | Master doc: scope, risks, priorities, milestones, metrics |
| **KANBAN.md** | `MAIN/project/` | Visual board: Backlog → To Do → In Progress → In Review → Done |
| **prd.json** | `MAIN/project/` | Machine-readable task data with exit conditions |

### Risk Impact Assessment (RIA)

**Formula:** `Risk Score = Likelihood (1-5) × Impact (1-5)`

| Score Range | Level | Action |
|-------------|-------|--------|
| 1-4 | Low | Accept/monitor |
| 5-9 | Medium | Mitigate |
| 10-14 | High | Mitigate actively |
| 15-25 | Critical | Avoid or escalate |

### Priority Framework

| Level | Meaning | SLA |
|-------|---------|-----|
| **P0** | Blocks all work, security/data issue | Immediate |
| **P1** | Important for current milestone | Same sprint |
| **P2** | Nice to have, incremental improvement | Next sprint |
| **P3** | Future enhancement, exploration | Backlog |

### Key Patterns

- **WIP Limits:** 3 in progress, 2 in review — prevents overcommitment
- **Exit Conditions:** Every task must have machine-verifiable completion criteria
- **Scope Change Requests:** Document impact before approving new features
- **Milestone-Driven:** Q1-Q4 2026 roadmap with clear deliverables

### Critical Risks Identified

| Risk | Score | Status |
|------|-------|--------|
| No empirical Cₛ validation | 16 (Critical) | Open — MOABB benchmarks planned |
| Single contributor (bus factor=1) | 20 (Critical) | Monitoring — documentation helps |
| Code-documentation drift | 9 (Medium) | Mitigated — Editor Agent |

---

## Future Iteration Notes

### Pending Investigations

- [ ] Verify all topic README.md files have correct layer references
- [ ] Check if Python code in `oni-framework/oni/layers.py` matches TechDoc
- [ ] Validate formula representations are consistent across all documents

### Suggested Improvements

- Add formula regex validation to Editor Agent
- Create automated CHANGELOG.md generation
- Implement git hooks to auto-run Editor Agent

---

## Loop Metadata

| Metric | Value |
|--------|-------|
| Total Iterations | 7 |
| Learnings Captured | 28 |
| Gotchas Documented | 8 |
| Patterns Established | 20 |
| Personas Defined | 7 |
| PM Documents | 3 |

---

*This file is read by AI agents at session start. Update after every significant discovery.*
