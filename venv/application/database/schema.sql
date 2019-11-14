CREATE TABLE User (
  fname VARCHAR(100) NOT NULL,
  lname VARCHAR(100) NOT NULL,
  stakeholderType VARCHAR(100) NOT NULL,
  username VARCHAR(30) NOT NULL,
  password VARCHAR(30) NOT NULL,
  email VARCHAR(50) NOT NULL,
  dob DATE NOT NULL,
  PRIMARY KEY (username)
);
CREATE TABLE Business (
  companyName VARCHAR(200) NOT NULL,
  companyOwnerName VARCHAR(100) NOT NULL,
  street VARCHAR(100) NOT NULL,
  area VARCHAR(100) NOT NULL,
  houseNumber VARCHAR(30) NOT NULL,
  pinCode VARCHAR(10) NOT NULL,
  gstNumber VARCHAR(40) NOT NULL,
  tinNumber VARCHAR(20) NOT NULL,
  pan VARCHAR(20) NOT NULL,
  username VARCHAR(30) NOT NULL,
  PRIMARY KEY (companyName),
  FOREIGN KEY (username) REFERENCES User(username)
);
CREATE TABLE Projects (
  projectId INT NOT NULL,
  projectName VARCHAR(200) NOT NULL,
  companyName VARCHAR(200) NOT NULL,
  PRIMARY KEY (projectId),
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
  uid INT NOT NULL,
  projectName VARCHAR(200) NOT NULL,
  resourceFileName VARCHAR(300) NOT NULL,
  projectStartDate DATE NOT NULL,
  dateCreated DATE NOT NULL,
  projectId INT NOT NULL,
  PRIMARY KEY (uid),
  FOREIGN KEY (projectId) REFERENCES Projects(projectId)
);
