from ...lib import functions
from PySide2 import QtCore


class motor_movement(QtCore.QThread):
    """moves the motor"""
    do = QtCore.Signal()

    def __init__(self, parent=None, number=1, mode="forward"):
        super().__init__()
        self.number = number
        self.mode = mode
        self.parent = parent

    def run(self):
        # moves motor and saves position
        for i in range(self.number):
            if self.mode == "forward":
                tmp = self.parent.position.copy()
                tmp[0][0] += 0.11
                self.parent.position = tmp
            elif self.mode == "backward":
                tmp = self.parent.position.copy()
                tmp[0][0] -= 0.11
                self.parent.position = tmp
            params = (self.parent.ser,)
            getattr(functions, self.mode)(*params)
            functions.save_txt(self.parent.pos_path, self.parent.position)
            if self.parent.failed is True or self.parent.ends is True:
                break
        self.do.emit()
