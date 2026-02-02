# Claude AI Instructions for QIF Repository

> This file provides instructions for Claude to follow when assisting with the QIF (Quantum Indeterministic Framework for Neural Security) repository. Read this file at the start of any session involving content creation, publishing, or repository maintenance.
>
> **GitHub:** github.com/qinnovates/qif (local folder: `@qikevinl/oni/`)

---

## Quick Reference

| Resource | Location | Purpose |
|----------|----------|---------|
| **Brand Constants** | `neurosecurity/legacy-core/resources/brand/brand.json` | **Single source of truth for ONI/TARA naming, slogans, versions, stats** |
| **Website Stats** | `docs/index.html` | **Dynamic stats system - see "Website Stats System" section** |
| **Main Wiki (INDEX)** | `neurosecurity/legacy-core/INDEX.md` | **Central hub - navigation, dependencies, cross-references** |
| **Python Package** | `neurosecurity/legacy-core/oni-framework/` | **pip install oni-framework** |
| **Transparency Statement** | `neurosecurity/qif/governance/TRANSPARENCY.md` | **Human-AI collaboration audit trail** |
| **Neuroethics Alignment** | `neurosecurity/qif/governance/NEUROETHICS_ALIGNMENT.md` | **Framework-to-ethics principle mapping** |
| **Research Verification** | `neurosecurity/legacy-core/resources/agents/RESEARCH_VERIFICATION_PROTOCOL.md` | **Anti-hallucination firewall for claims** |
| **Personas** | `neurosecurity/legacy-core/resources/agents/PERSONAS.md` | **Agent personas for research verification** |
| Topic README Template | `neurosecurity/legacy-core/resources/templates/README_TEMPLATE.md` | Template for topic-level overviews |
| APA Template | `neurosecurity/legacy-core/resources/templates/TECHDOC_TEMPLATE_APA.md` | Formatting for technical documents |
| Blog Template | `neurosecurity/legacy-core/resources/templates/BLOG_TEMPLATE.md` | Formatting for blog posts |
| Publishing Instructions | `neurosecurity/legacy-core/project/processes/PUBLISHING_INSTRUCTIONS.md` | Step-by-step publishing workflow |
| Research Monitor | `neurosecurity/legacy-core/resources/pipeline/scripts/research_monitor.py` | Fetch new academic papers |
| Keywords File | `neurosecurity/legacy-core/resources/pipeline/scripts/keywords.json` | Research search terms |
| Verified Claims | `neurosecurity/legacy-core/resources/pipeline/verified/` | Verified research claims with citations |
| **Editor Agent** | `neurosecurity/legacy-core/resources/editor/EDITOR_AGENT.md` | **Automated quality & sync (run before commits)** |
| **AGENTS.md** | `AGENTS.md` | **Ralph Loop learnings — read at session start** |
| **Project Management** | `neurosecurity/legacy-core/project/PROJECT_MANAGEMENT.md` | **Master PM doc — scope, risks, priorities, metrics** |
| **Kanban Board** | `neurosecurity/legacy-core/project/KANBAN.md` | **Visual task board — status at a glance** |
| **prd.json** | `neurosecurity/legacy-core/project/prd.json` | **Task tracker with exit conditions** |
| **Video Production** | `video/demo/CLAUDE.md` | **Remotion video production pipeline & audio sync** |
| **Sound Design** | `neurosecurity/legacy-core/resources/sound-engineering/ONI_VIDEO_SOUND_DESIGN.md` | **Audio psychology & specs** |
| This File | `CLAUDE.md` | Claude-specific instructions |

### Naming Convention: INDEX.md vs README.md

| File | Location | Purpose |
|------|----------|---------|
| `INDEX.md` | `neurosecurity/legacy-core/` only | **Main wiki hub** — single source of truth for navigation, dependencies, roadmap |
| `README.md` | Each topic folder | **Topic overview** — auto-rendered by GitHub when browsing folders |

> **Why this distinction?** `INDEX.md` is unique to the main wiki. Topic folders use `README.md` because GitHub automatically renders it when viewing folders, providing a better browsing experience.

