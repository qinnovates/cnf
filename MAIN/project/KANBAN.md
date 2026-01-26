# ONI Framework Kanban Board

> **Visual task board for tracking work in progress.**
> Synced with `prd.json` — update both when tasks move.

**Last Updated:** 2026-01-26
**Sprint:** Q1 2026

---

## Board Overview

```
+------------------+------------------+------------------+------------------+------------------+
|     BACKLOG      |      TO DO       |   IN PROGRESS    |    IN REVIEW     |       DONE       |
|   (Prioritized)  |  (Ready to Start)|   (Active Work)  |  (Needs Verify)  |   (Completed)    |
+------------------+------------------+------------------+------------------+------------------+
|                  |                  |                  |                  |                  |
| [P3] BrainFlow   | [P2] CHANGELOG   |                  |                  | [P0] Layer       |
| Integration      |                  |                  |                  | Validation       |
|                  | [P1] Python      |                  |                  |                  |
| [P2] MOABB       | Code Sync        |                  |                  | [P0] Editor      |
| Benchmarks       |                  |                  |                  | Agent            |
|                  | [P2] MOABB       |                  |                  |                  |
| [P2] MOABB       | Attack Scenarios |                  |                  | [P0] PM Agent    |
| Attack Scenarios |                  |                  |                  |                  |
|                  |                  |                  |                  | [P0] ONI Layer   |
|                  |                  |                  |                  | Correction       |
|                  |                  |                  |                  |                  |
|                  |                  |                  |                  | [P1] SIEM→NSAM   |
|                  |                  |                  |                  |                  |
|                  |                  |                  |                  | [P1] ONI_LAYERS  |
|                  |                  |                  |                  | Reference        |
|                  |                  |                  |                  |                  |
|                  |                  |                  |                  | ...+15 more      |
|                  |                  |                  |                  |                  |
+------------------+------------------+------------------+------------------+------------------+
     3 items            3 items           0 items           0 items           21 items
```

---

## Column Definitions

| Column | Entry Criteria | Exit Criteria |
|--------|----------------|---------------|
| **Backlog** | Idea captured, not yet prioritized | Priority assigned, dependencies clear |
| **To Do** | Prioritized, dependencies resolved, ready to start | Work begins |
| **In Progress** | Actively being worked on | Work complete, ready for review |
| **In Review** | Needs verification/testing | Exit condition verified |
| **Done** | Exit condition met, documented in prd.json | Learnings captured |

---

## Backlog (Prioritized)

### [P3] brainflow-integration
- **Description:** Add BrainFlow integration for real-time hardware support
- **Exit Condition:** `tara/data/brainflow_adapter.py` exists with OpenBCI Cyton support
- **Risk:** Low (nice-to-have feature)
- **Dependencies:** None
- **Estimate:** Medium effort

### [P2] moabb-coherence-benchmark
- **Description:** Benchmark Cₛ accuracy against real MOABB EEG data
- **Exit Condition:** Benchmark results with precision, recall, F1 for attack detection
- **Risk:** Medium (validation critical for credibility)
- **Dependencies:** moabb-adapter-implementation ✓
- **Estimate:** Medium effort

### [P2] moabb-attack-scenarios
- **Description:** Create real-signal attack scenarios using MOABB data
- **Exit Condition:** 3+ attack scenarios tested: spike injection, frequency hijacking, noise masking
- **Risk:** Medium (demonstrates practical applicability)
- **Dependencies:** moabb-adapter-implementation ✓
- **Estimate:** Medium effort

