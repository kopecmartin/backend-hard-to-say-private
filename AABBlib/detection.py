#!/usr/bin/env python3
from scipy import ndimage
import math


class Detector(object):
    """Class Detector
    Detect bounded boxes
    """
    def __init__(self, img):
        self.img = img

    def get_bounded_boxes(self):
        """Get bounded boxes from thresholded image"""
        s = ndimage.generate_binary_structure(2, 2)
        labeled_arr, num_objects = ndimage.label(self.img, structure=s)

        dots = ndimage.find_objects(labeled_arr)

        bboxes = []
        for i, j in enumerate(dots):

            if (dots[i][0].start != 0 and
                    dots[i][1].start != 0 and
                    dots[i][0].stop < self.img.shape[0] and
                    dots[i][1].stop < self.img.shape[1] and
                    labeled_arr[j].shape[0] > 10 and
                    labeled_arr[j].shape[1] > 10):

                garbage_arr, num_garbage = ndimage.label(labeled_arr[j],
                                                         structure=s)
                garbage = ndimage.find_objects(garbage_arr)

                if len(garbage) > 1:
                    for k, l in enumerate(garbage):
                        if (not (garbage[k][0].start == 0 and
                                 garbage[k][1].start == 0 and
                                 garbage[k][0].stop == labeled_arr[j].shape[0] and
                                 garbage[k][1].stop == labeled_arr[j].shape[1])):
                            garbage_arr[l] = 0
                    bboxes.append(garbage_arr)
                else:
                    bboxes.append(labeled_arr[j])

        return bboxes

    def _get_border_from_left(self, row):
        for i in range(0, len(row)):
            if row[i] != 0:
                # return index of the column where the
                # color is not background color (black)
                return i

    def _get_border_from_right(self, row):
        length = len(row)
        for i in range(length - 1, -1, -1):
            if row[i] != 0:
                return i

    def _get_border_from_top(self, c, matrix):
        for i in range(0, len(matrix)):
            if matrix[i, c] != 0:
                return i

    def _get_border_from_bottom(self, c, matrix):
        length = len(matrix)
        for i in range(length - 1, -1, -1):
            if matrix[i, c] != 0:
                return i

    def _append_if_not_in(self, what, to):
        if what not in to:
            to.append(what)
        return to

    def convex_hull(self, bbox):
        borders = []
        r_length = len(bbox)
        c_length = len(bbox[0])  # all rows has the same length

        for c in range(0, c_length):
            r = self._get_border_from_top(c, bbox)
            coordinates = [r, c]
            borders = self._append_if_not_in(coordinates, borders)

            r = self._get_border_from_bottom(c, bbox)
            coordinates = [r, c]
            borders = self._append_if_not_in(coordinates, borders)

        for r in range(0, r_length):
            c = self._get_border_from_left(bbox[r])
            coordinates = [r, c]
            borders = self._append_if_not_in(coordinates, borders)

            c = self._get_border_from_right(bbox[r])
            coordinates = [r, c]
            borders = self._append_if_not_in(coordinates, borders)

        return borders

    def _get_len(self, p1, p2):
        """Get distance between 2 points"""
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def _get_lengths(self, edge_list):
        """Get [{'length' : length, 'points': [[x1, y1], [x2, y2]]}]"""
        return [dict([('length', self._get_len(i, j)), ('points', [i, j])]) for i in edge_list for j in edge_list]

    def max_length(self, edge_list):
        lengths = self._get_lengths(edge_list)

        max_len = 0
        max_points = []
        for d in lengths:
            if d['length'] > max_len:
                max_len = d['length']
                max_points = d['points']

        return round(max_len, 2), max_points
