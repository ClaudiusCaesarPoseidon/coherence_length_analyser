from PySide2 import QtCore, QtWidgets


class ComboBox(QtWidgets.QComboBox):
    """subclass of QComboBox which ignores pressing of the arrow keys"""

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Left or event.key() == QtCore.Qt.Key_Right:
            event.ignore()
            return None
        else:
            return super().keyPressEvent(event)
