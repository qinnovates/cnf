# Claude AI Instructions for ONI Framework Repository

> This file provides instructions for Claude to follow when assisting with the ONI Framework repository. Read this file at the start of any session involving content creation, publishing, or repository maintenance.

---

## Quick Reference

| Resource | Location | Purpose |
|----------|----------|---------|
| **ONI Nexus** | `ONI_NEXUS.md` | **Central hub - start here for navigation** |
| Topic INDEX Template | `MAIN/artifacts/templates/INDEX_TEMPLATE.md` | Template for topic-level indexes |
| APA Template | `MAIN/artifacts/templates/TECHDOC_TEMPLATE_APA.md` | Formatting for technical documents |
| Medium Template | `MAIN/artifacts/templates/MEDIUM_TEMPLATE.md` | Formatting for Medium posts |
| Publishing Instructions | `MAIN/artifacts/processes/PUBLISHING_INSTRUCTIONS.md` | Step-by-step publishing workflow |
| Research Monitor | `MAIN/artifacts/cicd-pipeline/continuous-research-delivery/scripts/research_monitor.py` | Fetch new academic papers |
| Keywords File | `MAIN/artifacts/cicd-pipeline/continuous-research-delivery/scripts/keywords.json` | Research search terms |
| This File | `CLAUDE.md` | Claude-specific instructions |

---

## Repository File Tree

```
ONI/
├── README.md                           # Public entry point
├── ONI_NEXUS.md                        # Central hub - all topics, dependencies, navigation
├── CLAUDE.md                           # Claude AI instructions (this file)
├── ABOUT.md                            # Author bio
├── CONTRIBUTING.md                     # Contribution guidelines
├── LICENSE                             # Apache 2.0 License
│
└── MAIN/
    ├── publications/                   # CONTENT ONLY
    │   ├── 0-oni-framework/            # Base/foundational content (sorted first)
    │   │   ├── INDEX.md                # Topic index (each topic has one)
    │   │   ├── Medium-ONI_Framework.md
    │   │   └── TechDoc-ONI_Framework.md
    │   ├── coherence-metric/
    │   │   └── INDEX.md
    │   ├── neural-firewall/
    │   │   └── INDEX.md
    │   ├── neural-ransomware/
    │   │   └── INDEX.md
    │   └── scale-frequency/
    │       └── INDEX.md
    │
    └── artifacts/                      # NON-CONTENT (infrastructure)
        ├── templates/                  # Formatting templates
        │   ├── INDEX_TEMPLATE.md       # Template for topic indexes
        │   ├── TECHDOC_TEMPLATE_APA.md
        │   └── MEDIUM_TEMPLATE.md
        │
        ├── processes/                  # Workflow documentation
        │   ├── PUBLISHING_INSTRUCTIONS.md
        │   └── PROCESS_IMPROVEMENTS.md
        │
        └── cicd-pipeline/              # Continuous Research Delivery
            ├── incoming/               # New research discoveries
            ├── processed/              # Reviewed and integrated
            └── continuous-research-delivery/
                └── scripts/            # Automation scripts
                    ├── research_monitor.py
                    └── keywords.json   # Research keywords from publications
```

---

## Folder Purposes

| Folder | Purpose | What Goes Here |
|--------|---------|----------------|
| `publications/0-oni-framework/` | **Base content** | Foundational ONI Framework publications |
| `publications/` | **Content only** | Medium posts, technical documents |
| `artifacts/templates/` | Formatting templates | APA template, Medium template |
| `artifacts/processes/` | Workflow documentation | Publishing instructions, improvements |
| `artifacts/cicd-pipeline/` | Research pipeline | Incoming papers, processed, scripts, keywords |

**IMPORTANT:**
- The `0-oni-framework/` folder inside `publications/` contains the base/foundational content and sorts first alphabetically.
- The `publications/` folder is for **content only**. Never put templates, instructions, or scripts there.
- The `artifacts/` folder contains ALL non-content files (templates, processes, scripts, CICD).

---

## Naming Conventions

### Folder Names
- **Format:** lowercase with hyphens
- **Examples:** `coherence-metric`, `neural-firewall`, `scale-frequency`

### File Names

| Type | Format | Example |
|------|--------|---------|
| Medium Posts | `Medium-[Topic_Name].md` | `Medium-Coherence_Metric.md` |
| Technical Documents | `TechDoc-[Topic_Name].md` | `TechDoc-Neural_Ransomware.md` |
| Detailed TechDocs | `TechDoc-[Topic_Name]_Detailed.md` | `TechDoc-Coherence_Metric_Detailed.md` |
| Templates | `[NAME]_TEMPLATE_[TYPE].md` | `TECHDOC_TEMPLATE_APA.md` |
| CICD Research | `YYYY-MM-DD_[source]_[title].md` | `2026-01-21_arxiv_neural-security.md` |

