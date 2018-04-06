#!/usr/bin/env python3

import argparse
from PIL import Image
import otsu
import basic_threshold as bt
import numpy as np
import detection
from AABBlib import max_length
from AABBlib import convex_hull
import csv
import cv2


def get_threshold_by_otsu(img):
    return otsu.otsu(img)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image-path", required=True)
    parser.add_argument("--csv-path", required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    img = cv2.imread(args.image_path, 0)

    threshold = get_threshold_by_otsu(img)
    print("threshold is: ", threshold)

    img_thres = bt.threshold(threshold, img)
    # debug - save img after thresholding
    # import scipy
    # scipy.misc.imsave('outputNumpy.jpg', img_thres)

    # mask orig image with thresholded one - see differences
    # tools.mask_thresh(args.image_path, './threshed_pic.bmp')

    bboxes = detection.detect(img_thres)

    box_width = []
    box_height = []
    max_len = []
    max_points = []
    edge_list = []
    for bbox in bboxes:
        edge_list.append(convex_hull.convex_hull(bbox))
        box_height.append(bbox.shape[0])
        box_width.append(bbox.shape[1])

    for edges in edge_list:
        max_l, max_p = max_length.max_length(edges)
        max_len.append(max_l)
        max_points.append(max_p)

    zipped = zip(range(1, len(max_len) + 1),
                 box_width, box_height, max_len)

    with open(args.csv_path, 'w') as out_csv:
        writer = csv.writer(out_csv)
        writer.writerow(['Part #', 'Width', 'Height',
                         'Max Length', 'Thickness'])
        writer.writerows(zipped)
    cv2.imwrite('thresh' + args.image_path, img_thres)