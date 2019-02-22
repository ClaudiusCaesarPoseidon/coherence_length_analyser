from .motor_movement import motor_movement
from PySide2 import QtCore


class move_pos(QtCore.QThread):
    do = QtCore.Signal()

    def __init__(self, parent=None, mode="forward", number=1):
        self.parent = parent
        self.mode = mode
        self.number = number
        self.th = None
        super().__init__()

    def do_func(self):
        self.do.emit()

    def run(self):
        while True:
            self.th = motor_movement(
                self.parent, number=self.number, mode=self.mode)
            self.th.do.connect(self.do_func)
            self.th.start()
            self.th.wait()
            if self.mode == "forward":
                if self.parent.position[0][0] >= self.parent.pos:
                    break
            elif self.mode == "backward":
                if self.parent.position[0][0] <= self.parent.pos:
                    break
            if self.parent.ends is True:
                break
        if self.mode == "forward":
            self.mode = "backward"
        elif self.mode == "backward":
            self.mode = "forward"
        if self.parent.position[0][0] != self.parent.pos and self.parent.ends is False:
            while True:
                self.th = motor_movement(self.parent, number=1, mode=self.mode)
                self.th.do.connect(self.do_func)
                self.th.start()
                self.th.wait()
                if self.mode == "forward":
                    if self.parent.position[0][0] >= self.parent.pos:
                        break
                elif self.mode == "backward":
                    if self.parent.position[0][0] <= self.parent.pos:
                        break
                if self.parent.ends is True:
                    break
        print("Finished. Arrived at %s" % str(self.parent.pos))
