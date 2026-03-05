import cv2

img = cv2.imread("cablecar.bmp")

height, width, _ = img.shape

block_size = int(width / 2)

for y in range(0, height, block_size):
    for x in range(0, width, block_size):

        y_end = min(y + block_size, height)
        x_end = min(x + block_size, width)

        block = img[y:y_end, x:x_end]

        print(f"Bloc ({x},{y}) → ({x_end},{y_end})")

        cv2.imshow("Block", block)
        cv2.waitKey(100)

cv2.destroyAllWindows()