---

## Repository File Tree

```
mindloft/                               # Local folder (remote: github.com/qinnovates/mindloft)
├── README.md                           # Public entry point
├── CLAUDE.md                           # Claude AI instructions (this file)
├── AGENTS.md                           # Ralph Loop learnings (read at session start)
├── ABOUT.md                            # Author bio
├── GLOSSARY.md                         # Framework glossary
├── LICENSE                             # Apache 2.0 License
├── SECURITY.md                         # Security policy
│
├── .github/
│   ├── .gitignore                      # Git ignore rules
│   ├── workflows/                      # CI/CD pipelines (tests, publish, security, brand-sync)
│   └── security-audit/                 # Security scanning tools
│
├── neurosecurity/                      # ═══ ALL NEUROSECURITY CONTENT ═══
│   ├── README.md
│   │
│   ├── qif/                            # QIF — Quantum Indeterministic Framework (v2)
│   │   ├── README.md                   # Framework overview + model concept image
│   │   ├── framework/                  # 9 architectural documents (01-09)
│   │   ├── governance/                 # 9 neuroethics & compliance documents
│   │   └── images/                     # QIF model concept diagrams
│   │
│   ├── legacy-core/                    # Original ONI research (preserved)
│   │   ├── INDEX.md                    # Main wiki — navigation, dependencies
│   │   ├── CONTRIBUTING.md
│   │   ├── RELATED_WORK.md
│   │   ├── ACADEMIC_LANDSCAPE.md
│   │   ├── PARTNERSHIPS.md
│   │   ├── oni-framework/              # Python package (pip install oni-framework)
│   │   ├── tara-nsec-platform/         # TARA package (pip install oni-tara)
│   │   ├── publications/               # 31 research papers across 8 topics
│   │   ├── project/                    # Project management (prd.json, KANBAN.md)
│   │   ├── resources/                  # Brand, agents, templates, pipeline, editor
│   │   └── archive/                    # Website evolution (v1-v5)
│   │
│   └── autodidact/                     # Educational content
│       ├── oni-academy/                # ONI Academy (pip install oni-academy)
│       ├── neuroscience-bci/           # Personal neuroscience learning
│       └── learnviz/                   # Learning visualization tools
│
├── docs/                               # GitHub Pages website
│   ├── index.html                      # Landing page
│   ├── documentation/                  # Documentation hub
│   ├── visualizations/                 # 11 interactive tools
│   ├── whitepaper/                     # Published whitepaper
│   ├── oni-visualizations/             # Visualization source code
│   └── images/                         # Site images
│
└── video/                              # Video production
    ├── demo/                           # ONI Demo Video (Remotion)
    ├── bci-zoom/                       # BCI zoom animation
    └── motion/                         # Motion graphics
```

---

## Brand System (CRITICAL)

> **Single source of truth for all project naming, slogans, and versions.**

### Architecture

```
neurosecurity/legacy-core/resources/brand/brand.json      ← EDIT THIS to change any brand value
    │
    ├── oni/brand.py           ← Python API for ONI Framework
    ├── tara_mvp/_brand.py     ← Python API for TARA
    ├── oni_academy/_brand.py  ← Python API for ONI Academy
    │
    └── neurosecurity/legacy-core/resources/brand/sync_brand.py  ← Syncs changes to README.md
```

### Brand Values

| Project | Acronym | Full Name |
|---------|---------|-----------|
| **ONI** | ONI | Open Neurosecurity Interoperability |
| **TARA** | TARA | Telemetry Analysis & Response Automation |

### Session Start: Brand Consistency Check

**At the start of every session, verify brand consistency:**

```bash
# Quick check - run from repo root
python3 -c "
import json
with open('neurosecurity/legacy-core/resources/brand/brand.json') as f: b = json.load(f)
print(f\"ONI: {b['oni']['full_name']}\")
print(f\"TARA: {b['tara']['full_name']}\")
print(f\"ONI v{b['oni']['version']} | TARA v{b['tara']['version']}\")
"
```

### When to Update brand.json

