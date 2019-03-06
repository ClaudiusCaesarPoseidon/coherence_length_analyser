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
        if video is True and self.parent.ends is False:
            # check if Use is toggled
            if self.parent.Use.isChecked() is False:
                print(
                    "The first run is to determine the location of the peak in the fft.")
                print(
                    "The time this will take depends on the number of frames and the visibility of the peak.")
                print("Please wait.")
                cap = cv2.VideoCapture(path)
                frame_number = None
                max_count = 190  # 255 204 216 190
                i = 0
                while True:
                    if self.parent.ends is True:
                        break
                    ret, frame = cap.read()
                    if ret is True:
                        c = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    else:
                        i = 0
                        print("Checking Threshold: ", max_count)
                        indexes = functions.set_list(indexes)
                        self.indexes = indexes
                        if len(indexes) > 0:
                            if len(indexes) == 0:
                                self.ind = tuple((indexes[0])[0])
                            else:
                                ind = []
                                inde = []

