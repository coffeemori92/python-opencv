import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

img = np.zeros((480, 640, 3), dtype=np.uint8)

# COLOR = (255, 255, 255)
# THICKNESS = 1 # 글자 두께
# SCALE = 1 # 글자 크기

# cv2.FONT_HERSHEY_SIMPLEX: 보통 크기의 산세리프 글꼴
# cv2.FONT_HERSHEY_PLAIN: 작은 크기의 산세리프 글꼴
# cv2.FONT_HERSHEY_SCRIPT_SIMPLEX: 필기체 스타일
# cv2.FONT_HERSHEY_TRIPLEX: 보통 크기의 세리프 글꼴
# cv2.FONT_ITALIC: 기울임
# cv2.putText(img, 'hello_simplex', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
# cv2.putText(img, 'hello_plain', (20, 150), cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS)
# cv2.putText(img, 'hello_script_simplex', (20, 250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS)
# cv2.putText(img, 'hello_triplex', (20, 350), cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS)
# cv2.putText(img, 'hello_italic', (20, 450), cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE, COLOR, THICKNESS)

# 한글 우회
def myPutText(src, text, pos, font_size, font_color):
    img_pill = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pill)
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    draw.text(pos, text, font=font, fill=font_color)
    return np.array(img_pill)

COLOR = (255, 255, 255)
FONT_SIZE = 30

img = myPutText(img, '안녕', (20, 50), FONT_SIZE, COLOR)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
