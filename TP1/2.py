import cv2
import numpy as np

img = cv2.imread("cablecar.bmp")

resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

# Convert color spaces
img_ycrcb = cv2.cvtColor(resized_img, cv2.COLOR_BGR2YCrCb)
img_hsv = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

# Save images
cv2.imwrite("ycrcb.png", img_ycrcb)
cv2.imwrite("hsv.png", img_hsv)

# Concatenate images
images = np.concatenate(
    (cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR), img_ycrcb, img_hsv),
    axis=1
)

cv2.imshow("Gray | YCrCb | HSV", images)
cv2.waitKey(0)
cv2.destroyAllWindows()