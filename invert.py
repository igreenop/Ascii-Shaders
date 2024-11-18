import sys
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print("Usage: python3 invert_colors.py [-d] <file>")
    sys.exit(1)

input_filename = "images/" + sys.argv[-1]
output_filename = "images/inverted_" + sys.argv[-1]

if not os.path.exists(input_filename):
    print(input_filename, "doesn't exist!")
    sys.exit(1)

if os.path.exists(output_filename):
    print(output_filename, "already exists!")
    sys.exit(1)

with Image.open(input_filename).convert("RGB") as img:
    pixels = img.load()
    h = img.height
    w = img.width

for y in range(h):
    for x in range(w):
        r, g, b = pixels[x, y]
        inverted_pixel = (255 - r, 255 - g, 255 - b)
        pixels[x, y] = inverted_pixel

if len(sys.argv) == 3 and sys.argv[1] == "-d":
    plt.imshow(np.array(img))
    plt.title('Inverted Colors')
    plt.axis('off')  
    plt.show()

img.save(output_filename)
