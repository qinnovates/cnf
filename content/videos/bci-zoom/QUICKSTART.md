# BCI Zoom Animation - Quick Start Guide

## Assets Downloaded ✓

```
assets/
├── brain/Brain/Brain.blend          ✓ Macro brain model
├── neurons/pyramidal_cnic_001.swc   ✓ Pyramidal neuron morphology
├── receptors/
│   ├── dopamine_D2_receptor_6CM4.pdb  ✓ D2 receptor structure
│   └── sodium_channel_7W9K.pdb        ✓ Ion channel
└── molecules/
    ├── dopamine_CID681.sdf            ✓ Dopamine
    ├── glutamate_CID33032.sdf         ✓ Glutamate
    └── GABA_CID119.sdf                ✓ GABA
```

---

## Step 1: Install Molecular Nodes Addon

This is **required** for importing PDB/SDF molecular files.

1. Download: https://github.com/BradyAJohnston/MolecularNodes/releases
2. In Blender: **Edit > Preferences > Add-ons**
3. Click **Install...** and select the downloaded `.zip`
4. Enable **"Molecular Nodes"** checkbox
5. Restart Blender

---

## Step 2: Set Up Scene Structure

Open Blender and run the setup script:

1. Open **Brain.blend**: `assets/brain/Brain/Blend file (main)/Brain.blend`
2. Go to **Scripting** workspace (top tabs)
3. Click **Open** and select: `blender/setup_bci_zoom.py`
4. Press **Alt+P** to run

This creates:
- Collection structure for each scale
- Camera with zoom animation keyframes
- Placeholder objects (replace with real assets)
- Lighting setup

---

## Step 3: Import Real Assets

### A. Brain (already open)
The brain model is your starting point. It has:
- External cortex (Brain1.obj)
- Internal structures (Brain2.obj, Brain3.obj)

### B. Import Neuron (SWC file)

**Option 1: Online Converter (easiest)**
1. Go to: https://neuroinformatics.nl/swc2obj/
2. Upload: `assets/neurons/pyramidal_cnic_001.swc`
3. Download the `.obj` file
4. In Blender: **File > Import > Wavefront (.obj)**

**Option 2: NeuroMorphoVis Addon**
1. Install: https://github.com/BlueBrain/NeuroMorphoVis
2. **File > Import > SWC Morphology**

### C. Import Receptor (PDB file)

With Molecular Nodes installed:

1. Press **N** to open sidebar
2. Find **Molecular Nodes** tab
3. Click **PDB** import
4. Navigate to: `assets/receptors/dopamine_D2_receptor_6CM4.pdb`
5. Style: Set to **Surface** representation

Or fetch directly:
1. Molecular Nodes > **Fetch from PDB**
2. Enter: `6CM4`

### D. Import Dopamine (SDF file)

1. Molecular Nodes > **Import** > **SDF**
2. Select: `assets/molecules/dopamine_CID681.sdf`
3. Style: **Ball and Stick** representation

---

## Step 4: Scale and Position Assets

Each asset needs to be at the correct scale relative to camera zoom:

| Asset | Real Size | Blender Scale | Position (Y) |
|-------|-----------|---------------|--------------|
| Brain | 15 cm | 0.15 | 0 |
| Neuron | 50 μm | 0.00005 | 0 |
| Synapse | 1 μm | 0.000001 | 0 |
| Receptor | 10 nm | 0.00000001 | 0 |
| Dopamine | 1 nm | 0.000000001 | 0 |

**Important:** All assets should be centered at origin (0, 0, 0). The camera moves toward them.

---

## Step 5: Create Transitions

The key to seamless zoom is **transition effects** between scales:

### Transition 1: Brain → Neuron (Frame 150-200)

```
1. Select Brain object
2. Add keyframe at frame 150: fully visible
3. Add keyframe at frame 200: material opacity = 0
4. Simultaneously fade IN the neuron
```

