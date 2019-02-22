from ...lib import functions
import numpy as np
import cv2
import qimage2ndarray
from PySide2 import QtCore, QtGui


class show_fft(QtCore.QThread):
    changePixmap1 = QtCore.Signal(QtGui.QImage)
    changePixmap2 = QtCore.Signal(QtGui.QImage)
    changePixmap3 = QtCore.Signal(QtGui.QImage)
    changePixmap4 = QtCore.Signal(QtGui.QImage)

    def __init__(self, parent=None, filename=None, max_=2):
        super().__init__()
        self.parent = parent
        self.filename = filename
        self.max = max_
        self.ind = None

    def run(self):
        cap = cv2.VideoCapture(self.filename)
        max_ = self.max
        indexes = []
        max_count = 255
        while True:
            ret, frame = cap.read()
            if ret is True:
                img_ori = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                DFT_High = functions.dft(img_ori)
                FFT = functions.fft_cv2(DFT_High)
                FFT = functions.fft_shift_py(
                    FFT.astype(np.float64)).astype(np.uint8)
                row, col = FFT.shape
                DFT_High[0:max_, 0:max_] = 0
                DFT_High[row - max_:row, 0:max_] = 0
                DFT_High[0:max_, col - max_:col] = 0
                DFT_High[row - max_:row, col - max_:col] = 0
                BackTransform = functions.ifft_cv2(DFT_High)
                FFT_High = functions.fft_cv2(DFT_High)
                FFT_High = functions.fft_shift_py(
                    FFT_High.astype(np.float64)).astype(np.uint8)
                FFT = functions.cross(FFT, self.parent.Value.value())
                FFT_High = functions.cross(FFT_High, self.parent.Value.value())

                row, col = FFT.shape
                row, col = int(row / 2), int(col / 2)
                FFT_s = FFT[row - 25:row + 25, col - 25:col + 25]
                FFT_High_s = FFT_High[row - 25:row + 25, col - 25:col + 25]
                points = functions.maxi(
                    FFT_s, max_count, 3, self.parent.Value.value())
                if len(points) > 0:
                    indexes.append(points)
                if self.ind is not None:
                    FFT_s = cv2.cvtColor(FFT_s, cv2.COLOR_GRAY2BGR)
                    FFT_s[self.ind] = [0, 0, 255]
                    FFT_High_s = cv2.cvtColor(FFT_High_s, cv2.COLOR_GRAY2BGR)
                    FFT_High_s[self.ind] = [0, 0, 255]
                    convertToQtFormat1 = qimage2ndarray.gray2qimage(img_ori)
                    convertToQtFormat2 = qimage2ndarray.array2qimage(
                        FFT_s).rgbSwapped()
                    convertToQtFormat3 = qimage2ndarray.array2qimage(
                        FFT_High_s).rgbSwapped()
                    convertToQtFormat4 = qimage2ndarray.gray2qimage(
                        BackTransform)
                else:
                    convertToQtFormat1 = qimage2ndarray.gray2qimage(img_ori)
                    convertToQtFormat2 = qimage2ndarray.gray2qimage(FFT_s)
                    convertToQtFormat3 = qimage2ndarray.gray2qimage(FFT_High_s)
                    convertToQtFormat4 = qimage2ndarray.gray2qimage(
                        BackTransform)
                p1 = convertToQtFormat1.scaled(
                    self.parent.height,
                    self.parent.height,
                    QtCore.Qt.KeepAspectRatio)
                p2 = convertToQtFormat2.scaled(
                    self.parent.height,
                    self.parent.height,
                    QtCore.Qt.KeepAspectRatio)
                p3 = convertToQtFormat3.scaled(
                    self.parent.height,
                    self.parent.height,
                    QtCore.Qt.KeepAspectRatio)
                p4 = convertToQtFormat4.scaled(
                    self.parent.height,
                    self.parent.height,
                    QtCore.Qt.KeepAspectRatio)
                self.changePixmap1.emit(p1)
                self.changePixmap2.emit(p2)
                self.changePixmap3.emit(p3)
                self.changePixmap4.emit(p4)
            else:
                cap = cv2.VideoCapture(self.filename)
                print(max_count, indexes, len(indexes), end="")
                if len(indexes) > 0:
                    print(len(indexes[0]), end="")
                    try:
                        print(indexes[0].shape)
                    except AttributeError:
                        print()
                    self.ind = tuple((indexes[0])[0])
                    break
                else:
                    print()
                max_count -= 1
                indexes = []
            if self.parent.ends is True:
                break
        print(indexes)
