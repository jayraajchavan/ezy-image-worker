"""
ezy-image-worker
Version information for the RunPod Serverless Image Worker.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class WorkerInfo:
    """Static metadata describing this worker."""

    name: str = "ezy-image-worker"
    version: str = "1.0.0"
    description: str = (
        "Generic AI Image Generation Worker for the eZy ecosystem."
    )
    author: str = "Jayraaj Chavan"
    license: str = "Apache-2.0 Compatible Worker"
    default_model: str = "black-forest-labs/FLUX.2-klein-4B"


WORKER_INFO = WorkerInfo()