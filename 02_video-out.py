import cv2

cap = cv2.VideoCapture('./assets/video.mp4')

while cap.isOpened():
    ret, frame = cap.read() # ret: 성공여부, frame: 받아온 이미지 (프레임)
    if not ret: 
        print('더 이상 가져올 프레임이 없음')
        break
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        print('사용자 입력에 의해 종료')
        break
cap.release() # 자원해제
cv2.destroyAllWindows()
