import cv2

img = cv2.imread('./assets/card.png')

cv2.imshow('img', img)

# 경계 사각형
# 윤곽선의 경계면을 둘러싸는 사각형
target_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 윤곽선 검출
# 윤곽선 정보, 구조
# 이미지, 윤곽선 찾는 모드, 윤곽선 찾을 때 사용하는 근사치 방법
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

COLOR = (0, 200, 0)
THICKNESS = 2

for cnt in contours:
    x, y, width, height = cv2.boundingRect(cnt)
    cv2.rectangle(target_img, (x, y), (x + width, y + height), COLOR, THICKNESS)

cv2.imshow('gray', gray)
cv2.imshow('otsu', otsu)
cv2.imshow('target_img', target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