Update `neurosecurity/legacy-core/resources/brand/brand.json` when:
- Changing project name, acronym, or full name
- Updating taglines, slogans, or mission statements
- Bumping version numbers for releases
- Adding new project brands

### After Updating brand.json

1. **Run sync script:** `python neurosecurity/legacy-core/resources/brand/sync_brand.py`
2. **Verify Python loads correctly:** Test import from each package
3. **Commit both brand.json and any synced files**
4. **GitHub Action auto-syncs** README.md on push

### Brand Fields Reference

```json
{
  "acronym": "ONI",
  "full_name": "Open Neurosecurity Interoperability",
  "name": "ONI Framework",
  "tagline": "The OSI of Mind",
  "slogan": "Our minds. Our rules. Our future.",
  "mission": "The mind is the last frontier...",
  "description": "A unified 14-layer model...",
  "version": "0.2.0"
}
```

### Python Usage

```python
# From ONI Framework
from oni.brand import ONI, TARA, ONI_VERSION
print(ONI.full_name)  # "Open Neurosecurity Interoperability"

# From TARA (no oni-framework dependency needed)
from tara_mvp._brand import TARA, ONI
print(TARA.tagline)  # "Protection for the neural frontier"
```

---

## Website Stats System

> **The GitHub Pages site (`docs/index.html`) displays stats that update from two sources.**

### Stats Overview

| Stat | Source | Update Method |
|------|--------|---------------|
| **Commits** | GitHub API | **Auto** (real-time) |
| **Threat Signatures** | `brand.json → stats.threat_signatures` | Manual |
| **Security Layers** | `brand.json → stats.security_layers` | Manual (always 14) |
| **Interactive Tools** | GitHub API | **Auto** (counts `.html` in `docs/visualizations/`) |
| **Learning Portals** | `brand.json → stats.learning_portals` | Manual |

### How It Works

1. **Page loads** → displays default values from HTML
2. **JavaScript fetches** `brand.json` from GitHub raw URL
3. **Manual stats** (threat signatures, layers, portals) update from `brand.json`
4. **Auto stats** fetch from GitHub API:
   - Commits: `api.github.com/repos/qinnovates/mindloft/commits`
   - Tools: `api.github.com/repos/qinnovates/mindloft/contents/docs/visualizations`

### Updating Manual Stats

Edit `neurosecurity/legacy-core/resources/brand/brand.json`:

```json
{
  "stats": {
    "security_layers": 14,
    "threat_signatures": 46,
    "learning_portals": 1
  }
}
```

Push to GitHub → website auto-updates on next page load.

### Auto Stats Update Automatically When:

| Stat | Triggers Update |
|------|-----------------|
| Commits | Any push to main branch |
| Interactive Tools | Add/remove `.html` files in `docs/visualizations/` |

### Troubleshooting

- **Stats not updating?** GitHub API has rate limits (60 req/hr unauthenticated). Wait and refresh.
- **Wrong count?** Check that files match expected patterns (`.html` for tools, `pyproject.toml` for packages).
- **Local testing?** Stats fetch from GitHub raw/API, so local changes won't reflect until pushed.

---

## Folder Purposes

| Folder | Purpose | What Goes Here |
|--------|---------|----------------|
| `governance/` | **Ethics, transparency & regulatory** | 9 documents: TRANSPARENCY, NEUROETHICS_ALIGNMENT, UNESCO_ALIGNMENT, REGULATORY_COMPLIANCE, INFORMED_CONSENT, POST_DEPLOYMENT, PEDIATRIC, DATA_POLICY_FAQ, ACCESSIBILITY |
| `project/` | **Project management** | prd.json, processes/ (workflows, improvements) |
| `oni-framework/` | **Python library** | Source code, tests, package config (pip installable) |
| `tara-nsec-platform/` | **TARA package** | Source, tests, visualizations, pyproject.toml |
| `publications/` | **Content only** | Blog posts, technical documents |

