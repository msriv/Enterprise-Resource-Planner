import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from LoginWindow import LoginWindow
from UserRegisterWindow import UserRegisterWindow
from BusinessRegisterWindow import BusinessRegisterWindow
from AddDelivery import AddDelivery
from Dashboard import Dashboard
from AddProject import AddProject
from ItemSearch import ItemSearch
from database.Database import Database

class Controller:

    def __init__(self):
        self.database = Database()
        pass

    def show_login(self, username):
        self.login = LoginWindow(self.database, username)
        self.login.switchNewUser.connect(self.show_userRegister)
        self.login.switchNewBusiness.connect(self.show_businessRegistration)
        self.login.switchDashboard.connect(self.show_dashboard)
        self.login.window.show()

    def show_userRegister(self):
        self.uRegister = UserRegisterWindow(self.database)
        self.uRegister.switchLogin.connect(self.show_login)
        self.login.window.close()
        self.uRegister.window.show()

    def show_dashboard(self, username):
        self.dashboard = Dashboard(self.database, username)
        self.dashboard.switchAddProject.connect(self.show_addProject)
        self.dashboard.switchAddDelivery.connect(self.show_addDelivery)
        self.dashboard.switchInventoryInsert.connect(self.show_itemSearch)
        self.dashboard.window.showFullScreen()
        # self.bRegister.window.close()

    def show_businessRegistration(self, username):
        self.bRegister = BusinessRegisterWindow(self.database, username)
        self.login.window.close()
        self.bRegister.switchDashboard.connect(self.show_dashboard)
        self.bRegister.window.show()

    def show_addProject(self, companyName):
        self.addProjectWin = AddProject(self.database, companyName)
        self.addProjectWin.switchDashboard.connect(self.updateDashboardUI)
        self.addProjectWin.window.show()

    def updateDashboardUI(self, source):
        self.dashboard.updateUI(source)

    def show_addDelivery(self):
        self.addDeliveryPref = AddDelivery(self.database)
        self.addDeliveryPref.switchDashboardOM.connect(self.updateDashboardUI)
        self.addDeliveryPref.window.show()

    def show_itemSearch(self):
        self.itemSearch = ItemSearch(self.database)
        self.itemSearch.switchDashboard.connect(self.updateItemTable)
        self.itemSearch.window.show()

    def updateItemTable(self, itemId):
        self.dashboard.addToItemTable(itemId)

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open("css/main.css", "r").read())
    controller = Controller()
    controller.show_login("")
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()