### [P2] bci-macro-to-micro-visualization
- **Description:** Create animated Blender visualization showing macro-to-micro BCI interface (brain → region → neurons → synapses → neurotransmitters)
- **Exit Condition:** Blender animation file with seamless zoom from whole brain to molecular level
- **Risk:** Medium (engineering challenge to stitch scales)
- **Dependencies:** None
- **Estimate:** Large effort
- **Notes:**
  - Goal: Visualize how BCIs interface with the brain, where electrodes sit, which regions
  - Current tech limitation: BCIs use electrical stimulation, cannot directly stimulate neurotransmitters (VERIFIED)
  - Resources found:
    - brain2printAI: AI tool to convert MRI → 3D printable brain models (https://www.nature.com/articles/s41598-025-00014-5)
    - Free brain STL: https://www.cgtrader.com/free-3d-models/character/human-anatomy/brain-59cffe18-e669-4dae-a588-1f82cee6fd45
    - Molecular Nodes addon for Blender (neurotransmitter/molecule rendering)
    - PDB database for receptor structures (e.g., dopamine D2 receptor: 6CM4)
  - Approach: Programmatically stitch components across scales for seamless animation
  - Related: Research doc `neuroscience-homework-todo/Research-BCI_Mouse_Movement.md`

---

## To Do (Ready to Start)

### [P2] changelog-creation
- **Description:** Create CHANGELOG.md at repository root
- **Exit Condition:** `CHANGELOG.md` exists with semantic versioning
- **Risk:** Low
- **Dependencies:** None
- **Estimate:** Small effort

### [P1] python-code-sync
- **Description:** Verify `oni-framework/oni/layers.py` matches corrected ONI model
- **Exit Condition:** Layer definitions in Python match corrected ONI (L1-L7 OSI, L8-L14 Neural)
- **Risk:** High (code-docs mismatch causes confusion)
- **Dependencies:** oni-layer-correction ✓
- **Estimate:** Small effort

### [P2] moabb-attack-scenarios
- **Description:** Create real-signal attack scenarios using MOABB data
- **Exit Condition:** 3+ attack scenarios tested with real EEG
- **Risk:** Medium
- **Dependencies:** moabb-adapter-implementation ✓
- **Estimate:** Medium effort

---

## In Progress

*No active tasks*

---

## In Review

*No tasks awaiting verification*

---

## Done (Completed)

### Q1 2026 Completions

| Task ID | Description | Completed | Priority |
|---------|-------------|-----------|----------|
| layer-validation | All 14-layer tables match TechDoc | 2026-01-22 | P0 |
| editor-agent-implementation | Editor Agent with hybrid model | 2026-01-22 | P0 |
| pm-agent-implementation | PM Agent for task tracking | 2026-01-22 | P0 |
| oni-layer-correction | Correct ONI layers (L1-L7 OSI) | 2026-01-22 | P0 |
| siem-to-nsam-rename | Rename siem → nsam | 2026-01-22 | P1 |
| oni-layers-reference | Create ONI_LAYERS.md | 2026-01-22 | P1 |
| nsam-external-threats | Document external BCI threats | 2026-01-22 | P2 |
| images-organization | Copy images to resources | 2026-01-22 | P2 |
| readme-privacy-statement | Add privacy/ethics to README | 2026-01-22 | P0 |
| hourglass-diagram-prompt | ChatGPT visualization prompt | 2026-01-22 | P3 |
| related-work-documentation | RELATED_WORK.md | 2026-01-23 | P1 |
| lazaro-munoz-consent-framework | Informed consent framework | 2026-01-24 | P1 |
| lazaro-munoz-post-deployment | Post-deployment ethics | 2026-01-24 | P1 |
| lazaro-munoz-pediatric | Pediatric considerations | 2026-01-24 | P1 |
| lazaro-munoz-neuroethics-expansion | Stakeholder perspectives | 2026-01-24 | P2 |
| consent-validation-module | consent.py module | 2026-01-24 | P1 |
| neurosecurity-implementation | Kohno + BCI Anonymizer | 2026-01-23 | P1 |
| moabb-adapter-implementation | MOABB adapter for EEG | 2026-01-24 | P1 |
| pm-hub-readme | Project README dashboard | 2026-01-26 | P2 |
| github-pages-sri-fix | SRI hash fix for GitHub Pages | 2026-01-26 | P0 |
| pypi-security-scan | Bandit security scan + fixes | 2026-01-26 | P1 |

**Total Completed:** 21 tasks

---

## WIP Limits

| Column | Limit | Current | Status |
|--------|-------|---------|--------|
| In Progress | 3 | 0 | OK |
| In Review | 2 | 0 | OK |

**Rule:** No new work starts if WIP limits exceeded.

---

## Swimlanes by Category

### Infrastructure & Tooling
```
Backlog: brainflow-integration
To Do: changelog-creation
Done: editor-agent, pm-agent, images-organization, pm-hub-readme, github-pages-sri-fix, pypi-security-scan
```

### Code & Implementation
```
Backlog: moabb-benchmarks, moabb-attacks
To Do: python-code-sync, moabb-attack-scenarios
Done: siem-to-nsam, consent-validation-module, neurosecurity-implementation, moabb-adapter
```

### Documentation & Governance
```
Done: layer-validation, oni-layer-correction, oni-layers-reference, nsam-external-threats,
      readme-privacy-statement, related-work, consent-framework, post-deployment,
      pediatric-considerations, neuroethics-expansion
```

### Visualization
```
Done: hourglass-diagram-prompt
```

---

## Priority Legend

| Priority | Label | Meaning | SLA |
|----------|-------|---------|-----|
| **P0** | Critical | Blocks all work, security issue, major bug | Immediate |
| **P1** | High | Important feature, significant impact | This sprint |
| **P2** | Medium | Nice to have, incremental improvement | Next sprint |
| **P3** | Low | Future enhancement, exploration | Backlog |

---

## Quick Stats

| Metric | Value |
|--------|-------|
| Total Tasks | 27 |
| Completed | 22 (81%) |
| In Progress | 0 |
| Pending | 5 |
| Blocked | 0 |

---

## Blocked Tasks

*No blocked tasks currently*

---

## Future Work (Icebox)

These are tracked in `prd.json` under `future_work`:

| ID | Title | Feasibility | Effort |
|----|-------|-------------|--------|
| future-neural-consent-publication | Neural Consent Publication | Practical | Medium |
| future-ai-attack-prediction | AI-Based Attack Prediction | Research-needed | Large |
| future-blog-paper-updates | Update existing publications | Practical | Medium |
| future-l11-l14-standards | L11-L14 Standards Development | Blocked-external | Large |

---

## How to Use This Board

### Moving Tasks

1. **Backlog → To Do:** When dependencies resolved and priority assigned
2. **To Do → In Progress:** When starting work (respect WIP limits)
3. **In Progress → In Review:** When work complete, needs verification
4. **In Review → Done:** When exit condition verified

### Syncing with prd.json

After moving tasks:
1. Update task `status` in `prd.json`
2. Add `completed_at` date for Done tasks
3. Add `learnings` for completed tasks
4. Update `metrics` section totals

### Adding New Tasks

1. Add to `prd.json` with unique ID
2. Add to Backlog section here
3. Assign priority (P0-P3)
4. Define exit condition
5. Identify dependencies

---

*Synced with: `prd.json` v0.5.0*
*Board Version: 1.1*
