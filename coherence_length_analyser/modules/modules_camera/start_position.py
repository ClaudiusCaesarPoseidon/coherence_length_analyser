from ...lib import functions
import math
import numpy as np
import qimage2ndarray
import cv2
import scipy.signal
import scipy.fftpack
from PySide2 import QtCore, QtGui
from pyueye import ueye


def mean(lst):
    return sum(lst) / len(lst)


class start_position(QtCore.QThread):
    changePixmap = QtCore.Signal(QtGui.QImage)
    changePixmap2 = QtCore.Signal(QtGui.QImage)
    angle = QtCore.Signal(int)
    lines = QtCore.Signal(int)
    val = QtCore.Signal(tuple)
    White = QtCore.Signal(float)

    def __init__(self, parent=None):
        self.parent = parent
        self.exposure = 50.0
        self.gain = 100
        self.exposure, self.gain = functions.Set_Values(
            self.parent.cam, self.exposure, self.gain, 114, True)
        self.img = None
        super().__init__()

    def run(self):
        ImageData = np.zeros((480, 640), dtype=np.uint8)
        while True:
            if self.parent.ret == 0:
                functions.CopyImg(self.parent.cam, ImageData, self.parent.pcImgMem, self.parent.pid)
                self.msleep(100)
                self.exposure, self.gain = functions.Get_Values(
                    self.parent.cam, self.exposure)
                tup = (self.exposure, self.gain)
                self.val.emit(tup)
                self.img = ImageData.copy()
                self.img = np.roll(self.img, -40, axis=1)
                self.img = np.delete(self.img, np.s_[480:640], axis=1)

                unique, counts = np.unique(self.img, return_counts=True)
                x = dict(zip(unique, counts))
                x = {i: x.get(i, 0) for i in range(256)}
                z = [x.get(i) * i for i in range(256)]
                y = x.get(255)
                i = 0
#                while y < 25:
#                    y = x.get(255-i)
#                    i += 1
#                self.White.emit((y, 255 - i, functions.round(mean(z))))
                self.White.emit(functions.round(np.mean(self.img)))

                dft = functions.dft(self.img)
                fft = functions.fft_cv2(dft)
                fft = functions.fft_shift_py(
                    fft.astype(np.float64)).astype(np.uint8)
                row, col = fft.shape
                h_fft, w_fft = fft.shape
                row, col = int(row / 2), int(col / 2)
                tmp_value = 50
                section = fft[row - tmp_value:row +
                              tmp_value, col - tmp_value:col + tmp_value]
                h_sec, w_sec = section.shape
                section = np.ascontiguousarray(section)
                points = functions.maxi(section, 190, 3, 0)
                tmp = 0
                self.index = 0
                for item in points:
                    if section[tuple(item)] > tmp:
                        self.index = tuple(item)
                section = cv2.cvtColor(section, cv2.COLOR_GRAY2BGR)
                section[self.index] = [0, 0, 255]
                section = functions.resize(
                    section, h_fft / h_sec, w_fft / w_sec)
                self.img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2BGR)
                res = np.concatenate((self.img, section), axis=0)
                convertToQtFormat = qimage2ndarray.array2qimage(
                    res).rgbSwapped()
                p = convertToQtFormat.scaled(
                    self.parent.bild_width,
                    self.parent.bild_height,
                    QtCore.Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                # angle + lines
                x_0 = int(w_sec / 2)
                y_0 = int(h_sec / 2)
                try:
                    x = self.index[1]
                    y = self.index[0]
                    dx = x - x_0
                    dy = -1 * (y - y_0)
                    angle = math.atan2(dy, dx) * 180 / math.pi
                    angle = round(angle, 2)
                    self.angle.emit(angle)
                    self.image = functions.rotate_image(
                        self.img, angle, row, col)
                    self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

                    tmp = int(self.image.shape[0] / 2)
                    b = self.image[tmp]
                    N = 5
                    length = len(b)
                    procent = int(length / 100)
                    x = np.arange(length)
                    tmp = b[0:procent]
                    mean1 = np.mean(tmp)
                    tmp = b[-1 - procent + 1:]
                    mean2 = np.mean(tmp)
                    n = mean1
                    m = (mean2 - n) / (x[-1])
                    b_min = m * x + n
                    b = b.astype(np.float64)
                    b -= b_min
                    W = scipy.fftpack.fftfreq(b.size, d=x[1] - x[0])
                    signal = scipy.fftpack.rfft(b)
                    thresh = 1 / (2 * N * (x[1] - x[0]))
                    signal[(W >= thresh)] = 0
                    signal[(W <= -thresh)] = 0
                    b = scipy.fftpack.irfft(signal) + b_min
                    N = 51
                    O = 11
                    b = scipy.signal.savgol_filter(b, N, O)
                    temp = scipy.signal.find_peaks(b, prominence=10)
                    result = len(temp[0])
                    self.lines.emit(result)

                    dft = functions.dft(self.image)
                    fft = functions.fft_cv2(dft)
                    fft = functions.fft_shift_py(
                        fft.astype(np.float64)).astype(np.uint8)
                    row, col = fft.shape
                    h_fft, w_fft = fft.shape
                    row, col = int(row / 2), int(col / 2)
                    tmp_value = 50
                    section = fft[row - tmp_value:row +
                                  tmp_value, col - tmp_value:col + tmp_value]
                    h_sec, w_sec = section.shape
                    section = np.ascontiguousarray(section)
                    section = functions.resize(
                        section, h_fft / h_sec, w_fft / w_sec)
                    section = cv2.cvtColor(section, cv2.COLOR_GRAY2BGR)

                    self.image = cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)
                    res = np.concatenate((self.image, section), axis=0)
                    convertToQtFormat = qimage2ndarray.array2qimage(
                        res).rgbSwapped()
                    p = convertToQtFormat.scaled(
                        self.parent.bild_width,
                        self.parent.bild_height,
                        QtCore.Qt.KeepAspectRatio)
                    self.changePixmap2.emit(p)
                except (IndexError, TypeError):
                    pass
            if self.parent.cam_off is True:
                break
#            self.msleep(33)
