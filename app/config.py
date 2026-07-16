"""
ezy-image-worker
Global immutable configuration.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class WorkerConfig:
    """
    Global configuration for the ezy-image-worker.
    """

    # ---------------------------------------------------------
    # Worker
    # ---------------------------------------------------------
    worker_name: str = "ezy-image-worker"

    # ---------------------------------------------------------
    # AI Provider
    # ---------------------------------------------------------
    provider: str = "black-forest-labs"

    # Hugging Face repository
    model_id: str = "black-forest-labs/FLUX.2-klein-4B"

    # ---------------------------------------------------------
    # Image Generation Defaults
    # ---------------------------------------------------------
    image_width: int = 1024
    image_height: int = 1024

    num_inference_steps: int = 4
    guidance_scale: float = 1.0

    jpeg_quality: int = 90

    default_seed = None

    # ---------------------------------------------------------
    # Hugging Face Cache
    # ---------------------------------------------------------
    hf_cache: str = "/runpod-volume/huggingface"

    # ---------------------------------------------------------
    # Logging
    # ---------------------------------------------------------
    log_level: str = "INFO"

    # ---------------------------------------------------------
    # Local folders
    # ---------------------------------------------------------
    output_directory: Path = Path("outputs")
    log_directory: Path = Path("logs")


CONFIG = WorkerConfig()