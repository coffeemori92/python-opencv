import cv2

img = cv2.imread('./assets/snowman.png')

cv2.imshow('img', img)
# cv2.imshow('canny', canny)

# 대상 이미지, minValue(하위 임계값), maxValue(상위 임계값)
# 픽셀의 변화가 하위 임계값보다 낮으면 경계선으로 고려 하지 않는다
# 픽셀의 변화가 상위 임계값보다 크면 경계선으로 간주
canny = cv2.Canny(img, 150, 200)

def empty(position): pass

name = 'TrackBar'

cv2.namedWindow(name)
cv2.createTrackbar('threshold1', name, 0, 255, empty) # minValue
cv2.createTrackbar('threshold2', name, 0, 255, empty) # maxValue

while True:
    threshold1 = cv2.getTrackbarPos('threshold1', name)
    threshold2 = cv2.getTrackbarPos('threshold2', name)
    
    canny = cv2.Canny(img, threshold1, threshold2)
    
    cv2.imshow(name, canny)
    
    if cv2.waitKey(1) == ord('q'): break

# cv2.waitKey(0)
cv2.destroyAllWindows()
