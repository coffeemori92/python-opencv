import cv2

# 고정 크기로 설정
img = cv2.imread('./assets/image.jpg')
# dst = cv2.resize(img, (400, 500)) # width, height

# 비율로 설정
dst = cv2.resize(img, None, fx=0.5, fy=0.5) # x, y 비율 정의 (0.5배로 축소)

# 보간법
# cv2.INTER_AREA: 크기를 줄일 때 사용
# cv2.INTER_CUBIC: 크기를 늘릴 때 사용 (속도 느림, 퀄리티 좋음)
# cv2.INTER_LINER: 크기를 늘릴 때 사용 (기본값)
dst = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
dst = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

cv2.imshow('img', img)
cv2.imshow('resize', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
