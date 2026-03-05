import cv2

# Read image
img = cv2.imread("cablecar.bmp")

if img is None:
    print("Erreur : Impossible de charger l'image.")
else:
    height, width, _ = img.shape

    # Traverse image pixel by pixel
    for y in range(height):
        for x in range(width):
            pixel = img[y, x]
            B, G, R = pixel

            # Modify a region
            if 100 < x < 200 and 100 < y < 150:
                img[y, x] = (255, 0, 0)  # Blue region

    cv2.imshow("Modified Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()