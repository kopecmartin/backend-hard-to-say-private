#!/usr/bin/env python 3
import cv2


def mask_thresh(input, threshed):
    im = cv2.imread(input)
    # to grayscale
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # # Otsu's thresholding after Gaussian filtering
    # blur = cv2.GaussianBlur(imgray, (5, 5), 0)
    # ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    dst = cv2.addWeighted(imgray, 0.9, threshed, 0.1, 0)

    cv2.imshow('masked', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
