import cv2

img = cv2.imread('./assets/image.jpg')

cv2.imshow('img', img)

# 좌우대칭
# flipCode > 0 : 좌우 대칭 
flip_horizontal = cv2.flip(img, 1)
# cv2.imshow('flip_horizontal', flip_horizontal)

# 상하대칭
# flipCode == 0 : 상하 대칭 
flip_vertical = cv2.flip(img, 0)
# cv2.imshow('flip_vertical', flip_vertical)

# 상하좌우 대칭
# flipCode == -1 : 상하좌우 대칭
flip_both = cv2.flip(img, -1)
cv2.imshow('flip_both', flip_both)

cv2.waitKey(0)
cv2.destroyAllWindows()
