
import numpy as np


def otsu(image):
    total = image.size
    current_max = 0
    threshold = 0
    sumT = 0
    sumF = 0
    sumB = 0

    hist = np.histogram(image, range(0, 257))
    for i in range(0, 256):
        sumT += i * hist[0][i]

    weightB = 0
    weightF = 0
    varBetween = 0
    meanB = 0
    meanF = 0

    for i in range(0, 256):
        weightB += hist[0][i]
        weightF = total - weightB
        if weightF == 0:
            break
        sumB += i * hist[0][i]
        sumF = sumT - sumB

        if weightB != 0:
            meanB = sumB / weightB
        if weightF != 0:
            meanF = sumF / weightF
        varBetween = weightB * weightF
        varBetween *= (meanB - meanF) ** 2
        if varBetween > current_max:
            current_max = varBetween
            threshold = i
    return threshold
