import cv2
import numpy as np

src_img = cv2.imread('./assets/poker.jpg')
point_list = []
drawing = False

COLOR = (255, 0, 255)
THICKNESS = 3

def mouse_handler(event, x, y, flags, param):
    global drawing
    dst_img = src_img.copy()
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        point_list.append((x, y))
        print(point_list)
    
    if drawing:
        prev_point = None # 직선의 시작점
        for point in point_list:
            cv2.circle(dst_img, point, 15, COLOR, cv2.FILLED)
            if prev_point:
                cv2.line(dst_img, prev_point, point, COLOR, THICKNESS, cv2.LINE_AA)
            prev_point = point
        
        next_point = (x, y)
        if len(point_list) == 4:
            show_result(point_list)
            next_point = point_list[0]
        cv2.line(dst_img, prev_point, next_point, COLOR, THICKNESS, cv2.LINE_AA)
        
    cv2.imshow('img', dst_img)
    
def show_result(point_list):
    width, height = 530, 710
    src = np.float32(point_list)
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)
    
    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(src_img, matrix, (width, height))
    cv2.imshow('result', result)

# img란 이름의 윈도우를 만들어 두는 것
cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img', src_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
