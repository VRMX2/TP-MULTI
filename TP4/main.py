import cv2
import numpy as np

image = cv2.imread("image.bmp", cv2.IMREAD_GRAYSCALE)
_, image_bin = cv2.threshold(image,127,1,cv2.THRESH_BINARY)

fimage = image_bin.flatten()

rle=[]
count=1
prev=fimage[0]

for pixel in fimage[1:]:
    if pixel==prev:
        count+=1
    else:
        rle.append((count,prev))
        count=1
        prev=pixel

rle.append((count,prev))

code=""

for count,value in rle:
    count_bits="{:03}".format(count)
    code+=count_bits+str(value)

with open("compression.txt","w") as file:
    file.write(code)

taille_code=len(code)
taille_image=len(fimage)

taux=(taille_code/taille_image)*100

print("Code :",code)
print("Taille code :",taille_code)
print("Taille image :",taille_image)
print("Taux de compression :",taux,"%")