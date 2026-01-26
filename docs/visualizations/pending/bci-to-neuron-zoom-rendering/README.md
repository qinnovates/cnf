# BCI-to-Neuron Zoom Rendering

> **Status:** Backlogged
> **Type:** 3D Visualization / Animation
> **Goal:** Create a cinematic zoom from BCI device → electrode → neuron → synapse → molecular level

---

## Concept

A visual journey that starts at the BCI hardware level and zooms progressively deeper into the biological substrate, illustrating the L8 Neural Gateway boundary and what lies beneath it.

**Zoom Levels:**
1. BCI Device (external)
2. Electrode array / Neural threads
3. Cortical surface
4. Neuron cell bodies
5. Synaptic terminals
6. Molecular level (neurotransmitters, receptors)

---

## Related Resources

### 3D Brain Models

- **brain2print:** AI tool to convert MRI → 3D brain models
  - Paper: https://www.nature.com/articles/s41598-025-00014-5
  - Demo: https://brain2print.org
  - GitHub: https://github.com/niivue/brain2print

- **Free Brain STL:** https://www.cgtrader.com/free-3d-models/character/human-anatomy/brain-59cffe18-e669-4dae-a588-1f82cee6fd45

### Molecular Rendering

- **Molecular Nodes (Blender):** For rendering neurotransmitters and receptors
  - Dopamine D2 receptor PDB: 6CM4
  - Can fetch structures from RCSB Protein Data Bank
  - GitHub: https://github.com/BradyAJohnston/MolecularNodes

### Brain Region Research

- **[Research-BCI_Mouse_Movement.md](../../../../neuroscience-homework-todo/Research-BCI_Mouse_Movement.md)** — Deep dive on electrode placement, neural decoding, BCI specifications
- **[Neuroscience & BCI Research](../../../../neuroscience-homework-todo/)** — Folder structure for brain region documentation
- ONI_LAYERS.md biological foundation section for molecular cascade details

---

## Technical Approach

### Option A: Blender + Molecular Nodes
- Full 3D rendering
- High quality but time-intensive
- Best for final production

### Option B: After Effects / Motion Graphics
- 2.5D approach
- Faster iteration
- Good for concept validation

### Option C: Remotion (Programmatic)
- Code-driven animation
- Version controlled
- Matches existing ONI video pipeline

---

## Files

| File | Purpose |
|------|---------|
| `README.md` | This file |
| *(pending)* | Assets and source files when work resumes |

---

## References

- ONI_LAYERS.md: Biological Foundation section
- ONI_LAYERS.md: Time-Scale Hierarchy (femtoseconds → lifetime)
- Molecular substrate diagram in ONI_LAYERS.md

---

*Last Updated: 2026-01-26*
