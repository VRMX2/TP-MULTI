import cv2

img = cv2.imread("cablecar.bmp")

# Access row
row = img[100, :, :]
print("Row shape:", row.shape)

# Access column
column = img[:, 100, :]
print("Column shape:", column.shape)

# Remove green channel of column
img[:,100,1] = 0

cv2.imshow("Modified Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()