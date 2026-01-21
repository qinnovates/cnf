# Claude AI Instructions for ONI Framework Repository

> This file provides instructions for Claude to follow when assisting with the ONI Framework repository. Read this file at the start of any session involving content creation, publishing, or repository maintenance.

---

## Quick Reference

| Resource | Location | Purpose |
|----------|----------|---------|
| APA Template | `MAIN/templates/PAPER_TEMPLATE_APA.md` | Formatting for technical papers |
| Medium Template | `MAIN/templates/MEDIUM_TEMPLATE.md` | Formatting for Medium posts |
| Publishing Instructions | `MAIN/processes/PUBLISHING_INSTRUCTIONS.md` | Step-by-step publishing workflow |
| Research Monitor | `MAIN/scripts/continuous-research-delivery/research_monitor.py` | Fetch new academic papers |
| This File | `CLAUDE.md` | Claude-specific instructions |

---

## Repository File Tree

```
ONI/
├── README.md                           # Main repository documentation
├── CLAUDE.md                           # Claude AI instructions (this file)
├── ABOUT.md                            # Author bio
├── CONTRIBUTING.md                     # Contribution guidelines
├── LICENSE                             # Apache 2.0 License
│
└── MAIN/
    ├── oni-framework/                  # BASE CONTENT (foundational)
    │   ├── Medium-ONI_Framework.md
    │   └── ONI_Framework_Paper.md
    │
    ├── templates/                      # Formatting templates
    │   ├── PAPER_TEMPLATE_APA.md       # APA 7th edition template
    │   └── MEDIUM_TEMPLATE.md          # Medium post template
    │
    ├── processes/                      # Workflow documentation
    │   ├── PUBLISHING_INSTRUCTIONS.md  # Publishing workflow guide
    │   └── PROCESS_IMPROVEMENTS.md     # Improvement strategies
    │
    ├── scripts/                        # Automation scripts
    │   └── continuous-research-delivery/
    │       └── research_monitor.py     # Academic paper monitoring
    │
    ├── CICD/                           # Continuous Research Delivery
    │   ├── incoming/                   # New research discoveries
    │   └── processed/                  # Reviewed and integrated
    │
    └── publications/                   # CONTENT ONLY
        ├── coherence-metric/
        │   ├── Medium-Coherence_Metric.md
        │   └── Coherence_Metric_Detailed_Paper.md
        │
        ├── neural-firewall/
        │   ├── Medium-Neural_Firewall.md
        │   └── Neural_Firewall_Architecture_Paper.md
        │
        ├── neural-ransomware/
        │   ├── Medium-Neural_Ransomware.md
        │   └── Neural_Ransomware_Paper.md
        │
        └── scale-frequency/
            ├── Medium-Scale_Frequency.md
            └── Scale_Frequency_Paper.md
```

---

## Folder Purposes

| Folder | Purpose | What Goes Here |
|--------|---------|----------------|
| `oni-framework/` | **Base content** | Foundational ONI Framework publications |
| `templates/` | Formatting templates | APA template, Medium template, future templates |
| `processes/` | Workflow documentation | Publishing instructions, improvement strategies |
| `scripts/` | Automation scripts | Research monitoring, CI/CD pipelines |
| `CICD/incoming/` | New research discoveries | Auto-fetched papers, pending review |
| `CICD/processed/` | Reviewed research | Archived after integration |
| `publications/` | **Content only** | Medium posts, technical papers |

**IMPORTANT:**
- The `oni-framework/` folder at `MAIN/` level contains the base/foundational content.
- The `publications/` folder is for **content only**. Never put templates, instructions, or scripts in this folder.

---

## Naming Conventions

### Folder Names
- **Format:** lowercase with hyphens
- **Examples:** `coherence-metric`, `neural-firewall`, `scale-frequency`

### File Names

