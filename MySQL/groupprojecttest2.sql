CREATE DATABASE myStore;

USE myStore;

CREATE TABLE Customers(
ID INT PRIMARY KEY AUTO_INCREMENT,
Fname VARCHAR(40) NOT NULL,
Lname VARCHAR(40),
Phone VARCHAR(15) NOT NULL,
Email VARCHAR(40)
);

CREATE TABLE Products(
ID INT PRIMARY KEY AUTO_INCREMENT,
Color VARCHAR(40),
Size VARCHAR(40) NOT NULL,
Brand VARCHAR(40)
);

CREATE TABLE Tracking(
ID INT PRIMARY KEY AUTO_INCREMENT,
DeliveryDate DATE NOT NULL,
DeliveryAddress VARCHAR(200),
Status VARCHAR(100),
TrackingID VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Orders(
ID INT PRIMARY KEY AUTO_INCREMENT,
CustomerID INT NOT NULL,
ProductID INT NOT NULL,
Date DATETIME NOT NULL,
Status VARCHAR(10) NOT NULL,
TrackingID INT,
FOREIGN KEY (CustomerID) REFERENCES Customers(ID),
FOREIGN KEY (ProductID) REFERENCES Products(ID),
FOREIGN KEY (TrackingID) REFERENCES Tracking(ID)
);

CREATE TABLE Stock(
ProductID INT NOT NULL,
Quantity INT NOT NULL,
FOREIGN KEY (ProductID) REFERENCES Products(ID)
);

CREATE TABLE Payment(
OrderID INT NOT NULL,
CreditCardNumber BIGINT,
FOREIGN KEY (OrderID) REFERENCES Orders(ID)
);

CREATE TABLE Cart (
CustomerID INT NOT NULL,
ProductID INT NOT NULL,
Quantity INT NOT NULL,
FOREIGN KEY (CustomerID) REFERENCES Customers(ID),
FOREIGN KEY (ProductID) REFERENCES Products(ID)
);

INSERT INTO Products (Color, Size, Brand)
VALUES 
    ('Red', 'Large', 'Calvin Klein'),
    ('Red', 'Medium', 'Calvin Klein'),
    ('Red', 'Small', 'Calvin Klein'),
    ('Blue', 'Large', 'Calvin Klein'),
    ('Blue', 'Medium', 'Calvin Klein'),
    ('Blue', 'Small', 'Calvin Klein'),
    ('Green', 'Large', 'Calvin Klein'),
    ('Green', 'Medium', 'Calvin Klein'),
    ('Green', 'Small', 'Calvin Klein'),
    ('Yellow', 'Large', 'Calvin Klein'),
    ('Yellow', 'Medium', 'Calvin Klein'),
    ('Yellow', 'Small', 'Calvin Klein');

