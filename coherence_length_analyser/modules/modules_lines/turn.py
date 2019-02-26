import os
from .count_lines import count_thread
from .turn_thread import turn_thread
from .search_folder import search_folder
from .copy import copy_thread
from .convert_thread import convert_thread
from ...lib import functions
from ..eigen_widgets import Widgetb
from PySide2 import QtCore, QtWidgets, QtGui
from ConvertQt import uic


class Count(Widgetb):
    def __init__(self, parent=None, config=None):
        super().__init__()
        self.parent = parent
        self.config = config
        if self.parent is not None:
            self.direc_path = self.parent.direc_path
        file = functions.resource_path(os.path.join("ui", "turn.ui"))
        uic.loadUi(file, self)
        self.resized.connect(self.set_Size)
        self.fname = None
        self.files = None
        self.i = 0
        self.cont = False
        if os.path.exists(os.path.join(self.direc_path, "lines_csv")) is True:
            self.Count.setDisabled(False)
        if os.path.exists(os.path.join(self.direc_path, "lines")) is True:
            self.Start.setDisabled(False)
        if os.path.exists(os.path.join(self.direc_path, "lines.txt")) is True:
            self.Convert.setDisabled(False)
        self.Evaluate.setDisabled(True)
        self.Evaluate.setVisible(False)
        self.Next.setDisabled(True)
        self.Next.setVisible(False)
        self.Row.setDisabled(True)
        self.end_loop = False
        self.folder = None

        self.Copy.clicked.connect(self.copy)
        self.Start.clicked.connect(self.start_turning)
        self.Evaluate.clicked.connect(self.continue_)
        self.Next.clicked.connect(self.continue_)
        self.Count.clicked.connect(self.count)
        self.Open.clicked.connect(self.open_folder)

    def set_Size(self):
        self.height = self.geometry().height()
        self.img_height = self.height // 2
        fontsize = (self.height / 75)
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
        self.Start.setFont(font_button)
        self.Evaluate.setFont(font_button)
        self.Next.setFont(font_button)
        self.Copy.setFont(font_button)
        self.Close.setFont(font_button)
        self.Count.setFont(font_button)
        self.Console.setFont(font_text)

    def open_folder(self):
        self.folder = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Directory", os.path.join(
                self.direc_path, "converted_videos"))
        if self.folder == '':
            self.folder = None

    def copy(self):
        self.Start.setDisabled(True)
        self.Copy.setDisabled(True)
        self.Convert.SetDisabled(True)
        self.Count.setDisabled(True)
        if self.folder is None:
            path = os.path.join(self.direc_path, "converted_videos")
        else:
            path = os.path.join(
                self.direc_path, "converted_videos", self.folder)
        self.s = search_folder(path)
        self.files = self.s.file_names[0]
        if self.files.size == 0:
            print("There are no measurents in the folder.")
            return self.turn_end()
        self.th = copy_thread(self)
        self.th.start()
        self.th.finished.connect(self.turn_end)

    def continue_(self):
        self.cont = True

    def start_turning(self):
        self.Start.setDisabled(True)
        self.Start.setVisible(False)
        self.Evaluate.setVisible(True)
        self.Next.setVisible(True)
        self.Copy.setDisabled(True)
        self.Count.setDisabled(True)
        self.Convert.setDisabled(True)

        self.path = os.path.join(self.direc_path, "lines")
        self.images = [os.path.join(self.path, item)
                       for item in os.listdir(self.path)]
        with open(os.path.join(self.direc_path, "angles.txt"), "r") as file:
            tmp = [x.split("\t") for x in file.read().split("\n")]
        for item in tmp:
            del item[-1]
        self.angles = tmp
        self.turn()

    def turn(self):
        self.th = turn_thread(self)
        self.th.changePixmap.connect(self.setImage)
        self.th.changePixmap2.connect(self.setImage2)
        self.th.finished.connect(self.turn_end)
        self.th.start()

    def turn_end(self):
        if os.path.exists(os.path.join(self.direc_path, "lines")) is True:
            self.Start.setDisabled(False)
        self.Start.setVisible(True)
        self.Evaluate.setDisabled(True)
        self.Evaluate.setVisible(False)
        self.Next.setDisabled(True)
        self.Next.setVisible(False)
        self.Copy.setDisabled(False)
        if os.path.exists(os.path.join(self.direc_path, "lines_csv")) is True:
            self.Count.setDisabled(False)
        if os.path.exists(os.path.join(self.direc_path, "lines.txt")) is True:
            self.Convert.setDisabled(False)

    def count(self):
        self.Start.setDisabled(True)
        self.Copy.setDisabled(True)
        self.Count.setDisabled(True)
        self.Convert.setDisabled(True)
        self.th = count_thread(self)
        self.th.start()
        self.th.finished.connect(self.turn_end)

    def convert(self):
        self.Start.setDisabled(True)
        self.Copy.setDisabled(True)
        self.Count.setDisabled(True)
        self.Convert.setDisabled(True)
        path_in = os.path.join(self.direc_path, "lines.txt")
        path_out = os.path.join(self.direc_path, "lines.csv")
        self.th = convert_thread(self, path_in, path_out)
        self.th.finished.connect(self.turn_end)


    @QtCore.Slot(QtGui.QImage)
    def setImage(self, image):
        self.Image.setPixmap(QtGui.QPixmap.fromImage(image))

    @QtCore.Slot(QtGui.QImage)
    def setImage2(self, image):
        self.Turned.setPixmap(QtGui.QPixmap.fromImage(image))

    def end_(self):
        self.is_end()

    def is_end(self):
        self.end_loop = True
