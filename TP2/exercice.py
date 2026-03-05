import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("cablecar.bmp")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height, width = gray.shape

# Divide image into 3 vertical blocks
block_width = width // 3

left_block = gray[:, :block_width]
middle_block = gray[:, block_width:2*block_width]
right_block = gray[:, 2*block_width:]

# Binarize middle block
_, middle_bin = cv2.threshold(middle_block, 127, 255, cv2.THRESH_BINARY)

# Merge blocks again
result = gray.copy()
result[:, block_width:2*block_width] = middle_bin

# Display results
figure, plots = plt.subplots(1,2)

plots[0].imshow(gray, cmap="gray")
plots[0].set_title("Original Image")
plots[0].axis("off")

plots[1].imshow(result, cmap="gray")
plots[1].set_title("Middle Block Binarized")
plots[1].axis("off")

plt.show()