> **Note:** `oni-academy/` has moved to `autodidact/oni-academy/` (root-level `autodidact/` folder).
| `resources/templates/` | Formatting templates | APA template, Blog template |
| `resources/pipeline/` | Research pipeline | Incoming papers, processed, scripts, keywords |
| `resources/editor/` | **Editor Agent** | Quality validation, sync rules, auto-fix logic |

**IMPORTANT:**
- The `governance/` folder contains ethics and transparency documentation.
- The `project/` folder contains project management files (prd.json, processes).
- The `publications/` folder is for **content only**. Never put templates, instructions, or scripts there.
- The `resources/` folder contains infrastructure files (templates, pipeline, editor).

---

## Naming Conventions

### Folder Names
- **Format:** lowercase with hyphens
- **Examples:** `coherence-metric`, `neural-firewall`, `scale-frequency`

### File Names

| Type | Format | Example |
|------|--------|---------|
| Blog Posts | `Blog-[Topic_Name].md` | `Blog-Coherence_Metric.md` |
| Technical Documents | `TechDoc-[Topic_Name].md` | `TechDoc-Neural_Ransomware.md` |
| Detailed TechDocs | `TechDoc-[Topic_Name]_Detailed.md` | `TechDoc-Coherence_Metric_Detailed.md` |
| Templates | `[NAME]_TEMPLATE_[TYPE].md` | `TECHDOC_TEMPLATE_APA.md` |
| Pipeline Research | `YYYY-MM-DD_[source]_[title].md` | `2026-01-21_arxiv_neural-security.md` |

### Topic Name Rules
- Use PascalCase with underscores between words
- Match folder name but with underscores instead of hyphens
- Examples:
  - Folder: `coherence-metric` → File: `Coherence_Metric`
  - Folder: `neural-firewall` → File: `Neural_Firewall`

---

## Editor Agent (REQUIRED)

> **Run the Editor Agent before every commit and after content changes.**

### What It Does

The Editor Agent ensures consistency and accuracy across all documentation:

| Action Type | Behavior | Examples |
|-------------|----------|----------|
| **AUTO-FIX** | Applied immediately | Dates, counts, broken links, formatting |
| **APPROVAL** | Report and wait | Layer definitions, formulas, content changes |

### When to Run

1. **Before commits** — Validates changes before they're pushed
2. **After content changes** — Propagates updates to related files
3. **On request** — Manual validation with "Run editor validation"

### How to Run

```
1. Read: neurosecurity/legacy-core/resources/editor/EDITOR_AGENT.md
2. Read relevant checks from: neurosecurity/legacy-core/resources/editor/checks/
3. Execute validation workflow
4. Apply auto-fixes, report approval items
```

### Sub-Instruction Files

| File | Purpose |
|------|---------|
| `checks/layer_validation.md` | 14-layer model accuracy (CRITICAL) |
| `checks/sync_rules.md` | Cross-reference cascade rules |
| `checks/naming_rules.md` | File/folder naming patterns |
| `checks/format_rules.md` | Template compliance |

### Authoritative Sources (Truth Hierarchy)

When content conflicts, use this priority:

1. `TechDoc-*.md` files (technical truth)
2. `oni-framework/oni/*.py` (implementation)
3. `INDEX.md` (navigation)
4. Topic `README.md` (summaries)
5. Root `README.md` (public overview)

**Rule:** Lower priority files must match higher priority sources.

### Critical Validations

These MUST match the authoritative TechDoc:

**14-Layer Model:**
```
L1-L7: Silicon (Physical Carrier → Application Interface)
L8: Neural Gateway (Bridge)
L9-L14: Biology (Ion Channel Encoding → Identity & Ethics)
```

**Coherence Formula:** Cₛ = e^(−(σ²φ + σ²τ + σ²γ))

**Scale-Frequency:** f × S ≈ k

---

## Persona System (Research Verification)

> **Purpose:** Prevent AI hallucinations in academic research through domain-specific verification personas. See full documentation: `neurosecurity/legacy-core/resources/agents/PERSONAS.md`

### Quick Reference

