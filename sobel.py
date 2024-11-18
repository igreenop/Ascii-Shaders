import sys
import os
import cv2
import matplotlib.pyplot as plt

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

image = cv2.imread(input_filename)

if image is None:
    print("Error: Image could not be loaded!")
    sys.exit(1)

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)


gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)
gradient_magnitude = cv2.convertScaleAbs(gradient_magnitude)

threshold_value = 50
max_value = 255
_, thresholded_image = cv2.threshold(gradient_magnitude, threshold_value, max_value, cv2.THRESH_BINARY)

if len(sys.argv) == 3 and sys.argv[1] == "-d":
    plt.imshow(thresholded_image, cmap='gray')
    plt.title('Sobel Edge Detection')
    plt.axis('off')  
    plt.show()

cv2.imwrite(output_filename, thresholded_image)
