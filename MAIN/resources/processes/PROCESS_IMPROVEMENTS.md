# Process Improvement Strategy for ONI Framework Publishing

## Current State Analysis

### What's Working
1. **Clear folder structure** - Topic-based organization with `MAIN/publications/` and `MAIN/resources/` separation
2. **Naming conventions** - Consistent `Medium-*` and `TechDoc-*` patterns across all 10 publications
3. **Templates exist** - APA, Medium (v2), and INDEX templates provide comprehensive formatting guidance
4. **CLAUDE.md** - Comprehensive AI instructions with file trees, workflows, and quality checklists
5. **MAIN/INDEX.md** - Cross-reference registry with dependency maps and publication matrix
6. **Research Pipeline** - Automated research monitoring via `keywords.json` and `research_monitor.py`
7. **YAML front-matter** - Implemented on all publications with title, date, URL, and tags

### Gaps Identified
1. ~~No automated validation of file naming~~ → Checklist documented, automation pending
2. ~~README.md updates are manual and error-prone~~ → Process documented in CLAUDE.md
3. ~~No version tracking for individual documents~~ → Partial (front-matter on publications)
4. ~~Cross-references between papers not systematically maintained~~ → **RESOLVED: MAIN/INDEX.md**
5. No content calendar or publishing schedule tracking
6. INDEX.md only deployed to 1 of 5 topic folders
7. No CHANGELOG.md at repository root

---

## Recommended Improvements

### 1. Pre-Commit Checklist Automation

Create a checklist that Claude runs through before every commit:

```markdown
## Pre-Commit Verification

### File Naming
- [ ] All Medium posts match `Medium-[Topic_Name].md`
- [ ] All papers match `[Topic_Name]_Paper.md`
- [ ] Folder names are lowercase-hyphenated

### Content Quality
- [ ] Tables have bold numbers, italic titles
- [ ] References are APA formatted (papers)
- [ ] Acknowledgments included (papers)
- [ ] Front matter complete (Medium)

### Repository Updates
- [ ] README.md links updated
- [ ] README.md document count updated
- [ ] README.md date updated
- [ ] File trees in instructions updated if structure changed
```

### 2. Document Metadata Standard

Add consistent metadata to all documents:

```yaml
---
# Required for all documents
title: ""
type: "Medium" | "Paper" | "Template" | "Instructions"
topic: ""  # Maps to folder name
version: "1.0"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"

# For Medium posts
url: ""
tags: []

# For Papers
keywords: []
abstract: ""
---
```

### 3. Cross-Reference Registry

Maintain a registry of how documents reference each other:

| Document | References | Referenced By |
|----------|------------|---------------|
| ONI_Framework_Paper | - | All other papers |
| Coherence_Metric_Paper | ONI_Framework | Neural_Firewall, Neural_Ransomware |
| Neural_Firewall_Paper | ONI_Framework, Coherence_Metric | Neural_Ransomware |
| Neural_Ransomware_Paper | ONI_Framework, Coherence_Metric, Neural_Firewall | - |
| Scale_Frequency_Paper | ONI_Framework | - |

This helps maintain consistency when updating any document.

### 4. Version Changelog

Create `CHANGELOG.md` at repository root:

```markdown
# Changelog

## [2026-01-21]
### Added
- README.AI.md for Claude instructions
- MEDIUM_TEMPLATE.md for post formatting
- PUBLISHING_INSTRUCTIONS.md workflow guide

### Changed
- Reorganized into MAIN/publications structure
- Renamed files to consistent convention
- Updated ABOUT.md with expanded bio

### Removed
- Duplicate Medium post files
```

### 5. Publishing Workflow States

Track content through stages:

```
Draft → Review → Formatted → Committed → Published
```

For each document, track:
- Current state
- Last update date
- Medium URL (if published)
- Any pending updates needed

---

## Template Inventory

### Current Templates
| Template | Purpose | Location | Status |
|----------|---------|----------|--------|
| TECHDOC_TEMPLATE_APA.md | Technical papers | MAIN/resources/templates/ | ✓ Active |
| MEDIUM_TEMPLATE.md | Medium posts (v2) | MAIN/resources/templates/ | ✓ Active |
| medium_template_v2.py | Python template generator | MAIN/resources/templates/ | ✓ Active |
| INDEX_TEMPLATE.md | Topic folder indexes | MAIN/resources/templates/ | ✓ Active |
| PUBLISHING_INSTRUCTIONS.md | Workflow guide | MAIN/resources/processes/ | ✓ Active |

### Proposed Additional Templates

#### 1. Research Note Template (NOT YET IMPLEMENTED)
For shorter, less formal research notes that may become papers later:

```markdown
# Research Note: [Topic]

**Date:** YYYY-MM-DD
**Status:** Draft | In Review | Archived
**Related Papers:** [links]

## Key Insight

[1-2 paragraph summary]

## Supporting Evidence

[Bullet points or short sections]

## Questions for Further Research

- [ ] Question 1
- [ ] Question 2

## Raw Notes

[Unstructured notes, quotes, references]
```

#### 2. Topic Index Template — ✓ IMPLEMENTED
Template exists at `MAIN/resources/templates/INDEX_TEMPLATE.md`. Deployed to `0-oni-framework/INDEX.md`.
For each topic folder, create an INDEX.md:

