def _get_border_from_left(row):
    for i in range(0, len(row)):
        if row[i] != 0:
            # return index of the column where the
            # color is not background color (black)
            return i


def _get_border_from_right(row):
    length = len(row)
    for i in range(length-1, -1, -1):
        if row[i] != 0:
            return i


def _get_border_from_top(c, matrix):
    for i in range(0, len(matrix)):
        if matrix[i, c] != 0:
            return i


def _get_border_from_bottom(c, matrix):
    length = len(matrix)
    for i in range(length-1, -1, -1):
        if matrix[i, c] != 0:
            return i


def _append_if_not_in(what, to):
    if what not in to:
        to.append(what)
    return to


def convex_hull(matrix):
    borders = []
    r_length = len(matrix)
    c_length = len(matrix[0])  # all rows has the same length
    print(r_length, c_length)

    for c in range(0, c_length):
        r = _get_border_from_top(c, matrix)
        coordinates = [r, c]
        borders = _append_if_not_in(coordinates, borders)
        # print("from top: ", coordinates)
        r = _get_border_from_bottom(c, matrix)
        # print("from bottom: ", coordinates)
        coordinates = [r, c]
        borders = _append_if_not_in(coordinates, borders)

    for r in range(0, r_length):
        c = _get_border_from_left(matrix[r])
        coordinates = [r, c]
        # print("from left", coordinates)
        borders = _append_if_not_in(coordinates, borders)
        c = _get_border_from_right(matrix[r])
        coordinates = [r, c]
        # print("from right: ", coordinates)
        borders = _append_if_not_in(coordinates, borders)

    return borders
