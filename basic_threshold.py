
from multiprocessing import Process, Manager


# class Image(object):
#     def __init__(self, a, p):
#         self.lst = [a] * p
#         print("FAKE:", self.lst)

#     size = {0: 8, 1: 10}

#     def getpixel(self, h, w):
#         return self.lst[h][w]


def partial_thresholding(procnum, return_dict, h_from, lines_no, t, image):
    intensity_array = []
    # print("going from: ", procnum, h_from, lines_no + h_from)
    for h in range(h_from, h_from + lines_no):
        for w in range(0, image.size[1]):  # size[1] = width
            intensity = image.getpixel((h, w))
            print("fucking : ", intensity)
            if (intensity <= t):
                x = 0
            else:
                x = 255
            intensity_array.append(x)
    # print("i have ", procnum, intensity_array)
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
    height_total = image.size[0]
    quarter = int(height_total / 4)
    print("prop: ", image.size[1], image.size[0])
    print("total: ", height_total)
    print("quarter: ", quarter)

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
        print(i, h_from, quarter)
        p = Process(target=partial_thresholding,
                    args=(i, return_dict, h_from, quarter, t, image))
        h_from += quarter
        jobs.append(p)
        p.start()

    # join processes
    for p in jobs:
        p.join()

    # let's put data together
    intensity_array = []
    print(len(return_dict))
    for i in range(0, 4):
        intensity_array.extend(return_dict[i])

    image.putdata(intensity_array)
    print("prop: ", image.size[1], image.size[0])

    return image
