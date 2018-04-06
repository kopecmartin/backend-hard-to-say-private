""" Operation over line equation
"""

def get_line_eq(x1, y1, x2, y2):
    """ Compute line equation from given two points
    """
    #    A   x +    B   y +      C      = 0
    # (y1-y2)x + (x2-x1)y + (x1y2-x2y1) = 0
    return {'a':(y1-y2), 'b':(x2-x1), 'c':(x1*y2-x2*y1)}


def is_on_normal(line_eq, normal_eq):
    """ Returns True if given line is normal to given line equation
    """
    if (max(line_eq['a'], normal_eq['a'])%min(line_eq['a'], normal_eq['a']) == 0 and
        max(line_eq['b'], normal_eq['b'])%min(line_eq['b'], normal_eq['b']) == 0):
        True
    else:
        False
