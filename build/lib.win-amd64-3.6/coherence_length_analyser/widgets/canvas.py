from PySide2 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Canvas(QtWidgets.QWidget):
    """subclass of QWidget which displays a Matplotlib plot"""

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        grid = QtWidgets.QGridLayout(self)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(0)
        self.setLayout(grid)
        grid.addWidget(self.canvas, 0, 0, 1, 1)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    window = Canvas()
    window.show()
    app.exec_()
