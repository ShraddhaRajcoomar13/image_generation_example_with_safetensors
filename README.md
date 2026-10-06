# image_generation_example_with_safetensors
A simple CPU-based Stable Diffusion script that loads a local .safetensors model via from_single_file, generates a 512×512 image from a text prompt using 20 inference steps and CFG 7.5, and saves it as a PNG. The safety checker is disabled for lower memory usage. Requires torch, diffusers, and transformers.
