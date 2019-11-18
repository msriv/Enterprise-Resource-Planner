import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random

class Dashboard(QtWidgets.QMainWindow):

    switchAddProject = QtCore.pyqtSignal(str)

    def __init__(self, db, username):
        super(Dashboard, self).__init__()
        self.username = username

        # DB
        self.database = db

        # Setup UI
        Form, Window = uic.loadUiType('ui/Dashboard.ui', self)
        self.form = Form()
        self.window = Window()
        self.form.setupUi(self.window)
        # self.window.show()

        # Programming UI
        self.nameOfUser = self.database.fetchOne("fname || ' ' || lname", "User", "username", self.username)
        self.form.nameOfUser.setText(self.nameOfUser[0])
        self.businessList = self.database.fetchAllBy("companyName", "Company_User", "username", self.username)

        for i in self.businessList:
            self.form.businessList.addItem(i[0])

        self.deliverToButtonGroup = QtWidgets.QButtonGroup()
        self.deliverToButtonGroup.addButton(self.form.om_organizationRadio)
        self.deliverToButtonGroup.addButton(self.form.om_customerRadio)

        self.productTable = self.form.om_itemTable

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.form.mrpLayout.setColumnStretch(0, 2)
        self.form.mrpLayout.setColumnStretch(1, 2)
        self.form.mrpLayout.setRowStretch(0, 4)
        self.form.mrpLayout.addWidget(self.canvas, 0, 1)

        self.plot()

        self.form.addProject.clicked.connect(self.addProjectWindow)
    def addProjectWindow(self):

        self.companyName = self.form.businessList.currentItem().text()
        print(self.companyName)
        self.switchAddProject.emit(self.companyName)

    def plot(self):
        print("Hello")
        # Connect to Switch Window Function
        # self.form.registerBtn.clicked.connect(self.onClicked)

    def updateUI(self):
        self.projectList = self.database.fetchAll("Project")