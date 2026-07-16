import sys

print("=" * 60)
print("ezy-image-worker Runtime Validation")
print("=" * 60)

print(f"Python : {sys.version}")

# ---------------------------------------------------------

try:
    import torch

    print(f"✓ Torch : {torch.__version__}")

except Exception as e:

    print(f"✗ Torch : {e}")

# ---------------------------------------------------------

try:
    import transformers

    print(f"✓ Transformers : {transformers.__version__}")

except Exception as e:

    print(f"✗ Transformers : {e}")

# ---------------------------------------------------------

try:
    import diffusers

    print(f"✓ Diffusers : {diffusers.__version__}")

except Exception as e:

    print(f"✗ Diffusers : {e}")

# ---------------------------------------------------------

try:

    from diffusers import DiffusionPipeline

    print("✓ DiffusionPipeline")

except Exception as e:

    print(f"✗ DiffusionPipeline : {e}")

# ---------------------------------------------------------

try:

    from diffusers import Flux2KleinPipeline

    print("✓ Flux2KleinPipeline")

except Exception as e:

    print(f"✗ Flux2KleinPipeline : {e}")

# ---------------------------------------------------------

print("=" * 60)
print("Runtime Validation Finished")
print("=" * 60)