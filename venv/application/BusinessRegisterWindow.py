import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class BusinessRegisterWindow(QtWidgets.QMainWindow):

    switchDashboard = QtCore.pyqtSignal()

    def __init__(self, db):
        super(BusinessRegisterWindow, self).__init__()

        # DB
        self.database = db

        # Setup UI
        Form, Window = uic.loadUiType('ui/businessRegistration.ui', self)
        self.form = Form()
        self.window = Window()
        self.form.setupUi(self.window)
        self.window.setWindowTitle("Register Business")

        # Click Handlers
        self.form.comRegBtn.clicked.connect(self.registerBusiness)
        self.form.comCancelBtn.clicked.connect(self.handleNoBReg)

        # Connect to Switch Window Function
        # self.form.registerBtn.clicked.connect(self.regiisterBusiness)
    def registerBusiness(self):
        print("Hello")

    def handleNoBReg(self):
        self.window.close()
        self.switchDashboard.emit()

