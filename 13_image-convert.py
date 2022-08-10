import cv2
import numpy as np

img = cv2.imread('./assets/image.jpg')
cv2.imshow('img', img)

# 흑백으로 변형
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('img_gray', dst)

# 흐리게 변형
# 커널 사이즈 변화에 따른 흐림
kernel_3 = cv2.GaussianBlur(img, (3, 3), 0)
kernel_5 = cv2.GaussianBlur(img, (5, 5), 0)
kernel_7 = cv2.GaussianBlur(img, (7, 7), 0)
# cv2.imshow('kernel_3', kernel_3)
# cv2.imshow('kernel_5', kernel_5)
# cv2.imshow('kernel_7', kernel_7)

# 표준편차 변화에 따른 흐림
sigma_1 = cv2.GaussianBlur(img, (0, 0), 1)
sigma_2 = cv2.GaussianBlur(img, (0, 0), 2)
sigma_3 = cv2.GaussianBlur(img, (0, 0), 3)
# cv2.imshow('sigma_1', sigma_1)
# cv2.imshow('sigma_2', sigma_2)
# cv2.imshow('sigma_3', sigma_3)

# 원근 
# 사다리꼴 이미지 펼치기
img = cv2.imread('./assets/newspaper.jpg')
# cv2.imshow('img', img)

width, height = 640, 240

# 좌상, 우상, 우하, 좌하 (시계 방향으로 4 지점 정의)
# input 4개 지점
src = np.array([[511, 352], [1008, 345], [1122, 584], [455, 594]], dtype=np.float32)
# output 4개 지점
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

matrix = cv2.getPerspectiveTransform(src, dst)
# matrix 대로 변환을 함
result = cv2.warpPerspective(img, matrix, (width, height))
# cv2.imshow('result', result)

# 회전된 이미지
img = cv2.imread('./assets/poker.jpg')
cv2.imshow('img', img)

width, height = 530, 710

# input 4개 지점
src = np.array([[702, 143], [1133, 414], [726, 1007], [276, 700]], dtype=np.float32)
# output 4개 지점
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

matrix = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
