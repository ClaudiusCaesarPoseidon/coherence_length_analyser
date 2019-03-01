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
    # adds th qWait function, which is only defined in PyQt
    @staticmethod
    def qWait(t):
        end = datetime_.now() + timedelta(milliseconds=t)
        while datetime_.now() < end:
            QtWidgets.QApplication.processEvents()

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

    # sets the systemdrive enviroment variable in OSs other than windows
    if 'nt' not in os.name:
        os.environ['systemdrive'] = "/usr/local"

    # sets the QT_API enviroment variable to pyside2 in PyInstaller or to
    # the preferred binding otherwiese
    if getattr(sys, 'frozen', False):
        os.environ['QT_API'] = "pyside2"
    else:
        from .get_qt_module import get_qt_module
        os.environ['QT_API'] = get_qt_module()

    if 'PySide2' in sys.modules or 'PySide' in sys.modules:
        QtTest.QTest.qWait = qWait
    cv2.imread = imread

    # groups the taskbar icons when necessary
    myappid = 'GLubber'  # arbitrary string
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except AttributeError:
        pass

    try:
        os.environ['PATH'] += os.pathsep + \
            os.path.join(sys._MEIPASS, "binaries")  # pylint: disable=W0212
    except AttributeError:
        pass
