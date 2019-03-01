from ...lib.build_csv import build_csv
from PySide2 import QtCore


class convert_thread(QtCore.QThread):
    """builds csv from input file"""
    def __init__(self, parent=None, input="lines.txt", output="lines.csv"):
        super().__init__()
        self.parent = parent
        if self.parent is not None:
            self.direc_path = self.parent.direc_path
        self.input = input
        self.output = output

    def run(self):
        build_csv(self.input, self.output)
