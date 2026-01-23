# Claude AI Instructions for TARA

> **TARA**: Telemetry Awareness and Response Analyzer
> Neural Security Platform for Brain-Computer Interfaces

This file provides instructions for Claude to follow when updating, maintaining, or extending TARA. Read this file at the start of any session involving TARA development.

---

## Quick Reference

| Resource | Location | Purpose |
|----------|----------|---------|
| **Main README** | `README.md` | Public documentation, installation, API reference |
| **AGENTS.md** | `AGENTS.md` | Learnings from previous sessions |
| **pyproject.toml** | `pyproject.toml` | Package configuration and dependencies |
| **Main App** | `ui/app.py` | Streamlit dashboard entry point |
| **CLI** | `cli.py` | Command-line interface |
| **Core** | `core/` | ONI Framework security primitives |
| **This File** | `CLAUDE.md` | Claude-specific instructions |

---

## Module Architecture

```
tara/
├── CLAUDE.md              # Claude AI instructions (this file)
├── AGENTS.md              # Learnings from previous sessions
├── README.md              # Public documentation
├── pyproject.toml         # Package configuration
├── __init__.py            # Package entry point
├── cli.py                 # Command-line interface
│
├── core/                  # ONI Framework security primitives
│   ├── coherence.py       # Cₛ (Coherence Score) calculation
│   ├── layers.py          # 14-layer ONI model (L1-L14)
│   ├── firewall.py        # Neural firewall decision matrix
│   └── scale_freq.py      # Scale-frequency invariant (f × S ≈ k)
│
├── simulation/            # Neural network simulation
│   ├── neurons/           # LIF, Izhikevich, Hodgkin-Huxley, Adaptive LIF
│   ├── synapses/          # Chemical, Electrical, STDP
│   ├── networks/          # Layered, Recurrent, Small-World
│   └── engine/            # Simulation execution engine
│
├── attacks/               # Attack simulation & testing
│   ├── patterns.py        # Attack pattern definitions
│   ├── generator.py       # Signal generation
│   ├── scenarios.py       # Multi-stage attack scenarios
│   └── simulator.py       # Attack execution engine
│
├── siem/                  # Neural Signal Assurance Monitoring (NSAM)
│   ├── events.py          # Event storage
│   ├── rules.py           # Detection rules engine
│   ├── detector.py        # Anomaly detection
│   ├── alerts.py          # Alert management
│   └── monitor.py         # Real-time monitoring service
│
├── data/                  # Data models
│   ├── brain_regions.py   # Brain region definitions (10 regions)
│   ├── bci_nodes.py       # BCI node network models
│   └── export/            # Export functionality (placeholder)
│
├── visualization/         # Real-time visualization
│   ├── components/
│   │   ├── brain_topology.py      # 3D brain visualization
│   │   └── firewall_pipeline.py   # ONI L8-L14 pipeline visualization
│   ├── embeds/
│   │   └── html_bridge.py         # ONI-visualizations embedding
│   └── themes/
│       └── oni_theme.py           # ONI color scheme
│
├── ui/                    # Streamlit web interface
│   ├── app.py             # Main dashboard (all pages)
│   ├── widgets/           # Reusable UI components
│   └── pages/             # Page components (if split)
│
├── persistence/           # Data storage (SQLite, placeholder)
│
└── tests/                 # Unit tests
```

---

## ONI Framework Alignment

### 14-Layer Model

TARA is fully aligned with the ONI 14-layer model:

```
BIOLOGICAL DOMAIN (L1-L7):
  L1:  Molecular         - Ion channels, neurotransmitters
  L2:  Cellular          - Action potentials, synaptic transmission
  L3:  Microcircuit      - Local neural computation
  L4:  Regional          - Brain region specialization
  L5:  Systems           - Distributed network integration
  L6:  Whole-Brain       - Global coordination, consciousness
  L7:  Behavioral        - Motor output, observable behavior

BRIDGE (L8):
  L8:  Neural Gateway    - FIREWALL LOCATION (bio-digital boundary)

SILICON DOMAIN (L9-L14):
  L9:  Signal Processing - ADC, filtering, amplification
  L10: Protocol          - Data formatting, transmission rules
  L11: Transport         - Encryption, reliable delivery
  L12: Session           - Connection management, state tracking
  L13: Presentation      - Data interpretation, motor intention
  L14: Application       - End-user interfaces, identity & ethics
```

### Brain Regions → ONI Layer Mapping

| Region | Full Name | ONI Layer | Domain |
|--------|-----------|-----------|--------|
| M1 | Primary Motor Cortex | L13 | Presentation |
| S1 | Primary Somatosensory | L12 | Session |
| PMC | Premotor Cortex | L13 | Presentation |
| SMA | Supplementary Motor | L13 | Presentation |
| PFC | Prefrontal Cortex | L14 | Application |
| BROCA | Broca's Area | L14 | Application |
| WERNICKE | Wernicke's Area | L14 | Application |
| V1 | Primary Visual | L12 | Session |
| A1 | Primary Auditory | L12 | Session |
| HIPP | Hippocampus | L11 | Transport |

### Key Formulas

**Coherence Score:** `Cₛ = Σᵢ wᵢ × Φᵢ(Δtᵢ) × Θᵢ(fᵢ, Aᵢ)`

**Scale-Frequency Invariant:** `f × S ≈ k`

---

## UI Pages Reference

TARA's Streamlit UI has the following pages:

