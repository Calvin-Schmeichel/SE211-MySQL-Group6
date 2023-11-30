import mysql.connector
#import gui


db = mysql.connector.connect(
    host="127.0.0.1",
    port="3307",
    user="se211",
    passwd="se211",
    database="testdatabase"
)

mycursor = db. cursor()

def printsql():
    for x in mycursor:
        print(x)



mycursor.execute("DROP DATABASE IF EXISTS myStore;")
mycursor.execute("CREATE DATABASE myStore;")
mycursor.execute("USE myStore;")

mycursor.execute("CREATE TABLE Customers(ID INT PRIMARY KEY AUTO_INCREMENT,Fname VARCHAR(40) NOT NULL,Lname VARCHAR(40),Phone VARCHAR(15) NOT NULL,Email VARCHAR(40));")
mycursor.execute("CREATE TABLE Products(ID INT PRIMARY KEY AUTO_INCREMENT,Color VARCHAR(40),Size VARCHAR(40) NOT NULL,Brand VARCHAR(40));")
mycursor.execute("CREATE TABLE Tracking(ID INT PRIMARY KEY AUTO_INCREMENT,DeliveryDate DATE NOT NULL,DeliveryAddress VARCHAR(200),Status VARCHAR(100),TrackingID VARCHAR(255) NOT NULL UNIQUE);")
mycursor.execute("CREATE TABLE Orders(ID INT PRIMARY KEY AUTO_INCREMENT,CustomerID INT NOT NULL,ProductID INT NOT NULL,Date DATETIME NOT NULL,Status VARCHAR(10) NOT NULL,TrackingID INT,FOREIGN KEY (CustomerID) REFERENCES Customers(ID),FOREIGN KEY (ProductID) REFERENCES Products(ID),FOREIGN KEY (TrackingID) REFERENCES Tracking(ID));")
mycursor.execute("CREATE TABLE Stock(ProductID INT NOT NULL,Quantity INT NOT NULL,FOREIGN KEY (ProductID) REFERENCES Products(ID));")
mycursor.execute("CREATE TABLE Payment(OrderID INT NOT NULL,CreditCardNumber BIGINT,FOREIGN KEY (OrderID) REFERENCES Orders(ID));")
mycursor.execute("CREATE TABLE Cart (CustomerID INT NOT NULL,ProductID INT NOT NULL,Quantity INT NOT NULL,FOREIGN KEY (CustomerID) REFERENCES Customers(ID),FOREIGN KEY (ProductID) REFERENCES Products(ID));")

mycursor.execute("INSERT INTO Products (Color, Size, Brand)VALUES ('Red', 'Large', 'Calvin Klein'),('Red', 'Medium', 'Calvin Klein'),('Red', 'Small', 'Calvin Klein'),('Blue', 'Large', 'Calvin Klein'),('Blue', 'Medium', 'Calvin Klein'),('Blue', 'Small', 'Calvin Klein'),('Green', 'Large', 'Calvin Klein'),('Green', 'Medium', 'Calvin Klein'),('Green', 'Small', 'Calvin Klein'),('Yellow', 'Large', 'Calvin Klein'),('Yellow', 'Medium', 'Calvin Klein'),('Yellow', 'Small', 'Calvin Klein');")




mycursor.execute("INSERT INTO Customers (Fname, Lname, Phone, Email) VALUES ('John', 'Doe', '123-456-7890', 'john.doe@example.com');")
mycursor.execute("select* from Customers;")

printsql()

mycursor.execute("select* from Products;")

#printsql()

