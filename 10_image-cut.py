import cv2

img = cv2.imread('./assets/image.jpg')
print(img.shape)

# 세로기준 100:200, 가로기준 200:400 까지 자름
crop = img[100:200, 200:400]

# cv2.imshow('img', img)
# cv2.imshow('crop', crop)

img[100:200, 400:600] = crop
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()