# 얼굴을 인식하여 캐릭터 씌우기

import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture('./assets/face_video.mp4')

image_right_eye = cv2.imread('./assets/right_eye.png')
image_left_eye = cv2.imread('./assets/left_eye.png')
image_nose = cv2.imread('./assets/nose.png')

with mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.5
) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success: break
        
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)
        
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)
                
                h, w, _ = image.shape
                
                # 특정 위치 가져오기
                keypoints = detection.location_data.relative_keypoints
                right_eye = keypoints[0]
                left_eye = keypoints[1]
                nose_tip = keypoints[2]
                
                # 이미지 내에서 실제 좌표 (x, y)
                right_eye = (int(right_eye.x * w) - 70, int(right_eye.y * h) - 100)
                left_eye = (int(left_eye.x * w) + 70, int(left_eye.y * h) - 100)
                nose_tip = (int(nose_tip.x * w), int(nose_tip.y * h))
                
                image[
                    right_eye[1] - 50:right_eye[1] + 50,
                    right_eye[0] - 50:right_eye[0] + 50
                ] = image_right_eye
                
                image[
                    left_eye[1] - 50:left_eye[1] + 50,
                    left_eye[0] - 50:left_eye[0] + 50
                ] = image_left_eye
                
                image[
                    nose_tip[1] - 50:nose_tip[1] + 50,
                    nose_tip[0] - 150:nose_tip[0] + 150
                ] = image_nose

       
        cv2.imshow('MediaPipe Face Detection', cv2.resize(image, None, fx=0.25, fy=0.25))
        
        if cv2.waitKey(1) == ord('q'): break
        
cap.release()
cv2.destroyAllWindows()
