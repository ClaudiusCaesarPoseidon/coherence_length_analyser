from ...lib import functions
import cv2
import os
import numpy as np
import qimage2ndarray
from pymediainfo import MediaInfo
from PySide2 import QtCore, QtGui


class section_test(QtCore.QThread):
    """displays the video, the FFT, and the resizeable center of the FFT"""
    changePixmap = QtCore.Signal(QtGui.QImage)

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def run(self):
        video = False
        path = self.parent.fname
        print(path)
        if os.path.exists(path):
            fileInfo = MediaInfo.parse(path)
            for track in fileInfo.tracks:
                if track.track_type == "Video":
                    video = True
                    break
            else:
                print("Please choose a correct File.")
            if video is True:
                cap = cv2.VideoCapture(path)
                while True:
                    if self.parent.thread_pause is True:
                        while True:
                            self.msleep(100)
                            if self.parent.thread_pause is False:
                                break
                            if self.parent.end_section_check is True:
                                cap.release()
                                break
                    if self.parent.end_section_check is True:
                        cap.release()
                        break
                    ret, frame = cap.read()
                    if ret is True:
                        c = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        dft = functions.dft(c)
                        fft = functions.fft_cv2(dft)
                        fft = functions.fft_shift_py(
                            fft.astype(np.float64)).astype(np.uint8)
                        row, col = fft.shape
                        h_fft, w_fft = fft.shape
                        row, col = int(row / 2), int(col / 2)
                        tmp_value = int(
                            int(self.parent.Section_Size_Text.text()) / 2)
                        section = fft[row - tmp_value:row +
                                      tmp_value, col - tmp_value:col + tmp_value]
                        h_sec, w_sec = section.shape
                        fft = cv2.cvtColor(fft, cv2.COLOR_GRAY2BGR)
                        c = cv2.cvtColor(c, cv2.COLOR_GRAY2BGR)
                        tmp1 = self.parent.Spin_Row.value()
                        tmp2 = self.parent.Spin_Col.value()
                        section = section.copy(order='C')
                        section = cv2.cvtColor(section, cv2.COLOR_GRAY2BGR)
                        try:
                            section[tmp1][tmp2] = [0, 0, 255]
                        except IndexError:
                            pass
                        section = functions.resize(
                            section, h_fft / h_sec, w_fft / w_sec)
                        res = np.concatenate((c, fft, section), axis=1)
                        convertToQtFormat = qimage2ndarray.array2qimage(
                            res).rgbSwapped()
                        p = convertToQtFormat.scaled(
                            self.parent.cv2_width,
                            self.parent.cv2_height,
                            QtCore.Qt.KeepAspectRatio)
                        self.changePixmap.emit(p)
                    else:
                        cap = cv2.VideoCapture(path)
        else:
            print("The file does not exist.")
