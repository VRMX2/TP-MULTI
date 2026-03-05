import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("cablecar.bmp")

B, G, R = cv2.split(img)

R_img = np.zeros_like(img)
G_img = np.zeros_like(img)
B_img = np.zeros_like(img)

R_img[:, :, 0] = R
G_img[:, :, 1] = G
B_img[:, :, 2] = B

figure, plot = plt.subplots(1,3)

plot[0].imshow(R_img)
plot[0].set_title("Red Channel")
plot[0].axis("off")

plot[1].imshow(G_img)
plot[1].set_title("Green Channel")
plot[1].axis("off")

plot[2].imshow(B_img)
plot[2].set_title("Blue Channel")
plot[2].axis("off")

plt.show()