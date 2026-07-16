"""
RunPod Entry Point
"""

import runpod

from app.flux_model import FluxModel

model = FluxModel()


def handler(job):

    model.load()

    return {
        "success": True,
        "status": "READY"
    }


runpod.serverless.start(
    {
        "handler": handler
    }
)