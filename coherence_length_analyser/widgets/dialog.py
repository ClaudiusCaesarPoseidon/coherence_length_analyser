from PySide2 import QtCore, QtWidgets


class Dialog(QtWidgets.QDialog):
    """subclass of QDialog which ignores pressing of the escape key"""
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            event.ignore()
        else:
            event.accept()
