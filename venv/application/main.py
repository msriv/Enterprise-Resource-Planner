import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from LoginWindow import LoginWindow
from UserRegisterWindow import UserRegisterWindow
from BusinessRegisterWindow import BusinessRegisterWindow
from Dashboard import Dashboard
from database.Database import Database

class Controller:

    def __init__(self):
        self.database = Database()
        pass

    def show_login(self):
        self.login = LoginWindow(self.database)
        self.login.switchNewUser.connect(self.show_userRegister)
        self.login.switchNewBusiness.connect(self.show_businessRegistration)
        self.login.switchDashboard.connect(self.show_dashboard)
        self.login.window.show()

    def show_userRegister(self):
        self.uRegister = UserRegisterWindow(self.database)
        self.uRegister.switchLogin.connect(self.show_login)
        self.login.window.close()
        self.uRegister.window.show()

    def show_dashboard(self):
        self.dashboard = Dashboard(self.database)
        self.dashboard.switchRegBusiness2.connect(self.show_businessRegistration)
        # self.bRegister.window.close()
        # self.dashboard.window.show()

    def show_businessRegistration(self):
        self.bRegister = BusinessRegisterWindow(self.database)
        self.login.window.close()
        self.bRegister.switchDashboard.connect(self.show_dashboard)
        self.bRegister.window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open("css/main.css", "r").read())
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()