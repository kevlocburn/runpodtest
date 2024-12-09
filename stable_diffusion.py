import torch
from diffusers import StableDiffusionPipeline

class TextToImageGenerator:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipeline = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
        ).to(self.device)

    def generate_image(self, prompt):
        image = self.pipeline(prompt).images[0]
        output_path = "./generated_image.png"
        image.save(output_path)
        return output_path
    