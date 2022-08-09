import cv2
import os

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.mkdir(directory)
            print('Info: Created the directory.')
    except OSError:
        print('Error: Failed to create the directory.')

img = cv2.imread('./assets/image.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

createDirectory('out')

result = cv2.imwrite('./out/image-save.jpg', img)
print(result)