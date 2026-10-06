# README.md

```markdown
# 🎨 Stable Diffusion Image Generator

A minimal Python script that loads a Stable Diffusion model from a **single `.safetensors` file** and generates an image from a text prompt — running entirely on **CPU**.

---

## 📌 Overview

This project uses Hugging Face's 🤗 [`diffusers`](https://github.com/huggingface/diffusers) library to load a self-contained Stable Diffusion checkpoint (`.safetensors`) and generate images from text prompts. It's designed to be as simple as possible — one script, one model file, one output image.

No need for a full model directory or Hugging Face Hub download — just point it at a local `.safetensors` file.

---

## ✨ Features

- **Single-file model loading** via `StableDiffusionPipeline.from_single_file()`
- **CPU-compatible** — runs on any machine (no GPU required)
- **Safety checker disabled** — reduces memory usage and removes content filtering
- **Configurable inference** — steps, guidance scale, and resolution are easy to tweak
- **Saves output as PNG** to a local folder

---

## 📂 Project Structure

```
.
├── generate.py            # Main script
├── stuff.safetensors      # Stable Diffusion model (not included)
└── gend/
    └── generated.png      # Output image
```

---

## ⚙️ Requirements

- Python 3.9+
- ~8 GB RAM (more if using a larger model)
- A Stable Diffusion `.safetensors` checkpoint file

### Install dependencies

```bash
pip install torch diffusers transformers accelerate safetensors
```

> 💡 For CPU-only PyTorch (smaller download):
> ```bash
> pip install torch --index-url https://download.pytorch.org/whl/cpu
> ```

---

## 🚀 Usage

1. **Download a `.safetensors` model** (e.g., from [Civitai](https://civitai.com/) or [Hugging Face](https://huggingface.co/)) and place it somewhere on your machine.

2. **Edit the paths** in the script:

   ```python
   MODEL_FILE = r"C:/path/to/your/model.safetensors"
   ```

3. **Run the script:**

   ```bash
   python generate.py
   ```

4. The generated image will be saved to the path defined in `image.save(...)`, and you'll see:

   ```
   Image saved!
   ```

---

## 🧠 How It Works

```python
import torch
from diffusers import StableDiffusionPipeline

MODEL_FILE = r"C:/Users/Shraddha/Downloads/stuff/stuff.safetensors"

pipe = StableDiffusionPipeline.from_single_file(
    MODEL_FILE,
    torch_dtype=torch.float32,
    safety_checker=None
)

pipe = pipe.to("cpu")

prompt = "a pretty woman"

image = pipe(
    prompt,
    num_inference_steps=20,
    guidance_scale=7.5,
    height=512,
    width=512
).images[0]

image.save(r"C:/Users/Shraddha/Downloads/stuff/gend/generated.png")

print("Image saved!")
```

### Key parameters

| Parameter             | Value   | Description                                              |
|-----------------------|---------|----------------------------------------------------------|
| `torch_dtype`         | `float32` | CPU-safe precision (use `float16` for GPU)             |
| `safety_checker`      | `None`  | Disabled to save memory and skip NSFW filtering          |
| `num_inference_steps` | `20`    | Fewer steps → faster but lower quality                   |
| `guidance_scale`      | `7.5`   | Standard CFG — higher = closer to prompt                 |
| `height` / `width`    | `512`   | Output resolution (must be divisible by 8)               |

---

## ⚡ Performance Tips

| Change                              | Effect                              |
|-------------------------------------|-------------------------------------|
| `torch.float32` → `torch.float16`   | ~2× faster (GPU only)               |
| `.to("cpu")` → `.to("cuda")`        | Massive speedup if you have a GPU   |
| Reduce `num_inference_steps` to 10  | Faster, lower quality               |
| Reduce resolution to `384×384`      | Faster, smaller image               |

> ⚠️ **CPU-only inference is slow.** Expect **1–5+ minutes** per 512×512 image on a typical laptop.

---

## ⚠️ Notes & Caveats

- **Hardcoded paths** — update `MODEL_FILE` and `image.save(...)` to match your system.
- **`safety_checker=None`** disables content filtering. Use responsibly and in accordance with the model's license.
- **Model file size** — `.safetensors` checkpoints are usually **2–7 GB**. Do **not** commit them to Git (use `.gitignore` or Git LFS).
- **GPU users** — switch to `torch.float16` and `.to("cuda")` for dramatically faster generation.

---

## 📜 License

This script is provided as-is for educational and personal use. The Stable Diffusion model you load is subject to **its own license** — check the source (Civitai / Hugging Face) before commercial use.

---

## 🙏 Acknowledgements

- [Hugging Face Diffusers](https://github.com/huggingface/diffusers)
- [Stability AI](https://stability.ai/) for Stable Diffusion
- [Civitai](https://civitai.com/) for community model hosting
```

---

Want me to also add a **`.gitignore`** snippet, a **`requirements.txt`**, or a **`--prompt` CLI argument version** of the script so users don't have to edit the file every time?
