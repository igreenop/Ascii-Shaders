import sys
import os
import cv2
import numpy as np

if len(sys.argv) < 2:
    print("Usage: python3 sobel.py [-d] <file>")
    sys.exit(1)

input_filename = "images/" + sys.argv[-1]
output_filename = "images/sobel_" + sys.argv[-1]

if not os.path.exists(input_filename):
    print(input_filename, "doesn't exist!")
    sys.exit(1)

if os.path.exists(output_filename):
    print(output_filename, "already exists!")
    sys.exit(1)

image = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image could not be loaded!")
    sys.exit(1)

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)
gradient_magnitude = cv2.convertScaleAbs(gradient_magnitude)
gradient_angles = cv2.phase(sobel_x, sobel_y)

ascii_chars = " .:coPO?@▒"
num_chars = len(ascii_chars)

threshold_value = 50

height, width = image.shape

ascii_art = ""

for y in range(0, height, 16):
    line = ""
    for x in range(0, width, 8):
        char = ""
        if gradient_magnitude[y, x] > threshold_value:
            angle = gradient_angles[y, x] * 180 / np.pi
            if (angle >= 105 and angle < 165) or (angle >= 285 and angle < 345):
                char = '\\'
            elif (angle >= 15 and angle < 75) or (angle >= 195 and angle < 255):
                char = '/'
            elif (angle >= 75 and angle < 105) or (angle >= 255 and angle < 285):
                char = '-'
            else:
                char = '|'
        else:
            index = int((image[y, x] / 255) * (num_chars - 1))
            char = ascii_chars[index]

        line += char

    ascii_art += line + "\n"

print(ascii_art)

