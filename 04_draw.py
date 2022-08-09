import cv2
import numpy as np

# 세로 480, 가로 640, 3 Channel (BGR)
img = np.zeros((480, 640, 3), dtype=np.uint8)
# img[:] = (255, 255, 255) # 전체 공간을 흰 색으로 채우기
# print(img)
# img[100:200, 200:300] = (255, 255, 255)


# 선
# COLOR = (0, 255, 255) # yellow
# THICHNESS = 3 # 두께

# cv2.LINE_4: 상하좌우 4방향으로 연결된 선
# cv2.LINE_8: 대각선을 포함한 8방향으로 연결된 선
# cv2.LINE_AA: 부드러운 선
# cv2.line(img, (50, 100), (400, 50), COLOR, THICHNESS, cv2.LINE_8)
# cv2.line(img, (50, 200), (400, 150), COLOR, THICHNESS, cv2.LINE_4)
# cv2.line(img, (50, 300), (400, 250), COLOR, THICHNESS, cv2.LINE_AA)



# 원
# COLOR = (255, 255, 0)
# RADIOUS = 50 # 반지름
# THICHNESS = 10 # 두께

# 위치, 반지름, 색, 두께, 선
# cv2.circle(img, (200, 100), RADIOUS, COLOR, THICHNESS, cv2.LINE_AA)
# cv2.circle(img, (400, 100), RADIOUS, COLOR, cv2.FILLED, cv2.LINE_AA)



# 사각형
# COLOR = (0, 255, 0)
# THICHNESS = 3 # 두께

# 위치, 왼쪽 위 좌표, 오른쪽 아래 좌표, 색, 두께
# cv2.rectangle(img, (100, 100), (200, 200), COLOR, THICHNESS)
# cv2.rectangle(img, (300, 100), (400, 200), COLOR, cv2.FILLED)



# 다각형
COLOR = (0, 0, 255)
THICHNESS = 3 # 두께

pts1 = np.array([[100, 100], [200, 100], [100, 200]])
pts2 = np.array([[200, 100], [300, 100], [300, 200]])
# 위치, 닫힘여부, 색, 두께, 선
# cv2.polylines(img, [pts1], True, COLOR, THICHNESS, cv2.LINE_AA)
# cv2.polylines(img, [pts2], True, COLOR, THICHNESS, cv2.LINE_AA)
cv2.polylines(img, [pts1, pts2], True, COLOR, THICHNESS, cv2.LINE_AA)

pts3 = np.array([[[100, 300], [200, 300], [100, 400]], [[200, 300], [300, 300], [300, 400]]])
cv2.fillPoly(img, pts3, COLOR, cv2.LINE_AA)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
