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

        os.makedirs(CONFIG.CACHE_DIR, exist_ok=True)

        print("Loading FLUX model...")

        token = os.environ.get("HF_TOKEN")

        self._pipe = DiffusionPipeline.from_pretrained(
            CONFIG.MODEL_ID,
            torch_dtype=CONFIG.DTYPE,
            token=token,
            cache_dir=CONFIG.CACHE_DIR,
        )

        if CONFIG.DEVICE == "cuda":
            self._pipe.to("cuda")
        
        print("=" * 60)
        print("Model :", CONFIG.MODEL_ID)
        print("Device:", CONFIG.DEVICE)
        print("DType :", CONFIG.DTYPE)
        print("Cache :", CONFIG.CACHE_DIR)
        print("=" * 60)
        print("FLUX model loaded.")

    def unload(self):

        self._pipe = None

    def pipeline(self):

        if not self.loaded:
            self.load()

        return self._pipe