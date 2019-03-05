from ..eigen_widgets import Widgetb
from ...lib import functions
from .choose_action import choose_action
from .ptv_thread import ptv_thread
from .analyser_miscellaneous import search
from .dialogg import Dialogg
#import hashlib
import os
from PySide2 import QtCore, QtWidgets, QtGui
from ConvertQt import uic


class picture_to_video(Widgetb):
    def __init__(self, parent=None):
        """load widget from ui file, connect signals to slots and initialise"""\
            """class attribute"""
        super().__init__()
        self.parent = parent
        self.is_end = False
        self.value = 0
        file = functions.resource_path(
            os.path.join("ui", "Picture_Video_Convert.ui"))
        uic.loadUi(file, self)
        self.Close.setDisabled(False)
        self.Close.clicked.connect(self.close)
        self.Start.clicked.connect(self.start)
        self.ChooseFolder.clicked.connect(self.get_folder)
        print("Select a Folder with images in this format: img_0%_total-length_temperature_current_stepwidth.extension")
        print(
            "Then select a window Function for the images (Boxcar is the original image).")
        print("For using a custom window function, it must be specified like this: np.sin(np.arange(width)*math.pi/(width-1))**2")
        print("Where np.arange(width) are the values for the x-axis.")
        print("Mathematical constants must have the prefix math. like math.pi.")
        print("Please enter username and password.")
        self.Convert_All.setVisible(False)
        self.Switch.setVisible(False)
        self.setFixedSize(self.size())
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint)
        self.files = None
        self.dialogg = None
        self.folders = None
        self.th = None
        self.i = 0
        self.resized.connect(self.set_Size)
        self.Convert_All.clicked.connect(self.start_all)


    def get_folder(self):
        self.ChooseFolder.setDisabled(True)
        self.Convert_All.setDisabled(True)
        self.Windows.setDisabled(True)
        self.Start.setDisabled(True)
        self.dname = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Directory", self.parent.direc_path)
        self.th = choose_action(self)
        self.th.emitt.connect(self.get_action)
        self.th.no.connect(self.th_no)
        self.th.start()

    def th_no(self):
        self.ChooseFolder.setDisabled(False)

    def get_action(self, tup):
        data, mode = tup
        # chooses files or folders
        if mode == 0:
            self.files = data
            self.Start.setDisabled(False)
            self.Windows.setDisabled(False)
            self.ChooseFolder.setDisabled(False)
            self.Convert_All.setVisible(False)
            self.Start.setVisible(True)
            print("Folder " + self.dname + " selected.")
        elif mode == 1:
            self.folders = data
            self.Convert_All.setDisabled(False)
            self.Windows.setDisabled(False)
            self.ChooseFolder.setDisabled(False)
            self.Convert_All.setVisible(True)
            self.Start.setVisible(False)
            print("Folder " + self.dname + " selected.")
        else:
            raise OSError("Not Possible, You Hacker!")

    def exist(self, value):
        self.dialogg = Dialogg(self)
        self.dialogg.setModal(True)
        self.dialogg.show()
        self.value = self.dialogg.exec_()

    def end(self):
        print("Finished.")
        self.Close.setDisabled(False)
        self.is_end = True
        self.Start.setDisabled(False)
        self.Windows.setDisabled(False)
        self.ChooseFolder.setDisabled(False)
        self.Subtract_Background.setDisabled(False)
        self.Mirror_Image.setDisabled(False)
        self.Switch.setDisabled(False)

    def start(self):
        print("Start")
        self.th = ptv_thread(self)
        self.th.finished.connect(self.end)
        self.th.exists.connect(self.exist)
        self.th.start()
        self.ChooseFolder.setDisabled(True)
        self.Start.setDisabled(True)
        self.Windows.setDisabled(True)
        self.Close.setDisabled(True)
        self.Subtract_Background.setDisabled(True)
        self.Mirror_Image.setDisabled(True)
        self.Switch.setDisabled(True)

    def start_all(self):
        self.ChooseFolder.setDisabled(True)
        self.Convert_All.setDisabled(True)
        self.Windows.setDisabled(True)
        self.Close.setDisabled(True)
        self.Subtract_Background.setDisabled(True)
        self.Mirror_Image.setDisabled(True)
        self.Switch.setDisabled(True)

        dname = self.folders[self.i]
        s = search(dname, 'image')
        self.files = s.files
        self.th = ptv_thread(self)
        self.th.finished.connect(self.mid_all)
        self.th.exists.connect(self.exist)
        self.th.start()

    def mid_all(self):
        print("Finsihed ", self.i + 1, " of ", len(self.folders))
        self.i += 1
        if self.i >= len(self.folders):
            return self.end_all()
        else:
            return self.start_all()

    def end_all(self):
        self.i = 0
        self.Close.setDisabled(False)
        self.is_end = True
        self.Windows.setDisabled(False)
        self.ChooseFolder.setDisabled(False)
        self.Subtract_Background.setDisabled(False)
        self.Mirror_Image.setDisabled(False)
        self.Convert_All.setDisabled(False)
        self.Switch.setDisabled(False)

    def set_Size(self):
        # sets the fontsize of the widgets according to window size
        # sets the widget size according to window size
        self.height = int(self.geometry().height())
        self.width = int(self.geometry().width())
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
