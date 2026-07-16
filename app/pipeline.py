"""
Pipeline Manager

This class manages the lifecycle of the image generation model.
The actual model will be connected in Milestone 2.
"""

from __future__ import annotations

from typing import Optional


class PipelineManager:
    """
    Singleton Pipeline Manager.
    """

    _instance: Optional["PipelineManager"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._loaded = False
            cls._instance._model = None

        return cls._instance

    @property
    def loaded(self) -> bool:
        return self._loaded

    def load(self) -> None:
        """
        Placeholder.
        FLUX model loading will be implemented later.
        """
        self._loaded = True

    def unload(self) -> None:
        self._loaded = False
        self._model = None

    def get_model(self):
        return self._model


pipeline = PipelineManager()