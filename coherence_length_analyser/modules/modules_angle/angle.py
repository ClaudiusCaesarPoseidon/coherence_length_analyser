from PIL import Image
import numpy as np
import os
from .search_folder import search_folder
from .angle_thread import angle_thread
import cv2
import qimage2ndarray
from ...lib import functions
from ..eigen_widgets import Widgetb
from PySide2 import QtCore, QtWidgets, QtGui, QtTest
from ConvertQt import uic


default_imread = cv2.imread


# replaces the imread function, which can not read images whose path
# contains non ASCII characters
def imread(path, mode=1):
    if path.isascii() is True:
        return default_imread(path, mode)
    else:
        if mode == 0:
            return np.asarray(Image.open(path).convert('L'))
        else:
            return np.asarray(Image.open(path).convert('RGB'))


class Angle(Widgetb):
    def __init__(self, parent=None, config=None):
        """load widget from ui file, connect signals to slots and initialise"""\
            """class attribute"""
        cv2.imread = imread
        super().__init__()
        self.parent = parent
        self.config = config
        if self.parent is not None:
            self.direc_path = self.parent.direc_path
        # loads the widgets from the ui file
        file = functions.resource_path(os.path.join("ui", "angle.ui"))
        uic.loadUi(file, self)
        self.resized.connect(self.set_Size)
        self.Close.clicked.connect(self.close)
        self.Open.clicked.connect(self.open_image)
        self.Evaluate.clicked.connect(self.evaluate)
        self.Evaluate_All.clicked.connect(self.evaluate_all_start)
        if os.path.exists(os.path.join(self.direc_path, "converted_videos")):
            self.Evaluate_All.setEnabled(True)
            self.Windows.setEnabled(True)
        self.fname = None
        self.files = None
        self.i = 0
        self.folder = None
        self.Open_Folder.clicked.connect(self.open_folder)

    def set_Size(self):
        # sets the fontsize of the widgets according to window size
        self.height = int(self.geometry().height())
        self.width = int(self.geometry().width())
        self.label_height = int(self.height / 2)
        self.Label_Image.setMinimumSize(
            QtCore.QSize(self.label_height, self.label_height))
        self.Label_Result.setMinimumSize(
            QtCore.QSize(self.label_height, self.label_height))
        self.Label_Image.setMaximumSize(
            QtCore.QSize(self.label_height, self.label_height))
        self.Label_Result.setMaximumSize(
            QtCore.QSize(self.label_height, self.label_height))
        fontsize = (self.height / 50)
        font_button = QtGui.QFont()
        font_button.setPointSize(fontsize)
        fontsize = (self.height / 75)
        if fontsize <= 8:
            fontsize = 8
        if fontsize >= 16:
            fontsize = 16
        font_text = QtGui.QFont()
        font_text.setPointSize(fontsize)
        for item in self.findChildren(QtWidgets.QPushButton):
            item.setFont(font_button)
        for item in self.findChildren(QtWidgets.QLineEdit):
            item.setFont(font_text)
        for item in self.findChildren(QtWidgets.QPlainTextEdit):
            item.setFont(font_text)
        for item in self.findChildren(QtWidgets.QComboBox):
            item.setFont(font_text)
        self.Console.setMinimumSize(QtCore.QSize(0, 4 / 8 * self.height))

    def open_image(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open file', os.path.join(
                self.direc_path, "converted_videos"))[0]
        if functions.is_image(self.fname) is False:
            self.fname = None
            self.Evaluate.setEnabled(False)
            return None
        self.Evaluate.setEnabled(True)
        self.res = cv2.imread(self.fname)
        self.res = functions.rotate_image(self.res, 90)
        cv2.imshow('frame', self.res)
        cv2.waitKey()
        cv2.destroyAllWindows()
        convertToQtFormat = qimage2ndarray.array2qimage(self.res).rgbSwapped()
        p = convertToQtFormat.scaled(
            self.label_height, self.label_height, QtCore.Qt.KeepAspectRatio)
        self.setImage(p)

    def open_folder(self):
        self.folder = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Directory", os.path.join(
                self.direc_path, "converted_videos"))
        if self.folder == '':
            self.folder = None

    @QtCore.Slot(QtGui.QImage)
    def setImage(self, image):
        self.Label_Image.setPixmap(QtGui.QPixmap.fromImage(image))

    @QtCore.Slot(QtGui.QImage)
    def setImage2(self, image):
        self.Label_Result.setPixmap(QtGui.QPixmap.fromImage(image))

    def evaluate(self):
        self.Open.setEnabled(False)
        self.Evaluate.setEnabled(False)
        self.th = angle_thread(self)
        self.th.changePixmap.connect(self.setImage2)
        self.th.finished.connect(self.fin)
        self.th.start()

    def evaluate_all_start(self):
        self.Open.setEnabled(False)
        self.Evaluate.setEnabled(False)
        self.Evaluate_All.setEnabled(False)
        if self.files is None:
            if self.folder is None:
                path = os.path.join(self.direc_path, "converted_videos")
            else:
                path = os.path.join(
                    self.direc_path, "converted_videos", self.folder)
            s = search_folder(path, self.Windows.currentText())
            self.files = s.file_names
            if self.files.size == 0:
                print("There are no measurents in the folder.")
                return self.evaluate_all_end()
            self.max_ = len(self.files[1])
        self.fname = self.files[0][self.i]
        self.res = cv2.imread(self.fname)
        convertToQtFormat = qimage2ndarray.array2qimage(self.res).rgbSwapped()
        p = convertToQtFormat.scaled(
            self.label_height, self.label_height, QtCore.Qt.KeepAspectRatio)
        self.setImage(p)
        self.th = angle_thread(self)
        self.th.changePixmap.connect(self.setImage2)
        self.th.finished.connect(self.evaluate_all_mid)
        self.th.start()

    def evaluate_all_mid(self):
        print(self.files[1][self.i], self.th.angle, self.th.coherence_length)
        self.i += 1
        QtTest.QTest.qWait(250)
        if self.i >= self.max_:
            return self.evaluate_all_end()
        return self.evaluate_all_start()

    def evaluate_all_end(self):
        self.i = 0
        self.Open.setEnabled(True)
        self.Evaluate_All.setEnabled(True)
        self.files = None

    def fin(self):
        print(self.th.angle)
        self.Open.setEnabled(True)
        self.Evaluate.setEnabled(True)
