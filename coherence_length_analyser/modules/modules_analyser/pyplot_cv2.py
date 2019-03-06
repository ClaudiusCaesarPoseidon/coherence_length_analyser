from .choose_filter import choose_filter
import matplotlib.ticker as ticker
from ...lib import functions
from pymediainfo import MediaInfo
import os
import ctypes
import cv2
import numpy as np
import qimage2ndarray
from PySide2 import QtCore, QtGui

substring_in_list = functions.substring_in_list

# get dpi of monitor
LOGPIXELSX = 88
LOGPIXELSY = 90
dc = ctypes.windll.user32.GetDC(0)
h_dpi = ctypes.windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX)
v_dpi = ctypes.windll.gdi32.GetDeviceCaps(dc, LOGPIXELSY)
ctypes.windll.user32.ReleaseDC(0, dc)


class pyplot_cv2(QtCore.QThread):
    changePixmap = QtCore.Signal(QtGui.QImage)

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ind = None
        self.save = False
        self.ax = None
        self.indexes = None

    def run(self):
        indexes = []
        self.ind = None
        self.ax = self.parent.canvas.figure.add_subplot(111)
        path = self.parent.fname
        file_name = os.path.splitext(os.path.basename(path))[0]
        file_direc = os.path.dirname(path)
        step_width = float(os.path.splitext(
            os.path.basename(path).split("_")[-1])[0]) * 0.11
        video = False
        # check if file is video
        if os.path.exists(path):
            fileInfo = MediaInfo.parse(path)
            for track in fileInfo.tracks:
                if track.track_type == "Video":
                    video = True
                    break
            else:
                print("Please choose a correct File.")
        else:
            print("The File does not exist.")