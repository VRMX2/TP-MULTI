import cv2

# Read the image
img = cv2.imread("cablecar.bmp")

# Check if image loaded
if img is None:
    print("Error: Unable to load image")
else:
    print(type(img))

    # Get dimensions
    height, width, channels = img.shape
    print("Height:", height)
    print("Width:", width)
    print("Channels:", channels)

    # Display image
    cv2.imshow("Image", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()