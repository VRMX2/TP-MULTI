import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("cablecar.bmp")

RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Padding
padded_image = np.pad(
    RGB_img,
    pad_width=((10,10),(10,10),(0,0)),
    mode='constant',
    constant_values=0
)

figure, plot = plt.subplots(1,2)

plot[0].imshow(RGB_img)
plot[0].set_title("Original Image")
plot[0].axis("off")

plot[1].imshow(padded_image)
plot[1].set_title("After Padding")
plot[1].axis("off")

plt.show()