| Page | Nav Section | Purpose |
|------|-------------|---------|
| **Dashboard** | Monitoring | System status, alerts, BCI nodes, real-time metrics |
| **Brain Topology** | Monitoring | 3D brain visualization with electrode monitoring |
| **Neural Firewall** | Monitoring | ONI L8-L14 validation pipeline |
| **Signal Assurance** | Monitoring | Live metrics, alerts management, event logs |
| **Neural Simulator** | Testing | Brain region security analysis with attacks/defenses |
| **Attack Testing** | Testing | Execute attack scenarios and view results |
| **Settings** | Configuration | Thresholds, rules, system parameters |

### Dashboard Structure

```
Dashboard
├── Real-time Signal Monitor (expandable)
│   └── Coherence and Spike Rate charts
├── System Status row
│   ├── Monitor status
│   ├── Active Alerts
│   ├── BCI Nodes (online/total)
│   ├── Network Health
│   └── Firewall Pass Rate
└── Two columns
    ├── Recent Alerts
    └── BCI Node Network (with expandable node details)
```

### Neural Simulator Structure

```
Neural Simulator
├── 3D Brain with region spheres (ONI layer colored)
├── Region selector dropdown
├── ONI Layer Legend
├── Region Details panel
│   ├── Function description
│   ├── ONI layer mapping
│   ├── Neuron types
│   └── Connections
├── Neural Network Visualization (3D neurons)
├── Security Analysis tabs
│   ├── Attack Vectors (per region)
│   └── Defenses (per region)
└── ONI Framework Layer Stack (L5-L14)
```

---

## Update Checklist

When making changes to TARA, ensure:

### Code Changes
- [ ] Update relevant `__init__.py` exports
- [ ] Add/update docstrings
- [ ] Maintain ONI layer alignment
- [ ] Update type hints

### UI Changes
- [ ] Update page routing in `ui/app.py` if adding pages
- [ ] Update sidebar navigation if changing page names
- [ ] Maintain consistent styling with ONI theme
- [ ] Test on localhost:8505

### Documentation Changes
- [ ] Update `README.md` with new features
- [ ] Update architecture diagram if structure changes
- [ ] Update API reference if adding public classes
- [ ] Update CLI reference if adding commands

### Data Model Changes
- [ ] Update `data/brain_regions.py` for new regions
- [ ] Update `data/bci_nodes.py` for node changes
- [ ] Update `REGION_SECURITY_DATA` in `ui/app.py` for Neural Simulator

### Before Committing
- [ ] Update `AGENTS.md` with learnings
- [ ] Run `tara ui` to verify UI works
- [ ] Check for import errors
- [ ] Update version in `__init__.py` and `pyproject.toml` if releasing

---

## Naming Conventions

### Files
- Python modules: `snake_case.py`
- Classes: `PascalCase`
- Functions: `snake_case`
- Constants: `UPPER_SNAKE_CASE`

### UI Elements
- Page titles: Title Case ("Neural Simulator")
- Section headers: Title Case ("System Status")
- Button labels: Title Case ("Run Simulation")
- Metric labels: Title Case ("Active Alerts")

### ONI Alignment
- Always prefix layer references with "L" (L8, L13, etc.)
- Use full layer names in documentation (Neural Gateway, not just Gateway)
- Map brain regions to correct ONI layers per the table above

---

## Common Tasks

### Adding a New Brain Region

1. Add to `data/brain_regions.py`:
```python
"NEW": BrainRegion(
    abbreviation="NEW",
    name="New Region Name",
    center=(x, y, z),  # MNI coordinates
    radius=10,
    oni_layer=12,
    function="region function",
    category=RegionCategory.SENSORY,
    color="#hex",
)
```

2. Add to `REGION_SECURITY_DATA` in `ui/app.py`:
```python
"NEW": {
    "name": "New Region Name",
    "function": "Description of function",
    "oni_layer": 12,
    "oni_name": "Session",
    "neuron_types": [...],
    "connections": [...],
    "attack_vectors": [...],
    "defenses": [...],
}
```

3. Add to `region_positions` in `_create_brain_3d_with_regions()`

### Adding a New Attack Pattern

1. Add to `attacks/patterns.py`
2. Add to `REGION_SECURITY_DATA` attack_vectors in `ui/app.py`
3. Update `README.md` Attack Patterns table

### Adding a New UI Page

1. Create render function: `render_new_page()`
2. Add to `render_sidebar()` navigation
3. Add routing in `main()` function
4. Update UI Pages Reference in this file

---

## Testing

### Manual Testing
```bash
# Launch UI
tara ui --port 8505

# Check each page loads
# Test button interactions
# Verify visualizations render
```

### Unit Tests (when implemented)
```bash
pytest tests/ -v
```

---

## Dependencies

### Core (always installed)
- numpy >= 1.21.0
- scipy >= 1.7.0

### UI (optional)
- streamlit >= 1.28.0
- plotly >= 5.17.0

### Simulation (optional)
- matplotlib >= 3.5.0
- pandas >= 1.4.0

### Full (all features)
- scikit-learn >= 1.0.0

---

## Troubleshooting

### "Module not found" errors
- Check `__init__.py` exports
- Verify PYTHONPATH includes tara parent directory

### UI not loading
- Check Streamlit is installed: `pip install streamlit`
- Kill existing processes: `pkill -f streamlit`
- Restart: `tara ui` or `python -m streamlit run tara/ui/app.py`

### Visualization not rendering
- Check Plotly is installed: `pip install plotly`
- Check browser console for JavaScript errors

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-01 | Initial release with core, simulation, attacks, NSAM |
| 0.2.0 | 2026-01 | Added visualization, brain topology, firewall pipeline |
| 0.3.0 | 2026-01 | Added Neural Simulator with region security analysis |

---

*Version: 1.0*
*Last Updated: 2026-01-22*
*For: Claude AI Assistant*
