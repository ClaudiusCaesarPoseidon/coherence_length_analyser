import os
from ...lib import functions
from ..widgets import Dialog
from PySide2 import QtCore, QtWidgets, QtGui
from ConvertQt import uic


class Dialogg(Dialog):
    """dialog which return diffrent values"""

    def __init__(self, parent=None):
        """load widget from ui file, connect signals to slots and initialise"""\
            """class attribute"""
        super().__init__()
        self.parent = parent
        file = functions.resource_path(os.path.join("ui", "dialog.ui"))
        uic.loadUi(file, self)
        tmp = self.Again.findText(self.parent.Windows.currentText())
        self.Again.removeItem(tmp)
        self.Ja.clicked.connect(self.ja)
        self.Nein.clicked.connect(self.nein)
        self.setFixedSize(self.size())
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint)
        self.resized.connect(self.set_size)

    def ja(self):
        self.done(10)

    def nein(self):
        self.done(1)

    def choose_again(self):
        self.done(7)

    def set_size(self):
        self.height = int(self.geometry().height())
        self.width = int(self.geometry().width())
        fontsize = (self.height / 20)
        font_button = QtGui.QFont()
        font_button.setPointSize(fontsize)
        fontsize = (self.height / 20)
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
