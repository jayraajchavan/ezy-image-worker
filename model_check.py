import torch

from diffusers import DiffusionPipeline

print("=" * 60)
print("Loading FLUX.2 Klein")
print("=" * 60)

pipe = DiffusionPipeline.from_pretrained(
    "black-forest-labs/FLUX.2-klein-4B",
    torch_dtype=torch.bfloat16,
)

print()
print("SUCCESS")
print(type(pipe))