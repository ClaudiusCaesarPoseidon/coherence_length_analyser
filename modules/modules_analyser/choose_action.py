from .all_folders import get_all_folders
from .search import search
from PyQt5 import QtCore
QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot


class choose_action(QtCore.QThread):
    emit = QtCore.Signal(tuple)
    no = QtCore.Signal()

    def __init__(self, parent=None):
        self.parent = parent
        super().__init__()
        self.direc_path = self.parent.parent.direc_path
        self.dname = self.parent.dname
        self.files = None
        self.folders = None

    def run(self):
        if self.dname != '':
            s = search(self.dname, 'image')
            self.files = s.files
            if s.files == []:
                self.folders = get_all_folders(self.dname)
                self.emit.emit((self.folders, 1))
            else:
                self.emit.emit((self.files, 0))
        else:
            print("No folder selected.")
            self.no.emit()
