import numpy as np
from scipy import ndimage


def blur(img):

    pix_blur = (6, 6)
    k = np.ones(pix_blur) / float(pix_blur[0] * pix_blur[1])
    output = ndimage.convolve(img, k, mode='mirror')

    return output
