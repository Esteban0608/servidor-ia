from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def describir_imagen(image_path: str, etiquetas: list[str]) -> str:
    image = Image.open(image_path)
    inputs = processor(text=etiquetas, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    probs = outputs.logits_per_image.softmax(dim=1)
    top_idx = torch.argmax(probs).item()
    return etiquetas[top_idx]