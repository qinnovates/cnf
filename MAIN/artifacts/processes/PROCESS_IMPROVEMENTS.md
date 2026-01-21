# Process Improvement Strategy for ONI Framework Publishing

## Current State Analysis

### What's Working
1. **Clear folder structure** - Topic-based organization makes content discoverable
2. **Naming conventions** - Consistent `Medium-*` and `*_Paper.md` patterns
3. **Templates exist** - APA and Medium templates provide formatting guidance
4. **README.AI.md** - Claude has clear instructions to follow

### Gaps Identified
1. No automated validation of file naming
2. README.md updates are manual and error-prone
3. No version tracking for individual documents
4. Cross-references between papers not systematically maintained
5. No content calendar or publishing schedule tracking

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
| Template | Purpose | Location |
|----------|---------|----------|
| PAPER_TEMPLATE_APA.md | Technical papers | MAIN/publications/ |
| MEDIUM_TEMPLATE.md | Medium posts | MAIN/publications/ |
| PUBLISHING_INSTRUCTIONS.md | Workflow guide | MAIN/publications/ |

### Proposed Additional Templates

#### 1. Research Note Template
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

#### 2. Topic Index Template
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

## Proposed File Tree (Future State)

```
ONI/
├── README.md
├── README.AI.md
├── ABOUT.md
├── CHANGELOG.md                    # NEW: Version history
├── CONTRIBUTING.md
├── LICENSE
│
└── MAIN/
    └── publications/
        ├── PAPER_TEMPLATE_APA.md
        ├── MEDIUM_TEMPLATE.md
        ├── PUBLISHING_INSTRUCTIONS.md
        ├── PROCESS_IMPROVEMENTS.md   # This file
        │
        ├── coherence-metric/
        │   ├── INDEX.md              # NEW: Topic index
        │   ├── Medium-Coherence_Metric.md
        │   └── Coherence_Metric_Detailed_Paper.md
        │
        ├── neural-firewall/
        │   ├── INDEX.md
        │   ├── Medium-Neural_Firewall.md
        │   └── Neural_Firewall_Architecture_Paper.md
        │
        ├── neural-ransomware/
        │   ├── INDEX.md
        │   ├── Medium-Neural_Ransomware.md
        │   └── Neural_Ransomware_Paper.md
        │
        ├── oni-framework/
        │   ├── INDEX.md
        │   ├── Medium-ONI_Framework.md
        │   └── ONI_Framework_Paper.md
        │
        └── scale-frequency/
            ├── INDEX.md
            ├── Medium-Scale_Frequency.md
            └── Scale_Frequency_Paper.md
```

---

## Implementation Priority

### Phase 1 (Immediate)
- [x] Create README.AI.md
- [x] Create MEDIUM_TEMPLATE.md
- [x] Standardize file naming
- [x] Update all file trees in documentation

### Phase 2 (Next Session)
- [ ] Create CHANGELOG.md
- [ ] Add INDEX.md to each topic folder
- [ ] Create Research Note template

### Phase 3 (Future)
- [ ] Build cross-reference registry
- [ ] Implement pre-commit checklist as standard practice
- [ ] Add document metadata to all files

---

*Strategy Version: 1.0*
*Last Updated: January 21, 2026*
*Author: Kevin L. Qi with Claude (Anthropic)*
