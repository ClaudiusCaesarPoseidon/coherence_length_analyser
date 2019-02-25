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
#        import lib.setup as setup
#        import lib.visual_studio_installed_version
#        import importlib
#        modules = ['lib.resource_path', 'lib.defines', 'lib.enum_c_value', 'lib.uEye', 'lib.c_funktionen', 'lib.idle_switch']
#        names = ['resource_path', 'defines', 'enum_c_value', 'uEye', 'c_funktionen', 'idle_switch']
#        for item, name in zip(modules, names):
#            try:
#                importlib.import_module(item)
#            except ModuleNotFoundError:
#                if lib.visual_studio_installed_version.right_msvc_version_installed() is True:
#                    tmp = getattr(setup, "setup_" + name)
#                    tmp()
#                else:
#                    raise OSError("Microsoft Visual Studio ", lib.visual_studio_installed_version.get_build_version_major, "is not installed.")
    if 'PySide2' in sys.modules:
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
        os.environ['PATH'] += os.pathsep + \
            os.path.abspath(os.path.dirname(sys.argv[0]) + "\\dll")
