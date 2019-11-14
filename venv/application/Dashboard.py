import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

"""
Try this - Add a add new business button to this ui and if business table 
is create a new ui with disabled fields until a new business is created.
"""

class Dashboard(QtWidgets.QMainWindow):

    switchRegBusiness = QtCore.pyqtSignal()
    switchRegBusiness2 = QtCore.pyqtSignal()

    def __init__(self, db):
        super(Dashboard, self).__init__()

        # DB
        self.database = db
        Form, Window = uic.loadUiType('ui/Dashboard.ui', self)
        self.form = Form()
        self.window = Window()
        # Setup UI
        if self.database.business_exists():
            self.form.setupUi(self.window)
            self.window.show()
        else:
            self.showdialog()

        # Connect to Switch Window Function
        # self.form.registerBtn.clicked.connect(self.onClicked)

    def showdialog(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)

        self.msg.setText("You need to create a new business to use this application")
        self.msg.setWindowTitle("Warning")
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        self.msg.buttonClicked.connect(self.revert)

        retval = self.msg.exec_()

    def revert(self):
        print("Clicked ok")
        print(self.switchRegBusiness2.emit())
