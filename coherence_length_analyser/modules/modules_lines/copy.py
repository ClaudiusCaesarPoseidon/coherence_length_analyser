import numpy as np
from PIL import Image
from ...lib import functions
import cv2
import os
import shutil
from PySide2 import QtCore


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


class copy_thread(QtCore.QThread):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        if self.parent is not None:
            self.direc_path = self.parent.direc_path

    def run(self):
        # loads images from multiple folders and saves them in one folder
        cv2.imread = imread
        files = self.parent.files
        new_direc = os.path.join(self.direc_path, "lines")

        # remove directory before saving new files
        try:
            shutil.rmtree(new_direc)
        except FileNotFoundError:
            pass
        # builds the removed directory new
        if os.path.exists(new_direc) is False:
            functions.build_directory(new_direc)

        for item in files:
            img = cv2.imread(item)
            tmp1 = os.path.basename(os.path.dirname(item))
            tmp2 = os.path.basename(item.replace(".png", ""))
            tmp = tmp1 + "_" + tmp2 + ".png"
            cv2.imwrite(os.path.join(new_direc, tmp), img)
