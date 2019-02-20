from ...lib import functions
from PyQt5 import QtCore
QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot
VAL = functions.VAL


class Init_Thread(QtCore.QThread):
    emit = QtCore.Signal(tuple)
    emit2 = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def run(self):
        print("Connect Motor Controll")
        ser = functions.list_connect()
        number_of_cameras = functions.Number_Of_Cameras(self.parent.dll_path)
        if ser.isOpen() is True:
            print("Connected")
            connect = True
        else:
            print("Not Connected. Please Connect Arduino for Motor Controll.")
            connect = False
        if number_of_cameras > 0 and connect is True:
            if number_of_cameras == 1:
                print("Connect camera.")
            else:
                print("Multiple cameras detected, connect first not connected camera.")
            came = functions.Init_Cam(gain_boost=0, path=self.parent.dll_path)
            cam = came[0]
            xxx = functions.get_frame_extremes(cam, self.parent.dll_path)
#            tmp = namedtuple("FPS", xxx.keys())(*xxx.values())
            tmp = VAL(**xxx)
            max_fps = 1 / tmp.min
            functions.is_SetFrameRate(cam, max_fps, self.parent.dll_path)
            print("Camera Connected. Starting.")
        else:
            print("No Camera Detected. Please connect uEye Camera.")
            connect = False
        if connect is True:
            self.emit.emit((ser, came))
        else:
            self.emit2.emit()
