from .dialog import Dialog
import sys
import os
from ...lib import functions
from PyQt5 import QtCore, QtGui, uic, QtWidgets
QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot


class screen_size_dialog(Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.default_stdout = sys.stdout
        self.default_stderr = sys.stderr
        self.setWindowFlags(self.windowFlags() |
                            QtCore.Qt.WindowSystemMenuHint |
                            QtCore.Qt.WindowMinMaxButtonsHint)
        file = functions.resource_path(
            os.path.join("ui", "screen_size_dialog.ui"))
        uic.loadUi(file, self)
        self.OK.clicked.connect(self.close)
        self.resized.connect(self.resize)

    def resize(self):
        self.height = int(self.geometry().height())
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
        self.OK.setMinimumSize(QtCore.QSize(0, int(self.height * 1 / 4)))
        self.OK.setMaximumSize(
            QtCore.QSize(
                16777215, int(
                    self.height * 1 / 4)))
