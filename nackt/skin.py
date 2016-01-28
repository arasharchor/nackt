from settings import SIMILARITY_DISTANCE_CONSTANT_RGB
from metrics.meters import is_similar


def get_maximum_color(image, distance=SIMILARITY_DISTANCE_CONSTANT_RGB):
    cnt = []
    for i in range(256):
        array2d = []
        for j in range(256):
            array1d = []
            for k in range(256):
                array1d.append(0)
            array2d.append(array1d)
        cnt.append(array2d)
    rows, columns, tmp = image.shape
    for row in range(rows):
        for column in range(columns):
            r = image[row][column][0]
            g = image[row][column][1]
            b = image[row][column][2]

            r1 = max(0, r - distance)
            g1 = max(0, g - distance)
            b1 = max(0, b - distance)
            r2 = min(255, r + distance)
            g2 = min(255, g + distance)
            b2 = min(255, b + distance)
            cnt[r1][g1][b1] += 1
            cnt[r1][g1][b2] -= 1
            cnt[r1][g2][b1] -= 1
            cnt[r1][g2][b2] += 1
            cnt[r2][g1][b1] -= 1
            cnt[r2][g1][b2] += 1
            cnt[r2][g2][b1] += 1
            cnt[r2][g2][b2] -= 1
    answer = (0, 0, 0)
    for r in range(256):
        for g in range(256):
            for b in range(256):
                if b > 0:
                    cnt[r][g][b] += cnt[r - 0][g - 0][b - 1]
                if g > 0:
                    cnt[r][g][b] += cnt[r - 0][g - 1][b - 0]
                if g > 0 and b > 0:
                    cnt[r][g][b] -= cnt[r - 0][g - 1][b - 1]
                if r > 0:
                    cnt[r][g][b] += cnt[r - 1][g - 0][b - 0]
                if r > 0 and b > 0:
                    cnt[r][g][b] -= cnt[r - 1][g - 0][b - 1]
                if r > 0 and g > 0:
                    cnt[r][g][b] -= cnt[r - 1][g - 1][b - 0]
                if r > 0 and g > 0 and b > 0:
                    cnt[r][g][b] += cnt[r - 1][g - 1][b - 1]
                if cnt[answer[0]][answer[1]][answer[2]] < cnt[r][g][b]:
                    answer = (r, g, b)
    return answer


def get_ratio_of_color(image, color, distance=SIMILARITY_DISTANCE_CONSTANT_RGB):
    rows, columns, tmp = image.shape
    area = 0.0
    for row in range(rows):
        for column in range(columns):
            if is_similar(color, (image[row][column][0], image[row][column][1], image[row][column][2]), distance=distance):
                area += 1.0

    if (rows * columns) == 0.0:
        return float('inf')
    return area / (rows * columns)


def get_distance_by_percentage(image, percentage):
    le = 1
    ri = 100
    for cnt in range(4):
        mid = (le + ri) / 2
        distance = mid
        skin_color = get_maximum_color(image, distance=distance)
        skin_ratio = get_ratio_of_color(image, skin_color, distance=distance)
        print(mid, skin_ratio, skin_color)
        if abs(skin_ratio - percentage) < 0.03:
            ri = mid
            break
        elif skin_ratio > percentage:
            ri = mid
        else:
            le = mid
    distance = ri
    return distance


def get_color_by_percentage(image, percentage):
    distance = get_distance_by_percentage(image, percentage)
    return get_maximum_color(image, distance=distance)