| Type | Format | Example |
|------|--------|---------|
| Medium Posts | `Medium-[Topic_Name].md` | `Medium-Coherence_Metric.md` |
| Technical Papers | `[Topic_Name]_Paper.md` | `Neural_Ransomware_Paper.md` |
| Detailed Papers | `[Topic_Name]_Detailed_Paper.md` | `Coherence_Metric_Detailed_Paper.md` |
| Templates | `[NAME]_TEMPLATE_[TYPE].md` | `PAPER_TEMPLATE_APA.md` |
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
   Read: MAIN/templates/PAPER_TEMPLATE_APA.md
   Read: MAIN/templates/MEDIUM_TEMPLATE.md
   Read: MAIN/processes/PUBLISHING_INSTRUCTIONS.md
   ```

2. **Create topic folder (if new topic):**
   ```bash
   mkdir MAIN/publications/[topic-name]
   ```

3. **Create files with correct naming:**
   - Medium post: `Medium-[Topic_Name].md`
   - Technical paper: `[Topic_Name]_Paper.md`

4. **Apply proper formatting:**
   - Medium: Conversational, storytelling, web-optimized
   - Paper: APA 7th edition, formal, with references

5. **Update README.md** (see section below)

6. **Commit with proper message format**

### When Running Research Monitor

```bash
cd MAIN/scripts/continuous-research-delivery
python research_monitor.py --days 7 --sources all
```

Options:
- `--days N` - Look back N days (default: 7)
- `--sources arxiv,pubmed,biorxiv` - Specific sources or "all"
- `--quiet` - Suppress progress output
- `--summary-only` - Print summary without saving files

---

## README.md Update Protocol

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
| [Topic_Name Paper](MAIN/publications/topic-folder/Topic_Name_Paper.md) | *One-line description* |
```

### Step 3: Update Footer Stats
Update the document count at the bottom:
```markdown
*Documents: [X] | Topics: [Y]*
```

### Step 4: Update Date
```markdown
*Last update: YYYY-MM-DD*
```

---

## Standard Acknowledgments

Use this text in all technical papers:

> The author wishes to acknowledge the support of colleagues and mentors in the development of this work. Initial research validation was conducted through LMArena (LMSYS, 2024-2025), enabling cross-model verification of hypotheses and findings to mitigate single-model bias. Deep research synthesis and writing assistance was provided by Claude (Anthropic, 2025). All original ideas, theoretical frameworks, analyses, and conclusions are the author's own.

---

## Commit Message Format

```
[Action] [Topic/Scope]: Brief description

- Bullet point details
- What changed
- Why it changed

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
- [ ] Templates are in `templates/` only
- [ ] Process docs are in `processes/` only
- [ ] Medium posts have proper front matter (title, date_posted, url, tags)
- [ ] Medium posts have proper footer (Sub-Tags, Originally published with datetime)
- [ ] Papers follow APA template structure
- [ ] Tables use bold numbers (`**Table 1**`) and italic titles
- [ ] References are in APA format
- [ ] Acknowledgments section included (papers only)
- [ ] README.md updated with new links
- [ ] Document count updated in README.md footer
- [ ] Date updated in README.md footer

---

## Common Tasks Reference

### Extract Content from Medium RSS
1. Fetch content from RSS feed URL
2. Extract title, date_posted, URL, tags for front matter
3. Clean formatting artifacts
4. Rename bottom `Tags:` section to `Sub-Tags:`
5. Update "Originally published" line with full datetime
6. Save as `Medium-[Topic_Name].md` in `publications/[topic]/`

### Convert Draft to Paper
1. Apply `MAIN/templates/PAPER_TEMPLATE_APA.md` structure
2. Add Abstract with keywords
3. Number sections
4. Format tables (bold numbers, italic titles)
5. Add References in APA format
6. Add standard Acknowledgments

### Add New Topic
1. Create folder: `MAIN/publications/[topic-name]/`
2. Create Medium file: `Medium-[Topic_Name].md`
3. Create Paper file: `[Topic_Name]_Paper.md`
4. Add section to README.md Topics & Documents
5. Update document count

### Process CICD Incoming Research
1. Review files in `MAIN/CICD/incoming/`
2. Determine relevance to ONI Framework
3. If relevant: Extract key findings, create summary
4. Move processed file to `MAIN/CICD/processed/`
5. Update publications if new content warranted

### Rename/Reorganize Files
1. Use git mv for tracked files
2. Update all links in README.md
3. Verify no broken links
4. Commit with descriptive message

---

## Error Prevention

### Common Mistakes to Avoid
1. **Wrong location:** Don't put templates or instructions in `publications/`
2. **Wrong naming:** Don't use dates in publication filenames (use `Medium-*` prefix)
3. **Missing updates:** Always update README.md after adding content
4. **Inconsistent formatting:** Always check template before writing
5. **Broken links:** Use relative paths from repository root
6. **Wrong table format:** Numbers are BOLD, titles are ITALIC

### If Unsure
1. Read `MAIN/processes/PUBLISHING_INSTRUCTIONS.md`
2. Check existing files for examples
3. Ask user for clarification before proceeding

---

*Version: 2.0*
*Last Updated: January 2026*
*For: Claude AI Assistant*
