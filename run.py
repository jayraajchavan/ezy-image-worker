"""
Local development launcher.
"""

import json

from app.handler import handle_request


if __name__ == "__main__":

    response = handle_request({
        "mode": "health"
    })

    print(
        json.dumps(
            response,
            indent=4
        )
    )