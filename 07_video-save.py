import cv2
import os

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.mkdir(directory)
            print('Info: Created the directory.')
    except OSError:
        print('Error: Failed to create the directory.')

cap = cv2.VideoCapture('./assets/video.mp4')

# 코덱 정의
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 프레임 크기, FPS
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('./out/video-save.avi', fourcc, fps, (width, height))

createDirectory('out')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    out.write(frame) # 영상 데이터만 저장 (소리 X)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'): break

out.release()
cap.release()
cv2.destroyAllWindows()