| Persona | Role | Key Question |
|---------|------|--------------|
| **AURORA** | Main reasoning partner | "What's the insight here?" |
| **SOCRATES** | General fact-checking | "What evidence supports this?" |
| **GÖDEL** | Mathematical verification | "Does this formula hold?" |
| **FARADAY** | Physics/neuroscience claims | "What does the science say?" |
| **HYPATIA** | Documentation organization | "Where does this belong?" |
| **ARCHIMEDES** | Project management | "What's the lever?" |
| **EDITOR** | Cross-reference sync | "Is this consistent?" |

### Research Verification Protocol

> **CRITICAL:** All neuroscience, physics, and security claims must be verified before publication. See: `neurosecurity/legacy-core/resources/agents/RESEARCH_VERIFICATION_PROTOCOL.md`

#### Uncertainty Tags

Every claim gets tagged:

| Tag | Meaning | Action |
|-----|---------|--------|
| ✅ VERIFIED | Direct citation from peer-reviewed source | Safe to use |
| ⚠️ INFERRED | Logical inference from verified facts | Flag in text |
| 🔍 UNVERIFIED | Plausible but no source found | Do NOT use |
| ❌ CONTRADICTED | Evidence contradicts claim | Do NOT use |
| 🔬 HYPOTHESIS | Novel ONI contribution | Label clearly |

#### Domain Checks

| Domain | Persona | Common Errors |
|--------|---------|---------------|
| **Neuroscience** | FARADAY | Timescale errors (ms vs fs), uniform reliability assumptions |
| **Physics** | FARADAY | Thermodynamic violations, energy estimate errors |
| **Mathematics** | GÖDEL | Formula/code mismatch, notation inconsistency |
| **Security** | SOCRATES | Theoretical vs practical attack vectors |

#### Before Any Factual Claim

```
1. Do I have a source? → No = flag as 🔍 UNVERIFIED
2. Is it peer-reviewed? → No = downgrade confidence
3. Does claim match source exactly? → No = flag as ⚠️ INFERRED
4. Is this neuroscience/physics? → Yes = run through FARADAY
5. Is this mathematical? → Yes = verify with GÖDEL
6. Tag: ✅ ⚠️ 🔍 ❌ 🔬
7. Cite: (Author, Year)
```

### Verified Claims Workflow

```
1. Identify claim needing verification
         ↓
2. SOCRATES: Search for authoritative sources
         ↓
3. Add source to neurosecurity/legacy-core/resources/pipeline/sources/
         ↓
4. FARADAY/GÖDEL: Domain-specific validation
         ↓
5. HYPATIA: Document in verified/[topic]-verified.md
         ↓
6. Use ✅ claims in publications
```

---

## Ralph Loop (Continuous Iteration)

> **Purpose:** Knowledge compounding through persistent learnings. Each iteration starts fresh but benefits from discoveries documented in `AGENTS.md`.

### Session Start Protocol

```
1. Read CLAUDE.md (this file) — conventions and workflows
2. Read AGENTS.md — learnings from previous iterations
3. Read neurosecurity/legacy-core/project/prd.json — current task status and exit conditions
4. Execute tasks until exit condition met
5. Update AGENTS.md with new learnings
6. Update neurosecurity/legacy-core/project/prd.json with progress
7. Commit changes (memory persists via git)
```

### Key Files

| File | Purpose | When to Update |
|------|---------|----------------|
| `AGENTS.md` | Learnings, patterns, gotchas | After every significant discovery |
| `neurosecurity/legacy-core/project/prd.json` | Task tracking, exit conditions | After completing or adding tasks |
| `CLAUDE.md` | Conventions, workflows | When processes change |

### Ralph Loop Workflow

```
┌─────────────────────────────────────────┐
│  1. Define Exit Condition               │
│     (What does "done" look like?)       │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  2. Fresh Context                       │
│     Read: CLAUDE.md, AGENTS.md, prd.json  │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  3. Execute                             │
│     Run Editor Agent, complete tasks    │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  4. Persist Learnings                   │
│     Update AGENTS.md with discoveries   │
│     Update prd.json with progress         │
│     Commit to git                       │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  5. Check Exit Condition                │
│     Done? → End                         │
│     Not done? → Loop to step 2          │
└─────────────────────────────────────────┘
```

