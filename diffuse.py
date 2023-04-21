import os
from datetime import datetime

from diffusers import DiffusionPipeline
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

prompt_text = os.getenv(
    "PROMPT", ""
)
negative_prompt_text = os.getenv(
    "NEGATIVE_PROMPT", ""
)

num_images = 4
output_folder = "output"
model_id = "stabilityai/stable-diffusion-2-1"
date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
prompt_folder = f"{output_folder}/{date}"
prompt_info = f'prompt: {prompt_text}\nnegative prompt: {negative_prompt_text}'
prompt = [prompt_text] * num_images
negative_prompt = [negative_prompt_text] * num_images


def image_grid(imgs, rows, cols):
    assert len(imgs) == rows*cols
    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i % cols*w, i//cols*h))
    return grid


pipe = DiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to("mps")
pipe.enable_attention_slicing()

output = pipe(prompt=prompt, negative_prompt=negative_prompt)

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

os.mkdir(prompt_folder)

with open(f'{prompt_folder}/prompt.txt', 'w') as f:
    f.write(prompt_info)

for i in range(len(output.images)):
    output.images[i].save(f"{prompt_folder}/image_{i}.png")

grid = image_grid(output.images, rows=2, cols=2)

grid.save(f"{prompt_folder}/image_grid.png")
