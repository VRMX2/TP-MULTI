import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
gray_img = cv2.imread("cablecar.bmp", cv2.IMREAD_GRAYSCALE)

# Kernel
kernel = np.array([
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]
])

# Padding
p = int(kernel.shape[0]/2)
pad_img = np.zeros((gray_img.shape[0]+2*p, gray_img.shape[1]+2*p))
pad_img[p:-p, p:-p] = gray_img

# Convolution function
def convolution(pad_img, kernel):

    p = int(kernel.shape[0]/2)
    pheight, pwidth = pad_img.shape

    img_conv = np.zeros(pad_img.shape)

    for i in range(p, pheight-p):
        for j in range(p, pwidth-p):

            roi = pad_img[i-p:i+p+1, j-p:j+p+1]
            img_conv[i, j] = np.sum(kernel * roi)

    img_conv = img_conv[p:-p, p:-p]

    return img_conv


# Apply manual convolution
manual_conv = convolution(pad_img, kernel)

# Apply OpenCV convolution
opencv_conv = cv2.filter2D(gray_img, -1, kernel)

# Display comparison
plt.figure(figsize=(12,5))

plt.subplot(1,3,1)
plt.title("Original")
plt.imshow(gray_img, cmap='gray')

plt.subplot(1,3,2)
plt.title("OpenCV filter2D")
plt.imshow(opencv_conv, cmap='gray')

plt.subplot(1,3,3)
plt.title("Manual Convolution")
plt.imshow(manual_conv, cmap='gray')

plt.show()