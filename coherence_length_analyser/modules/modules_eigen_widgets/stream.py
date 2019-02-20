from PyQt5 import QtCore
QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot


class Stream(QtCore.QObject):
    newText = QtCore.Signal(str)

    def write(self, text):
        self.newText.emit(str(text))
