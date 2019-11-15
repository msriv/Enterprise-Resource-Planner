import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class BusinessRegisterWindow(QtWidgets.QMainWindow):

    switchDashboard = QtCore.pyqtSignal(str)

    def __init__(self, db, username):
        super(BusinessRegisterWindow, self).__init__()

        self.username = username
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
        # Fetch Data from Form
        self.companyName = self.form.companyName.text()
        self.companyOwner = self.form.companyOwner.text()
        self.mobileNumber = self.form.mobileNumber.text()
        self.email = self.form.email.text()
        self.comStreet = self.form.comStreet.text()
        self.comArea = self.form.comArea.text()
        self.comBuildingNumber = self.form.comBuildingNumber.text()
        self.comPincode = self.form.comPincode.text()
        self.companyGST = self.form.companyGST.text()
        self.companyTIN = self.form.companyTIN.text()
        self.companyPAN = self.form.companyPAN.text()

        # Insert into Business Table
        self.data = "'" + self.companyName + "','" + self.companyOwner + "','" + self.comStreet + \
                    "','" + self.comArea + "','" + self.comBuildingNumber + "','" + self.comPincode + "','" \
                    + self.companyGST + "','" + self.companyTIN + "','" + self.companyPAN + "','" + self.username + "'"

        self.data2 = "'" + self.mobileNumber + "','" + self.companyName + "'"

        self.database.insertOne("Business", self.data)
        self.database.insertOne("Business_mobileNumber", self.data2)

        self.switchDashboard.emit(self.username)

    def handleNoBReg(self):
        if self.showdialog():
            print("Yes")


    def showdialog(self):
        self.noBusinessResponse = QtWidgets.QMessageBox.warning(self, "No Business Warning",
                                                                "You need to create a business to use this application",
                                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                                QtWidgets.QMessageBox.Yes)
        if self.noBusinessResponse == QtWidgets.QMessageBox.Yes:
            return True
        else:
            return False
