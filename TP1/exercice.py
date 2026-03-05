import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("cablecar.bmp")

# Convert color spaces
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Convert for matplotlib
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ycrcb = cv2.cvtColor(ycrcb, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2RGB)

# Padding border
border = np.pad(rgb, ((20,20),(20,20),(0,0)), mode='constant', constant_values=0)

figure, plot = plt.subplots(1,4)

plot[0].imshow(gray, cmap="gray")
plot[0].set_title("Gray")
plot[0].axis("off")

plot[1].imshow(ycrcb)
plot[1].set_title("YCbCr")
plot[1].axis("off")

plot[2].imshow(hsv)
plot[2].set_title("HSV")
plot[2].axis("off")

plot[3].imshow(border)
plot[3].set_title("Border Image")
plot[3].axis("off")

plt.show()