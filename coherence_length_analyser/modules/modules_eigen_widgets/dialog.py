from PySide2 import QtCore, QtWidgets


class Dialog(QtWidgets.QDialog):
    resized = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.resized.connect(self.set_Size)

    def set_Size(self):
        pass

    def resizeEvent(self, event):
        self.resized.emit()
        return super().resizeEvent(event)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            event.ignore()
        else:
            event.accept()
