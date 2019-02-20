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
from ..eigen_widgets import Widget
from ..turn import Count
from ..angle import Angle
from ..register import Register
from ..camera import Camera
from ..analyser import Analyser
import os
import sys
from ...lib import functions
import shutil
from PyQt5 import QtCore, QtWidgets, QtGui, uic
QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot
is_admin = functions.is_admin
build_directory = functions.build_directory


class Master(Widget):
    def __init__(self, config=None):
        super().__init__()
        file = functions.resource_path(os.path.join("ui", "master.ui"))
        uic.loadUi(file, self)
        self.Close.clicked.connect(self.close)
        self.Analyse_Pictures.clicked.connect(self.analyse)
        self.Take_Pictures.clicked.connect(self.camera)
        self.Register.clicked.connect(self.register)
        self.Register.setVisible(False)
        self.Evaluate.clicked.connect(self.evaluate)
        self.Count.clicked.connect(self.count)
        if is_admin() is True:
            self.Register.setVisible(True)
        self.resized.connect(self.set_Size)
        self.config = config
        self.height = int(self.geometry().height())
        self.width = int(self.geometry().width())
        self.fontsize = None
        user_path = os.path.expanduser("~")
        if os.path.exists(
            os.path.join(
                user_path,
                "OUT",
                "coherence_length_analyser")) is False:
            build_directory(os.path.join(user_path, "OUT",
                                         "coherence_length_analyser"))
        self.direc_path = os.path.join(
            user_path, "OUT", "coherence_length_analyser")
        sys_drive = os.path.join(os.getenv("SystemDrive"), os.sep)
        if os.path.exists(
            os.path.join(
                sys_drive,
                "coherence_length_analyser",
                "login.txt")):
            shutil.copyfile(
                os.path.join(
                    sys_drive,
                    "coherence_length_analyser",
                    "login.txt"),
                os.path.join(
                    user_path,
                    "coherence_length_analyser",
                    "login.txt"))
        self.win = None
        self.win_width, self.win_height = None, None
        self.Console.setVisible(False)
        self.ipy = False
        if self.config['ipython'] is True:
            self.ipy = True
            self.jupyter_widget = make_jupyter_widget()
            self.gridLayout_4.addWidget(self.jupyter_widget, 0, 1, 1, 1)

    def set_Size(self):
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
        self.win = Analyser(self, self.config)
        self.win.setModal(True)
        if bool(self.config['windowed']) is False:
            self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.win.showFullScreen()
        else:
            self.hide()
            if bool(self.config['border']) is False:
                self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            if bool(self.config['fullscreen']) is True:
                self.win.showMaximized()
            else:
                self.win.resize(int(self.win_width * 3 / 4),
                                int(self.win_height * 3 / 4))
                self.win.show()
        self.win.exec_()
        if bool(self.config['windowed']) is True:
            self.show()
        self.closed()

    def camera(self):
        self.win = Camera(self, self.config)
        self.win.setModal(True)
        if bool(self.config['windowed']) is False:
            self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.win.showFullScreen()
        else:
            self.hide()
            if bool(self.config['border']) is False:
                self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            if bool(self.config['fullscreen']) is True:
                self.win.showMaximized()
            else:
                self.win.resize(int(self.win_width * 3 / 4),
                                int(self.win_height * 3 / 4))
                self.win.show()
        self.win.exec_()
        if bool(self.config['windowed']) is True:
            self.show()
        self.closed()

    def register(self):
        self.win = Register(self, self.config)
        self.win.setModal(True)
        if bool(self.config['windowed']) is False:
            self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.win.showFullScreen()
        else:
            self.hide()
            if bool(self.config['border']) is False:
                self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            if bool(self.config['fullscreen']) is True:
                self.win.showMaximized()
            else:
                self.win.resize(int(self.win_width * 3 / 4),
                                int(self.win_height * 3 / 4))
                self.win.show()
        self.win.exec_()
        if bool(self.config['windowed']) is True:
            self.show()
        sys_drive = os.path.join(os.getenv("SystemDrive"), os.sep)
        user_path = os.path.expanduser("~")
        if os.path.exists(
            os.path.join(
                sys_drive,
                "coherence_length_analyser",
                "login.txt")):
            shutil.copyfile(
                os.path.join(
                    sys_drive,
                    "coherence_length_analyser",
                    "login.txt"),
                os.path.join(
                    user_path,
                    "coherence_length_analyser",
                    "login.txt"))
        self.closed()

    def evaluate(self):
        self.win = Angle(self, self.config)
        self.win.setModal(True)
        if bool(self.config['windowed']) is False:
            self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.win.showFullScreen()
        else:
            self.hide()
            if bool(self.config['border']) is False:
                self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            if bool(self.config['fullscreen']) is True:
                self.win.showMaximized()
            else:
                self.win.resize(int(self.win_width * 3 / 4),
                                int(self.win_height * 3 / 4))
                self.win.show()
        self.win.exec_()
        if bool(self.config['windowed']) is True:
            self.show()

    def count(self):
        self.win = Count(self, self.config)
        self.win.setModal(True)
        if bool(self.config['windowed']) is False:
            self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.win.showFullScreen()
        else:
            self.hide()
            if bool(self.config['border']) is False:
                self.win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            if bool(self.config['fullscreen']) is True:
                self.win.showMaximized()
            else:
                self.win.resize(int(self.win_width * 3 / 4),
                                int(self.win_height * 3 / 4))
                self.win.show()
        self.win.exec_()
        if bool(self.config['windowed']) is True:
            self.show()

    def closed(self):
        sys.stdout = self.win.default_stdout
        sys.stderr = self.win.default_stderr
        self.activateWindow()
        self.win.end_()
