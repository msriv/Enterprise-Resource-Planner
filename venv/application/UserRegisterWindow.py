import sys, os, sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class UserRegisterWindow(QtWidgets.QMainWindow):

    # Create a pyqtSignal instance
    switch_next_window = QtCore.pyqtSignal()

    # Create a pyqtSignal instance for each different window switching
    switch_prev_window = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(UserRegisterWindow, self).__init__(parent)
        Form, Window = uic.loadUiType('ui/userRegistration.ui', self)

        self.form = Form()
        self.window = Window()

        self.form.setupUi(self.window)
        # Connect to Switch window function
        self.form.userCancelBtn.clicked.connect(self.cancel)

    def cancel(self):
        # Emits a signal in the environment
        self.window.close()
        self.switch_prev_window.emit()

    def register(self):

        # Emits a signal in the environment
        self.window.close()
        self.switch_prev_window.emit()
