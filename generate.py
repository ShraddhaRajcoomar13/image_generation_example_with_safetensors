import torch
from diffusers import StableDiffusionPipeline

MODEL_FILE = r"C:/Users/Shraddha/Downloads/stuff/stuff.safetensors"

pipe = StableDiffusionPipeline.from_single_file(
    MODEL_FILE,
    torch_dtype=torch.float32,
    safety_checker=None
)

pipe = pipe.to("cpu")

prompt = """
a pretty woman

"""

image = pipe(
    prompt,
    num_inference_steps=20,
    guidance_scale=7.5,
    height=512,
    width=512
).images[0]

image.save(
    r"C:/Users/Shraddha/Downloads/stuff/gend/generated.png"
)

print("Image saved!")

