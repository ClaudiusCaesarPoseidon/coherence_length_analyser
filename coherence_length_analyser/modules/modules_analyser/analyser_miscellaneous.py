import os
from ...lib import functions
from natsort import natsort_keygen
import cv2
import numpy as np
from PIL import Image
import timeit
natsort_key = natsort_keygen()
default_imread = cv2.imread


# replaces the imread function, which can not read images whose path
# contains non ASCII characters
def imread(path, mode=1):
    if functions.isascii(path) is True:
        return default_imread(path, mode)
    else:
        if mode == 0:
            return np.asarray(Image.open(path).convert('L'))
        else:
            return np.asarray(Image.open(path).convert('RGB'))


def convert(image_folder, vid_path, time):
    """converts an image folder to a video (.avi)"""
    cv2.imread = imread
    images = [img for img in os.listdir(image_folder)]
    images.sort(key=natsort_key)
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width = frame.shape[0:2]
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(vid_path, fourcc, 60, (width, height))
    a = timeit.default_timer()
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
        if timeit.default_timer() - a > time:
            print("Processing")
            a = timeit.default_timer()
    video.release()


def hasNumber(inputString):
    """check if string contains any number"""
    return any(char.isdigit() for char in inputString)


def get_all_folders(path):
    """get list of folders"""
    return [
        x[0] for x in os.walk(path) if 'converted_videos' not in x[0]
        and hasNumber(x[0]) is True]


class search():
    """searches for files in path"""

    def __init__(self, path, files=''):
        self.path = path
        self.files = []
        if files == "image":
            self.files = [
                os.path.join(
                    path,
                    file) for file in os.listdir(path) if os.path.isdir(
                    os.path.join(
                        path,
                        file)) is False and functions.is_image(
                    os.path.join(
                        path,
                        file)) is True]
        else:
            self.files = [os.path.join(path, file)
                          for file in os.listdir(path)]
        self.files.sort(key=natsort_key)


def index_containing_substring(the_list, substring):
    """get index of substring in list"""
    for i, s in enumerate(the_list):
        if substring in s and s.endswith('.avi'):
            return i
    return None


class get_video:
    """gets video with window"""

    def __init__(self, path):
        self.order = [
            'Dolph-Chebychev',
            'Kaiser',
            'Gauss',
            'Hanning',
            'Bohman',
            'Boxcar']
        self.folders = [x[0] for x in os.walk(path) if hasNumber(x[0]) is True]
        self.files = None

    def get(self, window='Kaiser'):
        order = self.order.copy()
        order.remove(window)
        order.insert(0, window)
        files = []
        for item in self.folders:
            tmp = os.listdir(item)
            for window in order:
                index = index_containing_substring(tmp, window)
                if index is not None:
                    break
            files.append(os.path.join(item, tmp[index]))
        try:
            return files
        finally:
            self.files = files
