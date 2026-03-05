import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
gray_img = cv2.imread("cablecar.bmp", cv2.IMREAD_GRAYSCALE)

# Define kernels
kernel1 = np.ones((5,5)) / 30
kernel2 = np.array([
    [-1,-1,-1],
    [-1, 8,-1],
    [-1,-1,-1]
])

# Apply convolution
img_conv1 = cv2.filter2D(src=gray_img, ddepth=cv2.CV_64F, kernel=kernel1)
img_conv2 = cv2.filter2D(src=gray_img, ddepth=cv2.CV_64F, kernel=kernel2)

# Display results
plt.figure(figsize=(10,5))

plt.subplot(1,3,1)
plt.title("Original Image")
plt.imshow(gray_img, cmap='gray')

plt.subplot(1,3,2)
plt.title("Kernel 1 - Blur")
plt.imshow(img_conv1, cmap='gray')

plt.subplot(1,3,3)
plt.title("Kernel 2 - Edge Detection")
plt.imshow(img_conv2, cmap='gray')

plt.show()