#!/usr/bin/env python3
import numpy as np


def otsu(image):
    maximum = -1
    threshold = -1

    hist, bins = np.histogram(image, np.array(range(0, 256)))

    mean_weight = 1.0/image.size
    for i in bins[1:-1]:    # 1 - 254
        weightB = np.sum(hist[:i]) * mean_weight
        weightF = np.sum(hist[i:]) * mean_weight

        meanB = np.mean(hist[:i])
        meanF = np.mean(hist[i:])

        between = weightB * weightF * (meanB - meanF) ** 2

        if between > maximum:
            maximum = between
            threshold = i
    return threshold
