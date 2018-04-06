#!/usr/bin/python3

import argparse
from PIL import Image
# import sys
# import numpy


def load_tiff_image(filepath):
    img = Image.open(filepath)

    w = img.size[0]
    h = img.size[1]

    pix = img.load()
    print(w, h, pix)
    return pix


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image-path", required=True)
    parser.add_argument("--csv-path", required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    print(args)
    load_tiff_image(args.image_path)
