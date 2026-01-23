# AGENTS.md — Knowledge Compounding for ONI Framework

> **Purpose:** Persistent learnings from Ralph Loop iterations. AI agents read this file at the start of each session to benefit from discovered patterns, gotchas, and conventions.

**Last Updated:** 2026-01-22
**Loop Iterations:** 1

---

## Editor Agent Learnings

### Critical Discoveries

| Date | Learning | Impact |
|------|----------|--------|
| 2026-01-22 | 14-layer table in README.md was completely inverted (Biology/Silicon domains swapped) | Created `layer_validation.md` check — always cross-reference against TechDoc |
| 2026-01-22 | Topic folders use `README.md`, main wiki uses `INDEX.md` | Documented in naming conventions |
| 2026-01-22 | Truth hierarchy: TechDoc > Python code > INDEX.md > README.md | Lower priority files must match higher priority sources |

### Patterns Established

- **Authoritative Source:** `TechDoc-ONI_Framework.md` is the single source of truth for 14-layer definitions
- **Cascade Sync:** Changes to TechDoc must propagate to README.md, INDEX.md, and verify against Python code
- **Hybrid Validation:** Auto-fix mechanical issues (dates, counts), require approval for content changes

### Gotchas Avoided

- Never trust layer tables in README.md without cross-checking TechDoc
- The old model had L1-L7 as Biology — this is WRONG. Correct: L1-L7 = Silicon
- README.md files don't auto-update when TechDoc changes — Editor Agent sync_rules.md handles this

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
| Total Iterations | 1 |
| Learnings Captured | 12 |
| Gotchas Documented | 4 |
| Patterns Established | 8 |

---

*This file is read by AI agents at session start. Update after every significant discovery.*
