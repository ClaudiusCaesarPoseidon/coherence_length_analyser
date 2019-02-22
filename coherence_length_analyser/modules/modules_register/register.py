from ...lib import functions
from ..eigen_widgets import Widgetb
import os
import hashlib
from PySide2 import QtCore, QtWidgets, QtGui
from ConvertQt import uic


class Register(Widgetb):
    def __init__(self, parent=None, config=None):
        super().__init__()
        self.parent = parent
        self.config = config
        file = functions.resource_path(os.path.join("ui", "register.ui"))
        uic.loadUi(file, self)
        print("To register Please enter a username and a password and repeat the passord.")
        print("The username must consist only of letters.")
        self.Close.clicked.connect(self.close)
        self.Register.clicked.connect(self.register)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.resized.connect(self.set_Size)
        self.height = None
        self.fontsize = None
        self.font_button = None
        self.font_text = None
        self.x = None
        self.y = None
        self.user_dict = None

    def set_Size(self):
        self.height = int(self.geometry().height())
        fontsize = (self.height / 75)
        font_button = QtGui.QFont()
        font_button.setPointSize(fontsize)
        fontsize = (self.height / 75)
        if fontsize <= 8:
            fontsize = 8
        if fontsize >= 16:
            fontsize = 16
        font_text = QtGui.QFont()
        font_text.setPointSize(fontsize)
        for item in self.findChildren(QtWidgets.QPushButton):
            item.setFont(font_button)
        for item in self.findChildren(QtWidgets.QLineEdit):
            item.setFont(font_text)
        for item in self.findChildren(QtWidgets.QPlainTextEdit):
            item.setFont(font_text)
        for item in self.findChildren(QtWidgets.QComboBox):
            item.setFont(font_text)

        self.Console.setMinimumSize(
            QtCore.QSize(0, int(350 / 450 * self.height)))

    def end_(self):
        pass

    def register(self):
        if len(self.Name.text()) >= 5:
            if self.Name.text().isalpha() is True:
                if self.Password.text().isalnum() is True:
                    if self.Password.text() == self.Password2.text():
                        if len(self.Password.text()) >= 8:
                            sys_drive = os.path.join(
                                os.getenv("SystemDrive"), os.sep)
                            if os.path.exists(
                                os.path.join(
                                    sys_drive,
                                    "coherence_length_analyser",
                                    "login.txt")) is False:
                                if os.path.exists(
                                    os.path.join(
                                        sys_drive,
                                        "coherence_length_analyser")) is False:
                                    functions.build_directory(os.path.join(
                                        sys_drive, "coherence_length_analyser"))
                                with open(os.path.join(sys_drive, "coherence_length_analyser", "login.txt"), 'w'):
                                    pass
                            if os.stat(
                                os.path.join(
                                    sys_drive,
                                    "coherence_length_analyser",
                                    "login.txt")).st_size > 0:
                                with open(os.path.join(sys_drive, "coherence_length_analyser", "login.txt"), 'r') as f:
                                    self.x = f.read()
                                lis = []
                                self.y = self.x.split("\n")
                                for i in self.y:
                                    lis.append(i.split("\t"))
                                self.user_dict = {k[0]: k[1] for k in lis}
                                try:
                                    self.user_dict[self.Name.text(
                                    )]  # pylint: disable=W0106
                                    print("Username already in use.")
                                except KeyError:
                                    with open(os.path.join(sys_drive, "coherence_length_analyser", "login.txt"), 'a') as f:
                                        pword = hashlib.md5(
                                            functions.vigenere(
                                                self.Password.text(),
                                                self.Name.text()).encode("UTF-8")).hexdigest()
                                        f.write(
                                            "\n" + self.Name.text() + "\t" + pword)
                                        print("Registration complete.")
                            else:
                                with open(os.path.join(sys_drive, "coherence_length_analyser", "login.txt"), 'a') as f:
                                    pword = hashlib.md5(
                                        functions.vigenere(
                                            self.Password.text(),
                                            self.Name.text()).encode("UTF-8")).hexdigest()
                                    f.write(self.Name.text() + "\t" + pword)
                                    print("Registration complete.")
                        else:
                            print("The password is not long enough.")
                    else:
                        print("The passwords do not match.")
                else:
                    print("The password is not alpha-numeric.")
            else:
                print("The username does not consist of only letters.")
        else:
            print("The username is not long enough.")
