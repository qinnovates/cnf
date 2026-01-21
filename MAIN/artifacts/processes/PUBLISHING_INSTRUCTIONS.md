# ONI Framework Publishing Instructions

## Overview

This document provides standardized instructions for Claude to follow when extracting, formatting, and uploading new content publications to the ONI Framework repository.

**Important:**
- The `publications/` and `oni-framework/` folders are for **content only**
- All templates, processes, scripts, and CICD files live in `MAIN/artifacts/`

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
    ├── publications/                   # CONTENT ONLY
    │   ├── coherence-metric/
    │   ├── neural-firewall/
    │   ├── neural-ransomware/
    │   └── scale-frequency/
    │
    └── artifacts/                      # NON-CONTENT (infrastructure)
        ├── templates/                  # Formatting templates
        │   ├── PAPER_TEMPLATE_APA.md
        │   └── MEDIUM_TEMPLATE.md
        │
        ├── processes/                  # Workflow documentation
        │   ├── PUBLISHING_INSTRUCTIONS.md  # This file
        │   └── PROCESS_IMPROVEMENTS.md
        │
        ├── scripts/                    # Automation scripts
        │   └── continuous-research-delivery/
        │       └── research_monitor.py
        │
        └── CICD/                       # Continuous Research Delivery
            ├── keywords.json           # Auto-generated research keywords
            ├── incoming/               # New research discoveries
            └── processed/              # Reviewed and integrated
```

---

## Folder Purposes

| Folder | Purpose | What Goes Here |
|--------|---------|----------------|
| `oni-framework/` | **Base content** | Foundational ONI Framework publications |
| `publications/` | **Content only** | Medium posts, technical papers |
| `artifacts/templates/` | Formatting templates | APA template, Medium template |
| `artifacts/processes/` | Workflow documentation | Publishing instructions, improvements |
| `artifacts/scripts/` | Automation scripts | Research monitoring, CI/CD pipelines |
| `artifacts/CICD/` | Research pipeline | Keywords, incoming papers, processed |

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
**Location:** `MAIN/publications/[topic]/` or `MAIN/oni-framework/`
**Template:** `MAIN/artifacts/templates/MEDIUM_TEMPLATE.md`

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
**Location:** `MAIN/publications/[topic]/` or `MAIN/oni-framework/`
**Template:** `MAIN/artifacts/templates/PAPER_TEMPLATE_APA.md`

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

## Keyword Extraction Workflow

**IMPORTANT:** When adding new publications, extract and add keywords to maintain research monitoring relevance.

### Step 1: Extract Keywords from New Publication

After creating a new publication, extract keywords in these categories:

1. **Primary Keywords** (5-8): Core concepts unique to this publication
2. **Technical Terms** (8-12): Specific technical vocabulary
3. **Biological Terms** (5-8): Neuroscience-specific terminology
4. **Security Terms** (5-8): Cybersecurity-related terms

### Step 2: Update keywords.json

Add keywords to `MAIN/artifacts/CICD/keywords.json`:

```json
{
  "publications": {
    "new-topic": {
      "title": "New Topic Title",
      "primary_keywords": [...],
      "technical_terms": [...],
      "biological_terms": [...],
      "security_terms": [...]
    }
  }
}
```

### Step 3: Update Combined Search Terms

If the new publication introduces new research areas, add relevant terms to `combined_search_terms` in keywords.json.

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
- Reference: `MAIN/artifacts/templates/MEDIUM_TEMPLATE.md`

**For Technical Papers:**
- Reference: `MAIN/artifacts/templates/PAPER_TEMPLATE_APA.md`
- Use bold table numbers: `**Table 1**`
- Use italic table titles: `*Table Title*`
- Include standard acknowledgments

### Step 3: Keyword Extraction

**For every new publication:**

1. Read the complete publication
2. Extract keywords by category
3. Update `MAIN/artifacts/CICD/keywords.json`
4. This ensures the research monitor finds relevant new papers

### Step 4: Quality Checks

Before committing:

1. **Verify file location:**
   - Content → `publications/` or `oni-framework/`
   - Templates → `artifacts/templates/`
   - Process docs → `artifacts/processes/`
   - Scripts → `artifacts/scripts/`

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

5. **Verify keywords updated:**
   - New publication added to keywords.json
   - Combined search terms updated if needed

### Step 5: Commit and Push

```bash
git add .
git commit -m "Add [Topic] publication

- [Brief description of content]
- [Type: Medium/Paper/Both]
- Updated keywords.json

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"

git push
```

---

## Standard Acknowledgments

Include this in all technical papers:

> The author wishes to acknowledge the support of colleagues and mentors in the development of this work. Initial research validation was conducted through LMArena (LMSYS, 2024-2025), enabling cross-model verification of hypotheses and findings to mitigate single-model bias. Deep research synthesis and writing assistance was provided by Claude (Anthropic, 2025). All original ideas, theoretical frameworks, analyses, and conclusions are the author's own.

---

## Research Monitor Usage

The research monitor script uses keywords from publications to find relevant new research.

### Running the Monitor

```bash
cd MAIN/artifacts/scripts/continuous-research-delivery
python research_monitor.py --days 7 --sources all
```

### Options
- `--days N` - Look back N days (default: 7)
- `--sources arxiv,pubmed,biorxiv,semantic_scholar,ieee` - Specific sources or "all"
- `--keywords-file path` - Custom keywords file path
- `--quiet` - Suppress progress output
- `--summary-only` - Print summary without saving files

### Academic Sources
- **arXiv** - cs.CR, q-bio.NC, cs.AI categories
- **PubMed** - Medical/neuroscience literature
- **bioRxiv/medRxiv** - Preprints
- **Semantic Scholar** - Cross-disciplinary
- **IEEE Xplore** - Engineering (requires API key)

---

## Common Tasks

### Adding a New Topic

1. Create folder: `MAIN/publications/[topic-name]/`
2. Add Medium post: `Medium-[Topic_Name].md`
3. Add technical paper: `[Topic_Name]_Paper.md`
4. **Extract keywords and update keywords.json**
5. Update README.md with new links

### Processing CICD Incoming Research

1. Review files in `MAIN/artifacts/CICD/incoming/`
2. Determine relevance to ONI Framework
3. If relevant: Extract key findings, create summary
4. Move processed file to `MAIN/artifacts/CICD/processed/`
5. Update publications if new content warranted

### Updating Existing Content

1. Read current file to understand structure
2. Make edits preserving formatting
3. Update any affected cross-references
4. **Update keywords.json if new terms introduced**
5. Commit with descriptive message

---

## Checklist for New Publications

- [ ] Content extracted and cleaned
- [ ] Placed in correct folder (content only in publications/)
- [ ] File named correctly (`Medium-*.md` or `*_Paper.md`)
- [ ] Front matter/metadata complete (date_posted, not date)
- [ ] Footer complete (Sub-Tags, Originally published with datetime)
- [ ] Formatting consistent with existing publications
- [ ] Tables numbered with bold numbers, italic titles
- [ ] References in APA format (papers only)
- [ ] Acknowledgments included (papers only)
- [ ] **Keywords extracted and added to keywords.json**
- [ ] README.md updated if needed
- [ ] Committed with proper message format

---

*Instructions Version: 3.0*
*Last Updated: January 2026*
*Series: ONI Framework Publications*
