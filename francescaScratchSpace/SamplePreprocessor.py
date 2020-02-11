# Prepares the images from the IAM dataset for the NN

from __future__ import division
from __future__ import print_function

import random
import numpy as np
import cv2


def preprocess(img, imgSize, dataAugmentation=False):
    "put img into target img of size imgSize, transpose for TF and normalize gray-values"

    # there are damaged files in IAM dataset - just use black image instead
    if img is None:
        img = np.zeros([imgSize[1], imgSize[0]])

    # increase dataset size by applying random stretches to the images
    # What is the fucking purpose of this????? Also, dataAugmentation=False on line 9 sooo
    # Possibly to add some noise to the data to prevent overtraining idk though
    if dataAugmentation:
        stretch = (random.random() - 0.5)  # a random number in  [-0.5, +0.5]
        wStretched = max(int(img.shape[1] * (1 + stretch)), 1)  # random width, but at least 1
        img = cv2.resize(img, (wStretched, img.shape[0]))  # stretch horizontally by factor in [0.5, 1.5]

    # create target image and copy sample image into it
    (wt, ht) = imgSize  # target size = size we want
    (h, w) = img.shape  # input image size = (rows, columns) of a grayscale image, non-grayscale returns a triple
    fx = w / wt
    fy = h / ht
    f = max(fx, fy)

    #don't get the fx and fy lines
    # I think it's just scaling, seeing the maximum by which it needs to scale so that the image doesn't get
    # distorted, admittedly it isn't needed as you could just do f = max(w / wt, h / ht)

    newSize = (max(min(wt, int(w / f)), 1),
               max(min(ht, int(h / f)), 1))  # scale according to f (result at least 1 and at most wt or ht)
    img = cv2.resize(img, newSize) # INTER_LINEAR – a bilinear interpolation (used by default)
    target = np.ones([ht, wt]) * 255
    target[0:newSize[1], 0:newSize[0]] = img

    # transpose for TF
    img = cv2.transpose(target) # what's the purpose of the transposition?
    # I'm gonna guess that there is some mathematical formula involving transposing matrices that is
    # in the maths behind this - no clue though

    # normalize
    #EXCUSE ME WTF - i actually have no idea what is going on here lmao
    (m, s) = cv2.meanStdDev(img)
    m = m[0][0]
    s = s[0][0]
    img = img - m
    img = img / s if s > 0 else img
    return img