"""
Application configuration.
"""

from dataclasses import dataclass
import os
import torch


@dataclass(frozen=True)
class Settings:
    # Model
    MODEL_ID = os.getenv(
        "MODEL_ID",
        "black-forest-labs/FLUX.2-klein-4B"
    )

    # Automatically detect GPU
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

    # Data type
    DTYPE = (
        torch.bfloat16
        if DEVICE == "cuda"
        else torch.float32
    )

    # Image defaults
    DEFAULT_HEIGHT = int(os.getenv("DEFAULT_HEIGHT", "1024"))
    DEFAULT_WIDTH = int(os.getenv("DEFAULT_WIDTH", "1024"))

    DEFAULT_STEPS = int(os.getenv("DEFAULT_STEPS", "4"))
    DEFAULT_GUIDANCE = float(os.getenv("DEFAULT_GUIDANCE", "1.0"))

    # Cache
    CACHE_DIR = os.getenv(
        "CACHE_DIR",
        "/runpod-volume/huggingface"
    )


CONFIG = Settings()