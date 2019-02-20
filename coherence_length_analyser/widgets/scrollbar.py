from PyQt5 import QtWidgets


class ScrollBar(QtWidgets.QScrollBar):
    def wheelEvent(self, event):
        tmp = event.delta() / 120
        if tmp > 0:
            tmp = self.value() - 2
        else:
            tmp = self.value() + 2
        self.setValue(tmp)
        print(tmp)
#        return super().wheelEvent(event)
