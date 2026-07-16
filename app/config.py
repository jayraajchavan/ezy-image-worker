"""
Application configuration.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    MODEL_ID = "black-forest-labs/FLUX.2-klein-4B"

    DEVICE = "cuda"

    DTYPE = "bfloat16"

    DEFAULT_HEIGHT = 1024
    DEFAULT_WIDTH = 1024

    DEFAULT_STEPS = 4

    DEFAULT_GUIDANCE = 1.0

    CACHE_DIR = "/runpod-volume/huggingface"


CONFIG = Settings()