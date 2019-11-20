import sys, os, sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets, uic

class AddDelivery(QtWidgets.QMainWindow):

    # Create a pyqtSignal instance
    switchDashboardOM = QtCore.pyqtSignal(str)

    def __init__(self, db):
        super(AddDelivery, self).__init__()

        # DB
        self.database = db

        # Setup UI
        Form, Window = uic.loadUiType('ui/addDelivery.ui', self)
        self.form = Form()
        self.window = Window()
        self.form.setupUi(self.window)
        self.window.setWindowTitle("Add Delivery Preference")

        # Connect to switch window function
        self.form.addDeliveryBtn.clicked.connect(self.switchDashboard)
        self.form.cancelBtn.clicked.connect(self.cancelWindow)

    def cancelWindow(self):
        self.window.close()

    def switchDashboard(self):
        self.deliveryService = self.form.deliveryServiceEdit.text()
        self.poc = self.form.servicePocEdit.text()
        self.serviceAddress = self.form.serviceAddressEdit.toPlainText()
        self.mobileNumber = self.form.deliveryMobileEdit.text()

        delimiter = "', '"

        self.dataArr = [self.deliveryService, self.poc, self.serviceAddress, self.mobileNumber]
        self.data = delimiter.join(self.dataArr)

        self.database.insertOne("ShipmentPref", "", "'"+self.data+"'")

        self.switchDashboardOM.emit("Delivery")
        self.window.close()
