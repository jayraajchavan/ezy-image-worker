"""
Health endpoint.
"""

from app.pipeline import pipeline
from app.version import WORKER_INFO


def get_health() -> dict:

    return {
        "status": "ready",
        "worker": WORKER_INFO.name,
        "version": WORKER_INFO.version,
        "model": WORKER_INFO.default_model,
        "loaded": pipeline.loaded
    }