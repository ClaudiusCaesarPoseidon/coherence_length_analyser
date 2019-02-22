from PySide2 import QtCore


class Stream(QtCore.QObject):
    newText = QtCore.Signal(str)

    def write(self, text):
        self.newText.emit(str(text))
