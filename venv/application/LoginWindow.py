import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class LoginWindow(QtWidgets.QMainWindow):

    # Create a pyqtSignal instance
    switchNewUser = QtCore.pyqtSignal()
    switchNewBusiness = QtCore.pyqtSignal(str)
    switchDashboard = QtCore.pyqtSignal(str)

    def __init__(self, db, username):
        super(LoginWindow, self).__init__()

        self.username = username

        # DB
        self.database = db

        # Setup UI
        Form, Window = uic.loadUiType('ui/LoginWindow.ui', self)
        self.form = Form()
        self.window = Window()
        self.form.setupUi(self.window)
        self.window.setWindowTitle("Login")
        # print(self.database.fetchAllBy("key, value", "_init_Config", "key", "storagePath"))
        # if len(self.database.fetchAllBy("key, value", "_init_Config", "key", "storagePath")) == 0:
        #     self.storagePath, self.ok = QtWidgets.QInputDialog.getText(self, 'Storage',
        #                                 'Initialize the Storage Path')
        #     if self.ok:
        #         delimiter = "', '"
        #         self.dataArr = ["storagePath", str(self.storagePath)]
        #         self.data = delimiter.join(self.dataArr)
        #         self.database.insertOne("_init_Config", "key, value", "'" + self.data + "'")

        # Programming UI
        self.form.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        if username != "":
            self.form.usernameEdit.setText(self.username)

        # Connect to Switch Window Function
        self.form.registerBtn.clicked.connect(self.onClicked)

        # Fetch Login Data
        self.form.loginBtn.clicked.connect(self.login)

    def login(self):
        self.username = self.form.usernameEdit.text()
        self.password = self.form.passwordEdit.text()

        if self.database.validate(["username", "password"], [self.username, self.password]):
            if self.database.business_exists(self.username):
                self.switchDashboard.emit(self.username)
                self.window.close()
            else:
                self.switchNewBusiness.emit(self.username)
        else:
            self.form.messageLabel.setText("Invalid Username/Password")

    def onClicked(self):
        # Emits a signal in the environment
        print(self.switchNewUser.emit())

