CREATE TABLE User (
  fname VARCHAR(100) NOT NULL,
  lname VARCHAR(100) NOT NULL,
  stakeholderType VARCHAR(100) NOT NULL,
  username VARCHAR(30) NOT NULL,
  password VARCHAR(30) NOT NULL,
  email VARCHAR(50) NOT NULL,
  dob DATE NOT NULL,
  address VARCHAR(500) NOT NULL,
  PRIMARY KEY (username)
);
CREATE TABLE Business (
  companyName VARCHAR(200) NOT NULL,
  companyOwnerName VARCHAR(100) NOT NULL,
  street VARCHAR(100) NOT NULL,
  area VARCHAR(100) NOT NULL,
  buildingNumber VARCHAR(30) NOT NULL,
  pinCode VARCHAR(10) NOT NULL,
  gstNumber VARCHAR(40) NOT NULL,
  tinNumber VARCHAR(20) NOT NULL,
  pan VARCHAR(20) NOT NULL,
  PRIMARY KEY (companyName)
);
CREATE TABLE Company_User (
    companyName VARCHAR(200) NOT NULL,
    username VARCHAR(30) NOT NULL,
    FOREIGN KEY (companyName) REFERENCES Business(companyName)
    FOREIGN KEY (username) REFERENCES User(Username)
);
CREATE TABLE Projects (
  projectId INTEGER PRIMARY KEY AUTOINCREMENT,
  projectName VARCHAR(200) NOT NULL,
  companyName VARCHAR(200) NOT NULL,
  projectDesc VARCHAR(1000) NOT NULL,
  startDate DATE NOT NULL,
  endDate DATE NOT NULL,
  pManager VARCHAR(100) NOT NULL,
  FOREIGN KEY (companyName) REFERENCES Business(companyName)
);
CREATE TABLE User_mobileNumber (
  mobileNumber VARCHAR(10) NOT NULL,
  username VARCHAR(30) NOT NULL,
  FOREIGN KEY (username) REFERENCES User(username)
);
CREATE TABLE Business_mobileNumber (
  mobileNumber VARCHAR(10) NOT NULL,
  companyName VARCHAR(200) NOT NULL,
  PRIMARY KEY (mobileNumber),
  FOREIGN KEY (companyName) REFERENCES Business(companyName)
);
CREATE TABLE MRP (
  uid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  projectName VARCHAR(200) NOT NULL,
  resourceFileName VARCHAR(300) NOT NULL,
  projectStartDate DATE NOT NULL,
  dateCreated DATE NOT NULL,
  companyName VARCHAR(200) NOT NULL,
  FOREIGN KEY (companyName) REFERENCES Business(companyName)
  FOREIGN KEY (projectName) REFERENCES Projects(projectName)
);
CREATE TABLE _init_Config (
  uid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  key VARCHAR(500) NOT NULL,
  value VARCHAR(300) NOT NULL
);
CREATE TABLE ShipmentPref(
    deliveryService VARCHAR(200) NOT NULL PRIMARY KEY,
    pointOfContact VARCHAR(200) NOT NULL,
    address VARCHAR(500) NOT NULL,
    mobileNuber VARCHAR(10) NOT NULL
);
CREATE TABLE OM (
    deliverTo VARCHAR(50) NOT NULL,
    buyerName VARCHAR(100) NOT NULL,
    buyerAddress VARCHAR(300) NOT NULL,
    purchaseOrderNumber INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    orderDate DATE NOT NULL,
    expectedDeliveryDate DATE NOT NULL,
    shipmentPref VARCHAR(200) NOT NULL,
    companyName VARCHAR(200) NOT NULL,
    FOREIGN KEY (companyName) REFERENCES Business(companyName)
);

CREATE TABLE Inventory (
    itemType VARCHAR(50) NOT NULL,
    itemId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    thumbnail VARCHAR(300),
    itemName VARCHAR(200) NOT NULL,
    itemSKU VARCHAR(200),
    itemUnit VARCHAR(100),
    returnable INT NOT NULL,
    manufacturer VARCHAR(200),
    ISBN VARCHAR(200),
    sellingPrice INT,
    sellingAccount VARCHAR(100),
    costPrice INT,
    costAccount VARCHAR(100)
);