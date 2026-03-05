import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

# Read color image
img = cv2.imread("cablecar.bmp")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = gray.shape

# Block size
bh = h // 4
bw = w // 4

# Define kernels
kernels = [

    np.ones((5,5))/25,     # blur

    np.array([[0,-1,0],
              [-1,5,-1],
              [0,-1,0]]),  # sharpen

    np.array([[-1,-1,-1],
              [-1,8,-1],
              [-1,-1,-1]]), # edge

    np.array([[1,0,-1],
              [1,0,-1],
              [1,0,-1]])   # vertical edges
]

result = np.zeros_like(gray)

# Process 16 blocks
for i in range(4):
    for j in range(4):

        block = gray[i*bh:(i+1)*bh, j*bw:(j+1)*bw]

        kernel = random.choice(kernels)

        filtered = cv2.filter2D(block, -1, kernel)

        result[i*bh:(i+1)*bh, j*bw:(j+1)*bw] = filtered


# Display
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original Gray Image")
plt.imshow(gray, cmap='gray')

plt.subplot(1,2,2)
plt.title("Filtered 16 Blocks")
plt.imshow(result, cmap='gray')

plt.show()