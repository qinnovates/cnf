# LearnViz - Adaptive Learning Visualization Engine

> **Vision:** Visualizations that adapt to how *you* learn, not the other way around.

An AI-powered, local-first pipeline that transforms concepts into educational visualizations — with the goal of adapting to each individual's learning style, pace, and cognitive patterns.

---

## What Is LearnViz?

LearnViz generates educational visualizations from natural language concept descriptions. Unlike static educational content, LearnViz aims to become **adaptive** — learning how you learn and adjusting its output accordingly.

### The Problem

Traditional educational visualizations are one-size-fits-all:
- Same pacing for everyone (too fast or too slow)
- Same visual style (some learn better with color, others with motion)
- Same level of detail (experts get bored, beginners get lost)
- No memory of what you already know
- Requires internet / cloud services

### The Solution

LearnViz runs locally, enabling:
- **Personalized pacing** based on your comprehension speed
- **Adaptive complexity** that matches your current understanding
- **Style preferences** (high contrast, animation speed, narration)
- **Learning history** that builds on what you already know
- **Privacy** — all data stays on your machine

---

## Architecture

### Current Implementation (v0.1)

```
┌─────────────────────────────────────────────────────────────────┐
│                    LEARNVIZ PIPELINE (v0.1)                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   [Concept Description]                                         │
│          │                                                      │
│          ▼                                                      │
│   ┌──────────────┐                                              │
│   │   ANALYZER   │ ← Pattern-based classification               │
│   │              │   Determines: type, engine, template         │
│   └──────┬───────┘                                              │
│          │                                                      │
│          ▼                                                      │
│   ┌──────────────┐                                              │
│   │  GENERATOR   │ ← Template-based code generation             │
│   │   (Manim)    │   Outputs: Python visualization script       │
│   └──────┬───────┘                                              │
│          │                                                      │
│          ▼                                                      │
│   ┌──────────────┐                                              │
│   │   RENDERER   │ ← Manim render engine                        │
│   │              │   Outputs: MP4/GIF video                     │
│   └─────────────┘                                               │
│                                                                 │
│   [100% Local - No cloud required]                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Future Vision (v1.0)

```
┌─────────────────────────────────────────────────────────────────┐
│                 ADAPTIVE LEARNVIZ (v1.0 Vision)                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   [Concept + Learner Profile]                                   │
│          │                                                      │
│          ▼                                                      │
│   ┌──────────────┐     ┌──────────────┐                         │
│   │   ANALYZER   │ ←── │   LEARNER    │ ← Tracks comprehension  │
│   │   + Context  │     │   PROFILE    │   pace, style prefs     │
│   └──────┬───────┘     └──────────────┘                         │
│          │                    ▲                                 │
│          ▼                    │                                 │
│   ┌──────────────┐            │                                 │
│   │  ADAPTIVE    │ ← Adjusts: pacing, complexity, style         │
│   │  GENERATOR   │   Uses: local LLM for custom scenes          │
│   └──────┬───────┘            │                                 │
│          │                    │                                 │
│          ▼                    │                                 │
│   ┌──────────────┐            │                                 │
│   │  INTERACTIVE │ ← Pause, rewind, ask questions               │
│   │   RENDERER   │   Feedback loop → profile update             │
│   └──────┬───────┘            │                                 │
│          │                    │                                 │
│          └────────────────────┘                                 │
│                                                                 │
│   [Local-First: All data stays on your machine]                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Initial Design Implementation (v0.1)

### What's Built

| Component | File | Status | Description |
|-----------|------|--------|-------------|
| **Concept Analyzer** | `analyzer.py` | ✅ Complete | Classifies concepts by type (math, physics, algorithm, etc.) |
| **Engine Selector** | `analyzer.py` | ✅ Complete | Maps concept types to optimal rendering engines |
| **Manim Generator** | `generators/manim_gen.py` | ✅ Complete | Generates Manim code from templates |
| **CLI Orchestrator** | `learnviz.py` | ✅ Complete | End-to-end pipeline with render support |
| **Template Library** | `generators/manim_gen.py` | ✅ 4 templates | Binary search, sorting, Pythagorean, tree traversal |

### Concept Classification

Pattern-based classification determines the best visualization approach:

