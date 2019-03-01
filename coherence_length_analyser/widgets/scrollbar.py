from PySide2 import QtWidgets


class ScrollBar(QtWidgets.QScrollBar):
    """subclass of QScrollbar which ignores pressing of the arrow keys"""
    def wheelEvent(self, event):
        tmp = event.delta() / 120
        if tmp > 0:
            tmp = self.value() - 2
        else:
            tmp = self.value() + 2
        self.setValue(tmp)