### AGENTS.md Structure

```markdown
## [Agent Name] Learnings

### Critical Discoveries
| Date | Learning | Impact |

### Patterns Established
- Pattern 1
- Pattern 2

### Gotchas Avoided
- Gotcha 1
- Gotcha 2
```

### prd.json Structure

```json
{
  "tasks": [
    {
      "id": "task-id",
      "description": "What needs to be done",
      "status": "pending|complete",
      "exit_condition": "Machine-verifiable condition",
      "learnings": "What was discovered (after completion)"
    }
  ]
}
```

### Exit Condition Best Practices

| Good Exit Condition | Bad Exit Condition |
|---------------------|-------------------|
| "grep finds 0 layer mismatches" | "Layers look correct" |
| "All tests pass" | "Code seems to work" |
| "EDITOR_AGENT.md exists" | "Editor is implemented" |
| "Date matches git commit date" | "Dates are updated" |

**Rule:** Exit conditions must be machine-verifiable, not subjective.

---

## Workflow Instructions

### When Adding New Content

1. **Read the templates first:**
   ```
   Read: neurosecurity/legacy-core/resources/templates/TECHDOC_TEMPLATE_APA.md
   Read: neurosecurity/legacy-core/resources/templates/BLOG_TEMPLATE.md
   Read: neurosecurity/legacy-core/project/processes/PUBLISHING_INSTRUCTIONS.md
   ```

2. **Create topic folder (if new topic):**
   ```bash
   mkdir neurosecurity/legacy-core/publications/[topic-name]
   ```

3. **Create files with correct naming:**
   - Blog post: `Blog-[Topic_Name].md` (include original Medium URL if applicable)
   - Technical document: `TechDoc-[Topic_Name].md`

4. **Apply proper formatting:**
   - Blog: Conversational, storytelling, web-optimized
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

2. Update `neurosecurity/legacy-core/resources/pipeline/scripts/keywords.json`:
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
cd neurosecurity/legacy-core/resources/pipeline/scripts
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
> - New navigation features (like INDEX.md)
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
| [Blog-Topic_Name](neurosecurity/legacy-core/publications/topic-folder/Blog-Topic_Name.md) | *One-line description* |
| [TechDoc-Topic_Name](neurosecurity/legacy-core/publications/topic-folder/TechDoc-Topic_Name.md) | *One-line description* |
```

### Step 3: Update Navigation Section (if needed)
If adding new navigation features or structural changes:
```markdown
## Navigation

| Start Here | Purpose |
|------------|---------|
| **[INDEX.md](neurosecurity/legacy-core/INDEX.md)** | Central hub — dependency map, cross-references, reading order, roadmap |
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

## INDEX.md Update Protocol

> **CRITICAL:** INDEX.md is the central wiki hub. Update it for ANY structural or package change:
> - Python package changes (versions, new modules, new packages)
> - Folder structure changes (moved files, renamed directories)
> - New topics or publications
> - Test count changes
> - Dependency map changes

**After every commit that modifies packages, structure, or dependencies, update INDEX.md:**

### Step 1: Python Packages Section
If package versions change or new modules are added:
- Update version numbers in the module tables
- Add new modules to the appropriate table
- Update `pip install` commands if package names change

### Step 2: Dependency Map
If adding new components that depend on existing ones:
- Update the ASCII diagram to show relationships
- Ensure arrows show correct dependency direction

### Step 3: Folder Structure
If files are moved or directories are renamed:
- Update the folder tree diagram
- Verify all paths are correct
- Include test counts and version numbers

### Step 4: Metrics Section
Update the metrics table:
- Python Packages: list all packages with versions
- Unit Tests: total count (sum of all packages)
- Document counts if publications change

### Step 5: Version and Date
```markdown
**Version:** [increment minor version]
**Last Updated:** YYYY-MM-DD
```

**Common Mistakes to Avoid:**
- Forgetting to update `siem/` to `nsam/` (the actual folder name)
- Outdated version numbers in metrics
- Stale test counts
- Referencing old paths (source is now in `tara-nsec-platform/tara_mvp/`, not `prototype-mvp/`)

