#!/usr/bin/env python3
import math


def _get_len(p1, p2):
    """Get distance between 2 points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def _get_lengths(edge_list):
    """Get [{'length' : length, 'points': [[x1, y1], [x2, y2]]}]"""
    return [dict([('length', _get_len(i, j)), ('points', [i, j])]) for i in edge_list for j in edge_list]


def max_length(edge_list):
    lengths = _get_lengths(edge_list)

    max_len = 0
    max_points = []
    for d in lengths:
        if d['length'] > max_len:
            max_len = d['length']
            max_points = d['points']

    return round(max_len, 2), max_points
