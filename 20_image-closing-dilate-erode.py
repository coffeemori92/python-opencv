import cv2
import numpy as np

# 열림(Opening) : 팽창 후 침식.

kernel = np.ones((3, 3), dtype=np.uint8)
print(kernel)

img = cv2.imread('./assets/dilate.png', cv2.IMREAD_GRAYSCALE)
dilate = cv2.dilate(img, kernel, iterations=3)
erode = cv2.erode(dilate, kernel, iterations=3)

cv2.imshow('gray', img)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
