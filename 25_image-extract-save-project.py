import cv2

img = cv2.imread('./assets/card.png')
target_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

COLOR = (0, 200, 0)
THICKNESS = 2

index = 0
for cnt in contours:
    if cv2.contourArea(cnt) > 25000:
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x, y), (x + width, y + height), COLOR, THICKNESS)

        crop = img[y:y + height, x: x + width]
        cv2.imshow(f'card_crop_{index}', crop)
        cv2.imwrite(f'./out/card_crop_{index}.png', crop)
        index += 1

cv2.imshow('img', img)
cv2.imshow('target_img', target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
