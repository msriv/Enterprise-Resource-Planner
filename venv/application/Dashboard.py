import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Dashboard(QtWidgets.QMainWindow):

    switchRegBusiness = QtCore.pyqtSignal()
    switchRegBusiness2 = QtCore.pyqtSignal()

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
        self.businessList = self.database.fetchAll("companyName", "Business", "username", self.username)

        self.deliverToButtonGroup = QtWidgets.QButtonGroup()
        self.deliverToButtonGroup.addButton(self.form.om_organizationRadio)
        self.deliverToButtonGroup.addButton(self.form.om_customerRadio)

        self.productTable = self.form.om_itemTable
        self.productTable.setColumnCount(7)
        self.productTable.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem(""))
        self.btn = QtWidgets.QPushButton(self.productTable)
        self.btn.setText('Hello')
        self.hLayout = QtWidgets.QHBoxLayout()
        self.hLayout.addWidget(self.btn)
        self.cellWidget = QtWidgets.QWidget()
        self.cellWidget.setLayout(self.hLayout)
        self.productTable.setCellWidget(5, 6, self.cellWidget)

        for i in self.businessList:
            self.form.businessList.addItem(i[0])
        # Connect to Switch Window Function
        # self.form.registerBtn.clicked.connect(self.onClicked)



