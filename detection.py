import cv2 as cv
import numpy as np
from scipy import ndimage

def detect(img):
    s = ndimage.generate_binary_structure(2,2)
    labeled_arr, num_objects = ndimage.label(img, structure=s)

    dots = ndimage.find_objects(labeled_arr)

    bboxes = []
    for i,j in enumerate(dots):

        if dots[i][0].start != 0 and dots[i][1].start != 0 and dots[i][0].stop < img.shape[0] and dots[i][1].stop < img.shape[1] and labeled_arr[j].shape[0] > 10 and labeled_arr[j].shape[1] > 10:

            garbage_arr, num_garbage = ndimage.label(labeled_arr[j], structure=s)
            garbage = ndimage.find_objects(garbage_arr)

            if len(garbage) > 1:
                for k,l in enumerate(garbage):
                    if not (garbage[k][0].start == 0 and garbage[k][1].start == 0 and garbage[k][0].stop == labeled_arr[j].shape[0] and garbage[k][1].stop == labeled_arr[j].shape[1]):
                        garbage_arr[l] = 0
                bboxes.append(garbage_arr)
            else:
                bboxes.append(labeled_arr[j])

    return bboxes