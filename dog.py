import sys
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print("Usage: python3 dog.py [-d] <file>")
    sys.exit(1)

input_filename = "images/" + sys.argv[-1]
output_filename = "images/dog_" + sys.argv[-1]

if not os.path.exists(input_filename):
    print(input_filename, "doesn't exist!")
    sys.exit(1)

if os.path.exists(output_filename):
    print(output_filename, "already exists!")
    sys.exit(1)

image = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)

blur1 = cv2.GaussianBlur(image, (0, 0), 1)
blur2 = cv2.GaussianBlur(image, (0, 0), 2)

dog = blur1 - blur2

dog_normalized = cv2.normalize(dog, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

if len(sys.argv) == 3 and sys.argv[1] == "-d":
    plt.imshow(dog_normalized, cmap="grey")
    plt.title('Difference of Gaussians')
    plt.axis('off')  
    plt.show()

cv2.imwrite(output_filename, dog_normalized)
