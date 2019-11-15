import sys, os, sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class UserRegisterWindow(QtWidgets.QMainWindow):

    # Create a pyqtSignal instance
    switchLogin = QtCore.pyqtSignal(str)

    def __init__(self, db):
        super(UserRegisterWindow, self).__init__()
        # DB
        self.database = db

        # Setup UI
        Form, Window = uic.loadUiType('ui/userRegistration.ui', self)
        self.form = Form()
        self.window = Window()
        self.form.setupUi(self.window)
        self.window.setWindowTitle("Register User")

        # Connect to Switch window function
        self.form.userCancelBtn.clicked.connect(self.cancel)
        self.form.userRegBtn.clicked.connect(self.register)

        # Programming UI Components
        self.form.userStakeholder.addItems(['Employees', 'Owner', 'Admin', 'Management', 'HR'])
        self.form.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.form.confirmPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.form.confirmPasswordEdit.textChanged.connect(self.matchPassword)

    def matchPassword(self):
        if self.form.passwordEdit.text() != self.form.confirmPasswordEdit.text():
            print("Checking")
            self.form.passwordEdit.setStyleSheet("border: 1px solid red")
        else:
            self.form.passwordEdit.setStyleSheet('')
    def cancel(self):
        # Emits a signal in the environment
        self.window.close()
        self.switchLogin.emit("")

    def register(self):
        # Fetching data from Form
        self.stakeHolderType = self.form.userStakeholder.currentText()
        self.userfname = self.form.userFnameEdit.text()
        self.userlname = self.form.userLnameEdit.text()
        self.mobile = self.form.mobileEdit.text()
        self.address = self.form.addressEdit.toPlainText()
        self.username = self.form.usernameEdit.text()
        self.password = self.form.passwordEdit.text()
        self.email = self.form.emailEdit.text()
        self.dob = self.form.dateEdit.text()
        # print(self.stakeHolderType, self.userfname, self.userlname, self.username, self.password
        # , self.email, self.dob)
        self.data = "'"+self.userfname+"','"+self.userlname+"','"+self.stakeHolderType+\
                    "','"+self.username+"','"+self.password+"','"+self.email+"','"+self.dob+"'," \
                    "'"+self.address+"'"

        self.data2 = "'"+self.mobile+"','"+self.username+"'"
        # Inserting data to database
        self.database.insertOne("User", self.data)
        self.database.insertOne("User_mobileNumber", self.data2)
        # Emits a signal in the environment
        self.window.close()
        self.switchLogin.emit(self.username)
