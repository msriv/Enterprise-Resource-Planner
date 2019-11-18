import sys, os, sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class AddProject(QtWidgets.QMainWindow):

    switchDashboard = QtCore.pyqtSignal(str)

    def __init__(self, db, companyName):
        super(AddProject, self).__init__()
        self.companyName = companyName
        # DB
        self.database = db

        # Setup UI
        Form, Window = uic.loadUiType('ui/AddProject.ui', self)
        self.form = Form()
        self.window = Window()
        self.form.setupUi(self.window)
        self.window.setWindowTitle("Add Project")

        self.form.addPBtn.clicked.connect(self.newProject)

    def newProject(self):
        self.switchDashboard.emit()