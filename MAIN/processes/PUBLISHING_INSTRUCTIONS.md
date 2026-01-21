# ONI Framework Publishing Instructions

## Overview

This document provides standardized instructions for Claude to follow when extracting, formatting, and uploading new content publications to the ONI Framework repository.

**Important:** The `publications/` folder is for **content only**. All templates, processes, and scripts live in their respective folders under `MAIN/`.

---

## Repository Structure

```
ONI/
├── README.md                           # Main documentation
├── CLAUDE.md                           # Claude AI instructions
├── ABOUT.md                            # Author bio
├── CONTRIBUTING.md                     # Contribution guidelines
├── LICENSE                             # Apache 2.0
│
└── MAIN/
    ├── oni-framework/                  # BASE CONTENT (foundational)
    │   ├── Medium-ONI_Framework.md
    │   └── ONI_Framework_Paper.md
    │
    ├── templates/                      # Formatting templates
    │   ├── PAPER_TEMPLATE_APA.md
    │   └── MEDIUM_TEMPLATE.md
    │
    ├── processes/                      # Workflow documentation
    │   ├── PUBLISHING_INSTRUCTIONS.md  # This file
    │   └── PROCESS_IMPROVEMENTS.md
    │
    ├── scripts/                        # Automation scripts
    │   └── continuous-research-delivery/
    │       └── research_monitor.py
    │
    ├── CICD/                           # Continuous Research Delivery
    │   ├── incoming/                   # New research discoveries
    │   └── processed/                  # Reviewed and integrated
    │
    └── publications/                   # CONTENT ONLY
        ├── coherence-metric/
        │   ├── Medium-Coherence_Metric.md
        │   └── Coherence_Metric_Detailed_Paper.md
        ├── neural-firewall/
        │   ├── Medium-Neural_Firewall.md
        │   └── Neural_Firewall_Architecture_Paper.md
        ├── neural-ransomware/
        │   ├── Medium-Neural_Ransomware.md
        │   └── Neural_Ransomware_Paper.md
        └── scale-frequency/
            ├── Medium-Scale_Frequency.md
            └── Scale_Frequency_Paper.md
```

---

## Folder Purposes

| Folder | Purpose | What Goes Here |
|--------|---------|----------------|
| `templates/` | Formatting templates | APA template, Medium template, future templates |
| `processes/` | Workflow documentation | Publishing instructions, improvement strategies |
| `scripts/` | Automation scripts | Research monitoring, CI/CD pipelines |
| `CICD/incoming/` | New research discoveries | Auto-fetched papers, pending review |
| `CICD/processed/` | Reviewed research | Archived after integration |
| `oni-framework/` | **Base content** | Foundational ONI Framework publications |
| `publications/` | **Content only** | Medium posts, technical papers |

---

## File Naming Conventions

### Publications (Content)
| Type | Format | Example |
|------|--------|---------|
| Medium Posts | `Medium-[Topic_Name].md` | `Medium-Coherence_Metric.md` |
| Technical Papers | `[Topic_Name]_Paper.md` | `Neural_Ransomware_Paper.md` |
| Detailed Papers | `[Topic_Name]_Detailed_Paper.md` | `Coherence_Metric_Detailed_Paper.md` |

### Templates
| Type | Format | Example |
|------|--------|---------|
| Paper Templates | `[TYPE]_TEMPLATE_[FORMAT].md` | `PAPER_TEMPLATE_APA.md` |
| Post Templates | `[TYPE]_TEMPLATE.md` | `MEDIUM_TEMPLATE.md` |

### CICD Research
| Type | Format | Example |
|------|--------|---------|
| Incoming | `YYYY-MM-DD_[source]_[title].md` | `2026-01-21_arxiv_neural-security.md` |
| Processed | Same, moved to processed/ | After review and integration |

### Folder Names
- Use lowercase with hyphens
- Descriptive of the topic
- Examples: `coherence-metric`, `neural-firewall`, `scale-frequency`

---

## Content Types

### 1. Medium Posts (`Medium-*.md`)
**Location:** `MAIN/publications/[topic]/`
**Template:** `MAIN/templates/MEDIUM_TEMPLATE.md`

**Characteristics:**
- Conversational tone
- Uses storytelling and analogies
- Shorter paragraphs for web readability
- Includes section breaks (`• • •` or `---`)
- 5-15 minute read time (1,500-4,000 words)

