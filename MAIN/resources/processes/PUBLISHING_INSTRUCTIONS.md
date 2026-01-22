# ONI Framework Publishing Instructions

## Overview

This document provides standardized instructions for Claude to follow when extracting, formatting, and uploading new content publications to the ONI Framework repository.

**Important:**
- The `publications/` folder is for **content only**
- All templates, processes, and scripts live in `MAIN/resources/`

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
    ├── INDEX.md                        # Master index
    ├── INDEX.md                     # Central hub
    ├── publications/                   # CONTENT ONLY
    │   ├── 0-oni-framework/
    │   ├── coherence-metric/
    │   ├── neural-firewall/
    │   ├── neural-ransomware/
    │   ├── quantum-security/
    │   └── scale-frequency/
    │
    ├── prototypes/                     # Interactive demos
    │   └── oni-visualizations/
    │
    └── resources/                      # NON-CONTENT (infrastructure)
        ├── templates/                  # Formatting templates
        │   ├── TECHDOC_TEMPLATE_APA.md
        │   ├── BLOG_TEMPLATE.md
        │   └── INDEX_TEMPLATE.md
        │
        ├── processes/                  # Workflow documentation
        │   ├── PUBLISHING_INSTRUCTIONS.md  # This file
        │   └── PROCESS_IMPROVEMENTS.md
        │
        └── pipeline/                   # Research pipeline
            ├── scripts/
            │   ├── research_monitor.py
            │   └── keywords.json
            ├── incoming/               # New research discoveries
            └── processed/              # Reviewed and integrated
```

---

## Folder Purposes

| Folder | Purpose | What Goes Here |
|--------|---------|----------------|
| `publications/0-oni-framework/` | **Base content** | Foundational ONI Framework publications |
| `publications/` | **Content only** | Blog posts, technical documents |
| `prototypes/` | **Interactive demos** | Web apps, visualizations |
| `resources/templates/` | Formatting templates | APA template, Blog template, INDEX template |
| `resources/processes/` | Workflow documentation | Publishing instructions, improvements |
| `resources/pipeline/` | Research pipeline | Scripts, incoming papers, processed research |

---

## File Naming Conventions

### Publications (Content)
| Type | Format | Example |
|------|--------|---------|
| Blog Posts | `Blog-[Topic_Name].md` | `Blog-Coherence_Metric.md` |
| Technical Documents | `TechDoc-[Topic_Name].md` | `TechDoc-Neural_Ransomware.md` |
| Detailed TechDocs | `TechDoc-[Topic_Name]_Detailed.md` | `TechDoc-Coherence_Metric_Detailed.md` |

### Templates
| Type | Format | Example |
|------|--------|---------|
| TechDoc Templates | `[TYPE]_TEMPLATE_[FORMAT].md` | `TECHDOC_TEMPLATE_APA.md` |
| Post Templates | `[TYPE]_TEMPLATE.md` | `BLOG_TEMPLATE.md` |

### Pipeline Research
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

### 1. Blog Posts (`Blog-*.md`)
**Location:** `MAIN/publications/[topic]/`
**Template:** `MAIN/resources/templates/BLOG_TEMPLATE.md`

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
original_url: [Original Medium URL if applicable]
tags: ['tag1', 'tag2', 'tag3']
---
```

**Required Footer:**
```markdown
**Sub-Tags:** #Tag1 #Tag2 #Tag3

---
*Originally published on [Medium](URL) on [Month Day, Year] at [HH:MM:SS GMT]*
```

**Note:** Use `date_posted` (not `date`) in front matter. Use `Sub-Tags:` (not `Tags:`) for the hashtag line at the bottom. Include original Medium URL if the post was originally published there.

### 2. Technical Documents (`*_TechDoc.md`)
**Location:** `MAIN/publications/[topic]/`
**Template:** `MAIN/resources/templates/TECHDOC_TEMPLATE_APA.md`

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

Add keywords to `MAIN/resources/pipeline/scripts/keywords.json`:

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
   - Pipeline incoming folder

2. **Determine publication category:**
   - Which existing topic folder does this belong to?
   - Does it require a new topic folder?

3. **Extract and clean:**
   - Remove conversion resources
   - Fix encoding issues (em-dashes, quotes, etc.)
   - Preserve meaningful formatting

### Step 2: Formatting

**For Blog Posts:**
- Reference: `MAIN/resources/templates/BLOG_TEMPLATE.md`

**For Technical Documents:**
- Reference: `MAIN/resources/templates/TECHDOC_TEMPLATE_APA.md`
- Use bold table numbers: `**Table 1**`
- Use italic table titles: `*Table Title*`
- Include standard acknowledgments

### Step 3: Keyword Extraction

**For every new publication:**

1. Read the complete publication
2. Extract keywords by category
3. Update `MAIN/resources/pipeline/scripts/keywords.json`
4. This ensures the research monitor finds relevant new papers

### Step 4: Quality Checks

Before committing:

1. **Verify file location:**
   - Content → `publications/`
   - Templates → `resources/templates/`
   - Process docs → `resources/processes/`
   - Scripts → `resources/pipeline/scripts/`

2. **Verify file naming:**
   - Blog files: `Blog-[Topic].md`
   - TechDocs: `TechDoc-[Topic].md`

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
- [Type: Medium/TechDoc/Both]
- Updated keywords.json

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"

git push
```

---

## Standard Acknowledgments

Include this in all technical documents:

> The author wishes to acknowledge the support of colleagues and mentors in the development of this work. Initial research validation was conducted through LMArena (LMSYS, 2024-2025), enabling cross-model verification of hypotheses and findings to mitigate single-model bias. Deep research synthesis and writing assistance was provided by Claude (Anthropic, 2025). All original ideas, theoretical frameworks, analyses, and conclusions are the author's own. Final revisions, editing, and validation were performed by the author.

---

## Research Monitor Usage

The research monitor script uses keywords from publications to find relevant new research.

### Running the Monitor

```bash
cd MAIN/resources/pipeline/scripts
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
2. Add blog post: `Blog-[Topic_Name].md` (include original Medium URL if applicable)
3. Add technical document: `TechDoc-[Topic_Name].md`
4. **Extract keywords and update keywords.json**
5. Update README.md with new links

### Processing Pipeline Incoming Research

1. Review files in `MAIN/resources/pipeline/incoming/`
2. Determine relevance to ONI Framework
3. If relevant: Extract key findings, create summary
4. Move processed file to `MAIN/resources/pipeline/processed/`
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
- [ ] File named correctly (`Blog-*.md` or `TechDoc-*.md`)
- [ ] Front matter/metadata complete (date_posted, original_url if applicable)
- [ ] Footer complete (Sub-Tags, Originally published with datetime and link)
- [ ] Formatting consistent with existing publications
- [ ] Tables numbered with bold numbers, italic titles
- [ ] References in APA format (TechDocs only)
- [ ] Acknowledgments included (TechDocs only)
- [ ] **Keywords extracted and added to keywords.json**
- [ ] README.md updated if needed
- [ ] Committed with proper message format

---

*Instructions Version: 4.0*
*Last Updated: January 2026*
*Series: ONI Framework Publications*
