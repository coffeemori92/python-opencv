import cv2

img = cv2.imread('./assets/card.png')

cv2.imshow('img', img)


# 경계선을 연결한 선, 윤곽선
target_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 윤곽선 검출
# 윤곽선 정보, 구조
# 이미지, 윤곽선 찾는 모드, 윤곽선 찾을 때 사용하는 근사치 방법
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

COLOR = (0, 200, 0)
THICKNESS = 2

# 대상 이미지, 윤곽선 정보, 인덱스 (-1 이면 전체), 색, 두께
cv2.drawContours(target_img, contours, -1, COLOR, THICKNESS)

cv2.imshow('gray', gray)
cv2.imshow('otsu', otsu)
cv2.imshow('target_img', target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
