import cv2

print(cv2.__version__)

img = cv2.imread('./assets/image.jpg')
cv2.imshow('img', img)

# 이미지의 height, width, channel 정보
print(img.shape)

# cv2.IMREAD_COLOR: 컬러 이미지, 투명 영역은 무시 (기본값)
# cv2.IMREAD_GRAYSCALE: 흑백 이미지
# cv2.IMREAD_UNCHANGED: 투명영역까지 포함
img_color = cv2.imread('./assets/image.jpg', cv2.IMREAD_COLOR)
img_grayscale = cv2.imread('./assets/image.jpg', cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread('./assets/image.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('img_color', img_color)
cv2.imshow('img_grayscale', img_grayscale)
cv2.imshow('img_unchanged', img_unchanged)

cv2.waitKey(0)
cv2.destroyAllWindows()
