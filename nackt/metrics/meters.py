from nackt.settings import SIMILARITY_DISTANCE_CONSTANT_RGB


def city_blocks_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) + abs(point1[2] - point2[2])


def maximum_distance(point1, point2):
    return max(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]), abs(point1[2] - point2[2]))


def minkowski_distance(point1, point2, p=2):
    if p == 1:
        return city_blocks_distance(point1, point2)
    if p == float('inf'):
        return maximum_distance(point1, point2)
    return (abs(point1[0] - point2[0])**p + abs(point1[1] - point2[1])**p + abs(point1[2] - point2[2])**p) ** (1.0/float(p))


def euclidean_distance(point1, point2):
    return minkowski_distance(point1, point2)


def square_euclidean_distance(point1, point2):
    return abs(point1[0] - point2[0])**2 + abs(point1[1] - point2[1])**2 + abs(point1[2] - point2[2])**2


def is_similar(point1, point2, distance=SIMILARITY_DISTANCE_CONSTANT_RGB, meter=maximum_distance):
    return meter(point1, point2) < distance