| Category | Examples | Engine | Why |
|----------|----------|--------|-----|
| **Mathematical** | Pythagorean theorem, derivatives, matrices | Manim | LaTeX, geometric precision |
| **Physics** | Gravity, waves, forces, momentum | Manim | Physics primitives, parametric |
| **Algorithms** | Sorting, searching, recursion | Manim | Step-by-step animation |
| **Data Structures** | Trees, graphs, arrays | Manim | Node/edge visualization |
| **Statistics** | Charts, distributions, trends | Remotion | Data-driven, templated |
| **Timelines** | History, processes, workflows | Remotion | Component model |
| **Networks** | Graphs, connections, flows | D3.js | Force layouts |

### Current Templates

| Template | What It Visualizes |
|----------|-------------------|
| `binary_search` | Step-by-step search with L/R pointers, elimination highlighting |
| `sorting` | Bubble/selection/insertion sort with bar chart representation |
| `pythagorean` | Theorem proof with squares on triangle sides |
| `tree_traversal` | Inorder/preorder/postorder with visit order display |

### Usage

```bash
cd autodidact/learnviz

# Generate visualization code
python learnviz.py "Explain how binary search works"

# Generate and render to video
python learnviz.py "Bubble sort algorithm" --render

# Specify output format
python learnviz.py "Pythagorean theorem" --render --format gif

# Use custom parameters
python learnviz.py "Binary search" --params '{"target": 15, "array": [2,4,6,8,10,12,14,16]}'

# Interactive mode (refine plan before generation)
python learnviz.py "Tree traversal" --interactive
```

---

## Future Implementation Goals

### Phase 1: Expanded Content (v0.2)

**Goal:** More templates, more rendering engines

| Feature | Priority |
|---------|----------|
| Graph algorithms (BFS, DFS, Dijkstra, A*) | High |
| Linked list operations (insert, delete, reverse) | High |
| Recursion visualization (call stack, tree unfolding) | High |
| Remotion generator (data-driven charts, timelines) | Medium |
| D3.js generator (interactive web visualizations) | Medium |
| Physics simulations (projectile motion, waves) | Medium |

### Phase 2: LLM Integration (v0.3)

**Goal:** Generate custom visualizations for any concept

| Feature | Priority |
|---------|----------|
| Custom scene generation (LLM writes Manim code) | High |
| Explanation synthesis (auto-generate narration) | High |
| Concept decomposition (break complex → visual scenes) | High |
| Error correction (LLM fixes render errors) | Medium |

**Local LLM options:** Ollama, LM Studio, llama.cpp

### Phase 3: Learner Profiles (v0.4) ⭐ Core Vision

**Goal:** Visualizations that adapt to YOU

| Feature | Description |
|---------|-------------|
| **Learning style detection** | Visual/auditory/kinesthetic preferences |
| **Pace tracking** | How fast you comprehend new concepts |
| **Knowledge graph** | What you already know (skip repetition) |
| **Difficulty calibration** | Adjust complexity to your level |
| **Preference memory** | Animation speed, colors, narration |

**Proposed Learner Profile Schema:**
```json
{
  "learner_id": "local_user",
  "preferences": {
    "animation_speed": 1.0,
    "color_scheme": "high_contrast",
    "narration": true,
    "pause_on_key_points": true,
    "detail_level": "moderate"
  },
  "pace": {
    "concepts_per_session": 3,
    "avg_rewatch_count": 1.2,
    "preferred_duration": "5-10min",
    "comprehension_curve": [0.6, 0.75, 0.85, 0.92]
  },
  "knowledge_graph": {
    "mastered": ["binary_search", "arrays", "loops"],
    "learning": ["recursion", "trees"],
    "unexplored": ["graphs", "dynamic_programming"]
  },
  "learning_style": {
    "visual": 0.8,
    "verbal": 0.5,
    "sequential": 0.7,
    "global": 0.4
  },
  "history": [
    {
      "concept": "binary_search",
      "date": "2026-01-28",
      "duration": 180,
      "rewinds": 2,
      "comprehension_score": 0.9
    }
  ]
}
```

**Adaptation Examples:**

| If learner profile shows... | Then LearnViz will... |
|----------------------------|----------------------|
| High rewind count on recursion | Add more step-by-step breakdown |
| Fast pace on math concepts | Skip basic derivations |
| Preference for visual over verbal | Reduce text, increase diagrams |
| Already mastered arrays | Skip array intro in sorting viz |
| Struggles with abstract concepts | Add concrete examples first |

### Phase 4: Interactive Mode (v0.5)

**Goal:** Two-way learning experience

| Feature | Description |
|---------|-------------|
| **Pause and explain** | Click any element for deeper explanation |
| **Rewind with context** | "Go back to where you explained X" |
| **Ask questions** | "Why did we eliminate the left half?" |
| **Quiz checkpoints** | "Before we continue, predict what happens next" |
| **Branching paths** | "Want the simple or detailed version?" |

