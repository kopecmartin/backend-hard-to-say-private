""" Operation over line equation
"""

def get_line_eq(points):
    """ Compute line equation from given two points
    """
    #    A   x +    B   y +      C      = 0
    # (y1-y2)x + (x2-x1)y + (x1y2-x2y1) = 0
    # points = [[x1, y1], [x2, y2]]
    x1 = points[0, 0]
    y1 = points[0, 1]
    x2 = points[1, 0]
    y2 = points[1, 1]
    return {'a':(y1-y2), 'b':(x2-x1), 'c':(x1*y2-x2*y1)}


def is_below_line(line_eq, point):
    result = line_eq['a'] * point[0] + line_eq['b'] * point[1] + line_eq['c']
    if result > 0:
        return False
    else:
        return True


def is_normal(line_eq, normal_eq):
    """ True if lines are orthogonal
    """
    if (max(line_eq['a'], normal_eq['a'])%min(line_eq['a'], normal_eq['a']) == 0 and
        max(line_eq['b'], normal_eq['b'])%min(line_eq['b'], normal_eq['b']) == 0):
        return True
    else:
        return False


def get_normal(line_eq, point):
    lamb = (-line_eq['c'] - (line_eq['a']*point[0]) - (line_eq['b']*point[1]) ) / (line_eq['a']*line_eq['a'] + line_eq['b']*line_eq['b'])
    x = point[0] + lamb * line_eq['a']
    y = point[1] + lamb * line_eq['b']
    return get_line_eq([point,[x, y]])
