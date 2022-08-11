import cv2
import numpy as np

# 이미지를 깍아서 노이즈 제거
# 흰색 영역의 외곽 픽셀을 검은색으로 변경

kernel = np.ones((3, 3), dtype=np.uint8)
print(kernel)

img = cv2.imread('./assets/erode.png', cv2.IMREAD_GRAYSCALE)
erode1 = cv2.erode(img, kernel, iterations=1)
erode2 = cv2.erode(img, kernel, iterations=2)
erode3 = cv2.erode(img, kernel, iterations=3)

cv2.imshow('gray', img)
cv2.imshow('erode1', erode1)
cv2.imshow('erode2', erode2)
cv2.imshow('erode3', erode3)

cv2.waitKey(0)
cv2.destroyAllWindows()