### Topic Name Rules
- Use PascalCase with underscores between words
- Match folder name but with underscores instead of hyphens
- Examples:
  - Folder: `coherence-metric` → File: `Coherence_Metric`
  - Folder: `neural-firewall` → File: `Neural_Firewall`

---

## Workflow Instructions

### When Adding New Content

1. **Read the templates first:**
   ```
   Read: MAIN/artifacts/templates/TECHDOC_TEMPLATE_APA.md
   Read: MAIN/artifacts/templates/MEDIUM_TEMPLATE.md
   Read: MAIN/artifacts/processes/PUBLISHING_INSTRUCTIONS.md
   ```

2. **Create topic folder (if new topic):**
   ```bash
   mkdir MAIN/publications/[topic-name]
   ```

3. **Create files with correct naming:**
   - Medium post: `Medium-[Topic_Name].md`
   - Technical document: `TechDoc-[Topic_Name].md`

4. **Apply proper formatting:**
   - Medium: Conversational, storytelling, web-optimized
   - TechDoc: APA 7th edition, formal, with references

5. **Extract keywords and update keywords.json** (see below)

6. **Update README.md** with new links

7. **Commit with proper message format**

### Keyword Extraction (REQUIRED for new publications)

**For every new publication:**

1. Extract keywords in these categories:
   - **Primary Keywords** (5-8): Core concepts
   - **Technical Terms** (8-12): Technical vocabulary
   - **Biological Terms** (5-8): Neuroscience terms
   - **Security Terms** (5-8): Cybersecurity terms

2. Update `MAIN/artifacts/cicd-pipeline/continuous-research-delivery/scripts/keywords.json`:
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

3. Update `combined_search_terms` if new research areas introduced

### When Running Research Monitor

```bash
cd MAIN/artifacts/cicd-pipeline/continuous-research-delivery/scripts
python research_monitor.py --days 7 --sources all
```

Options:
- `--days N` - Look back N days (default: 7)
- `--sources arxiv,pubmed,biorxiv,semantic_scholar,ieee` - Specific sources or "all"
- `--keywords-file path` - Custom keywords file
- `--quiet` - Suppress progress output
- `--summary-only` - Print summary without saving files

---

## README.md Update Protocol

> **CRITICAL:** README.md is the public face of the repository. Update it for ANY major change:
> - New topics or publications
> - Structural changes (new folders, renamed files)
> - New navigation features (like ONI_NEXUS.md)
> - Changes to key concepts or framework components

**After every commit that adds or modifies content, update README.md:**

### Step 1: Locate the Topics & Documents Section
Find the section starting with `## Topics & Documents`

### Step 2: Add/Update Table Entry
For each topic, maintain this format:

```markdown
### [Emoji] [Topic Name]

[Brief description of topic area]

| Document | Summary |
|----------|----------|
| [Medium-Topic_Name](MAIN/publications/topic-folder/Medium-Topic_Name.md) | *One-line description* |
| [TechDoc-Topic_Name](MAIN/publications/topic-folder/TechDoc-Topic_Name.md) | *One-line description* |
```

### Step 3: Update Navigation Section (if needed)
If adding new navigation features or structural changes:
```markdown
## Navigation

| Start Here | Purpose |
|------------|---------|
| **[ONI_NEXUS.md](ONI_NEXUS.md)** | Central hub — dependency map, cross-references, reading order, roadmap |
| **This README** | Public overview — key concepts, quick reference, document list |
```

### Step 4: Update Repository Structure (if needed)
If folder structure changes, update the file tree diagram in README.md.

### Step 5: Update Footer Stats
Update the document count at the bottom:
```markdown
*Documents: [X] | Topics: [Y] | Topic Indexes: [Z]*
```

### Step 6: Update Date
```markdown
*Last update: YYYY-MM-DD*
```

---

## Standard Acknowledgments

Use this text in all technical documents:

> The author wishes to acknowledge the support of colleagues and mentors in the development of this work. Initial research validation was conducted through LMArena (LMSYS, 2024-2025), enabling cross-model verification of hypotheses and findings to mitigate single-model bias. Deep research synthesis and writing assistance was provided by Claude (Anthropic, 2025). All original ideas, theoretical frameworks, analyses, and conclusions are the author's own. Final revisions, editing, and validation were performed by the author.

