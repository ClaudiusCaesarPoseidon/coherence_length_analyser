from screeninfo import get_monitors
from .show_fft import show_fft
from ...lib import functions
from ..eigen_widgets import Dialog
import os
from PySide2 import QtCore, QtWidgets, QtGui
from ConvertQt import uic


tmp = get_monitors()[0].height


class Check_FFT(Dialog):
    def __init__(self, parent=None, filename=None, max_=2):
        super().__init__()
        self.parent = parent
        file = functions.resource_path(os.path.join("ui", "check_fft.ui"))
        uic.loadUi(file, self)
        self.Close.clicked.connect(self.close)
        self.ends = False
        self.height = None
        self.fontsize = None
        self.font_button = None
        self.th = show_fft(self, filename=filename, max_=2)
        self.th.changePixmap1.connect(self.setImage1)
        self.th.changePixmap2.connect(self.setImage2)
        self.th.changePixmap3.connect(self.setImage3)
        self.th.changePixmap4.connect(self.setImage4)
        self.th.start()
        height = int(tmp / 2.5)
        self.height = height
        self.Original.setMaximumSize(QtCore.QSize(height, height))
        self.Original.setMinimumSize(QtCore.QSize(height, height))
        self.FFT.setMaximumSize(QtCore.QSize(height, height))
        self.FFT.setMinimumSize(QtCore.QSize(height, height))
        self.FFT_High.setMaximumSize(QtCore.QSize(height, height))
        self.FFT_High.setMinimumSize(QtCore.QSize(height, height))
        self.BackTransform.setMaximumSize(QtCore.QSize(height, height))
        self.BackTransform.setMinimumSize(QtCore.QSize(height, height))
        self.Value.valueChanged.connect(self.value_changed)
        self.Threshold.valueChanged.connect(self.value_changed2)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def set_Size(self):
        height = int(self.geometry().height())
        fontsize = (height / 50)
        font_button = QtGui.QFont()
        font_button.setPointSize(fontsize)
        for item in self.findChildren(QtWidgets.QPushButton):
            item.setFont(font_button)

    def value_changed(self):
        self.Value_Show.setText(str(self.Value.value()))

    def value_changed2(self):
        self.Threshold_Value.setText(str(self.Threshold.value()))

    @QtCore.Slot(QtGui.QImage)
    def setImage1(self, image):
        self.Original.setPixmap(QtGui.QPixmap.fromImage(image))

    @QtCore.Slot(QtGui.QImage)
    def setImage2(self, image):
        self.FFT.setPixmap(QtGui.QPixmap.fromImage(image))

    @QtCore.Slot(QtGui.QImage)
    def setImage3(self, image):
        self.FFT_High.setPixmap(QtGui.QPixmap.fromImage(image))

    @QtCore.Slot(QtGui.QImage)
    def setImage4(self, image):
        self.BackTransform.setPixmap(QtGui.QPixmap.fromImage(image))

    def closeEvent(self, event):
        self.ends = True
        return super().closeEvent(event)

    def is_end(self):
        self.ends = True
