"""
Development handler.

RunPod integration will be added later.
"""

from app.health import get_health


def handle_request(payload: dict) -> dict:

    mode = payload.get("mode", "health")

    if mode == "health":
        return get_health()

    return {
        "status": "error",
        "message": f"Unsupported mode: {mode}"
    }