# ============================================================
# FLUX.2 Klein 4B Configuration
# ============================================================

MODEL_ID = "black-forest-labs/FLUX.2-klein-4B"

# Hugging Face cache location on RunPod Network Volume
HF_CACHE = "/runpod-volume/huggingface"

# Default image size
IMAGE_WIDTH = 1024
IMAGE_HEIGHT = 1024

# Official FLUX.2 Klein defaults
DEFAULT_STEPS = 4
DEFAULT_GUIDANCE = 1.0

# Output
JPEG_QUALITY = 90

# Default seed (None = random)
DEFAULT_SEED = None