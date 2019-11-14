import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from LoginWindow import LoginWindow
from UserRegisterWindow import UserRegisterWindow
from database.Database import Database

class Controller:

    def __init__(self):
        self.database = Database()
        pass

    def show_login(self):
        self.login = LoginWindow(self.database)
        self.login.switch_next_window.connect(self.show_register)
        self.login.window.show()

    def show_register(self):
        self.register = UserRegisterWindow()
        self.register.switch_prev_window.connect(self.show_login)
        self.login.window.close()
        self.register.window.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open("css/main.css", "r").read())
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()