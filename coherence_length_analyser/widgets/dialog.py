from PySide2 import QtCore, QtWidgets


class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            event.ignore()
        else:
            event.accept()
