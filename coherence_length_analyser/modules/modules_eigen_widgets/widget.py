from PySide2 import QtCore, QtWidgets


class Widget(QtWidgets.QWidget):
    resized = QtCore.Signal()
    closedz = QtCore.Signal()

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def resizeEvent(self, event):
        self.resized.emit()
        return super().resizeEvent(event)

    def closeEvent(self, event):
        self.closedz.emit()
        return super().closeEvent(event)
