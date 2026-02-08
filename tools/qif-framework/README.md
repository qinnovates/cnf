# QIF Framework

**Quantum Indeterministic Framework for Neural Security — v4.0 Hourglass Model**

The QIF framework provides the 11-band hourglass architecture (7-1-3) for brain-computer interface security, along with signal validation tools (coherence metric, scale-frequency invariant, neural firewall).

## Quick Start

```python
from qif import QIFModel

model = QIFModel()
print(model.version)       # '4.0'
print(len(model.bands))    # 11
print(model.band("N7").name)  # 'Neocortex'
print(model.ascii_diagram())
```

## Architecture

```
  NEURAL DOMAIN (7 bands)
  N7  Neocortex           ████████████████████
  N6  Limbic System        █████████████████
  N5  Basal Ganglia         █████████████
  N4  Diencephalon           ██████████
  N3  Cerebellum              █████████
  N2  Brainstem                ██████
  N1  Spinal Cord               █████
  INTERFACE
  I0  Neural Interface           ████     <- waist
  SILICON DOMAIN (3 bands)
  S1  Analog / Near-Field       ███████
  S2  Digital / Telemetry     ██████████████
  S3  Radio / Wireless / DE ████████████████████
```

## Signal Validation

```python
from qif import CoherenceMetric, NeuralFirewall, Signal

# Coherence score
metric = CoherenceMetric(reference_freq=40.0)
cs = metric.calculate([0.0, 0.025, 0.050], [100, 98, 102])

# Firewall
fw = NeuralFirewall()
result = fw.filter(Signal([0.0, 0.025, 0.050], [100, 98, 102], authenticated=True))
print(result.decision.name)  # ACCEPT / ACCEPT_FLAG / REJECT
```

## Predecessor

This package replaces the legacy ONI Framework (14-layer model). See `archived/oni-framework/` for the previous version.
