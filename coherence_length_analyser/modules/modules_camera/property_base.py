import os
import numpy as np
from PySide2 import QtCore


class property_base(object):
    # signals that will be emmited when the value of the propertys changes
    valueChanged = QtCore.Signal(object)
    valueChanged_angle = QtCore.Signal(object)
    valueChanged_lines = QtCore.Signal(object)
    valueChanged_exposure_time_current = QtCore.Signal(object)
    valueChanged_exposure_time_saved = QtCore.Signal(object)
    valueChanged_gain_current = QtCore.Signal(object)
    valueChanged_gain_saved = QtCore.Signal(object)
    valueChanged_mean = QtCore.Signal(object)

    def __init__(self, parent=None):
        super().__init__()
        print("Ich werde aufgerufen.")
        # variabled for propertys
        self._exposure_current = 0.0
        self._gain_current = 50
        self._exposure_saved = None
        self._gain_saved = None
        self._angle = 0
        self._lines = None
        self._white = None
        self._white_val = None
        self._mean = None
        self._position = None

        sys_drive = self.parent.sys_drive
        self.pos_path = os.path.join(
            sys_drive, "coherence_length_analyser", "position.csv")
        if os.path.exists(self.pos_path) is False:
            os.makedirs(os.path.dirname(self.pos_path), exist_ok=True)
            with open(self.pos_path, "a+") as file:
                file.write("0,0\n0,0")
        self.position = np.loadtxt(self.pos_path, delimiter=',')

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
        self.valueChanged.emit(value)

    @property
    def exposure_current(self):
        return self._exposure_current

    @exposure_current.setter
    def exposure_current(self, value):
        self._exposure_current = value
        self.valueChanged_exposure_time_current.emit(value)

    @property
    def exposure_saved(self):
        return self._exposure_saved

    @exposure_saved.setter
    def exposure_saved(self, value):
        self._exposure_saved = value
        self.valueChanged_exposure_time_saved.emit(value)

    @property
    def gain_current(self):
        return self._gain_current

    @gain_current.setter
    def gain_current(self, value):
        self._gain_current = value
        self.valueChanged_gain_current.emit(value)

    @property
    def gain_saved(self):
        return self._gain_saved

    @gain_saved.setter
    def gain_saved(self, value):
        self._gain_saved = value
        self.valueChanged_gain_saved.emit(value)

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value
        self.valueChanged_angle.emit(value)

    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, value):
        self._lines = value
        self.valueChanged_lines.emit(value)

    @property
    def mean(self):
        return self._mean

    @mean.setter
    def mean(self, value):
        self._mean = value
        self.valueChanged_mean.emit(value)
