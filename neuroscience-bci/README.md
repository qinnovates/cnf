# Brain Anatomy Research

> **Purpose:** Document research, questions, and learnings about brain structure and function as it relates to BCI interfaces and neurosecurity.

---

## Folder Structure

```
brain-anatomy/
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

- **Backlog:** [bci-macro-to-micro-visualization](../../project/KANBAN.md) — Blender animation from brain → neurons → molecules
- **Video Assets:** `oni/video/bci-zoom/` — Visualization project files

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
