import cv2
import numpy as np


image = cv2.imread("image.bmp", cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 127, 1, cv2.THRESH_BINARY)

print("Binary image:")
print(binary)


fimage = binary.flatten()

print("\nFlattened image:")
print(fimage)


rle = []
count = 1
prev = fimage[0]

for pixel in fimage[1:]:
    if pixel == prev:
        count += 1
    else:
        rle.append((count, prev))
        prev = pixel
        count = 1

rle.append((count, prev))

print("\nRLE tuples:")
print(rle)

encoded = ""

for count, value in rle:
    count_str = "{:03}".format(count)
    encoded += count_str + str(value)

print("\nEncoded string:")
print(encoded)

file_name = "compressed.txt"

with open(file_name, "w") as file:
    file.write(encoded)

print("\nCompressed data written to file.")

with open(file_name, "r") as file:
    txt = file.readlines()[0]

print("\nData read from file:")
print(txt)

original_bits = binary.size
encoded_bits = len(encoded)

compression_rate = (encoded_bits / original_bits) * 100

print("\nOriginal size (bits):", original_bits)
print("Encoded size (bits):", encoded_bits)
print("Compression rate:", compression_rate, "%")