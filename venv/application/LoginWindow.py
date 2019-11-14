import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class LoginWindow(QtWidgets.QMainWindow):

    # Create a pyqtSignal instance
    switch_next_window = QtCore.pyqtSignal()
    UserTable = []

    def __init__(self, db):
        super(LoginWindow, self).__init__()
        Form, Window = uic.loadUiType('ui/LoginWindow.ui', self)
        self.form = Form()
        self.window = Window()

        self.form.setupUi(self.window)
        self.database = db
        # Connect to Switch Window Function
        self.form.registerBtn.clicked.connect(self.onClicked)
        # self.show()
        # if(len(UserTable) == 0):
        #     UserTable = self.database.getAll()
        # else:
        # print("Already filled usertable")
        self.database.getAll()
    def onClicked(self):
        # Emits a signal in the environment
        self.switch_next_window.emit()

