# ONI Framework Project Management

> **Master document for tracking scope, risks, priorities, and project health.**
> This document provides comprehensive project oversight beyond task-level tracking.

**Version:** 1.0
**Last Updated:** 2026-01-24
**Project Start:** 2026-01-21
**Current Phase:** Foundation Building

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Scope Management](#2-scope-management)
3. [Risk Impact Assessment](#3-risk-impact-assessment)
4. [Priority Framework](#4-priority-framework)
5. [Completed Work Log](#5-completed-work-log)
6. [Upcoming Work](#6-upcoming-work)
7. [Dependencies & Blockers](#7-dependencies--blockers)
8. [Milestones & Timeline](#8-milestones--timeline)
9. [Resource Allocation](#9-resource-allocation)
10. [Decision Log](#10-decision-log)
11. [Metrics & Health](#11-metrics--health)

---

## 1. Project Overview

### Vision

The ONI (Organic Neural Interface) Framework provides a comprehensive security architecture for brain-computer interfaces, extending the OSI model into biological domains to protect neural data and cognitive integrity.

### Mission

Create an open-source, academically rigorous, and practically implementable security standard for BCIs that prioritizes human sovereignty, privacy, and cognitive freedom.

### Strategic Objectives

| Objective | Key Results | Status |
|-----------|-------------|--------|
| **Academic Credibility** | Peer-reviewed publication, arXiv preprint | In Progress |
| **Technical Foundation** | Working Python packages (oni-framework, oni-tara) | Achieved |
| **Ethical Framework** | Neuroethics alignment, consent architecture | Achieved |
| **Industry Readiness** | Reference implementation, manufacturer guide | Planned |
| **Community Building** | GitHub contributors, academic collaborators | Planned |

### Project Scope Statement

**In Scope:**
- 14-layer ONI security model (L1-L14)
- Coherence Metric (Cₛ) implementation
- Neural Firewall architecture
- Threat modeling (ransomware, DoS, eavesdropping)
- Consent and ethics frameworks
- Python reference implementation
- Academic publications

**Out of Scope:**
- Hardware BCI device development
- Clinical trials
- FDA regulatory submissions (documentation only)
- Real-time production deployment
- Proprietary manufacturer integrations

---

## 2. Scope Management

### Scope Baseline

| Category | Baseline (Jan 2026) | Current | Delta |
|----------|---------------------|---------|-------|
| Python Packages | 2 | 2 | 0 |
| Unit Tests | 77 | 90+ | +13 |
| Publications | 14 | 14 | 0 |
| Governance Docs | 2 | 5 | +3 |
| Topic Areas | 8 | 8 | 0 |

### Scope Change Requests

| ID | Description | Requested | Impact | Decision |
|----|-------------|-----------|--------|----------|
| SCR-001 | Add consent.py module | 2026-01-24 | Medium | **Approved** - Aligns with neuroethics |
| SCR-002 | MOABB adapter integration | 2026-01-24 | Medium | **Approved** - Enables validation |
| SCR-003 | BrainFlow hardware support | 2026-01-24 | Low | **Deferred** - Nice-to-have |
| SCR-004 | AI attack prediction | 2026-01-24 | High | **Future** - Research needed |

### Scope Creep Prevention

**Guardrails:**
1. All new features require exit condition before starting
2. Each task must map to a strategic objective
3. "Nice to have" features go to P3 backlog
4. Weekly scope review during active development

**Decision Framework:**
```
Does this directly advance a strategic objective?
    ├─ Yes → Is effort ≤ 1 sprint?
    │         ├─ Yes → Approve
    │         └─ No → Break into phases, prioritize
    └─ No → Add to future_work in prd.json
```

---

## 3. Risk Impact Assessment

### Risk Assessment Methodology

#### Likelihood Scale (L)

| Score | Label | Description | Frequency |
|-------|-------|-------------|-----------|
| 1 | Rare | Unlikely to occur | <10% chance |
| 2 | Unlikely | Could occur but not expected | 10-25% |
| 3 | Possible | Might occur | 25-50% |
| 4 | Likely | Probably will occur | 50-75% |
| 5 | Almost Certain | Expected to occur | >75% |

#### Impact Scale (I)

| Score | Label | Schedule | Scope | Quality | Reputation |
|-------|-------|----------|-------|---------|------------|
| 1 | Negligible | <1 day delay | No change | Minor issue | None |
| 2 | Minor | 1-3 days | Minor adjustment | Workaround needed | Internal only |
| 3 | Moderate | 1-2 weeks | Feature reduced | Noticeable defect | Some external |
| 4 | Major | 1+ month | Scope cut required | Significant defect | Public visibility |
| 5 | Severe | Project delay | Project pivot | Unusable | Reputational damage |

#### Risk Score Calculation

```
Risk Score = Likelihood × Impact

Matrix:
         Impact →
         1    2    3    4    5
    ┌────────────────────────────
  1 │  1    2    3    4    5     Low (1-4)
L 2 │  2    4    6    8   10     Medium (5-9)
i 3 │  3    6    9   12   15     High (10-14)
k 4 │  4    8   12   16   20     Critical (15-25)
e 5 │  5   10   15   20   25
```

### Active Risk Register

| ID | Risk | Category | L | I | Score | Level | Mitigation | Owner | Status |
|----|------|----------|---|---|-------|-------|------------|-------|--------|
| R-001 | Layer documentation inconsistency | Quality | 3 | 4 | 12 | High | Editor Agent validation | Editor | Mitigated |
| R-002 | No empirical Cₛ validation | Credibility | 4 | 4 | 16 | Critical | MOABB benchmarking | TBD | Open |
| R-003 | Single contributor (bus factor=1) | Sustainability | 4 | 5 | 20 | Critical | Documentation, OSS community | Author | Monitoring |
| R-004 | Academic claim without citation | Reputation | 2 | 4 | 8 | Medium | Research verification protocol | SOCRATES | Mitigated |
| R-005 | Code-documentation drift | Quality | 3 | 3 | 9 | Medium | Editor Agent sync_rules | Editor | Monitoring |
| R-006 | Scope creep into hardware | Scope | 2 | 3 | 6 | Medium | Scope statement, guardrails | PM | Mitigated |
| R-007 | Ethics framework gaps | Reputation | 2 | 4 | 8 | Medium | Lázaro-Muñoz integration | Author | Mitigated |
| R-008 | PyPI package vulnerabilities | Security | 2 | 3 | 6 | Medium | GitHub Actions, Dependabot | CI/CD | Monitoring |

### Risk Heatmap

```
        Impact
        1    2    3    4    5
      ┌─────────────────────────┐
    5 │                         │
    4 │           R-005  R-002  │  R-003
L   3 │           ─────  R-001  │
    2 │     R-006  R-008  R-004 │  R-007
    1 │                         │
      └─────────────────────────┘
         Low   Med   High  Crit
```

### Risk Response Strategies

| Strategy | When to Use | Example |
|----------|-------------|---------|
| **Avoid** | High impact, can eliminate cause | Don't commit unverified claims |
| **Mitigate** | Reduce likelihood or impact | Editor Agent reduces doc errors |
| **Transfer** | Shift risk to third party | Use established libraries |
| **Accept** | Low impact or unavoidable | Single contributor reality |
| **Monitor** | Watch for change | Bus factor risk |

### Closed Risks

| ID | Risk | Resolution | Closed Date |
|----|------|------------|-------------|
| R-009 | ONI layer model inverted | Fixed across all docs, Editor Agent prevents recurrence | 2026-01-22 |
| R-010 | Missing ethics statement | Added Privacy & Ethics section to README | 2026-01-22 |
| R-011 | Unacknowledged prior work | Created RELATED_WORK.md | 2026-01-23 |

---

## 4. Priority Framework

### Priority Definitions

| Level | Name | Criteria | Response Time | Examples |
|-------|------|----------|---------------|----------|
| **P0** | Critical | Blocks all work, security issue, data corruption | Immediate | Layer validation errors, broken tests |
| **P1** | High | Important for current milestone, significant impact | Same sprint | Core feature implementation |
| **P2** | Medium | Improves quality, nice to have this sprint | Next sprint | Documentation improvements |
| **P3** | Low | Future enhancement, exploratory | Backlog | New integrations, experiments |

### Priority Matrix

```
                     Impact
                Low         High
           ┌──────────┬──────────┐
    Urgent │    P2    │    P0    │
           ├──────────┼──────────┤
Not Urgent │    P3    │    P1    │
           └──────────┴──────────┘
```

### Current Priority Distribution

| Priority | Count | Percentage |
|----------|-------|------------|
| P0 | 0 | 0% |
| P1 | 2 | 40% |
| P2 | 2 | 40% |
| P3 | 1 | 20% |
| **Total Pending** | 5 | 100% |

### Priority Assignment Criteria

When assigning priority, score each criterion (0-2):

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| Strategic Alignment | No alignment | Indirect | Direct |
| User/Stakeholder Impact | Low | Medium | High |
| Technical Dependencies | None dependent | Some | Many blocked |
| Risk Reduction | None | Moderate | Significant |
| Effort Required | Large (>1 week) | Medium (days) | Small (<1 day) |

**Total Score → Priority:**
- 8-10: P0
- 5-7: P1
- 3-4: P2
- 0-2: P3

---

## 5. Completed Work Log

### Summary by Phase

| Phase | Period | Tasks Completed | Key Deliverables |
|-------|--------|-----------------|------------------|
| Foundation | Jan 21-22 | 10 | Editor Agent, PM Agent, Layer correction, ONI_LAYERS.md |
| Ethics Integration | Jan 23-24 | 8 | Neurosecurity module, Consent framework, Governance docs |

### Detailed Completion Log

#### Week of 2026-01-20

| Date | Task | Category | Impact | Learnings |
|------|------|----------|--------|-----------|
| 01-22 | Layer validation fix | Quality | Critical | README had inverted layers; always cross-check TechDoc |
| 01-22 | Editor Agent v1.0 | Tooling | High | Modular check files enable expansion |
| 01-22 | PM Agent | Tooling | Medium | Structured task tracking enables alignment |
| 01-22 | ONI layer correction | Quality | Critical | L1-L7 = Silicon (OSI), L8-L14 = Biology |
| 01-22 | SIEM → NSAM rename | Code | Medium | Updated imports across codebase |
| 01-22 | ONI_LAYERS.md | Docs | High | Single source of truth for 14 layers |
| 01-22 | External threats doc | Docs | Medium | MRI, EMP, trauma, RF interference |
| 01-22 | Images organization | Assets | Low | Centralized in resources/images/ |
| 01-22 | Privacy statement | Docs | Critical | Framework is for protection, NOT surveillance |
| 01-22 | Hourglass prompt | Visualization | Low | ChatGPT can generate diagrams |

#### Week of 2026-01-23

| Date | Task | Category | Impact | Learnings |
|------|------|----------|--------|-----------|
| 01-23 | Related work | Docs | High | Acknowledged Kohno, IEEE, BCI Anonymizer |
| 01-23 | Neurosecurity module | Code | High | Kohno threats map to ONI layers perfectly |
| 01-24 | Informed consent | Governance | High | Continuous consent for adaptive devices |
| 01-24 | Post-deployment ethics | Governance | High | $10K+/year maintenance, no US requirements |
| 01-24 | Pediatric considerations | Governance | High | 4 pressing concerns, assent at 80% |
| 01-24 | Neuroethics expansion | Governance | Medium | Relational autonomy model |
| 01-24 | consent.py module | Code | High | ConsentManager, ConsentValidator classes |
| 01-24 | MOABB adapter | Code | High | BSD license, Jayaram & Barachant citation |

### Velocity Metrics

| Week | Tasks Completed | Story Points* | Notes |
|------|-----------------|---------------|-------|
| W1 (01-20) | 10 | 25 | Foundation sprint |
| W2 (01-23) | 8 | 20 | Ethics integration |

*Story points estimated: Small=1, Medium=3, Large=5

---

## 6. Upcoming Work

### Next Sprint (Ready to Start)

| Task | Priority | Est. Effort | Owner | Dependencies |
|------|----------|-------------|-------|--------------|
| python-code-sync | P1 | Small | TBD | oni-layer-correction ✓ |
| changelog-creation | P2 | Small | TBD | None |
| moabb-attack-scenarios | P2 | Medium | TBD | moabb-adapter ✓ |

### Backlog (Prioritized)

| Task | Priority | Est. Effort | Dependencies | Notes |
|------|----------|-------------|--------------|-------|
| moabb-coherence-benchmark | P2 | Medium | moabb-adapter ✓ | Validation critical |
| brainflow-integration | P3 | Medium | None | Hardware support |

### Future Work (Research Phase)

| Initiative | Feasibility | Prerequisites | Effort |
|------------|-------------|---------------|--------|
| Neural Consent Publication | Practical | Consent framework complete | Medium |
| AI Attack Prediction | Research-needed | Attack database, ML models | Large |
| Update existing publications | Practical | Layer model finalized | Medium |
| L11-L14 Standards | Blocked-external | Industry standards maturity | Large |

---

## 7. Dependencies & Blockers

### Dependency Map

```
┌─────────────────────────────────────────────────────────────┐
│                     COMPLETED                                │
├─────────────────────────────────────────────────────────────┤
│  oni-layer-correction ──┬──→ python-code-sync (pending)     │
│                         └──→ layer-validation ✓             │
│                                                             │
│  moabb-adapter ──┬──→ moabb-coherence-benchmark (pending)   │
│                  └──→ moabb-attack-scenarios (pending)      │
│                                                             │
│  consent-framework ──→ neural-consent-publication (future)  │
│                                                             │
│  neurosecurity-implementation ──→ (unblocks future work)    │
└─────────────────────────────────────────────────────────────┘
```

### Current Blockers

| Blocker | Blocked Tasks | Severity | Resolution Path | ETA |
|---------|---------------|----------|-----------------|-----|
| *None currently* | — | — | — | — |

### External Dependencies

| Dependency | Type | Status | Impact if Missing |
|------------|------|--------|-------------------|
| MOABB library | Software | Available | Cannot validate Cₛ on real data |
| PyPI | Infrastructure | Available | Cannot publish packages |
| GitHub Actions | Infrastructure | Available | No CI/CD |
| Peer review | Process | Future | Academic credibility limited |
| FDA guidance | Regulatory | Evolving | Industry adoption unclear |

---

## 8. Milestones & Timeline

### Milestone Roadmap

```
2026 Q1                    Q2                    Q3                    Q4
│                          │                     │                     │
├─ M1: Foundation ✓        ├─ M3: Validation     ├─ M5: Publication    ├─ M7: Industry
│  - Editor Agent          │  - MOABB benchmark  │  - arXiv preprint   │  - Manufacturer guide
│  - Layer correction      │  - Attack scenarios │  - Peer review sub  │  - FDA alignment
│  - Ethics framework      │  - Performance      │  - Conference       │
│                          │                     │                     │
├─ M2: Implementation ◐    ├─ M4: Integration    ├─ M6: Community      │
│  - Python packages       │  - BrainFlow        │  - Contributors     │
│  - Neurosecurity         │  - Real hardware    │  - Documentation    │
│  - Consent module        │  - CI/CD complete   │  - Tutorials        │
│                          │                     │                     │
◄────────────────────────────────────────────────────────────────────────►
         We are here (Jan 2026)
```

### Milestone Details

| ID | Milestone | Target Date | Status | Key Deliverables |
|----|-----------|-------------|--------|------------------|
| M1 | Foundation Complete | 2026-01-24 | **Complete** | Editor Agent, PM Agent, Layer model, Ethics |
| M2 | Implementation Ready | 2026-02-15 | In Progress | Python sync, CHANGELOG, MOABB scenarios |
| M3 | Validation Complete | 2026-03-31 | Planned | Cₛ benchmarks, attack scenarios verified |
| M4 | Integration Ready | 2026-04-30 | Planned | BrainFlow, hardware support |
| M5 | Publication Ready | 2026-06-30 | Planned | arXiv, peer review submission |
| M6 | Community Launch | 2026-08-31 | Planned | Contributors, tutorials |
| M7 | Industry Ready | 2026-12-31 | Planned | Manufacturer guide, FDA docs |

---

## 9. Resource Allocation

### Current Team

| Role | Allocation | Responsibilities |
|------|------------|------------------|
| **Author (Kevin)** | 100% | Architecture, writing, decisions |
| **Claude AI** | Support | Code, documentation, analysis |
| **Editor Agent** | Automated | Quality validation |
| **PM Agent** | Automated | Task tracking |

### Time Allocation by Category

| Category | % of Effort | Notes |
|----------|-------------|-------|
| Code Development | 35% | Python packages, modules |
| Documentation | 30% | Publications, governance |
| Research | 20% | Literature, validation |
| Infrastructure | 10% | CI/CD, tooling |
| Planning | 5% | PM, coordination |

### Skill Gaps

| Skill | Current | Needed | Gap Resolution |
|-------|---------|--------|----------------|
| ML/AI | Moderate | High | For attack prediction |
| Hardware BCI | Low | Medium | For BrainFlow integration |
| Academic publishing | Moderate | High | For peer review |
| Regulatory | Low | Medium | For FDA alignment |

---

## 10. Decision Log

### Major Decisions

| Date | Decision | Context | Alternatives Considered | Rationale |
|------|----------|---------|-------------------------|-----------|
| 2026-01-21 | L1-L7 = Silicon (OSI), L9-L14 = Biology | Layer model confusion | Biology at L1, Mixed models | OSI compatibility, clear bridge at L8 |
| 2026-01-22 | Editor Agent hybrid model | Quality automation | Full automation, Manual only | Balance speed with safety |
| 2026-01-22 | Topic folders use README.md, main uses INDEX.md | GitHub rendering | All INDEX.md, All README.md | GitHub auto-renders README in folders |
| 2026-01-23 | Acknowledge prior work explicitly | Academic integrity | Claim novelty | Credibility, ethics |
| 2026-01-24 | Integrate Lázaro-Muñoz framework | Ethics completeness | Own framework only | Academic rigor, completeness |
| 2026-01-24 | Use MOABB for validation | Cₛ credibility | Synthetic data, BCI Competition | BSD license, comprehensive |

### Pending Decisions

| Decision Needed | Options | Criteria | Target Date |
|-----------------|---------|----------|-------------|
| Primary publication venue | arXiv, Journal of Neural Eng, Frontiers | Impact factor, speed, fit | 2026-02-28 |
| BrainFlow vs MNE-Python | Integrate one, both, neither | Hardware support, complexity | 2026-03-15 |

---

## 11. Metrics & Health

### Project Health Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│                    PROJECT HEALTH                           │
├─────────────────────────────────────────────────────────────┤
│  Scope:        ████████████░░░░░░░░  [60%]  On Track       │
│  Schedule:     ████████████████░░░░  [80%]  On Track       │
│  Quality:      ██████████████████░░  [90%]  Excellent      │
│  Risk:         ████████░░░░░░░░░░░░  [40%]  Monitoring     │
│  Team:         ████████████████████  [100%] Healthy        │
└─────────────────────────────────────────────────────────────┘
```

### Key Performance Indicators

| KPI | Target | Current | Trend |
|-----|--------|---------|-------|
| Task Completion Rate | >70% | 78% | ↑ |
| Documentation Coverage | 100% | 95% | → |
| Test Coverage | >80% | ~85% | ↑ |
| Open Critical Risks | 0 | 2 | → |
| Blocked Tasks | 0 | 0 | ✓ |
| Average Task Age (pending) | <7 days | 2 days | ✓ |

### Burndown Chart (Conceptual)

```
Tasks
  25 │ ●
     │   ╲
  20 │     ●
     │       ╲
  15 │         ●
     │           ╲
  10 │             ● ← We are here (5 remaining)
     │               ╲
   5 │                 ○ (projected)
     │                   ╲
   0 │─────────────────────○────────
     │  W1    W2    W3    W4    W5
     └────────────────────────────────
```

### Quality Metrics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Layer mismatches | 0 | 0 | ✓ |
| Broken links | 0 | 0 | ✓ |
| Undocumented modules | 0 | 0 | ✓ |
| Missing citations | 0 | 0 | ✓ |
| Code-doc sync issues | TBD | 0 | Pending |

---

## Quick Reference

### File Locations

| Document | Path | Purpose |
|----------|------|---------|
| This file | `MAIN/project/PROJECT_MANAGEMENT.md` | Master PM doc |
| Kanban Board | `MAIN/project/KANBAN.md` | Visual task board |
| Task Tracker | `MAIN/project/prd.json` | Machine-readable tasks |
| Process Improvements | `MAIN/project/processes/PROCESS_IMPROVEMENTS.md` | Workflow docs |
| Learnings | `AGENTS.md` | Ralph Loop knowledge |

### Update Schedule

| Document | Update Frequency | Trigger |
|----------|------------------|---------|
| KANBAN.md | Per task movement | Status change |
| prd.json | Per task change | Any task update |
| PROJECT_MANAGEMENT.md | Weekly + major changes | Sprint end, milestone |
| AGENTS.md | Per significant discovery | New learning |

### Escalation Path

| Issue Type | First Response | Escalation |
|------------|----------------|------------|
| Blocked task | Review dependencies | Adjust scope |
| Quality issue | Editor Agent | Manual review |
| Risk materialized | Assess impact | Update response |
| Scope creep | Check guardrails | Decision log |

---

*Document Version: 1.0*
*Last Updated: 2026-01-24*
*Next Review: 2026-01-31*
