import cv2
from nackt.settings import BASE_DIR
from nackt.nude.nude_face import is_nude_with_face


positive_cases = []
negative_cases = []

for i in range(9):
    positive_cases.append(BASE_DIR + '/tests/true_0%d.jpg' % int(i + 1))
    negative_cases.append(BASE_DIR + '/tests/false_0%d.jpg' % int(i + 1))


false_positive = 0
false_negative = 0
true_positive = 0
true_negative = 0

for path in positive_cases:
    image = cv2.imread(path)
    if is_nude_with_face(image):
        true_positive += 1
    else:
        false_negative += 1

for path in negative_cases:
    image = cv2.imread(path)
    if is_nude_with_face(image):
        false_positive += 1
    else:
        true_negative += 1

precision = float(true_positive) / float(true_positive + false_positive)
recall = float(true_positive) / float(true_positive + false_negative)
f1 = 2 * (precision * recall) / (precision + recall)

print 'FP:', false_positive
print 'FN:', false_negative
print 'TP:', true_positive
print 'TN:', true_negative