### Transition 2: Neuron → Synapse (Frame 600-650)

Same fade technique, plus:
- Add particle effect (neural sparks)
- Brief blur/glow during transition

### Transition 3: L8 Gateway Moment (Frame 900)

This is the **climax** - where silicon meets biology:

```
1. Create orange emission plane at origin
2. Keyframe emission: 0 at frame 890, peak at 900, 0 at 910
3. Add text overlay: "L8 — Neural Gateway"
4. Flash the GatewayLight_L8 object
```

### Transition 4: Synapse → Molecular (Frame 900-1000)

- Zoom into synaptic cleft
- Fade in receptor protein
- Fade in dopamine molecule approaching

---

## Step 6: Camera Animation

The setup script creates keyframes, but you may want to adjust:

1. Select **ZoomCamera**
2. Open **Graph Editor**
3. See the Y-location curve (logarithmic zoom)
4. Adjust timing by moving keyframes

**Keyframe Timeline:**
```
Frame    1: Full brain view (0.5m away)
Frame  150: Zoom to brain region
Frame  300: Enter cortex
Frame  450: Cortical column visible
Frame  600: Neural network
Frame  750: Single neuron fills frame
Frame  900: ★ L8 GATEWAY - Synapse ★
Frame 1050: Synaptic cleft
Frame 1200: Receptor protein
Frame 1350: Dopamine binding (END)
```

---

## Step 7: Render Settings

For test renders:
```
Resolution: 1280 x 720
Samples: 64
Output: renders/test/
```

For final:
```
Resolution: 1920 x 1080 (or 4K)
Samples: 256+
Denoising: ON
Output: renders/final/
Format: PNG sequence (then compile to video)
```

---

## Step 8: Add Post-Production Elements

After rendering, add in video editor (DaVinci/Premiere/After Effects):

1. **Scale bar** - Updates at each zoom level
2. **ONI layer labels** - Fade in with color coding:
   - L14 Identity `#4ade80`
   - L13 Semantic `#22c55e`
   - L12 Session `#16a34a`
   - L11 Transport `#15803d`
   - L10 Protocol `#166534`
   - L9 Processing `#14532d`
   - **L8 Gateway `#d97706`** (ORANGE FLASH!)
3. **Audio** - Ambient tones, whoosh transitions, electrical crackles

---

## Troubleshooting

**"Molecular Nodes not showing"**
- Restart Blender after installing addon
- Check it's enabled in Preferences > Add-ons

**"PDB import fails"**
- Try fetching by ID instead: `6CM4`
- Check internet connection

**"SWC file won't import"**
- Use online converter: https://neuroinformatics.nl/swc2obj/
- Import resulting OBJ file instead

**"Objects disappear at small scales"**
- Blender has clipping issues at tiny scales
- Camera > Clip Start: set to 0.0000001
- Camera > Clip End: set to 1000

**"Animation is jerky"**
- In Graph Editor, select all keyframes
- Key > Interpolation Mode > Bezier
- Smooth the curves

---

## File Organization

After setup, your project should look like:

```
bci-zoom/
├── QUICKSTART.md (this file)
├── README.md
├── blender/
│   ├── setup_bci_zoom.py
│   └── bci-zoom-main.blend (save your work here)
├── assets/
│   ├── brain/Brain/
│   ├── neurons/
│   ├── receptors/
│   └── molecules/
├── renders/
│   ├── test/
│   └── final/
└── reference/
    └── oni-layers-mapping.md
```

---

## Quick Commands Reference

| Action | Shortcut |
|--------|----------|
| Run script | Alt+P |
| Play animation | Space |
| Go to frame | Shift+Left/Right |
| Set keyframe | I |
| Open Graph Editor | Shift+F6 |
| Render frame | F12 |
| Render animation | Ctrl+F12 |
| Toggle sidebar | N |

---

Good luck with the animation! The L8 Gateway moment is the narrative climax - make it dramatic.