```markdown
# [Topic Name] Index

## Overview
[2-3 sentence summary of this topic area]

## Documents

| Document | Type | Last Updated | Status |
|----------|------|--------------|--------|
| Medium-Topic.md | Medium | 2026-01-21 | Published |
| Topic_Paper.md | Paper | 2026-01-21 | Complete |

## Key Concepts
- Concept 1: [brief definition]
- Concept 2: [brief definition]

## Related Topics
- [Link to related topic 1]
- [Link to related topic 2]
```

---

## Automation Opportunities

### 1. README.md Auto-Update Script

Logic for Claude to follow after each content addition:

1. Scan `MAIN/publications/*/` for all markdown files
2. Count total documents
3. Update document count in README.md footer
4. Update date in README.md footer
5. Verify all links in Topics & Documents section are valid

### 2. File Naming Validator

Before commit, verify:
```
- Medium posts: /^Medium-[A-Z][a-zA-Z_]+\.md$/
- Papers: /^[A-Z][a-zA-Z_]+_(Paper|Detailed_Paper)\.md$/
- Folders: /^[a-z]+(-[a-z]+)*$/
```

### 3. Cross-Reference Checker

After editing any paper:
1. Extract all internal references (links to other ONI papers)
2. Verify referenced documents exist
3. Check if referenced documents need updates for consistency

---

## Current File Tree (Implemented)

```
ONI/
├── README.md
├── CLAUDE.md                       # ✓ AI instructions (was README.AI.md)
├── MAIN/INDEX.md                    # ✓ Cross-reference registry
├── ABOUT.md
├── CHANGELOG.md                    # ✗ PENDING
├── CONTRIBUTING.md
├── LICENSE
│
└── MAIN/
    ├── resources/
    │   ├── templates/
    │   │   ├── TECHDOC_TEMPLATE_APA.md
    │   │   ├── MEDIUM_TEMPLATE.md
    │   │   ├── medium_template_v2.py
    │   │   └── INDEX_TEMPLATE.md
    │   ├── processes/
    │   │   ├── PUBLISHING_INSTRUCTIONS.md
    │   │   └── PROCESS_IMPROVEMENTS.md   # This file
    │   └── pipeline/
    │       └── continuous-research-delivery/
    │           └── scripts/
    │               ├── keywords.json
    │               └── research_monitor.py
    │
    └── publications/
        ├── 0-oni-framework/
        │   ├── INDEX.md              # ✓ COMPLETE
        │   ├── Medium-ONI_Framework.md
        │   └── TechDoc-ONI_Framework.md
        │
        ├── coherence-metric/
        │   ├── INDEX.md              # ✗ PENDING
        │   ├── Medium-Coherence_Metric.md
        │   └── TechDoc-Coherence_Metric_Detailed.md
        │
        ├── neural-firewall/
        │   ├── INDEX.md              # ✗ PENDING
        │   ├── Medium-Neural_Firewall.md
        │   └── TechDoc-Neural_Firewall_Architecture.md
        │
        ├── neural-ransomware/
        │   ├── INDEX.md              # ✗ PENDING
        │   ├── Medium-Neural_Ransomware.md
        │   └── TechDoc-Neural_Ransomware.md
        │
        └── scale-frequency/
            ├── INDEX.md              # ✗ PENDING
            ├── Medium-Scale_Frequency.md
            └── TechDoc-Scale_Frequency.md
```

---

## Implementation Priority

### Phase 1 (Immediate) — ✓ COMPLETE
- [x] Create README.AI.md → **Implemented as CLAUDE.md** (11KB, comprehensive instructions)
- [x] Create MEDIUM_TEMPLATE.md → **v2 with Python generator**
- [x] Standardize file naming → **`Medium-*` and `TechDoc-*` patterns**
- [x] Update all file trees in documentation → **MAIN/publications + resources structure**

### Phase 2 (Next Session) — 🔄 IN PROGRESS
- [ ] Create CHANGELOG.md at repository root
- [x] Create INDEX_TEMPLATE.md → **Implemented**
- [ ] Deploy INDEX.md to topic folders (1 of 5 complete):
  - [x] `0-oni-framework/INDEX.md`
  - [ ] `coherence-metric/INDEX.md`
  - [ ] `neural-firewall/INDEX.md`
  - [ ] `neural-ransomware/INDEX.md`
  - [ ] `scale-frequency/INDEX.md`
- [ ] Create Research Note template file

### Phase 3 (Future) — 🔄 PARTIALLY COMPLETE
- [x] Build cross-reference registry → **MAIN/INDEX.md with dependency map & matrix**
- [x] Document pre-commit checklist → **In CLAUDE.md (lines 239-256)**
- [ ] Automate pre-commit checklist as `.git/hooks/pre-commit`
- [x] Add document metadata to publications → **YAML front-matter on all 10 publications**
- [ ] Add consistent metadata to infrastructure files (templates, processes)

---

## Next Steps (Recommended Actions)

### Immediate Priority
1. **Create CHANGELOG.md** at repository root with semantic versioning history
2. **Deploy INDEX.md** to remaining 4 topic folders using INDEX_TEMPLATE.md:
   - `coherence-metric/`
   - `neural-firewall/`
   - `neural-ransomware/`
   - `scale-frequency/`

### Short-Term
3. **Create Research Note template** as `MAIN/resources/templates/RESEARCH_NOTE_TEMPLATE.md`
4. **Add YAML metadata** to all infrastructure files in `resources/`

### Medium-Term
5. **Create pre-commit hook** (`.git/hooks/pre-commit`) to automate validation
6. **Implement content calendar** for publishing schedule tracking

---

*Strategy Version: 2.0*
*Last Updated: January 21, 2026*
*Author: Kevin L. Qi with Claude (Anthropic)*
