import cv2
from nackt.settings import FACE_SKIN_RATIO
from nackt.paint import get_subrectangle, paint
from nackt.skin import get_color_by_percentage, get_ratio_of_color


def is_nude_with_face(image, show=False):
    face_cascade = cv2.CascadeClassifier('xmls/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    is_nude = False

    skin_color = (1000, 1000, 1000)

    for (x, y, w, h) in faces:
        face = image[y:y + h, x:x + w]
        skin_color = get_color_by_percentage(face, FACE_SKIN_RATIO)
        print('Skin color:', skin_color)
        upper_body = get_subrectangle(image, (x - w / 2, y + h), (x + w + w / 2, y + h + 3 * h))
        nudity = get_ratio_of_color(upper_body, skin_color)
        print('Face nudity:', nudity)
        if nudity > 0.5:
            is_nude = True

    if show:
        paint(image, skin_color, (255, 0, 0))
        cv2.imshow('img', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return is_nude
