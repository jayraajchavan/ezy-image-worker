"""
FLUX.2 Model Manager
"""

from __future__ import annotations

import os
import torch

from diffusers import DiffusionPipeline

from app.config import CONFIG


class FluxModel:
    """
    Singleton FLUX model.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._pipe = None

        return cls._instance

    @property
    def loaded(self):
        return self._pipe is not None

    def load(self):

        if self.loaded:
            return

        print("Loading FLUX model...")

        token = os.environ.get("HF_TOKEN")

        self._pipe = DiffusionPipeline.from_pretrained(
            CONFIG.MODEL_ID,
            torch_dtype=torch.bfloat16,
            token=token,
            cache_dir=CONFIG.CACHE_DIR,
        )

        self._pipe.to(CONFIG.DEVICE)

        print("FLUX model loaded.")

    def unload(self):

        self._pipe = None

    def pipeline(self):

        if not self.loaded:
            self.load()

        return self._pipe