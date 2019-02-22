from PySide2 import QtCore, QtWidgets


class Label(QtWidgets.QLabel):
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Left or event.key() == QtCore.Qt.Key_Right:
            event.ignore()
            return None
        else:
            return super().keyPressEvent(event)
