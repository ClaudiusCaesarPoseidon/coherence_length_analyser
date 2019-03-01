import os
import sys
import ctypes
import cv2
import numpy as np
from PIL import Image
from PySide2 import QtTest, QtWidgets
from datetime import datetime as datetime_, timedelta

default_imread = cv2.imread


def main_init():
    @staticmethod
    def qWait(t):
        end = datetime_.now() + timedelta(milliseconds=t)
        while datetime_.now() < end:
            QtWidgets.QApplication.processEvents()

    def imread(path, mode=1):
        if path.isascii() is True:
            return default_imread(path, mode)
        else:
            if mode == 0:
                return np.asarray(Image.open(path).convert('L'))
            else:
                return np.asarray(Image.open(path).convert('RGB'))

    if 'nt' not in os.name:
        os.environ['systemdrive'] = "/usr/local"
    if getattr(sys, 'frozen', False):
        os.environ['QT_API'] = "pyside2"
    else:
        from .get_qt_module import get_qt_module
        os.environ['QT_API'] = get_qt_module()
    if 'PySide2' in sys.modules or 'PySide' in sys.modules:
        QtTest.QTest.qWait = qWait
    cv2.imread = imread

    myappid = 'GLubber'  # arbitrary string
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except AttributeError:
        pass
    try:
        os.environ['PATH'] += os.pathsep + \
            sys._MEIPASS + "\\dll"  # pylint: disable=W0212
    except AttributeError:
        pass