---

## Standard Acknowledgments

Use this text in all technical documents:

> The author wishes to acknowledge the support of colleagues and mentors in the development of this work. Initial research validation was conducted through LMArena (LMSYS, 2024-2025), enabling cross-model verification of hypotheses and findings to mitigate single-model bias. Deep research synthesis and writing assistance was provided by Claude (Anthropic, 2025). All original ideas, theoretical frameworks, analyses, and conclusions are the author's own. Final revisions, editing, and validation were performed by the author.

---

## Transparency Documentation (REQUIRED)

> **CRITICAL:** The ONI Framework maintains a transparency standard for Human-AI collaboration. This documentation supports academic review, Responsible AI principles, and neuroethics alignment.

### Key Documents

| Document | Location | Purpose |
|----------|----------|---------|
| `TRANSPARENCY.md` | `neurosecurity/qif/governance/` | Audit trail of Human-AI cognitive boundary |
| `NEUROETHICS_ALIGNMENT.md` | `neurosecurity/qif/governance/` | Maps framework components to ethical principles |

### When to Update TRANSPARENCY.md

Update `neurosecurity/qif/governance/TRANSPARENCY.md` whenever:

1. **New publications are added** — Add to contribution matrix if significant AI assistance used
2. **Code changes with AI assistance** — Document any AI suggestions that were rejected/modified
3. **New modules or features** — Categorize human vs AI contributions
4. **Corrections to AI output** — Add to "Documented Corrections" section as examples

### Transparency Update Checklist

For each publishing session, verify:

- [ ] Any AI corrections/overrides documented in governance/TRANSPARENCY.md "Refinement Loop" section
- [ ] Contribution matrix updated if new content domains added
- [ ] "Last Updated" date changed in governance/TRANSPARENCY.md header
- [ ] Commit includes `Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>` tag

### Cognitive Boundary Documentation Format

When documenting significant AI interactions, use this format:

```markdown
#### Example N: [Brief Title]
- **AI Initial Output**: [What AI suggested]
- **Human Override/Correction**: [What was changed and why]
- **Action Taken**: [Where the correction was implemented]
- **Ethical/Technical Reasoning**: [Why this decision matters]
```

### NEUROETHICS_ALIGNMENT.md Updates

Update `neurosecurity/qif/governance/NEUROETHICS_ALIGNMENT.md` when:

1. **New framework components added** — Map to ethical principles
2. **Security features modified** — Update ethical reasoning
3. **New ethical considerations identified** — Add to gaps/future work

### Enhanced Commit Message Format (For Significant Contributions)

For major features or content, use extended format:

