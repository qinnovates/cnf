"""
QIF Band Definitions — Single source of truth for the v4.0 Hourglass Model.

Source: qinnovates/mindloft/drafts/ai-working/qif-lab/src/config.py

Architecture: 11 bands in 3 zones (7-1-3 asymmetric hourglass).
Numbers increase AWAY from the interface in both directions.
"""

from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


class Zone(Enum):
    """Three zones of the QIF hourglass model."""
    NEURAL = auto()     # N7-N1: biological processing
    INTERFACE = auto()  # I0: electrode-tissue boundary
    SILICON = auto()    # S1-S3: classical digital processing


@dataclass(frozen=True)
class Band:
    """A single band in the QIF hourglass model."""
    id: str
    name: str
    zone: Zone
    description: str
    brain_regions: Tuple[str, ...]
    dominant_freq_hz: str
    L_m: Optional[Tuple[Optional[float], Optional[float]]]
    determinacy: str
    severity: str
    severity_description: str
    qi_range: Tuple[float, float]
    hourglass_width: float
    bci_devices: Tuple[str, ...]


# ── BAND DEFINITIONS (from config.py) ──

BANDS: List[Band] = [
    # ── NEURAL DOMAIN (7 bands, N7 outermost → N1 closest to periphery) ──
    Band(
        id="N7", name="Neocortex", zone=Zone.NEURAL,
        description="PFC, M1, S1, V1, A1, Broca, Wernicke, association cortex — executive function, language, movement, perception",
        brain_regions=("PFC", "ACC", "Broca", "Wernicke", "M1", "S1_cortex", "V1", "A1", "PMC", "SMA", "PPC"),
        dominant_freq_hz="13-100 (Beta 13-30, Gamma 30-100)",
        L_m=(0.04, 0.3),
        determinacy="Quantum Uncertain",
        severity="High",
        severity_description="Cognitive impairment, motor paralysis, sensory loss, language disruption",
        qi_range=(0.3, 0.5),
        hourglass_width=1.0,
        bci_devices=("Neuralink N1", "Blackrock Utah Array", "Precision Layer 7", "ECoG grids", "cortical DBS"),
    ),
    Band(
        id="N6", name="Limbic System", zone=Zone.NEURAL,
        description="Hippocampus, amygdala, insula, ACC, cingulate — emotion, memory, interoception",
        brain_regions=("HIPP", "BLA", "insula", "ACC", "CeA", "cingulate"),
        dominant_freq_hz="4-13 (Theta 4-8, Alpha 8-13)",
        L_m=(0.3, 1.0),
        determinacy="Chaotic → Quantum Uncertain",
        severity="High",
        severity_description="Memory erasure, emotional dysregulation, PTSD trigger, addiction manipulation",
        qi_range=(0.2, 0.4),
        hourglass_width=0.85,
        bci_devices=("NeuroPace RNS (depth)", "DBS (ANT target)", "depth electrodes"),
    ),
    Band(
        id="N5", name="Basal Ganglia", zone=Zone.NEURAL,
        description="Striatum, GPi/GPe, STN, substantia nigra — motor selection, reward, habit",
        brain_regions=("striatum", "GPi", "GPe", "STN", "substantia_nigra"),
        dominant_freq_hz="13-30 (Beta — pathological oscillations in Parkinson's)",
        L_m=(0.13, 0.3),
        determinacy="Chaotic",
        severity="High",
        severity_description="Movement disorders (Parkinson's, dystonia), reward hijacking, compulsive behavior",
        qi_range=(0.15, 0.35),
        hourglass_width=0.65,
        bci_devices=("Medtronic Percept (STN)", "Abbott Infinity (GPi)", "Boston Scientific Vercise"),
    ),
    Band(
        id="N4", name="Diencephalon", zone=Zone.NEURAL,
        description="Thalamus, hypothalamus — sensory gating, consciousness relay, autonomic regulation",
        brain_regions=("thalamus", "hypothalamus", "VIM", "ANT", "CM-Pf"),
        dominant_freq_hz="4-13 (Alpha spindles, Theta)",
        L_m=(0.3, 1.0),
        determinacy="Stochastic → Chaotic",
        severity="CRITICAL",
        severity_description="Consciousness disruption, sensory blackout, sleep-wake cycle attack, thermal regulation failure",
        qi_range=(0.1, 0.3),
        hourglass_width=0.5,
        bci_devices=("DBS (VIM for tremor)", "thalamic depth electrodes", "ANT stimulation for epilepsy"),
    ),
    Band(
        id="N3", name="Cerebellum", zone=Zone.NEURAL,
        description="Cerebellar cortex, deep nuclei, vermis — motor coordination, timing, learning",
        brain_regions=("cerebellar_cortex", "dentate_nucleus", "fastigial_nucleus", "vermis"),
        dominant_freq_hz="50-100 (Purkinje cell complex spikes)",
        L_m=(0.04, 0.08),
        determinacy="Stochastic",
        severity="High",
        severity_description="Ataxia, coordination loss, speech disruption (dysarthria), motor learning impairment",
        qi_range=(0.1, 0.25),
        hourglass_width=0.45,
        bci_devices=("Experimental cerebellar stimulation",),
    ),
    Band(
        id="N2", name="Brainstem", zone=Zone.NEURAL,
        description="Medulla, pons, midbrain, cranial nerve nuclei — vital functions, arousal, reflexes",
        brain_regions=("medulla", "pons", "midbrain", "reticular_formation", "cranial_nuclei"),
        dominant_freq_hz="0.5-4 (Delta, low-frequency rhythmic)",
        L_m=(1.0, None),
        determinacy="Stochastic",
        severity="LETHAL",
        severity_description="Respiratory arrest, cardiac failure, loss of consciousness, cranial nerve paralysis",
        qi_range=(0.05, 0.15),
        hourglass_width=0.3,
        bci_devices=("Vagus nerve stimulators", "auditory brainstem implants", "DBS (PPN for gait)"),
    ),
    Band(
        id="N1", name="Spinal Cord", zone=Zone.NEURAL,
        description="Cervical, thoracic, lumbar, sacral, cauda equina — reflexes, peripheral motor/sensory relay",
        brain_regions=("cervical_cord", "thoracic_cord", "lumbar_cord", "sacral_cord", "cauda_equina"),
        dominant_freq_hz="Reflex arcs (ms-scale, not oscillatory)",
        L_m=None,
        determinacy="Stochastic",
        severity="Severe",
        severity_description="Paralysis (quadri/para), bladder/bowel dysfunction, chronic pain, autonomic dysreflexia",
        qi_range=(0.02, 0.1),
        hourglass_width=0.25,
        bci_devices=("Spinal cord stimulators (SCS)", "InterStim (sacral)", "epidural stimulation", "ONWARD ARC-IM"),
    ),
    # ── INTERFACE ZONE ──
    Band(
        id="I0", name="Neural Interface", zone=Zone.INTERFACE,
        description="Electrode-tissue boundary, measurement/collapse, quasi-quantum zone",
        brain_regions=(),
        dominant_freq_hz="N/A (boundary, not oscillatory)",
        L_m=None,
        determinacy="Quasi-quantum (ΓD ∈ (0,1))",
        severity="Depends on adjacent N band",
        severity_description="Interface degradation, impedance failure, tissue damage, signal corruption",
        qi_range=(0.01, 0.1),
        hourglass_width=0.2,
        bci_devices=("All implanted/semi-invasive BCIs",),
    ),
    # ── SILICON DOMAIN (3 bands, S1 closest to I0 → S3 outermost) ──
    Band(
        id="S1", name="Analog / Near-Field", zone=Zone.SILICON,
        description="Amplification, filtering, ADC/DAC, near-field EM (0 Hz - 10 kHz)",
        brain_regions=(),
        dominant_freq_hz="0-10,000 (analog front-end passband)",
        L_m=(3e4, None),
        determinacy="Stochastic (analog noise)",
        severity="N/A (silicon)",
        severity_description="Signal corruption, ADC saturation, impedance artifact",
        qi_range=(0.001, 0.01),
        hourglass_width=0.35,
        bci_devices=("All BCIs (analog front-end is universal)",),
    ),
    Band(
        id="S2", name="Digital / Telemetry", zone=Zone.SILICON,
        description="Decoding, classification, telemetry, MICS (10 kHz - 1 GHz)",
        brain_regions=(),
        dominant_freq_hz="10,000-1,000,000,000 (digital processing + telemetry)",
        L_m=(0.3, 3e4),
        determinacy="Deterministic",
        severity="N/A (silicon)",
        severity_description="Data corruption, BLE exploit, MICS intermodulation, firmware compromise",
        qi_range=(0.0, 0.0),
        hourglass_width=0.7,
        bci_devices=("All wireless BCIs (BLE, WiFi, MICS)",),
    ),
    Band(
        id="S3", name="Radio / Wireless / DE", zone=Zone.SILICON,
        description="RF, wireless links, directed energy, application layer (1 GHz+)",
        brain_regions=(),
        dominant_freq_hz="1,000,000,000+ (GHz+ RF and beyond)",
        L_m=(3e-5, 0.3),
        determinacy="Deterministic",
        severity="N/A (silicon)",
        severity_description="RF hijack, directed energy, cloud compromise, supply chain attack",
        qi_range=(0.0, 0.0),
        hourglass_width=1.0,
        bci_devices=("BLE/WiFi consumer, satellite links, DE weapons",),
    ),
]

# Quick lookup
BANDS_BY_ID = {b.id: b for b in BANDS}
