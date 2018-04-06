#!/usr/bin/env python 3

import argparse
from PIL import Image
import otsu
import basic_threshold as bt
from tools import tools
# import sys
import numpy as np
import cv2
import detection
from AABBlib import max_length
from AABBlib import convex_hull



def load_tiff_image(filepath):
    img = Image.open(filepath)

    w = img.size[0]
    h = img.size[1]

    pix = img.load()
    print(w, h, pix)
    return pix


def get_threshold_by_otsu(img):
    # convert the image to black and white
    bw_img = img.convert('L')
    return otsu.otsu(bw_img)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image-path", required=True)
    parser.add_argument("--csv-path", required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    print(args)
    # load_tiff_image(args.image_path)
    img = Image.open(args.image_path)

    threshold = get_threshold_by_otsu(img)
    print("threshold is: ", threshold)
    img_thres = bt.threshold(threshold, img)

    ocv_img = np.array(img_thres)
    bboxes = detection.detect(ocv_img)

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

    zipped = zipped = zip(box_width, box_height, max_len)

    from IPython import embed; embed()
    # show file after thresholding
    #img_thres.show()
    #img_thres.save('./threshed_pic.bmp')
    #tools.mask_thresh(args.image_path, './threshed_pic.bmp')
