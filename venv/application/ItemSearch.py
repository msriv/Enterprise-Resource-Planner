import sys, os, sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets, uic

class ItemSearch(QtWidgets.QMainWindow):

    # Create a pyqtSignal instance
    switchDashboard = QtCore.pyqtSignal(str)

    def __init__(self, db):
        super(ItemSearch, self).__init__()

        # DB
        self.database = db

        # Setup UI
        Form, Window = uic.loadUiType('ui/itemSearch.ui', self)
        self.form = Form()
        self.window = Window()
        self.form.setupUi(self.window)
        self.window.setWindowTitle("Add Item")

        # Connect to switch window function
        self.form.AddToTableBtn.clicked.connect(self.addToTable)
        self.form.searchItemBtn.clicked.connect(self.searchItem)

        self.itemList = self.database.fetchAll("*", "Inventory")
        print(self.itemList)

    def searchItem(self):
        counter = 0
        self.itemName = self.form.searchItemEdit.text()
        for x in self.itemList:
            if self.itemName == x[3]:
                self.form.itemListTable.insertRow(counter)
                self.form.itemListTable.setItem(counter, 0, QtWidgets.QTableWidgetItem(str(x[1])))
                self.form.itemListTable.setItem(counter, 1, QtWidgets.QTableWidgetItem(x[3]))
                self.form.itemListTable.setItem(counter, 2, QtWidgets.QTableWidgetItem(x[0]))
                self.form.itemListTable.setItem(counter, 3, QtWidgets.QTableWidgetItem(x[4]))
                self.form.itemListTable.setItem(counter, 4, QtWidgets.QTableWidgetItem(x[7]))
            else:
                self.noSuchProductMessage = QtWidgets.QMessageBox.critical(self, "No Such Item/Service",
                                                                      "You have to add this product/service to your inventory",
                                                                      QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                                      QtWidgets.QMessageBox.Yes)
            counter = counter + 1

    def addToTable(self):
        self.selectedRow = self.form.itemListTable.currentRow()
        self.selectedId = self.form.itemListTable.item(self.selectedRow, 0).text()
        self.switchDashboard.emit(self.selectedId)
        self.window.close()





