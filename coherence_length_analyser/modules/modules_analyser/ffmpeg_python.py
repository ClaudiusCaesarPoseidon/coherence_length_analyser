import cv2
import os
from natsort import natsort_keygen
import numpy as np
from PIL import Image
import timeit
from ...lib import functions
natsort_key = natsort_keygen()
default_imread = cv2.imread


def imread(path, mode=1):
    if functions.isascii(path) is True:
        return default_imread(path, mode)
    else:
        if mode == 0:
            return np.asarray(Image.open(path).convert('L'))
        else:
            return np.asarray(Image.open(path).convert('RGB'))


def convert(image_folder, vid_path, time):
    cv2.imread = imread
    images = [img for img in os.listdir(image_folder)]
    images.sort(key=natsort_key)
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(vid_path, fourcc, 60, (width, height))
    a = timeit.default_timer()
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
        if timeit.default_timer() - a > time:
            print("Processing")
            a = timeit.default_timer()
    video.release()
