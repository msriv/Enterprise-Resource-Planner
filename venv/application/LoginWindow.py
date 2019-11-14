import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class LoginWindow(QtWidgets.QMainWindow):

    # Create a pyqtSignal instance
    switchNewUser = QtCore.pyqtSignal()
    switchNewBusiness = QtCore.pyqtSignal()
    switchDashboard = QtCore.pyqtSignal()

    def __init__(self, db):
        super(LoginWindow, self).__init__()

        # DB
        self.database = db

        # Setup UI
        Form, Window = uic.loadUiType('ui/LoginWindow.ui', self)
        self.form = Form()
        self.window = Window()
        self.form.setupUi(self.window)
        self.window.setWindowTitle("Login")

        # Programming UI
        self.form.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        # Connect to Switch Window Function
        self.form.registerBtn.clicked.connect(self.onClicked)

        # Fetch Login Data
        self.form.loginBtn.clicked.connect(self.login)

    def login(self):
        self.username = self.form.usernameEdit.text()
        self.password = self.form.passwordEdit.text()

        if self.database.validate(["username", "password"], [self.username, self.password]):
            if self.database.business_exists():
                self.switchDashboard.emit()
            else:
                self.switchNewBusiness.emit()
        else:
            self.form.messageLabel.setText("Invalid Username/Password")

    def onClicked(self):
        # Emits a signal in the environment
        print(self.switchNewUser.emit())

