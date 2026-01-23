# AGENTS.md — Knowledge Compounding for ONI Framework

> **Purpose:** Persistent learnings from Ralph Loop iterations. AI agents read this file at the start of each session to benefit from discovered patterns, gotchas, and conventions.

**Last Updated:** 2026-01-23
**Loop Iterations:** 2

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
| Total Iterations | 4 |
| Learnings Captured | 23 |
| Gotchas Documented | 7 |
| Patterns Established | 12 |

---

*This file is read by AI agents at session start. Update after every significant discovery.*