### Phase 5: Multi-Modal Output (v0.6)

**Goal:** Right format for the right context

| Format | Use Case | Status |
|--------|----------|--------|
| Video (MP4/GIF) | Standard sharing | ✅ Done |
| Interactive web | Exploration, Q&A | Planned |
| Slides (PDF) | Presentations | Planned |
| Audio narration | Accessibility, multitasking | Planned |
| AR/VR export | Spatial learning for 3D | Future |

### Phase 6: Community Templates (v1.0)

**Goal:** Learn from others (opt-in, privacy-preserving)

| Feature | Description |
|---------|-------------|
| Template sharing | Community-contributed visualizations |
| Difficulty ratings | Crowdsourced complexity calibration |
| Aggregate insights | "Most learners pause here" |
| **Privacy-first** | No personal data leaves device |

---

## Design Principles

### 1. Local-First

All computation and data stays on your machine:
- ✅ No cloud dependency for rendering
- ✅ Learner profiles stored locally (SQLite)
- ✅ Works offline
- ✅ You own your learning data

### 2. Adaptive by Default

Every visualization adapts to:
- Your current knowledge level
- Your preferred learning pace
- Your visual/cognitive style
- What you've already learned

### 3. Transparent Generation

The pipeline is explainable:
- Why was this template chosen?
- What assumptions were made?
- How can you override decisions?

### 4. Incremental Complexity

```
v0.1: Static templates         ← We are here
v0.2: More templates
v0.3: LLM-generated custom scenes
v0.4: Learner-aware adaptation ← Core vision
v0.5: Interactive two-way learning
v1.0: Full adaptive engine
```

---

## Technical Requirements

### Current (v0.1)

```bash
# Python dependencies
pip install manim

# Verify installation
manim --version  # Should show 0.19+
```

### Future (v0.4+)

```bash
# Learner profiles
pip install sqlite3

# Local LLM (choose one)
# Option A: Ollama
brew install ollama && ollama pull llama2

# Option B: LM Studio
# Download from https://lmstudio.ai/

# Voice/narration
pip install gtts pyttsx3

# Additional render engines
npm install -g @remotion/cli
npm install d3 puppeteer
```

---

## File Structure

```
autodidact/learnviz/
├── README.md                 # This file - vision and roadmap
├── learnviz.py               # Main CLI orchestrator
├── analyzer.py               # Concept classification engine
├── .gitignore                # Excludes render artifacts
│
├── generators/               # Code generators by engine
│   ├── __init__.py
│   ├── manim_gen.py          # ✅ Manim template generator
│   ├── remotion_gen.py       # 🔲 (Planned) React video generator
│   └── d3_gen.py             # 🔲 (Planned) D3.js generator
│
├── profiles/                 # 🔲 (Planned) Learner profiles
│   └── learner.db            # SQLite database
│
├── output/                   # Generated visualization code
│   └── *.py                  # Manim scripts
│
└── media/                    # (gitignored) Render artifacts
    └── videos/               # Rendered MP4/GIF files
```

---

## Research Foundations

LearnViz draws inspiration from:

| Theory | Application in LearnViz |
|--------|------------------------|
| **Spaced Repetition** | Adaptive timing based on retention curves |
| **Zone of Proximal Development** | Complexity matching to current ability |
| **Multimedia Learning Theory** | Cognitive load optimization |
| **Learning Styles (VARK)** | Visual/auditory/kinesthetic adaptation |
| **Mastery Learning** | Don't proceed until current concept is solid |

---

## Version History

| Version | Date | Milestone |
|---------|------|-----------|
| **0.1.0** | 2026-01-28 | Initial: analyzer, Manim generator, CLI, 4 templates |
| 0.2.0 | TBD | Expanded templates (graphs, recursion, linked lists) |
| 0.3.0 | TBD | LLM integration for custom generation |
| **0.4.0** | TBD | **Learner profiles and adaptive pacing** |
| 0.5.0 | TBD | Interactive mode with Q&A |
| 1.0.0 | TBD | Full adaptive learning engine |

---

## Credits

Built on:
- [Manim Community](https://www.manim.community/) — Mathematical animations
- [3Blue1Brown](https://www.3blue1brown.com/) — Inspiration for visual math
- [Remotion](https://www.remotion.dev/) — React-based video (planned)
- [D3.js](https://d3js.org/) — Data visualization (planned)

---

*Part of the ONI Framework — autodidact module*

> *"Learn how you learn, then learn faster."*
