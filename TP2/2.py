import cv2

img = cv2.imread("cablecar.bmp")

if img is None:
    print("Erreur de chargement")
else:
    # Modify region
    img[100:150, 100:200] = (255,0,0)

    cv2.imshow("Modified Region", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()