# Neuroscience & BCI Research

> **Purpose:** Personal research and learning repository for neuroscience concepts I need to understand to build the ONI Framework. This is where I figure out things I don't know but need to know.

**This is NOT polished documentation.** It's a working knowledge base for building understanding of the biological substrate that BCIs interface with.

---

## Table of Contents

1. [Folder Structure](#folder-structure)
2. [Purpose of Each Folder](#purpose-of-each-folder)
3. [Research Documents](#research-documents)
4. [Key Questions](#key-questions-this-research-aims-to-answer)
5. [Related Projects](#related-projects)
6. [Adding Research](#adding-research)

---

## Folder Structure

```
neuroscience-homework-todo/
├── README.md                           # This file
├── Research-BCI_Mouse_Movement.md      # How BCIs enable cursor/keyboard control
│
├── cerebral-cortex/                    # Outer brain layer (higher functions)
│   ├── motor-cortex/                   # Movement control (BCI primary target)
│   ├── sensory-cortex/                 # Touch, proprioception
│   ├── prefrontal-cortex/              # Executive function, planning
│   ├── visual-cortex/                  # Vision processing
│   ├── auditory-cortex/                # Hearing processing
│   └── parietal-cortex/                # Spatial awareness, integration
│
├── cerebellum/                         # Movement coordination, balance
│
├── brainstem/                          # Vital functions
│   ├── medulla/                        # Heart rate, breathing
│   ├── pons/                           # Sleep, arousal
│   └── midbrain/                       # Eye movement, hearing
│
├── limbic-system/                      # Emotion, memory
│   ├── amygdala/                       # Fear, emotion processing
│   ├── hippocampus/                    # Memory formation
│   └── cingulate-cortex/               # Decision-making, emotion
│
├── thalamus/                           # Sensory relay station
├── hypothalamus/                       # Hormones, homeostasis
├── basal-ganglia/                      # Movement initiation, habits
├── corpus-callosum/                    # Hemispheric communication
└── neural-pathways/                    # Major fiber tracts
```

---

## Purpose of Each Folder

Each brain region folder is for documenting:

1. **How it works** — Function, anatomy, connections
2. **Research notes** — Papers, findings, key facts
3. **Questions** — Things to ask researchers/professionals
4. **Unknowns** — What science hasn't figured out yet
5. **BCI relevance** — How this region relates to brain-computer interfaces
6. **Security implications** — Potential vulnerabilities, attack surfaces

---

## Research Documents

| Document | Description |
|----------|-------------|
| [Research-BCI_Mouse_Movement.md](./Research-BCI_Mouse_Movement.md) | Deep dive on how BCIs decode motor cortex signals for cursor control |

---

## Key Questions This Research Aims to Answer

1. Where exactly do BCI electrodes sit in the brain?
2. How deep do they go?
3. What signals do they record?
4. How are those signals decoded into actions?
5. What are the current technological limitations?
6. What questions remain unanswered in the field?

---

## Related Projects

- **Backlog:** [bci-to-neuron-zoom-rendering](../docs/visualizations/pending/bci-to-neuron-zoom-rendering/) — Blender animation from brain → neurons → molecules
- **Video Assets:** `video/bci-zoom/` — Visualization project files
- **ONI_LAYERS.md:** Biological Foundation section — How this maps to L8-L14
- **oni/neuromapping.py:** Python API for brain region → layer mappings

---

## Adding Research

When adding research to a brain region folder:

1. Create a file named `Notes-[Topic].md` for informal notes
2. Create `Research-[Topic].md` for structured research
3. Include sources with links
4. Tag questions with `[Q]` prefix
5. Tag unknowns with `[?]` prefix

Example:
```markdown
## Motor Cortex Notes

[Q] Why do some neurons respond to imagined movement but not actual movement?

[?] Unknown: The exact mechanism by which motor cortex neurons "know" whether movement is intended vs executed.

Source: Smith et al. (2023) - https://example.com/paper
```

---

*Last Updated: 2026-01-26*
