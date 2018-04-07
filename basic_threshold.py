
from multiprocessing import Process, Manager
import numpy


def partial_thresholding(procnum, return_dict, h_from, lines_no, t, image):
    """Do thresholding only on certain rows.intensity

    The function is appropriate for multiprocessing where each process
    can thresholds pixels on different lines.

    :param procnum: number of the process
    :type procnum: int
    :param return_dict: Shared dict among processes
    :param h_from: starting index of a row
    :param lines_no: amount of lines which will be processed by this process
    :type lines_no: int
    :param t: threshold
    :type t: int
    :param image: 2D array containing pixels
    :type image: numpy.Array
    """
    intensity_array = numpy.zeros((lines_no, image.shape[1]))
    for h in range(0, lines_no):
        for w in range(0, intensity_array.shape[1]):  # size[1] = width
            intensity = image[h + h_from][w]
            if (intensity <= t):
                x = 0
            else:
                x = 255
            intensity_array[h][w] = x
    return_dict[procnum] = intensity_array


def threshold(t, image):
    """Applies given threshold on the given image

    :param t: threshold
    :type t: int
    :type image: ImageFile
    :return: image on which threshold was applied
    :rtype: ImageFile
    """
    # let's devide height to 4 parts
    height_total = image.shape[0]
    quarter = int(height_total / 4)

    h_from = 0
    is_total_height = 0
    return_dict = Manager().dict()
    jobs = []

    # let's create 4 processes
    for i in range(0, 4):
        # if creating the last process, give it the rest of the lines
        if i == 3:
            quarter = height_total - is_total_height
        is_total_height += quarter
        p = Process(target=partial_thresholding,
                    args=(i, return_dict, h_from, quarter, t, image))
        h_from += quarter
        jobs.append(p)
        p.start()

    # join processes
    for p in jobs:
        p.join()

    # let's put data together
    image_th = numpy.concatenate((return_dict[0], return_dict[1],
                                  return_dict[2], return_dict[3]), axis=0)

    return image_th
