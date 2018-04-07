""" Max height
"""

from AABBlib import line
from AABBlib import max_length
from fractions import Fraction


def is_uninterrupted(box, equation, x1, y1, x2, y2):
    normal = draw_line(x1, y1, x2, y2)
    for point in normal:
        if box[point[0]][point[1]] == 0:
            return False
    return True


def draw_line(x0, y0, x1, y1):
    points = []
    rev = reversed
    if abs(y1 - y0) <= abs(x1 - x0):
        x0, y0, x1, y1 = y0, x0, y1, x1
        rev = lambda x: x
    if x1 < x0:
        x0, y0, x1, y1 = x1, y1, x0, y0
    leny = abs(y1 - y0)
    for i in range(leny + 1):
        points.append([*rev((round(Fraction(i, leny) * (x1 - x0)) + x0, (1 if y1 > y0 else -1) * i + y0))])
    return points


def _split_along_line(line_eq, points):
    points_below = []
    points_above = []
    for point in points:
        if line.is_below_line(line_eq, point):
            points_below.append(point)
        else:
            points_above.append(point)
    return points_below, points_above


def max_thickness(points, edge, box):
    max_value = 0
    value = None

    line_eq = line.get_line_eq(points)

    edge_below, edge_above = _split_along_line(line_eq, edge)

    normal_eq = line.get_normal(line_eq, edge_above[len(edge_above)/2])

    normal_above_left, normal_above_rigth = _split_along_line(normal_eq, edge_above)
    normal_below_left, normal_below_rigth = _split_along_line(normal_eq, edge_below)

    for a in normal_above_left:
        for b in normal_below_left:
            propsed_normal = line.get_line_eq([a, b])
            if line.is_normal(line_eq, propsed_normal):
                if is_uninterrupted(box, propsed_normal, a[0], a[1], b[0], b[1]):
                    value = max_length._get_len(a, b)
                    if value > max_value:
                        max_value = value


    for a in normal_above_rigth:
        for b in normal_below_rigth:
            propsed_normal = line.get_line_eq([a, b])
            if line.is_normal(line_eq, propsed_normal):
                if is_uninterrupted(box, propsed_normal, a[0], a[1], b[0], b[1]):
                    value = max_length._get_len(a, b)
                    if value > max_value:
                        max_value = value

    return max_value
