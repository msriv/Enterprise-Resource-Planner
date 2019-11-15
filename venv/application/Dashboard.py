import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

"""
Try this - Add a add new business button to this ui and if business table 
is create a new ui with disabled fields until a new business is created.
"""

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
        self.window.show()

        # Programming UI
        self.nameOfUser = self.database.fetchOne("fname || ' ' || lname", "User", "username", self.username)
        self.form.nameOfUser.setText(self.nameOfUser[0][0])
        self.businessList = self.database.fetchAll("companyName", "Business", "username", self.username)
        for i in self.businessList:
            self.form.businessList.addItem(i[0])
        # Connect to Switch Window Function
        # self.form.registerBtn.clicked.connect(self.onClicked)



