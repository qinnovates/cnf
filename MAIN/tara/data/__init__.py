"""
TARA Data Models

Data definitions for brain regions, electrode templates,
BCI nodes, and export functionality.
"""

from .brain_regions import (
    BrainRegion,
    BRAIN_REGIONS,
    Electrode,
    ElectrodeThread,
    ElectrodeArray,
    ElectrodeStatus,
    get_region_by_oni_layer,
    create_demo_array,
)

from .bci_nodes import (
    BCINode,
    BCINodeNetwork,
    NodeConnection,
    NodeMetrics,
    NodeStatus,
    ConnectionStatus,
    create_demo_network,
)

__all__ = [
    # Brain regions
    "BrainRegion",
    "BRAIN_REGIONS",
    "Electrode",
    "ElectrodeThread",
    "ElectrodeArray",
    "ElectrodeStatus",
    "get_region_by_oni_layer",
    "create_demo_array",
    # BCI Nodes
    "BCINode",
    "BCINodeNetwork",
    "NodeConnection",
    "NodeMetrics",
    "NodeStatus",
    "ConnectionStatus",
    "create_demo_network",
]
