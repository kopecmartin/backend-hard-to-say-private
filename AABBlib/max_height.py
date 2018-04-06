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


def max_thickness(equation, edge, box):
    max_value = 0
    points_below_norm = []
    for A in edge:
        for B in edge:
            if A == B and B in points_below_norm:
                continue
            points_below_norm.append(B)
            norm = line.get_line_eq([A, B])
            if line.is_normal(equation, norm):
                if is_uninterrupted(box, norm, A[0], A[1], B[0], B[1]):
                    max_value = max_length._get_len(A, B)
            else:
                points_below_norm = []
                continue
    return max_value