```
[Action] [Topic/Scope]: Brief description

Original conception: Human/AI/Joint
Implementation: Human/AI-assisted
Verification: Human (method used)

- Detailed changes
- Human decisions noted
- AI suggestions accepted/rejected noted

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

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

### Content Quality
- [ ] File naming follows conventions
- [ ] Folder naming follows conventions
- [ ] Content files are in `publications/` only
- [ ] Non-content files are in `resources/` only
- [ ] Blog posts have proper front matter (title, date_posted, original_url, tags)
- [ ] Blog posts have proper footer (Sub-Tags, Originally published with datetime and link)
- [ ] TechDocs follow APA template structure
- [ ] Tables use bold numbers (`**Table 1**`) and italic titles
- [ ] References are in APA format
- [ ] Acknowledgments section included (TechDocs only)

### Repository Updates
- [ ] **Keywords extracted and added to keywords.json**
- [ ] README.md updated with new links
- [ ] Document count updated in README.md footer
- [ ] Date updated in README.md footer
- [ ] **Topic README.md created** (for new topics — auto-rendered by GitHub)
- [ ] **neurosecurity/legacy-core/INDEX.md updated** (main wiki: dependency map, tables, metrics)

### Package/Structure Changes (CRITICAL)
- [ ] **INDEX.md Python Packages section updated** (versions, new modules)
- [ ] **INDEX.md Folder Structure updated** (file moves, directory changes)
- [ ] **INDEX.md Metrics updated** (test counts, versions)
- [ ] **INDEX.md version/date incremented**
- [ ] **CLAUDE.md file tree updated** (if structure changed)
- [ ] **README.md file tree updated** (if structure changed)

### Transparency Documentation (REQUIRED)
- [ ] **TRANSPARENCY.md updated** if significant AI assistance used
- [ ] **AI corrections/overrides documented** in Refinement Loop section
- [ ] **Contribution matrix updated** if new content domains added
- [ ] **Commit includes Co-Authored-By tag** for AI-assisted work
- [ ] **NEUROETHICS_ALIGNMENT.md updated** if new framework components added

---

## Common Tasks Reference

### Extract Content from Medium RSS
1. Fetch content from RSS feed URL
2. Extract title, date_posted, URL, tags for front matter
3. Clean formatting resources
4. Rename bottom `Tags:` section to `Sub-Tags:`
5. Update "Originally published" line with full datetime and Medium link
6. Save as `Blog-[Topic_Name].md` in `publications/[topic]/`
7. **Extract keywords and update keywords.json**

### Convert Draft to TechDoc
1. Apply `neurosecurity/legacy-core/resources/templates/TECHDOC_TEMPLATE_APA.md` structure
2. Add Abstract with keywords
3. Number sections
4. Format tables (bold numbers, italic titles)
5. Add References in APA format
6. Add standard Acknowledgments
7. **Extract keywords and update keywords.json**

### Add New Topic (Full Expansion Workflow)

**Step 1: Create topic folder**
```bash
mkdir neurosecurity/legacy-core/publications/[topic-name]/
```

**Step 2: Create topic README.md**
- Copy from `neurosecurity/legacy-core/resources/templates/README_TEMPLATE.md`
- Fill in: summary, dependencies, key concepts, related topics
- Link back to `neurosecurity/legacy-core/INDEX.md` (main wiki)
- **Note:** Use `README.md` (not INDEX.md) — GitHub auto-renders it when browsing folders

**Step 3: Create publications**
- `Blog-[Topic_Name].md` — Accessible narrative (include original Medium URL if applicable)
- `TechDoc-[Topic_Name].md` — Academic depth

**Step 4: Extract keywords and update keywords.json**

**Step 5: Update INDEX.md**
- Add topic to appropriate section table
- Update dependency map (if new dependencies)
- Update cross-reference matrix
- Update metrics (topic/document counts)

**Step 6: Update README.md**
- Add section to Topics & Documents
- Update document count in footer

### Process Pipeline Incoming Research
1. Review files in `neurosecurity/legacy-core/resources/pipeline/incoming/`
2. Determine relevance to ONI Framework
3. If relevant: Extract key findings, create summary
4. Move processed file to `neurosecurity/legacy-core/resources/pipeline/processed/`
5. Update publications if new content warranted

### Rename/Reorganize Files
1. Use git mv for tracked files
2. Update all links in README.md
3. Verify no broken links
4. Commit with descriptive message

---

## Error Prevention

### Common Mistakes to Avoid
1. **Wrong location:** Don't put templates or instructions in `publications/` - use `resources/`
2. **Wrong naming:** Don't use dates in publication filenames (use `Blog-*` or `TechDoc-*` prefix)
3. **Missing README updates:** Always update README.md after ANY major change (topics, structure, navigation)
4. **Missing WIKI updates:** Always update INDEX.md when adding topics or changing dependencies
5. **Missing keywords:** Always extract and add keywords to keywords.json
6. **Inconsistent formatting:** Always check template before writing
7. **Broken links:** Use relative paths from repository root
8. **Wrong table format:** Numbers are BOLD, titles are ITALIC
9. **Stale footer:** Always update document/topic counts and date in README.md footer

### If Unsure
1. Read `neurosecurity/legacy-core/project/processes/PUBLISHING_INSTRUCTIONS.md`
2. Check existing files for examples
3. Ask user for clarification before proceeding

---

*Version: 8.1*
*Last Updated: 2026-01-24*
*For: Claude AI Assistant*
