from PyQt5 import QtCore, QtWidgets
QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot


class Label(QtWidgets.QLabel):
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Left or event.key() == QtCore.Qt.Key_Right:
            event.ignore()
            return None
        else:
            return super().keyPressEvent(event)
