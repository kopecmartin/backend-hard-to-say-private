#!/usr/bin/env python 3

import argparse
from PIL import Image
import otsu
import basic_threshold as bt
from tools import tools
# import sys
# import numpy as np


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
    print ("threshold is: ", threshold)
    img_thres = bt.threshold(threshold, img)
    # show file after thresholding
    #img_thres.show()
    #img_thres.save('./threshed_pic.bmp')
    #tools.mask_thresh(args.image_path, './threshed_pic.bmp')
