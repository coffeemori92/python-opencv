import cv2

img = cv2.imread('./assets/book.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('img', img)

# 127보다 클때 255 (흰색) 아니면 검은색
ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow('binary', binary)

# Trackbar 값 변화에 따른 변형 확인
def empty(position):
    # print(position)
    pass

# img = cv2.imread('./assets/threshold.png')

name = 'Trackbar'
cv2.namedWindow(name)
# bar 이름, 창의 이름, 기준값, 최대값, 이벤트 처리
# cv2.createTrackbar('threshold', name, 127, 255, empty)
# while True:
#     thresh = cv2.getTrackbarPos('threshold', name)
#     ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
#     if not ret: break
#     cv2.imshow(name, binary)
#     if cv2.waitKey(1) == ord('q'): break
    
# Adaptive Threshold
# 이미지를 작은 영역으로 나누어서 임계치 적용
name = 'Trackbar'
cv2.namedWindow(name)

# cv2.createTrackbar('block_size', name, 25, 100, empty)
# cv2.createTrackbar('c', name, 3, 10, empty)

# while True:
#     block_size = cv2.getTrackbarPos('block_size', name)
#     c = cv2.getTrackbarPos('c', name)
    
#     if block_size <= 1:
#         block_size = 3
        
#     if block_size % 2 == 0:
#         block_size += 1
    
#     binary = cv2.adaptiveThreshold(
#         img,
#         255,
#         cv2.ADAPTIVE_THRESH_MEAN_C,
#         cv2.THRESH_BINARY,
#         block_size,
#         c
#     )

#     cv2.imshow(name, binary)
#     if cv2.waitKey(1) == ord('q'): break
    
# 오츠 알고리즘
# Bimodal Image에 사용하기 적합 (최적의 임계치 자동으로 발견)
name = 'Trackbar'
cv2.namedWindow(name)

ret, otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('otsu threshold', ret)
cv2.imshow(name, otsu)
cv2.waitKey(0)

cv2.destroyAllWindows()
