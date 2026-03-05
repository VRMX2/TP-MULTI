import cv2
import matplotlib.pyplot as plt

img = cv2.imread("cablecar.bmp")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

threshold = 127

# Manual threshold
_, img_bw = cv2.threshold(gray_img, threshold, 255, cv2.THRESH_BINARY)

# Otsu threshold
threshold, img_bw_otsu = cv2.threshold(gray_img, threshold, 255, cv2.THRESH_OTSU)

print("Otsu threshold:", threshold)

figure, plots = plt.subplots(1,2)

plots[0].imshow(img_bw, cmap='gray')
plots[0].set_title("Binarized Image")
plots[0].axis("off")

plots[1].imshow(img_bw_otsu, cmap='gray')
plots[1].set_title("Otsu Binarized Image")
plots[1].axis("off")

plt.show()