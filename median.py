import sys
import os
import cv2
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print("Usage: python3 median.py [-d] <file>")
    sys.exit(1)

input_filename = "images/" + sys.argv[-1]
output_filename = "images/median_" + sys.argv[-1]

if not os.path.exists(input_filename):
    print(input_filename, "doesn't exist!")
    sys.exit(1)

if os.path.exists(output_filename):
    print(output_filename, "already exists!")
    sys.exit(1)

image = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)

denoised_image = cv2.medianBlur(image, 5)

if len(sys.argv) == 3 and sys.argv[1] == "-d":
    plt.imshow(denoised_image, cmap='gray')
    plt.title('Median Noise Filtering')
    plt.axis('off')  
    plt.show()

cv2.imwrite(output_filename, denoised_image)
