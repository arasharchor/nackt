from nackt.metrics.meters import is_similar
import cv2


def paint(image, color, with_color):
    rows, columns, tmp = image.shape
    for row in range(rows):
        for column in range(columns):
            if is_similar(color, image[row][column]):
                cv2.rectangle(image, (column, row), (column, row), with_color)


def get_subrectangle(image, p1, p2):
    rows, columns, tmp = image.shape
    p10 = max(0, min(rows, p1[0]))
    p11 = max(0, min(columns, p1[1]))
    p20 = max(0, min(rows, p2[0]))
    p21 = max(0, min(columns, p2[1]))
    return image[p11:p21, p10:p20]
