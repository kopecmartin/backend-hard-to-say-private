
import numpy as np


def total_pix(image):
    size = image.size[0] * image.size[1]
    return size


def histogramify(image):
    grayscale_array = []
    for w in range(0, image.size[0]):
        for h in range(0, image.size[1]):
            intensity = image.getpixel((w, h))
            grayscale_array.append(intensity)

    bins = range(0, 257)
    img_histogram = np.histogram(grayscale_array, bins)
    return img_histogram


def otsu(image):
    total = total_pix(image)
    current_max = 0
    threshold = 0
    sumT = 0
    sumF = 0
    sumB = 0

    hist = histogramify(image)
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
        meanB = sumB / weightB
        meanF = sumF / weightF
        varBetween = weightB * weightF
        varBetween *= (meanB - meanF) * (meanB - meanF)
        if varBetween > current_max:
            current_max = varBetween
            threshold = i

    return threshold