---

## Commit Message Format

```
[Action] [Topic/Scope]: Brief description

- Bullet point details
- What changed
- Why it changed
- Updated keywords.json (if applicable)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

### Action Verbs
- `Add` - New content
- `Update` - Modified content
- `Fix` - Corrections
- `Reorganize` - Structural changes
- `Remove` - Deletions

---

## Quality Checklist

Before committing, verify:

- [ ] File naming follows conventions
- [ ] Folder naming follows conventions
- [ ] Content files are in `publications/` only
- [ ] Non-content files are in `artifacts/` only
- [ ] Medium posts have proper front matter (title, date_posted, url, tags)
- [ ] Medium posts have proper footer (Sub-Tags, Originally published with datetime)
- [ ] TechDocs follow APA template structure
- [ ] Tables use bold numbers (`**Table 1**`) and italic titles
- [ ] References are in APA format
- [ ] Acknowledgments section included (TechDocs only)
- [ ] **Keywords extracted and added to keywords.json**
- [ ] README.md updated with new links
- [ ] Document count updated in README.md footer
- [ ] Date updated in README.md footer
- [ ] **Topic INDEX.md created** (for new topics)
- [ ] **ONI_NEXUS.md updated** (dependency map, tables, metrics)

---

## Common Tasks Reference

### Extract Content from Medium RSS
1. Fetch content from RSS feed URL
2. Extract title, date_posted, URL, tags for front matter
3. Clean formatting artifacts
4. Rename bottom `Tags:` section to `Sub-Tags:`
5. Update "Originally published" line with full datetime
6. Save as `Medium-[Topic_Name].md` in `publications/[topic]/`
7. **Extract keywords and update keywords.json**

### Convert Draft to TechDoc
1. Apply `MAIN/artifacts/templates/TECHDOC_TEMPLATE_APA.md` structure
2. Add Abstract with keywords
3. Number sections
4. Format tables (bold numbers, italic titles)
5. Add References in APA format
6. Add standard Acknowledgments
7. **Extract keywords and update keywords.json**

### Add New Topic (Full Expansion Workflow)

**Step 1: Create topic folder**
```bash
mkdir MAIN/publications/[topic-name]/
```

**Step 2: Create topic INDEX.md**
- Copy from `MAIN/artifacts/templates/INDEX_TEMPLATE.md`
- Fill in: summary, dependencies, key concepts, related topics
- Link back to `ONI_NEXUS.md`

**Step 3: Create publications**
- `Medium-[Topic_Name].md` — Accessible narrative
- `TechDoc-[Topic_Name].md` — Academic depth

**Step 4: Extract keywords and update keywords.json**

**Step 5: Update ONI_NEXUS.md**
- Add topic to appropriate section table
- Update dependency map (if new dependencies)
- Update cross-reference matrix
- Update metrics (topic/document counts)

**Step 6: Update README.md**
- Add section to Topics & Documents
- Update document count in footer

### Process CICD Incoming Research
1. Review files in `MAIN/artifacts/cicd-pipeline/incoming/`
2. Determine relevance to ONI Framework
3. If relevant: Extract key findings, create summary
4. Move processed file to `MAIN/artifacts/cicd-pipeline/processed/`
5. Update publications if new content warranted

### Rename/Reorganize Files
1. Use git mv for tracked files
2. Update all links in README.md
3. Verify no broken links
4. Commit with descriptive message

---

## Error Prevention

### Common Mistakes to Avoid
1. **Wrong location:** Don't put templates or instructions in `publications/` - use `artifacts/`
2. **Wrong naming:** Don't use dates in publication filenames (use `Medium-*` or `TechDoc-*` prefix)
3. **Missing README updates:** Always update README.md after ANY major change (topics, structure, navigation)
4. **Missing NEXUS updates:** Always update ONI_NEXUS.md when adding topics or changing dependencies
5. **Missing keywords:** Always extract and add keywords to keywords.json
6. **Inconsistent formatting:** Always check template before writing
7. **Broken links:** Use relative paths from repository root
8. **Wrong table format:** Numbers are BOLD, titles are ITALIC
9. **Stale footer:** Always update document/topic counts and date in README.md footer

### If Unsure
1. Read `MAIN/artifacts/processes/PUBLISHING_INSTRUCTIONS.md`
2. Check existing files for examples
3. Ask user for clarification before proceeding

---

*Version: 3.2*
*Last Updated: January 2026*
*For: Claude AI Assistant*
