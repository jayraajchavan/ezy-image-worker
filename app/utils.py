"""
Common utility functions for ezy-image-worker.
"""

from __future__ import annotations

import base64
import io
import logging
import time
import uuid
from datetime import datetime
from typing import Any

import torch
from PIL import Image


# ==========================================================
# Logging
# ==========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("ezy-image-worker")


# ==========================================================
# Request ID
# ==========================================================

def generate_request_id() -> str:
    """
    Generate a unique request ID.

    Example:
        20260716-145510-A3F91B
    """

    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    short_uuid = uuid.uuid4().hex[:6].upper()

    return f"{timestamp}-{short_uuid}"


# ==========================================================
# Timer
# ==========================================================

class Timer:

    def __init__(self):

        self.start_time = time.perf_counter()

    @property
    def elapsed(self) -> float:

        return round(time.perf_counter() - self.start_time, 3)


# ==========================================================
# GPU
# ==========================================================

def get_gpu_name() -> str:

    if not torch.cuda.is_available():
        return "CPU"

    return torch.cuda.get_device_name(0)


def get_gpu_memory_mb() -> int:

    if not torch.cuda.is_available():
        return 0

    props = torch.cuda.get_device_properties(0)

    return int(props.total_memory / 1024 / 1024)


# ==========================================================
# Image
# ==========================================================

def image_to_base64(
    image: Image.Image,
    quality: int = 90
) -> str:
    """
    Convert PIL image to Base64 JPEG.
    """

    buffer = io.BytesIO()

    image.save(
        buffer,
        format="JPEG",
        quality=quality,
        optimize=True
    )

    return base64.b64encode(
        buffer.getvalue()
    ).decode("utf-8")


# ==========================================================
# JSON Logging
# ==========================================================

def log_dict(title: str, data: dict[str, Any]) -> None:

    logger.info("========== %s ==========", title)

    for key, value in data.items():

        logger.info("%-22s : %s", key, value)

    logger.info("=" * 40)