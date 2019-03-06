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
        self.quadrant = None
        self.indexes = None
        self.ind_mult = None
        self.section = None
        self.sect = None