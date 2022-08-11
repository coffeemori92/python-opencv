import cv2
import numpy as np

# 열림(Opening) : 침식 후 팽창. 깍아서 노이즈 제거 후 팽창

kernel = np.ones((3, 3), dtype=np.uint8)
print(kernel)

img = cv2.imread('./assets/erode.png', cv2.IMREAD_GRAYSCALE)
erode = cv2.erode(img, kernel, iterations=3)
dilate = cv2.dilate(erode, kernel, iterations=3)

cv2.imshow('gray', img)
cv2.imshow('erode', erode)
cv2.imshow('dilate', dilate)

cv2.waitKey(0)
cv2.destroyAllWindows()
