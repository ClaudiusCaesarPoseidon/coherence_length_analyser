from .measure import Measure
from .motor_movement import motor_movement
from .start_position import start_position
from ..eigen_widgets import Widgetb
from ...lib import functions
from .constants import max_for
from .constants import max_back
from .move_pos import move_pos
from .camera_init_thread import Init_Thread
from .property_base import property_base
import os
import timeit
import numpy as np
from functools import partial
from PySide2 import QtCore, QtWidgets, QtGui
from ConvertQt import uic


inting = functions.inting
toggle = functions.toggle


class Camera(property_base, Widgetb):
    def __init__(self, parent=None, config=None):
        """load widget from ui file, connect signals to slots and initialise"""\
            """class attribute"""
        super().__init__(parent=parent)

        self.parent = parent
        if self.parent is not None:
            self.direc_path = self.parent.direc_path
        else:
            self.direc_path = os.path.join(os.path.expanduser(
                "~"), "OUT", "coherence_length_analyser")
        self.config = config

        # loads the widgets from the ui file
        file = functions.resource_path(os.path.join(
            "ui", "interference_pattern_camera.ui"))
        file = functions.resource_path(os.path.join("ui", "new_camera.ui"))
        uic.loadUi(file, self)
        self.accept_mode = self.Accept_Parameter.isEnabled()
        self.thread_run = False
        self.Close.clicked.connect(self.close)
        self.Accept_Parameter.clicked.connect(self.accept)
        self.Reset.clicked.connect(self.reset)
        self.Left.clicked.connect(partial(self.move_motor, 'backward'))
        self.Right.clicked.connect(partial(self.move_motor, 'forward'))
        self.Start.clicked.connect(self.start_multiple)
        self.ends = False
        self.cam_off = True
        self.resized.connect(self.set_Size)
        self.Cam_Off.clicked.connect(self.Off)
        self.Cam_On.clicked.connect(self.On)
        self.bild_width = self.geometry().width()
        self.height = self.geometry().height()
        self.fontsize = None
        self.th = None
        self.mm = None
        self.Not_Measuring = True
        self.Gain_Boost.clicked.connect(self.gain_boost)
        self.Stop.clicked.connect(self.is_ends)
        self.check_end = False
        self.failed = False
        self.max = False
        self.m_max = None
        self.Left_Max.clicked.connect(partial(self.goto, max_back))
        self.Right_Max.clicked.connect(partial(self.goto, max_for))
        self.Go_To_Line.setPlaceholderText("%d - %d" % (max_back, max_for))
        self.Go_To.clicked.connect(self.goto)
        self.pos = None
        self.m_p = None

        self.Value = None
        self.Reset_None.clicked.connect(self.reset_lines)
        self.stop = False
        self.i = 0
        self.Save.clicked.connect(self.save_values)

        self.valueChanged.connect(self.check)
        self.valueChanged_angle.connect(self.set_gui_values)
        self.valueChanged_l.connect(self.set_gui_values)
        self.valueChanged_exposure_time_current.connect(self.set_gui_values)
        self.valueChanged_exposure_time_saved.connect(self.set_gui_values)
        self.valueChanged_gain_curren.connect(self.set_gui_values)
        self.valueChanged_gain_saved.connect(self.set_gui_values)
        self.valueChanged_mean.connect(self.set_gui_values)

        # set start info text
        self.tmp = self.Info.toPlainText().split("\n")
        self.set_info()

        self.threadd = Init_Thread(self)
        self.threadd.emit1.connect(self.do_connect)
        self.threadd.emit2.connect(self.do_not_connect)
        self.threadd.start()

    def save_values(self):
        self.gain_saved = self.gain_current
        self.exposure_saved = self.exposure_current

    def set_gui_values(self):
        # prints the current settings of the camera and pattern to the GUI
        temp = self.Values_GUI.toPlainText().split("\n")
        tmp = [y.split("\t") for y in temp]
        tmp[0][5] = str(self.angle)
        tmp[1][6] = str(self.lines)
        tmp[1][1] = str(self.exposure_current)
        tmp[2][1] = str(self.exposure_saved)
        tmp[1][4] = str(self.gain_current)
        tmp[2][4] = str(self.gain_saved)
        tmp[2][6] = str(self.mean)
        tmp = '\n'.join(['\t'.join(x) for x in tmp])
        self.Values_GUI.setPlainText(tmp)

    def set_info(self):
        # prints the current position of the motor
        tmp = self.tmp.copy()
        tmp[0] = tmp[0] + "\tMaximum available length: " + \
            str(int(functions.round(max_for - self.position[0][0])))
        tmp[1] = tmp[1] + "\tMaximum available length: " + \
            str(int(functions.round(self.position[0][0] - max_back)))
        tmp = [item + "\n" for item in tmp]
        tmp.append("Position: " +
                   str(int(functions.round(self.position[0][0]))))
        tmp = ''.join(tmp)
        self.Info.setPlainText(tmp)

    @QtCore.Slot(tuple)
    def do_connect(self, tup):
        ser, came = tup
        self.ser = ser
        self.Right.setDisabled(False)
        self.Left.setDisabled(False)
        self.Right_Max.setDisabled(False)
        self.Left_Max.setDisabled(False)
        self.Go_To.setDisabled(False)
        self.Cam_On.setEnabled(True)
        self.Accept_Parameter.setEnabled(True)
        self.Lock.setEnabled(True)
        self.Gain_Boost.setEnabled(True)
        self.Save.setEnabled(True)
        self.Reset.setEnabled(True)
        self.Reset_None.setEnabled(True)
        self.Close.setEnabled(True)
        self.Cam_Active = True
        self.cam = came[0]
        self.ret = came[1]
        self.pcImgMem, self.pid = came[2:4]
        self.accept_mode = self.Accept_Parameter.isEnabled()
        self.thread = start_position(self)
        self.thread.changePixmap.connect(self.setImage)
        self.thread.changePixmap2.connect(self.setImage2)
        self.thread.angle.connect(self.setAngle)
        self.thread.lines.connect(self.setLines)
        self.thread.val.connect(self.lock)
        self.thread.White.connect(self.set_white)

    @QtCore.Slot()
    def do_not_connect(self, tup):
        self.Cam_Active = False
        ser, came = tup
        self.ser = ser
        self.cam = came[0]
        self.ret = came[1]

    def set_Size(self):
        # sets the fontsize of the widgets according to window size
        self.height = int(self.geometry().height())
        self.width = int(self.geometry().width())
        self.fontsize = (self.height / 75)
        font_button = QtGui.QFont()
        font_button.setPointSize(self.fontsize)
        self.fontsize = (self.height / 75)
        if self.fontsize <= 8:
            self.fontsize = 8
        if self.fontsize >= 16:
            self.fontsize = 16
        font_text = QtGui.QFont()
        font_text.setPointSize(self.fontsize)
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
        self.height = self.geometry().height()
        self.bild_height = int(self.height * 0.75)
        self.bild_width = int(self.bild_height / 2)
        self.Bildausgabe.setMinimumSize(
            QtCore.QSize(self.bild_width, self.bild_height))
        self.Bildausgabe.setMaximumSize(
            QtCore.QSize(self.bild_width, self.bild_height))
        self.Bild_Label.setMinimumSize(
            QtCore.QSize(self.bild_width, self.bild_height))
        self.Bild_Label.setMaximumSize(
            QtCore.QSize(self.bild_width, self.bild_height))
        self.Console.setMinimumSize(
            QtCore.QSize(0, int(4 / 8 * self.bild_height)))

    def goto(self, value=None):
        # moves the motor to the new position
        if value is False:
            try:
                number = int(self.Step_Width.text())
            except ValueError:
                number = 1
            pos = self.position[0][0]
            self.pos = None
            try:
                self.pos = int(self.Go_To_Line.text())
            except ValueError:
                pass
            if self.pos is not None:
                self.Left.setDisabled(True)
                self.Left_Max.setDisabled(True)
                self.Right.setDisabled(True)
                self.Right_Max.setDisabled(True)
                self.Go_To.setDisabled(True)
                self.Go_To_Line.setReadOnly(True)
                self.accept_mode = self.Accept_Parameter.isEnabled()
                self.Accept_Parameter.setEnabled(False)

                if self.pos < max_back or self.pos > max_for:
                    print("Position not possible.")
                elif self.pos < pos:
                    mode = "backward"
                elif self.pos > pos:
                    mode = "forward"
                try:
                    self.m_p = move_pos(parent=self, number=number, mode=mode)
                    self.m_p.do.connect(self.set_info)
                    self.m_p.finished.connect(self.reset_pos)
                    self.m_p.start()
                except UnboundLocalError:
                    self.Not_Measuring = True
                    self.Left.setDisabled(False)
                    self.Left_Max.setDisabled(False)
                    self.Right.setDisabled(False)
                    self.Right_Max.setDisabled(False)
                    self.Go_To.setDisabled(False)
                    self.Go_To_Line.setReadOnly(False)
                    self.Accept_Parameter.setEnabled(self.accept_mode)
                    self.failed = False
                    self.pos = None
            else:
                print("An integer is required.")
        else:
            try:
                number = int(self.Step_Width.text())
            except ValueError:
                number = 1
            pos = self.position[0][0]
            self.pos = value
            self.Left.setDisabled(True)
            self.Left_Max.setDisabled(True)
            self.Right.setDisabled(True)
            self.Right_Max.setDisabled(True)
            self.Go_To.setDisabled(True)
            self.Go_To_Line.setReadOnly(True)
            self.accept_mode = self.Accept_Parameter.isEnabled()
            self.Accept_Parameter.setEnabled(False)

            if self.pos < max_back or self.pos > max_for:
                print("Position not possible.")
            elif self.pos < pos:
                mode = "backward"
            elif self.pos > pos:
                mode = "forward"
            try:
                self.m_p = move_pos(parent=self, number=number, mode=mode)
                self.m_p.do.connect(self.set_info)
                self.m_p.finished.connect(self.reset_pos)
                self.m_p.start()
            except UnboundLocalError:
                self.Not_Measuring = True
                self.Left.setDisabled(False)
                self.Left_Max.setDisabled(False)
                self.Right.setDisabled(False)
                self.Right_Max.setDisabled(False)
                self.Go_To.setDisabled(False)
                self.Go_To_Line.setReadOnly(False)
                self.Accept_Parameter.setEnabled(self.accept_mode)
                self.failed = False
                self.pos = None

    def reset_pos(self):
        self.Not_Measuring = True
        self.Left.setDisabled(False)
        self.Left_Max.setDisabled(False)
        self.Right.setDisabled(False)
        self.Right_Max.setDisabled(False)
        self.Go_To.setDisabled(False)
        self.Go_To_Line.setReadOnly(False)
        self.Accept_Parameter.setEnabled(self.accept_mode)
        self.failed = False
        self.pos = None

    def gain_boost(self):
        if self.Gain_Boost.isChecked() is True:
            functions.BOOOOOOOOOOST(self.cam, True)
        else:
            functions.BOOOOOOOOOOST(self.cam, False)

    def On(self):
        toggle(self.Cam_Off)
        self.Cam_On.setEnabled(False)
        self.Current.setReadOnly(True)
        self.Temperature.setReadOnly(True)
        self.ID.setReadOnly(True)
        self.Max_Width.setReadOnly(True)
        self.Step_Width.setReadOnly(True)
        self.Accept_Parameter.setDisabled(True)
        self.Mode.setDisabled(True)
        self.Reset.setDisabled(True)
        self.Number_Of_Measurements.setEnabled(False)
        self.cam_off = False
        self.thread.start()

    def Off(self):
        toggle(self.Cam_On)
        self.Cam_Off.setEnabled(False)
        self.Current.setReadOnly(False)
        self.Temperature.setReadOnly(False)
        self.ID.setReadOnly(False)
        self.Max_Width.setReadOnly(False)
        self.Step_Width.setReadOnly(False)
        self.Accept_Parameter.setDisabled(False)
        self.Mode.setDisabled(False)
        self.Reset.setDisabled(False)
        self.Number_Of_Measurements.setEnabled(True)
        self.cam_off = True

    @QtCore.Slot(QtGui.QImage)
    def setImage(self, image):
        self.Bildausgabe.setPixmap(QtGui.QPixmap.fromImage(image))

    @QtCore.Slot(QtGui.QImage)
    def setImage2(self, image):
        self.Bild_Label.setPixmap(QtGui.QPixmap.fromImage(image))

    @QtCore.Slot(int)
    def setAngle(self, value):
        if value < 0:
            value += 180
        self.angle = value

    @QtCore.Slot(int)
    def setLines(self, value):
        if self.lines is None or value > self.lines:
            self.lines = value

    @QtCore.Slot(tuple)
    def lock(self, tup):
        self.exposure_current, self.gain_current = tup

    @QtCore.Slot(float)
    def set_white(self, tup):
        self.mean = tup

    def reset_lines(self):
        self.lines = None

    def accept(self):
        # checks if the parameters are ok
        if functions.string_is_int(self.Current.text()) is True\
                and functions.string_is_int(self.Temperature.text()) is True\
                or inting(self.Temperature.text()) == -1\
                and functions.string_is_int(self.Step_Width.text()) is True\
                and functions.string_is_int(self.ID.text()) is True\
                and len(self.ID.text()) == 4\
                and functions.is_float(self.Max_Width.text()) is True:
            self.Current.setReadOnly(True)
            self.Temperature.setReadOnly(True)
            self.ID.setReadOnly(True)
            self.Max_Width.setReadOnly(True)
            self.Step_Width.setReadOnly(True)
            self.Start.setDisabled(False)
            self.Accept_Parameter.setDisabled(True)
            self.Mode.setDisabled(True)
            self.Cam_On.setEnabled(False)
            self.Cam_Off.setEnabled(False)
            self.Left.setDisabled(True)
            self.Left_Max.setDisabled(True)
            self.Right.setDisabled(True)
            self.Right_Max.setDisabled(True)
            self.Go_To.setDisabled(True)
            self.Go_To_Line.setReadOnly(True)
            self.Gain_Boost.setDisabled(True)
            self.Lock.setDisabled(True)
            self.Save.setDisabled(True)
            self.Number_Of_Measurements.setEnabled(False)
            self.Reset_None.setEnabled(False)
            self.number_of_measurements = self.Number_Of_Measurements.value()
            self.stop = False
            self.ends = False
            print("Parameter Accepted")
        else:
            print("Parameter not Accepted")

    def reset(self):
        self.Current.setReadOnly(False)
        self.Temperature.setReadOnly(False)
        self.ID.setReadOnly(False)
        self.Step_Width.setReadOnly(False)
        self.Max_Width.setReadOnly(False)
        self.Start.setDisabled(True)
        self.Accept_Parameter.setDisabled(False)
        self.Reset.setDisabled(False)
        self.Mode.setDisabled(False)
        self.Cam_On.setEnabled(True)
        self.Cam_Off.setEnabled(False)
        self.Not_Measuring = True
        self.Left.setDisabled(False)
        self.Left_Max.setDisabled(False)
        self.Right.setDisabled(False)
        self.Right_Max.setDisabled(False)
        self.Go_To.setDisabled(False)
        self.Gain_Boost.setDisabled(False)
        self.Go_To_Line.setReadOnly(False)
        self.Lock.setDisabled(False)
        self.Save.setDisabled(False)
        self.Number_Of_Measurements.setEnabled(True)
        self.Reset_None.setEnabled(True)

    def move_motor(self, mode="forward"):
        self.Right.setDisabled(True)
        self.Left.setDisabled(True)
        try:
            number = int(self.Step_Width.text())
        except ValueError:
            number = 1
        self.mm = motor_movement(parent=self, number=number, mode=mode)
        self.mm.do.connect(self.set_info)
        self.mm.finished.connect(self.reset2)
        self.mm.start()
        self.mm.wait()

    def reset_max(self, mode):
        if mode == "forward":
            while self.failed is True:
                self.Left.click()
                tmp = timeit.default_timer()
                while True:
                    if timeit.default_timer() - tmp > 0.5:
                        break
        if mode == "backward":
            while self.failed is True:
                self.Right.click()
                tmp = timeit.default_timer()
                while True:
                    if timeit.default_timer() - tmp > 0.5:
                        break
        self.Go_To_Line.setReadOnly(False)
        self.Go_To.setDisabled(False)
        self.failed = False

    def reset2(self):
        if self.failed is False:
            self.Right.setDisabled(False)
            self.Left.setDisabled(False)
        elif self.position[0][0] <= max_back:
            self.Right.setDisabled(False)
        elif self.position[0][0] >= max_for:
            self.Left.setDisabled(False)

    def reset3(self):
        self.Stop.setDisabled(True)

    def start_multiple(self):
        self.i = 0
        self.Right.setDisabled(True)
        self.Left.setDisabled(True)
        self.Start.setDisabled(True)
        self.Reset.setDisabled(True)
        self.Stop.setDisabled(False)
        self.Not_Measuring = False
        self.middle = self.position[0][0]
        self.start = self.middle - (float(self.Max_Width.text())) / 2
        self.mid2_multiple()

    def mid_multiple(self):
        self.th = Measure(parent=self)
        self.th.do.connect(self.set_info)
        self.th.changePixmap.connect(self.setImage)
        self.th.finished.connect(self.mid2_multiple)
        self.th.start()

    def mid2_multiple(self):
        if self.i < self.number_of_measurements and self.stop is False:
            self.pos = self.start
            pos = self.position[0][0]
            try:
                number = int(self.Step_Width.text())
            except ValueError:
                number = 1
            if self.pos < pos:
                mode = "backward"
            elif self.pos > pos:
                mode = "forward"
            try:
                self.m_p = move_pos(parent=self, number=number, mode=mode)
                self.m_p.do.connect(self.set_info)
                self.m_p.finished.connect(self.mid3_multiple)
                self.m_p.start()
            except UnboundLocalError:
                self.Not_Measuring = True
                self.Left.setDisabled(False)
                self.Left_Max.setDisabled(False)
                self.Right.setDisabled(False)
                self.Right_Max.setDisabled(False)
                self.Go_To.setDisabled(False)
                self.Go_To_Line.setReadOnly(False)
                self.Accept_Parameter.setEnabled(self.accept_mode)
                self.failed = False
                self.pos = None
        else:
            self.mid3_multiple()

    def mid3_multiple(self):
        if self.i >= self.number_of_measurements or self.stop is True:
            self.end_multiple()
        else:
            self.i += 1
            self.mid_multiple()

    def end_multiple(self):
        self.pos = self.middle
        pos = self.position[0][0]
        try:
            number = int(self.Step_Width.text())
        except ValueError:
            number = 1
        mode = "äbc"
        if self.pos < pos:
            mode = "backward"
        elif self.pos > pos:
            mode = "forward"
        try:
            self.m_p = move_pos(parent=self, number=number, mode=mode)
            self.m_p.do.connect(self.set_info)
            self.m_p.finished.connect(self.reset)
            self.m_p.finished.connect(self.reset2)
            self.m_p.finished.connect(self.reset3)
            self.m_p.start()
        except UnboundLocalError:
            self.Not_Measuring = True
            self.Left.setDisabled(False)
            self.Left_Max.setDisabled(False)
            self.Right.setDisabled(False)
            self.Right_Max.setDisabled(False)
            self.Go_To.setDisabled(False)
            self.Go_To_Line.setReadOnly(False)
            self.Accept_Parameter.setEnabled(self.accept_mode)
            self.failed = False
            self.pos = None

    def closeEvent(self, event):
        self.ends = True
        self.cam_off = True
        self.ser.close()
        if self.Cam_Active is True:
            functions.Exit_Cam(self.cam, self.pcImgMem, self.pid)
        if self.thread_run is True:
            functions.Exit_Cam(self.cam, self.pcImgMem, self.pid)
        return super().closeEvent(event)

    def end_(self):
        self.is_end()
        self.end_check()

    def is_end(self):
        self.ends = True
        self.cam_off = True
        self.ser.close()
        if self.Cam_Active is True:
            functions.Exit_Cam(self.cam, self.pcImgMem, self.pid)

    def is_ends(self):
        self.stop = True
        self.ends = True
        self.th.wait()
        self.ends = False

    def end_check(self):
        self.check_end = True

    def keyPressEvent(self, event):
        # moves the motor with left and right arrow keys
        if event.key() == QtCore.Qt.Key_Left and self.Not_Measuring is True:
            self.Left.click()
        elif event.key() == QtCore.Qt.Key_Right and self.Not_Measuring is True:
            self.Right.click()
        event.accept()

    def check(self):
        # checks if the motorposition is ok
        if (self.position[0][0] <= max_back or self.position[0]
                [0] >= max_for) and self.failed is False:
            self.check_failed()
        elif (self.position[0][0] > max_back and self.position[0][0] < max_for) and self.max is False and self.pos is None and self.Not_Measuring is True:
            self.failed = False
            self.check_not_failed()

    def check_failed(self):
        # disables the motor
        if self.position[0][0] <= -max_back:
            self.Left.setDisabled(True)
            self.Left_Max.setDisabled(True)
            self.Right.setDisabled(False)
            self.Right_Max.setDisabled(False)
            self.max = False
        elif self.position[0][0] >= max_for:
            self.Left.setDisabled(False)
            self.Left_Max.setDisabled(False)
            self.Right.setDisabled(True)
            self.Right_Max.setDisabled(True)
            self.max = False
        self.failed = True

    def check_not_failed(self):
        self.Right.setDisabled(False)
        self.Left.setDisabled(False)
        self.Right_Max.setDisabled(False)
        self.Left_Max.setDisabled(False)
        self.failed = False
