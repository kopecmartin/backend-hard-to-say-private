#!/usr/bin/env python3

from AABBlib import convex_hull
from AABBlib import max_length
import basic_threshold as bt
import argparse
import csv
import cv2
import detection
import otsu


def get_threshold_by_otsu(img):
    return otsu.otsu(img)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image-path", required=True,
                        help="Path to an image to be processed")
    parser.add_argument("--csv-path", required=True,
                        help="Path where csv file will be stored")
    parser.add_argument("--resize", required=False, default=100,
                        help="Percentage to scale picture down")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    img = cv2.imread(args.image_path, 0)    # load as grayscale

    if args.resize != 100:
        resize_percentage = int(args.resize) / 100
        img = cv2.resize(img, (int(img.shape[1] * resize_percentage),
                               int(img.shape[0] * resize_percentage)))

    img = cv2.GaussianBlur(img, (5, 5), 10)  # blur img - TODO: write own

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

    # calculate a coefficient for changig lengths
    # based on resize of input picture
    k = int((1 / int(args.resize)) * 100)

    for bbox in bboxes:
        edge_list.append(convex_hull.convex_hull(bbox))
        box_height.append(bbox.shape[0] * k)
        box_width.append(bbox.shape[1] * k)

    for edges in edge_list:
        max_l, max_p = max_length.max_length(edges)
        max_len.append(max_l * k)
        max_points.append(max_p)

    zipped = zip(range(1, len(max_len) + 1),
                 box_width, box_height, max_len)

    with open(args.csv_path, 'w') as out_csv:
        writer = csv.writer(out_csv)
        writer.writerow(['Part #', 'Width', 'Height',
                         'Max Length', 'Thickness'])
        writer.writerows(zipped)
    cv2.imwrite('thresh.tif', img_thres)    # dump threshed img
