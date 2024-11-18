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

tao = 0.2

sigma_1 = 1.4
sigma_2 = tao * sigma_1


blur1 = cv2.GaussianBlur(image, (0, 0), sigma_1)
blur2 = cv2.GaussianBlur(image, (0, 0), sigma_2)

dog = blur1 - blur2

dog_normalized = cv2.normalize(dog, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

threshold_value = 50
max_value = 255
_, thresholded_image = cv2.threshold(dog_normalized, threshold_value, max_value, cv2.THRESH_BINARY)

if len(sys.argv) == 3 and sys.argv[1] == "-d":
    plt.imshow(thresholded_image, cmap="grey")
    plt.title('Difference of Gaussians')
    plt.axis('off')  
    plt.show()

cv2.imwrite(output_filename, thresholded_image)
