from .stream import Stream
from .dialog import Dialog
import sys
from PySide2 import QtCore, QtGui


class Widgetb(Dialog):
    """Subclasses QDaialog to include a function the use the print functio"""\
        """the print to a QTextEdit"""

    def __init__(self, parent=None, config=None):
        super().__init__()
        self.parent = parent
        self.config = config
        self.default_stdout = sys.stdout
        self.default_stderr = sys.stderr
        self.setWindowFlags(self.windowFlags() |
                            QtCore.Qt.WindowSystemMenuHint |
                            QtCore.Qt.WindowMinMaxButtonsHint)
        sys.stdout = Stream()
        sys.stdout.newText.connect(self.onUpdateText)

    def resizeEvent(self, event):
        self.resized.emit()
        return super().resizeEvent(event)

    def onUpdateText(self, text):
        cursor = self.Console.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.Console.setTextCursor(cursor)
        self.Console.ensureCursorVisible()
