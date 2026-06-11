import os
import shutil
import torch
from PIL import Image
from transformers import pipeline

WEBSITE_ASSETS_DIR = "/Users/robbyj/Documents/Projects/Client Websites/randolph-shoe-care-website/assets"

LABELS = [
    "a storefront or building exterior", 
    "a pair of dress shoes or formal leather shoes", 
    "a pair of sneakers or athletic shoes",
    "a shoe repair or sole replacement",
    "a shoe polish, cleaning product, or polishing brush"
]

CATEGORY_MAP = {
    "a storefront or building exterior": "storefront",
    "a pair of dress shoes or formal leather shoes": "dress_shoes",
    "a pair of sneakers or athletic shoes": "sneakers",
    "a shoe repair or sole replacement": "shoe_repair",
    "a shoe polish, cleaning product, or polishing brush": "products"
}

device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Using device: {device.upper()}")

print("Loading CLIP model...")
classifier = pipeline("zero-shot-image-classification", 
                      model="openai/clip-vit-base-patch32", 
                      device=device)

images = [f for f in os.listdir(WEBSITE_ASSETS_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
print(f"Found {len(images)} images to classify.")

category_counts = {v: 0 for v in CATEGORY_MAP.values()}

for img_name in images:
    if img_name.startswith(tuple(CATEGORY_MAP.values())):
        continue # Already renamed
    
    img_path = os.path.join(WEBSITE_ASSETS_DIR, img_name)
    try:
        img = Image.open(img_path).convert("RGB")
        
        preds = classifier(img, candidate_labels=LABELS)
        best_match = preds[0]["label"]
        category = CATEGORY_MAP[best_match]
        
        category_counts[category] += 1
        new_filename = f"{category}_{category_counts[category]}.jpg"
        new_path = os.path.join(WEBSITE_ASSETS_DIR, new_filename)
        
        os.rename(img_path, new_path)
        print(f"Classified {img_name} -> {new_filename} ({preds[0]['score']:.2%})")
        
    except Exception as e:
        print(f"Error processing {img_name}: {e}")

print("Classification complete!")