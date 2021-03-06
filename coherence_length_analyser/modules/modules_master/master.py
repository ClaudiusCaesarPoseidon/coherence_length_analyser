# pylint: disable=line-too-long
# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=C0411
# pylint: disable=C0412
# pylint: disable=C0413
# pylint: disable=R0902
# pylint: disable=R0912
# pylint: disable=R0914
# pylint: disable=R0915
# pylint: disable=E1101
from .make_jupyter_widget import make_jupyter_widget
from ..widgets import Widget
from ..turn import Count
from ..angle import Angle
from ..camera import Camera
from ..analyser import Analyser
import os
import sys
from ...lib import functions
from PySide2 import QtCore, QtWidgets, QtGui
from ConvertQt import uic


class Master(Widget):
    """GUI for choosing the subprograms"""

    def __init__(self, config=None):
        super().__init__()
        # loads the widgets from the ui file
        file = functions.resource_path(os.path.join("ui", "master.ui"))
        uic.loadUi(file, self)
        self.Close.clicked.connect(self.close)
        self.Analyse_Pictures.clicked.connect(self.analyse)
        self.Take_Pictures.clicked.connect(self.camera)
        self.Evaluate.clicked.connect(self.evaluate)
        self.Count.clicked.connect(self.count)
        self.resized.connect(self.set_Size)
        self.config = config
        self.height = int(self.geometry().height())
        self.width = int(self.geometry().width())
        self.fontsize = None
        user_path = os.path.expanduser("~")
        os.makedirs(os.path.join(user_path, "OUT",
                                 "coherence_length_analyser"), exist_ok=True)
        self.direc_path = os.path.join(
            user_path, "OUT", "coherence_length_analyser")
        self.sys_drive = os.path.abspath("/usr/bin/local")
        self.win = None
        self.win_width, self.win_height = None, None
        self.ipy = False
        if self.config['ipython'] is True:
            self.ipy = True
            self.jupyter_widget = make_jupyter_widget()
            self.gridLayout_4.addWidget(self.jupyter_widget, 0, 1, 1, 1)

    def set_Size(self):
        # sets the fontsize of the widgets according to window size
        self.height = int(self.geometry().height())
        self.width = int(self.geometry().width())
        fontsize = (self.height / 20)
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

    def analyse(self):
        # shows the window according to the settings
        self.win = Analyser(self, self.config)
        self.win.setModal(True)
        if self.config['windowed'] is False:
            self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.win.showFullScreen()
        else:
            self.hide()
            if self.config['border'] is False:
                self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            if self.config['fullscreen'] is True:
                self.win.showMaximized()
            else:
                self.win.resize(int(self.win_width * 3 / 4),
                                int(self.win_height * 3 / 4))
                self.win.show()
        self.win.exec_()
        if self.config['windowed'] is True:
            self.show()
        self.closed()

    def camera(self):
        # shows the window according to the settings
        self.win = Camera(self, self.config)
        self.win.setModal(True)
        if self.config['windowed'] is False:
            self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.win.showFullScreen()
        else:
            self.hide()
            if self.config['border'] is False:
                self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            if self.config['fullscreen'] is True:
                self.win.showMaximized()
            else:
                self.win.resize(int(self.win_width * 3 / 4),
                                int(self.win_height * 3 / 4))
                self.win.show()
        self.win.exec_()
        if self.config['windowed'] is True:
            self.show()
        self.closed()

    def evaluate(self):
        # shows the window according to the settings
        self.win = Angle(self, self.config)
        self.win.setModal(True)
        if self.config['windowed'] is False:
            self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.win.showFullScreen()
        else:
            self.hide()
            if self.config['border'] is False:
                self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            if self.config['fullscreen'] is True:
                self.win.showMaximized()
            else:
                self.win.resize(int(self.win_width * 3 / 4),
                                int(self.win_height * 3 / 4))
                self.win.show()
        self.win.exec_()
        if self.config['windowed'] is True:
            self.show()

    def count(self):
        # shows the window according to the settings
        self.win = Count(self, self.config)
        self.win.setModal(True)
        if self.config['windowed'] is False:
            self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.win.showFullScreen()
        else:
            self.hide()
            if self.config['border'] is False:
                self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            if self.config['fullscreen'] is True:
                self.win.showMaximized()
            else:
                self.win.resize(int(self.win_width * 3 / 4),
                                int(self.win_height * 3 / 4))
                self.win.show()
        self.win.exec_()
        if self.config['windowed'] is True:
            self.show()

    def closed(self):
        # ends all threads of the windows and resets stdout
        sys.stdout = self.win.default_stdout
        sys.stderr = self.win.default_stderr
        self.activateWindow()
        self.win.end_()
