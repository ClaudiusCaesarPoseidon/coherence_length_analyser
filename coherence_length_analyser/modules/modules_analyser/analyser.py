#from .analyse_everything import everything
#from ..check_fft import Check_FFT
from ...lib import functions
from ..widgets import Stream, Widgetb
from .section_test import section_test
from .picture_to_video import picture_to_video
from .pyplot_cv2 import pyplot_cv2
from .analyser_miscellaneous import get_video
import os
import timeit
import sys
import cv2
from PySide2 import QtCore, QtWidgets, QtGui
from ConvertQt import uic


monitor_format = functions.monitor_format


class Analyser(Widgetb):
    def __init__(self, parent=None, config=None):
        """load widget from ui file, connect signals to slots and initialise"""\
            """class attribute"""
        super(Analyser, self).__init__()
        self.parent = parent
        if self.parent is not None:
            self.direc_path = self.parent.direc_path
        else:
            self.direc_path = os.path.join(os.path.expanduser(
                "~"), "OUT", "coherence_length_analyser")
        self.config = config
        file_path = sys.argv[0]
        self.dir_path = os.path.dirname(file_path)
        # loads the widgets from the ui file
        file = functions.resource_path(
            os.path.join("ui", "fft_peak_analyser.ui"))
        uic.loadUi(file, self)
        if self.parent is not None:
            self.setModal(True)
        self.first = True
        self.fname = functions.resource_path(os.path.join(
            "data", "demo_35_25_100_9.0909090909090909.avi"))
        self.demo = True
        self.height = None
        self.pyplot_width = None
        self.ends = False
        self.number = 0
        self.num = 0
        self.State = self.Open_Demo.isEnabled()
        if os.path.exists(
            functions.resource_path(
                os.path.join(
                    "data",
                "ffmpeg.exe"))):
            self.ffmpeg_path = functions.resource_path(
                os.path.join("data", "ffmpeg.exe"))
        if os.path.exists(
            functions.resource_path(
                os.path.join(
                    "data",
                    "ffmpeg_python",
                "ffmpeg_python.exe"))):
            self.ffmpeg_python_path = functions.resource_path(
                os.path.join("data", "ffmpeg_python", "ffmpeg_python.exe"))
        print("To start please choose file with \"Open File\".")
        print("If no file is opened, a demo file will be used.")
        print("The video must be in a square format; e.g. 480x480")
        self.Start.clicked.connect(self.start)
        self.Close.clicked.connect(self.close)
        self.oPen.clicked.connect(self.Open)
        self.Convert.clicked.connect(self.convert)
        self.resized.connect(self.set_Size)
        if self.Convert.sizeHint().width() >= self.Convert.geometry().width():
            self.Convert.setText("Convert Pictures\nto Video")
        self.Open_Demo.clicked.connect(self.open_demo)
        self.Switch_Demo.valueChanged.connect(self.demo_switched)
        self.width = None
        self.cv2_height = None
        self.cv2_width = None
        self.pyplot_height = None
        self.convert_width = None
        self.fontsize = None
        self.font_button = None
        self.font_text = None
        self.dialog = None
        self.tic = None
        self.toc = None
        cap = cv2.VideoCapture(self.fname)
        dump, tmp = cap.read()
        max_value, dump, dump2 = tmp.shape
        self.Section_Size.setMaximum(max_value)
        self.Section_Size.valueChanged.connect(self.print_section_Size)
        value = int(max_value / 2)
        if value % 2 != 0:
            value += 1
        value = 26  # 24
        self.Section_Size.setValue(value)
        self.Section_Size_Text.setText(str(value))
        self.end_section_check = False
        self.section_thread = section_test(self)
        self.section_thread.changePixmap.connect(self.setImage)
        self.Check_Section_Size.clicked.connect(self.test_section)
        self.tmp = False
        self.fist = True
        self.i = 0
        self.Stop.clicked.connect(self.stop)
        self.Start_Raum.clicked.connect(self.start_raum)
        self.Open_Folder.clicked.connect(self.open_folder)
        self.dname = os.path.join(self.direc_path, "converted_videos")
        self.stopped = False

    def set_Size(self):
        # sets the fontsize of the widgets according to window size
        # sets the widget size according to window size
        self.height = int(self.geometry().height())
        self.width = int(self.geometry().width())
        value = monitor_format()
        value = 7 / 36 * (32 / 9 - value) + 32 / 9
        self.cv2_height = int(self.width / value)
        self.cv2_width = self.cv2_height * 3
        self.pyplot_width = self.cv2_width
        self.pyplot_height = self.height - self.cv2_height
        self.convert_width = self.width - self.cv2_width
        self.cv2.setMinimumSize(QtCore.QSize(self.cv2_width, self.cv2_height))
        self.canvas.setMinimumSize(QtCore.QSize(
            self.pyplot_width, self.pyplot_height))
        self.cv2.setMaximumSize(QtCore.QSize(self.cv2_width, self.cv2_height))
        self.canvas.setMaximumSize(QtCore.QSize(
            self.pyplot_width, self.pyplot_height))
        if self.Convert.sizeHint().width() >= self.Convert.geometry().width():
            self.Convert.setText("Convert Pictures\nto Videos")
        self.height = int(self.geometry().height())
        fontsize = (self.height / 50)
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
        for item in self.findChildren(QtWidgets.QSpinBox):
            item.setFont(font_text)
        self.Console.setMinimumSize(QtCore.QSize(0, 6 / 16 * self.height))
        if self.cv2_height >= 3 / 4 * self.height:
            height = int(4 / 3 * self.cv2_height)
            self.resize(self.width, height)

    def print_section_Size(self):
        value = self.Section_Size.value()
        if value % 2 != 0:
            value += 1
        self.Spin_Row.setMaximum(value - 1)
        self.Spin_Col.setMaximum(value - 1)
        self.Section_Size_Text.setText(str(value))

    def number_toggle(self, num):
        return 1 if num == 0 else 0

    def open_folder(self):
        self.dname = QtWidgets.QFileDialog.getExistingDirectory(
            self, "Select Directory", os.path.join(
                self.direc_path, "converted_videos"))

    def start_raum(self):
        path = self.dname
        self.files = []
        self.demo = False
        get = get_video(path)
        self.files = get.get(self.Windows.currentText())
        if len(self.files) > 0:
            try:
                self.canvas.figure.delaxes(self.th.ax)
            except (KeyError, AttributeError):
                pass
            self.canvas.figure.clf()
            self.i = 0
            self.th = pyplot_cv2(self)
            self.th.changePixmap.connect(self.setImage)
            self.th.finished.connect(self.mid_2_raum)
            self.using = self.Use.isChecked()
            self.mid_raum()
            self.toc = timeit.default_timer()
        else:
            print("There are no files to analyse.")
        print(1)

    def mid_raum(self):
        self.fname = self.files[self.i]
        self.end_test()
        self.ends = False
        path = os.path.join(
            os.path.dirname(
                self.fname),
            "coherence_length.txt")
        try:
            with open(path, "r") as file:
                tmp = file.read()
            tmp = ''.join(['(', [x.split("\t")
                                 for x in tmp.split("\n")][0][-1].split("(")[-1]])
            tup = eval(tmp)
            self.Spin_Row.setValue(tup[0])
            self.Spin_Col.setValue(tup[1])
            self.Use.setChecked(True)
        except FileNotFoundError:
            self.Use.setChecked(self.using)
        self.th.start()
        try:
            self.canvas.figure.delaxes(self.th.ax)
        except (KeyError, AttributeError):
            pass
        self.canvas.figure.clf()
        self.first = False
        self.Start.setDisabled(True)
        self.oPen.setDisabled(True)
        self.Convert.setDisabled(True)
        self.Section_Size.setDisabled(True)
        self.State = self.Open_Demo.isEnabled()
        self.Open_Demo.setEnabled(False)
        self.Switch_Demo.setEnabled(False)
        self.Check_Section_Size.setDisabled(True)
        self.Filter_Switch.setDisabled(True)
        self.Calculate.setDisabled(True)
        self.Stop.setDisabled(False)
        self.Use.setDisabled(True)
        self.Close.setDisabled(True)
        self.Start_Raum.setDisabled(True)
        self.Open_Folder.setDisabled(True)
        self.Windows.setDisabled(True)

    def mid_2_raum(self):
        self.i += 1
        if self.i >= len(self.files) or self.stopped is True:
            self.end_raum()
        else:
            self.mid_raum()

    def end_raum(self):
        self.Start.setDisabled(False)
        self.oPen.setDisabled(False)
        self.Convert.setDisabled(False)
        self.Open_Demo.setEnabled(self.State)
        self.Switch_Demo.setEnabled(True)
        self.Check_Section_Size.setEnabled(True)
        self.Filter_Switch.setDisabled(False)
        self.Calculate.setDisabled(False)
        self.Stop.setDisabled(True)
        self.Use.setDisabled(False)
        self.Close.setDisabled(False)
        self.Start_Raum.setDisabled(False)
        self.Open_Folder.setDisabled(False)
        self.Windows.setDisabled(False)
        self.stopped = False
        self.tic = timeit.default_timer()
        print("END, elapsed time: %0.2f" % (self.tic - self.toc), " s")

    def open_demo(self):
        self.demo = True
        if self.number >= 0 and self.number <= 1:
            if self.number == 0:
                demo_name = "demo_35_25_100_9.0909090909090909.avi"
            elif self.number == 1:
                demo_name = "demi_35_25_100_9.0909090909090909.avi"
            self.fname = functions.resource_path(
                os.path.join("data", demo_name))
            print("Opened demo file: " + demo_name)
            self.Open_Demo.setEnabled(False)
            self.number = self.number_toggle(self.num)
            self.end_test()
            self.section_thread.wait()
            self.section_thread = section_test(self)
            self.section_thread.changePixmap.connect(self.setImage)
        else:
            print("Not Possible.")

    def demo_switched(self):
        self.number = self.Switch_Demo.value()
        if self.Open_Demo.isEnabled() is True and self.demo is True:
            self.Open_Demo.setEnabled(False)
        elif self.Open_Demo.isEnabled() is False and self.demo is True:
            self.Open_Demo.setEnabled(True)

    @QtCore.Slot(QtGui.QImage)
    def setImage(self, image):
        self.cv2.setPixmap(QtGui.QPixmap.fromImage(image))

    def closeEvent(self, event):
        self.ends = True
        self.is_end()
        return super().closeEvent(event)

    def convert(self):
        # shows the window according to the settings
        self.dialog = picture_to_video(self)
        self.dialog.setModal(True)
        if self.config['windowed'] is False:
            self.dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.dialog.showFullScreen()
        else:
            self.hide()
            if self.config['border'] is False:
                self.dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            if self.config['fullscreen'] is True:
                self.dialog.showMaximized()
            else:
                self.dialog.resize(int(self.win_width * 3 / 4),
                                   int(self.win_height * 3 / 4))
                self.dialog.show()
        self.dialog.exec_()
        if self.config['windowed'] is True:
            self.show()

        sys.stdout = Stream()
        sys.stdout.newText.connect(self.onUpdateText)

    def Open(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open file', os.path.join(
                self.direc_path, "converted_videos"))[0]
        if self.fname == "":
            print("No File selected.")
            self.fname = functions.resource_path(os.path.join(
                "data", "demo_35_25_100_9.0909090909090909.avi"))
            self.end_test()
            self.section_thread.wait()
            self.section_thread = section_test(self)
            self.section_thread.changePixmap.connect(self.setImage)
        else:
            print("Opened File:", self.fname)
            self.demo = False
            self.Open_Demo.setEnabled(True)
            self.num = self.number
            self.end_test()
            self.section_thread.wait()
            self.section_thread = section_test(self)
            self.section_thread.changePixmap.connect(self.setImage)

    def start(self):
        self.end_test()
        self.ends = False
        self.th = pyplot_cv2(self)
        self.th.changePixmap.connect(self.setImage)
        self.th.finished.connect(self.enable)
        self.th.start()
        try:
            self.canvas.figure.delaxes(self.th.ax)
        except (KeyError, AttributeError):
            pass
        self.canvas.figure.clf()
        self.first = False
        self.Start.setDisabled(True)
        self.oPen.setDisabled(True)
        self.Convert.setDisabled(True)
        self.Section_Size.setDisabled(True)
        self.State = self.Open_Demo.isEnabled()
        self.Open_Demo.setEnabled(False)
        self.Switch_Demo.setEnabled(False)
        self.Check_Section_Size.setDisabled(True)
        self.Filter_Switch.setDisabled(True)
        self.Calculate.setDisabled(True)
        self.Stop.setDisabled(False)
        self.Use.setDisabled(True)
        self.Close.setDisabled(True)
        self.Start_Raum.setDisabled(True)
        self.Open_Folder.setDisabled(True)
        self.Windows.setDisabled(True)
        self.toc = timeit.default_timer()

    def enable(self):
        self.Start.setDisabled(False)
        self.oPen.setDisabled(False)
        self.Convert.setDisabled(False)
        self.Open_Demo.setEnabled(self.State)
        self.Switch_Demo.setEnabled(True)
        self.Check_Section_Size.setEnabled(True)
        self.Filter_Switch.setDisabled(False)
        self.Calculate.setDisabled(False)
        self.Stop.setDisabled(True)
        self.Use.setDisabled(False)
        self.Close.setDisabled(False)
        self.Start_Raum.setDisabled(False)
        self.Open_Folder.setDisabled(False)
        self.Windows.setDisabled(False)
        self.end()

    def test_section(self):
        self.tmp = self.Check_Section_Size.isChecked()
        if self.tmp is True:
            if self.fist is True:
                self.section_thread.start()
                self.fist = False
            self.end_section_check = False
            self.thread_pause = False
            self.Open_Demo.setEnabled(False)
            self.Switch_Demo.setEnabled(False)
            self.Start.setDisabled(True)
            self.oPen.setDisabled(True)
            self.Convert.setDisabled(True)
            self.Section_Size.setDisabled(False)
            self.Filter_Switch.setDisabled(True)
            self.Spin_Row.setEnabled(True)
            self.Spin_Col.setEnabled(True)
            self.Start_Raum.setDisabled(True)
            self.Open_Folder.setDisabled(True)
            self.Windows.setDisabled(True)
        else:
            self.thread_pause = True
            self.section_thread.start()
            self.Open_Demo.setEnabled(True)
            self.Switch_Demo.setEnabled(True)
            self.Start.setDisabled(False)
            self.oPen.setDisabled(False)
            self.Convert.setDisabled(False)
            self.Section_Size.setDisabled(True)
            self.Filter_Switch.setDisabled(False)
            self.Spin_Row.setEnabled(False)
            self.Spin_Col.setEnabled(False)
            self.Start_Raum.setDisabled(False)
            self.Open_Folder.setDisabled(False)
            self.Windows.setDisabled(False)

    def stop(self):
        self.stopped = True
        self.end_()

    def end_(self):
        self.is_end()
        self.end_test()

    def end_test(self):
        self.end_section_check = True
        self.fist = True

    def is_end(self):
        self.ends = True

    def end(self):
        self.tic = timeit.default_timer()
        print("END, elapsed time: %0.2f" % (self.tic - self.toc), " s")

    def wheelEvent(self, event):
        # connect scrolling of mouse to scrollbar
        try:
            tmp = event.delta()  # Qt4
        except AttributeError:
            tmp = event.angleDelta().y()  # Qt5
        finally:
            if self.tmp is True:
                if tmp > 0:
                    tmp = self.Section_Size.value() - 2
                elif tmp < 0:
                    tmp = self.Section_Size.value() + 2
                else:
                    pass
                self.Section_Size.setValue(tmp)
            event.accept()
