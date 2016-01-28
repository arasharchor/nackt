import cv2
from nackt.settings import BASE_DIR
from nackt.nude.nude_face import is_nude_with_face


image = cv2.imread('tests/true_05.jpg')
print is_nude_with_face(image, True)


# if not is_nude:
#     nipple_cascade = cv2.CascadeClassifier('xmls/haarcascade_breast.xml')
#     nipples = nipple_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in nipples:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0))
# paint(img, skin_color, (255, 0, 0))
