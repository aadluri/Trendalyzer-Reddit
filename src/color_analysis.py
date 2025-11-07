from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter

def extract_dominant_colors(image_path, num_colors=5):
    """Extract the most common hues from an image."""
    image = Image.open(image_path).convert('RGB')
    image = image.resize((150, 150))  # smaller = faster
    pixels = np.array(image).reshape(-1, 3)
    pixels = [tuple(p) for p in pixels]
    counter = Counter(pixels)
    most_common = counter.most_common(num_colors)
    return [color for color, count in most_common]

def display_palette(colors):
    """Display color palette."""
    fig, ax = plt.subplots(1, len(colors), figsize=(len(colors)*2, 2))
    for i, color in enumerate(colors):
        ax[i].imshow(np.ones((10,10,3), dtype=np.uint8)*color)
        ax[i].axis('off')
    plt.show()

# Example use:
# colors = extract_dominant_colors("data/images/post1.jpg")
# display_palette(colors)
