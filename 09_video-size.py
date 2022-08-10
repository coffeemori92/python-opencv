import cv2


cap = cv2.VideoCapture('./assets/video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    
    # 고정 크기로 설정
    # frame_resize = cv2.resize(frame, (400, 500))
    
    # 비율로 설정
    frame_resize = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    
    cv2.imshow('video', frame_resize)
    if cv2.waitKey(5) == ord('q'): break
cap.release()
cv2.destroyAllWindows()