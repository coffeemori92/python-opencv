import cv2

def mouse_handler(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: 
        print('왼쪽 버튼 down')
        print(x, y)
    elif event == cv2.EVENT_LBUTTONUP: 
        print('왼쪽 버튼 up')
        print(x, y)
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print('왼쪽 버튼 더블 클릭')
    # elif event == cv2.EVENT_MOUSEMOVE:
    #     print('마우스 이동')
    elif event == cv2.EVENT_RBUTTONDOWN:
        print('오른쪽 버튼 down')
    elif event == cv2.EVENT_RBUTTONUP:
        print('오른쪽 버튼 up')
      

img = cv2.imread('./assets/poker.jpg')
# img란 이름의 윈도우를 만들어 두는 것
cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
