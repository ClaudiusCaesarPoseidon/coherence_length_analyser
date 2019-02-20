from ...lib import functions
import qimage2ndarray
import os
import math
import numpy as np
from PyQt5 import QtCore, QtGui
QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot
round = functions.round
substring_in_list = functions.substring_in_list


def find(array):
    """finds index of first coloured pixel in grayscale image"""
    for tmp in array:
        for item in tmp:
            if np.mean(item) != item[0]:
                return item
    return None


class angle_thread(QtCore.QThread):
    changePixmap = QtCore.Signal(QtGui.QImage)

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.image = self.parent.res
        self.label_height = self.parent.label_height
        self.direc_path = self.parent.direc_path
        file = os.path.basename(self.parent.fname)
        self.dirname = os.path.basename(os.path.dirname(self.parent.fname))
        coherence_length_file = os.path.join(
            os.path.dirname(self.parent.fname), "coherence_length.txt")
        self.value = int(file.split('_')[-1].split('.')[0])
        self.angle = None
        self.coherence_length = str(None)
        try:
            with open(coherence_length_file, "r") as file:
                tmp = file.read()
                tmp = tmp.split("\n")
                tmp[:] = [x for x in tmp if self.parent.Windows.currentText() in x]
                tmp = ';\t'.join(tmp)
                self.coherence_length = tmp
        except FileNotFoundError:
            pass

    def run(self):
        x_0 = self.value
        y_0 = self.value
        tmp = find(self.image)
        xx = np.where(self.image == tmp)
        y = [xx[0][0]][0]
        x = [xx[1][0]][0]
        if y == y_0:
            y = [xx[0][1]][0]
        if x == y_0:
            x = [xx[1][1]][0]
#        y2 = y_0
#        x2 = x_0
#        y1 = y
#        x1 = x
#        print(x,x_0,y,y_0)

#        def line_eq(X):
#            m = (y2 - y1) / (x2 - x1)
#            return m * (X - x1) + y1
#        line = np.vectorize(line_eq)
#        x_n = np.arange(0, self.image.shape[1])
#        y_n = line(x_n).astype(np.uint)
#        if x2 != x1:
#            cv2.line(self.image, (x_n[0], y_n[0]), (x_n[-1], y_n[-1]), (0, 0, 255))
#        else:
#            cv2.line(self.image, (x1, 0), (x2, self.image.shape[0]), (0, 0, 255))

        dx = x - x_0
        dy = -1 * (y - y_0)
        angle = math.atan2(dy, dx) * 180 / math.pi
        angle = round(angle, 2)
        if angle < 0:
            angle += 180
        with open(os.path.join(self.direc_path, "angles.txt"), "a+") as file:
            file.seek(0)
            dump = file.read().split("\n")
        if dump[0] == '':
            del dump[0]
#        dump = []
        i = 0
        for line in dump:
            if self.dirname in line:
                dump[i] = self.dirname + "\t" + \
                    str(angle) + "\t" + self.coherence_length
            i += 1
        if substring_in_list(self.dirname, dump) is True:
            pass
        else:
            dump.append(self.dirname + "\t" + str(angle) +
                        "\t" + self.coherence_length)
        with open(os.path.join(self.direc_path, "angles.txt"), "w") as file:
            file.write("\n".join(dump))

        convertToQtFormat = qimage2ndarray.array2qimage(
            self.image).rgbSwapped()
        p = convertToQtFormat.scaled(
            self.label_height, self.label_height, QtCore.Qt.KeepAspectRatio)
        self.changePixmap.emit(p)
        self.angle = angle
