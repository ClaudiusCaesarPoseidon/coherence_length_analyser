from PIL import Image
import qimage2ndarray
from ...lib import functions
import cv2
import os
import shutil
import numpy as np
from PySide2 import QtCore, QtGui, QtTest


default_imread = cv2.imread


def imread(path, mode=1):
    if functions.isascii(path) is True:
        return default_imread(path, mode)
    else:
        if mode == 0:
            return np.asarray(Image.open(path).convert('L'))
        else:
            return np.asarray(Image.open(path).convert('RGB'))


class turn_thread(QtCore.QThread):
    changePixmap = QtCore.Signal(QtGui.QImage)
    changePixmap2 = QtCore.Signal(QtGui.QImage)

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        if self.parent is not None:
            self.direc_path = self.parent.direc_path

    def run(self):
        cv2.imread = imread
        new_direc = os.path.join(self.direc_path, "lines_csv")
        try:
            shutil.rmtree(new_direc)
        except FileNotFoundError:
            pass
        if os.path.exists(new_direc) is False:
            functions.build_directory(new_direc)
        for item, file in zip(self.parent.images, self.parent.angles):
            if self.parent.end_loop is True:
                break
            self.parent.Evaluate.setDisabled(False)
            self.parent.Next.setDisabled(True)
            self.parent.Row.setDisabled(True)
            name, angle = file[:2]
            self.img = cv2.imread(item)
            row, col = self.img.shape[:-1]
            row, col = row // 2, col // 2
            while True:
                if self.parent.end_loop is True:
                    break
                self.img = cv2.imread(item)
                self.image = self.img.copy()
                convertToQtFormat = qimage2ndarray.array2qimage(
                    self.img).rgbSwapped()
                p = convertToQtFormat.scaled(
                    self.parent.img_height,
                    self.parent.img_height,
                    QtCore.Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                QtTest.QTest.qWait(10)
                if self.parent.cont is True:
                    break
            self.parent.Evaluate.setDisabled(True)
            self.parent.Next.setDisabled(False)
            self.parent.cont = False
            self.parent.cont = True
            self.img = functions.rotate_image(self.img, float(angle), row, col)
            row = self.img.shape[0]
            roww = row // 2
            self.parent.Row.setMaximum(row - 1)
            convertToQtFormat = qimage2ndarray.array2qimage(
                self.img).rgbSwapped()
            p = convertToQtFormat.scaled(
                self.parent.img_height,
                self.parent.img_height,
                QtCore.Qt.KeepAspectRatio)
            self.changePixmap2.emit(p)
            while True:
                self.parent.Row.setDisabled(False)
                self.parent.Row.setValue(roww)
                row = self.parent.Row.value()
                img = self.img.copy()
                tmp = img[row].copy()
                x = np.arange(tmp.shape[0])
                named = os.path.join(
                    self.direc_path, "lines_csv", name + ".csv")
                functions.save_txt(named, np.column_stack((x, tmp)))
                img[row, 0:-1] = [0, 0, 255]
                convertToQtFormat = qimage2ndarray.array2qimage(
                    img).rgbSwapped()
                p = convertToQtFormat.scaled(
                    self.parent.img_height,
                    self.parent.img_height,
                    QtCore.Qt.KeepAspectRatio)
                self.changePixmap2.emit(p)
                if self.parent.end_loop is True:
                    break
                QtTest.QTest.qWait(10)
                if self.parent.cont is True:
                    break
            self.parent.cont = False
            self.parent.cont = True
