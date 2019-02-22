from matplotlib.figure import Figure
import math
import scipy.signal
import matplotlib.ticker as ticker
from ...lib import functions
from pymediainfo import MediaInfo
from scipy.signal import savgol_filter
import os
import cv2
import numpy as np
from PySide2 import QtCore, QtGui


round = functions.round
X = functions.x


def mean(*args):
    return sum(args) / len(args)


class everything(QtCore.QThread):
    changePixmap = QtCore.Signal(QtGui.QImage)

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.glubber = None

    def run(self):
        viode = False
        path = self.parent.fname
        np.set_printoptions(threshold=np.nan)
        if os.path.exists(path):
            fileInfo = MediaInfo.parse(path)
            for track in fileInfo.tracks:
                if track.track_type == "Video":
                    viode = True
                    break
            else:
                print("Please choose a correct File.")
            if viode is True:
                print("Please wait.")
                cap = cv2.VideoCapture(path)
                i = 0
                while True:
                    ret, frame = cap.read()
                    if ret is False:
                        break
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
                    self.section = section.copy()
                    if self.glubber is None:
                        self.glubber = self.section.copy()
                    else:
                        self.glubber = np.dstack((self.glubber, self.section))
                height, width, dump = self.glubber.shape
                self.figure = Figure()
                with open("glubber.txt", "w+") as file:
                    for i in range(height):
                        for j in range(width):
                            self.ax = self.figure.add_subplot(111)
                            item = self.glubber[i, j]
                            break

                            N = 10
                            length = item.shape[0]
                            x = X(0, length, 0.11)
                            procent = int(length / 100)
                            if procent >= 1:
                                tmp = item[0:procent]
                                mean1 = np.mean(tmp)
                                tmp = item[-1 - procent + 1:]
                                mean2 = np.mean(tmp)
                                n = mean1
                                m = (mean2 - n) / (x[-1])
                                x_a = np.array(x)
                                data_a_min = m * x_a + n
                                item = item.astype(np.float64)
                                item -= data_a_min
                                W = scipy.fftpack.fftfreq(
                                    item.size, d=x[1] - x[0])
                                signal = scipy.fftpack.rfft(item)
                                thresh = 1 / (2 * N * (x[1] - x[0]))
                                signal[(W >= thresh)] = 0
                                signal[(W <= -thresh)] = 0
                                item = scipy.fftpack.irfft(signal) + data_a_min
                            N = 51
                            O = 11
                            if len(item) < N:
                                N = len(item)
                            if O >= N:
                                O = N - 1
                            item = savgol_filter(item, N, O)

                            max_ = np.amax(item)
                            if item.shape[0] >= 100:
                                procent = int(item.shape[0] / 100)
                                tmp = item[0:procent]
                                mean1 = np.mean(tmp)
                                tmp = item[-1 - procent + 1:]
                                mean2 = np.mean(tmp)
                                min_ = mean(mean1, mean2)
                            else:
                                min_ = np.amin(item)
                            thresh = (max_ - min_) / math.e + min_
                            s = -1
                            e = 0
                            _max = np.argmax(item)
                            k = 0
                            for item in self.glubber[i, j]:
                                if item > thresh and s == -1:
                                    s = k
                                if item < thresh and s != -1 and e == 0 and k > _max:
                                    e = k
                                k += 1

                            data_max = [max_] * len(item)
                            data_min = [min_] * len(item)
                            data_threshold = [thresh] * len(item)
                            x = np.arange(0, 1819)
                            self.ax.plot(x, item, color="black")
                            self.ax.axvline(s * 0.11, color="green")
                            self.ax.axvline(e * 0.11, color="green")
                            self.ax.plot(x, data_threshold, color="red")
                            self.ax.plot(x, data_max, color="cyan")
                            self.ax.plot(x, data_min, color="magenta")
                            self.figure.savefig("%d-%d.png" %
                                                (i, j), format="png")
                            file.write(str(i) +
                                       "\t" +
                                       str(j) +
                                       "\t" +
                                       str(max_) +
                                       "\t" +
                                       str(round(thresh, 2)) +
                                       "\t" +
                                       str(round(min_, 2)) +
                                       "\tlc:" +
                                       str(round(s *
                                                 0.11, 2)) +
                                       "\t" +
                                       str(round(e *
                                                 0.11, 2)) +
                                       "\t" +
                                       str(round((e -
                                                  s) *
                                                 0.11, 2)))
                            if max_ - min_ >= 20 and max_ > 175:
                                file.write("\tx")
                            file.write("\n")
                            self.msleep(10)
                            self.figure.delaxes(self.ax)
                            self.figure.clf()
                print(self.glubber.shape)
        else:
            print("The file is not existent")