**Required Front Matter:**
```yaml
---
title: "Article Title"
date_posted: [Publication date in RFC 2822 format]
url: [Medium URL if published]
tags: ['tag1', 'tag2', 'tag3']
---
```

**Required Footer:**
```markdown
**Sub-Tags:** #Tag1 #Tag2 #Tag3

---
*Originally published on [Medium](URL) on [Month Day, Year] at [HH:MM:SS GMT]*
```

**Note:** Use `date_posted` (not `date`) in front matter. Use `Sub-Tags:` (not `Tags:`) for the hashtag line at the bottom.

### 2. Technical Papers (`*_Paper.md`)
**Location:** `MAIN/publications/[topic]/`
**Template:** `MAIN/templates/PAPER_TEMPLATE_APA.md`

**Characteristics:**
- Formal academic tone
- APA 7th edition formatting
- Detailed mathematical formulations
- Comprehensive references section
- Tables with bold numbers, italic titles

**Required Sections:**
1. Abstract (with keywords)
2. Introduction
3. [Methods/Framework/Analysis sections]
4. Discussion
5. Limitations
6. Future Work
7. Conclusion
8. References
9. Acknowledgments

---

## Publishing Workflow

### Step 1: Content Extraction
When extracting content from a new source:

1. **Identify the source type:**
   - Medium RSS feed
   - Draft document
   - Conversation notes
   - Research synthesis
   - CICD incoming folder

2. **Determine publication category:**
   - Which existing topic folder does this belong to?
   - Does it require a new topic folder?

3. **Extract and clean:**
   - Remove conversion artifacts
   - Fix encoding issues (em-dashes, quotes, etc.)
   - Preserve meaningful formatting

### Step 2: Formatting

**For Medium Posts:**
- Reference: `MAIN/templates/MEDIUM_TEMPLATE.md`

**For Technical Papers:**
- Reference: `MAIN/templates/PAPER_TEMPLATE_APA.md`
- Use bold table numbers: `**Table 1**`
- Use italic table titles: `*Table Title*`
- Include standard acknowledgments

### Step 3: Quality Checks

Before committing:

1. **Verify file location:**
   - Content → `publications/`
   - Templates → `templates/`
   - Process docs → `processes/`
   - Scripts → `scripts/`

2. **Verify file naming:**
   - Medium files: `Medium-[Topic].md`
   - Papers: `[Topic]_Paper.md`

3. **Check formatting consistency:**
   - Tables formatted correctly
   - Headers hierarchy proper
   - No orphaned formatting

4. **Validate references:**
   - APA format for papers
   - Working URLs where applicable

### Step 4: Commit and Push

```bash
git add .
git commit -m "Add [Topic] publication

- [Brief description of content]
- [Type: Medium/Paper/Both]

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"

git push
```

---

## Standard Acknowledgments

Include this in all technical papers:

> The author wishes to acknowledge the support of colleagues and mentors in the development of this work. Initial research validation was conducted through LMArena (LMSYS, 2024-2025), enabling cross-model verification of hypotheses and findings to mitigate single-model bias. Deep research synthesis and writing assistance was provided by Claude (Anthropic, 2025). All original ideas, theoretical frameworks, analyses, and conclusions are the author's own.

---

## Common Tasks

### Adding a New Topic

1. Create folder: `MAIN/publications/[topic-name]/`
2. Add Medium post: `Medium-[Topic_Name].md`
3. Add technical paper: `[Topic_Name]_Paper.md`
4. Update README.md with new links

### Processing CICD Incoming Research

1. Review files in `MAIN/CICD/incoming/`
2. Determine relevance to ONI Framework
3. If relevant: Extract key findings, create summary
4. Move processed file to `MAIN/CICD/processed/`
5. Update publications if new content warranted

### Updating Existing Content

1. Read current file to understand structure
2. Make edits preserving formatting
3. Update any affected cross-references
4. Commit with descriptive message

---

## Checklist for New Publications

- [ ] Content extracted and cleaned
- [ ] Placed in `MAIN/publications/[topic]/` (content only!)
- [ ] File named correctly (`Medium-*.md` or `*_Paper.md`)
- [ ] Front matter/metadata complete
- [ ] Formatting consistent with existing publications
- [ ] Tables numbered with bold numbers, italic titles
- [ ] References in APA format (papers only)
- [ ] Acknowledgments included (papers only)
- [ ] README.md updated if needed
- [ ] Committed with proper message format

---

*Instructions Version: 2.0*
*Last Updated: January 21, 2026*
*Series: ONI Framework Publications*
