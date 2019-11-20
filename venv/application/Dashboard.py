import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
from matplotlib.collections import PolyCollection
import time
import random
from threading import Thread

class Dashboard(QtWidgets.QMainWindow):

    switchAddProject = QtCore.pyqtSignal(str)
    switchAddDelivery = QtCore.pyqtSignal()

    def __init__(self, db, username):
        super(Dashboard, self).__init__()
        self.username = username
        self.timelineData = []
        self.cats = []
        self.colormapping = []
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

        self.productTable = self.form.om_itemTable

        QtWidgets.QCheckBox().stateChanged.connect()



        # MRP Plot
        self.plt = plt
        self.figure = self.plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.form.mrpLayout.setColumnStretch(0, 2)
        self.form.mrpLayout.setColumnStretch(1, 2)
        self.form.mrpLayout.setRowStretch(0, 4)
        self.form.mrpLayout.addWidget(self.canvas, 0, 1)

        # Button Connections
        self.form.addProject.clicked.connect(self.addProjectWindow)
        self.form.addTask.clicked.connect(self.plot)
        self.form.rstGraph.clicked.connect(self.clearPlot)
        self.form.saveFile.clicked.connect(self.saveTimeline)
        self.form.om_addShipmentPref.clicked.connect(self.addShipmentWindow)
        self.form.om_printInvoice.clicked.connect(self.saveOrder)
        self.form.addToTableBtn.clicked.connect(self.addToTable)
        self.form.addThumbnailBtn.clicked.connect(self.setThumbnail)
        self.form.addToInventoryBtn.clicked.connect(self.addToInventory)
        self.form.itemSalesInformation.stateChanged.connect(self.spInformation)
        self.form.itemPurchaseInformation.stateChanged.connect(self.cpInformation)
        # ComboBox Updates
        self.projectList = self.database.fetchAll("projectName", "Projects")
        self.form.projectTitle.addItem("Select Project")
        for i in self.projectList:
            self.form.projectTitle.addItem(i[0])
        self.deliverPrefList = self.database.fetchAll("deliveryService", "ShipmentPref")
        self.form.om_selectShipmentPref.addItem("Select Delivery Service")
        for x in self.deliverPrefList:
            self.form.om_selectShipmentPref.addItem(x[0])

    # Complete these function for toggle information !!!!!!!
    def spInformation(self, state):
        if state > 0:


    def cpInformation(self, state):


    def addToTable(self):
        if len(self.database.fetchAll("itemName", "Inventory")) == 0:
            self.noProductMessage = QtWidgets.QMessageBox.warning(self, "No Inventory Warning",
                                                                  "You have to add products/services to your inventory",
                                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                          QtWidgets.QMessageBox.Yes)
    def addShipmentWindow(self):
        self.switchAddDelivery.emit()

    def addToInventory(self):
        self.itemType = self.radioLabel(self.form.inventoryGoodsRBtn, self.form.inventoryServiceRBtn)
        self.thumbnailPath = self.fThumbnail
        self.itemName = self.form.itemNameEdit.text()
        self.itemSKU = self.form.itemSKUEdit.text()
        self.itemUnit = self.form.itemUnitEdit.text()
        self.itemReturnable = int(self.form.itemReturnableCheck.isChecked())
        self.itemManufacturer = self.form.itemManufacturerEdit.text()
        self.itemISBN = self.form.itemISBNEdit.text()

    def setThumbnail(self):
        self.openedFileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                              '', "*.jpg ;; *.png")
        self.fThumbnail = str(self.openedFileName[0])
        self.fThumbnailPixmap = QtGui.QPixmap(self.fThumbnail)
        self.form.thumbnailLabel.setPixmap(self.fThumbnailPixmap)


    def saveOrder(self):
        self.deliveryTo = self.radioLabel(self.form.om_organizationRadio, self.form.om_customerRadio)
        self.buyerName = self.form.om_buyerName.text()
        self.buyerAdd = self.form.om_buyerAddress.toPlainText()
        self.orderDate = self.form.om_orderDate.text()
        self.expectedDeliveryDate = self.form.om_expDelDate.text()
        self.shipmentPref = self.form.selectShipment.currentText()


    def radioLabel(self, btn1, btn2):
        if btn1.isChecked() == True:
            return btn1.text()
        elif btn2.isChecked() == True:
            return btn2.text()

    def addProjectWindow(self):
        self.companyName = self.form.businessList.currentItem().text()
        print(self.companyName)
        self.switchAddProject.emit(self.companyName)

    def clearPlot(self):
        self.plt.clf()
        self.canvas.draw()

    def saveTimeline(self):
        savedFileName = QtWidgets.QFileDialog.getSaveFileName(self, 'Save file',
         '/home/msrivastava/untitled.jpg', "*.jpg ;; *.png")
        fName = str(savedFileName[0])
        file_extension = fName.split(".")[-1]
        if file_extension == 'png' or file_extension == 'PNG':
            self.canvas.print_png(fName)
        if file_extension == 'jpg' or file_extension == 'jpeg' or file_extension == 'JPG' or file_extension == 'JPEG':
            self.canvas.print_jpg(fName)
        t1 = Thread(target=self.fileSaved)
        t1.start()

        self.projectName = self.form.projectTitle.currentText()
        self.resourceFileName = fName
        self.projectStartDate = self.timelineData[0][0].strftime("%Y-%m-%d")
        self.dateCreated = dt.date.today().strftime("%Y-%m-%d")

        delimiter = "', '"
        self.companyName = self.form.businessList.currentItem().text()
        self.dataArr = [self.projectName, self.resourceFileName, self.projectStartDate,
                        self.dateCreated, self.companyName]
        self.data = delimiter.join(self.dataArr)
        self.database.insertOne("MRP", "projectName, resourceFileName, projectStartDate, dateCreated, companyName", "'"+self.data+"'")

        self.form.taskTitle.setText("")
        self.form.taskDescription.setText("")
        self.form.startDateEdit.setDate(dt.datetime.strptime("2000-01-01", "%Y-%m-%d").date())
        self.form.endDateEdit.setDate(dt.datetime.strptime("2000-01-01", "%Y-%m-%d").date())

    def fileSaved(self):
        self.form.fileSavedNotif.setText("File Saved.")
        time.sleep(3)
        self.form.fileSavedNotif.setText("")

    def plot(self):
        self.taskTitle = self.form.taskTitle.text().strip()
        self.taskDescription = self.form.taskDescription.toPlainText()
        self.taskStartDate = dt.datetime.strptime(self.form.startDateEdit.text(), "%Y-%m-%d").date()
        self.taskEndDate = dt.datetime.strptime(self.form.endDateEdit.text(), "%Y-%m-%d").date()

        self.timelineData.append(((dt.datetime(self.taskStartDate.year, self.taskStartDate.month, self.taskStartDate.day))
                                 , dt.datetime(self.taskEndDate.year, self.taskEndDate.month, self.taskEndDate.day),
                                 self.taskTitle))
        self.counter = 0

        for i in self.cats:
            if self.taskTitle == i:
                self.counter = self.counter+1

        if self.counter == 0:
            self.cats.append(self.taskTitle)
            self.colormapping.append(self.taskTitle)

        self.verts = []
        self.colors = []

        for d in self.timelineData:
            v = [(mdates.date2num(d[0]), (self.cats.index(d[2])+1) - .4),
                 (mdates.date2num(d[0]), (self.cats.index(d[2])+1) + .4),
                 (mdates.date2num(d[1]), (self.cats.index(d[2])+1) + .4),
                 (mdates.date2num(d[1]), (self.cats.index(d[2])+1) - .4),
                 (mdates.date2num(d[0]), (self.cats.index(d[2])+1) - .4)]
            self.verts.append(v)
            self.colors.append("C"+str(self.colormapping.index(self.cats[self.cats.index(d[2])])))

        bars = PolyCollection(self.verts, facecolors=self.colors)

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.add_collection(bars)
        ax.autoscale()
        loc = mdates.DayLocator(bymonthday=[7,14,21,28])
        ax.xaxis.set_major_locator(loc)
        ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(loc))

        ax.set_yticks(list(range(1, len(self.cats)+1)))
        print(self.cats)
        ax.set_yticklabels(self.cats)
        self.canvas.draw()

        self.form.taskTitle.setText("")
        self.form.taskDescription.setText("")
        self.form.startDateEdit.setDate(dt.datetime.strptime("2000-01-01", "%Y-%m-%d").date())
        self.form.endDateEdit.setDate(dt.datetime.strptime("2000-01-01", "%Y-%m-%d").date())

    def updateUI(self, source):
        if source == "Project":
            self.projectList = self.database.fetchAll("projectName", "Projects")
            self.form.projectTitle.clear()
            self.form.projectTitle.addItem("Select Project")
            for i in self.projectList:
                self.form.projectTitle.addItem(i[0])
        elif source == "Delivery":
            self.deliverPrefList = self.database.fetchAll("deliveryService", "ShipmentPref")
            self.form.om_selectShipmentPref.clear()
            self.form.om_selectShipmentPref.addItem("Select Delivery Service")
            for x in self.deliverPrefList:
                self.form.om_selectShipmentPref.addItem(x[0])