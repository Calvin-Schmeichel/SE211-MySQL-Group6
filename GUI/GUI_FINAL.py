import mysql.connector
import tkinter as tk
from tkinter import simpledialog, messagebox
import datetime
import random

db = mysql.connector.connect(
    host="127.0.0.1",
    port="3307",
    user="se211",
    passwd="se211",
    database="testdatabase"
    )

#mycursor = db.cursor()
mycursor = db.cursor(buffered=True)


def printsql():
    for x in mycursor:
        print(x)    


def GenerateDB():



    mycursor.execute("DROP DATABASE IF EXISTS myStore;")
    mycursor.execute("CREATE DATABASE myStore;")
    mycursor.execute("USE myStore;")

    mycursor.execute("CREATE TABLE Customers(ID INT PRIMARY KEY AUTO_INCREMENT,Fname VARCHAR(40) NOT NULL,Lname VARCHAR(40),Phone VARCHAR(15) NOT NULL,Email VARCHAR(40));")
    mycursor.execute("CREATE TABLE Products(ID INT PRIMARY KEY AUTO_INCREMENT,Color VARCHAR(40),Size VARCHAR(40) NOT NULL,Brand VARCHAR(40));")
    mycursor.execute("CREATE TABLE Tracking(ID INT PRIMARY KEY AUTO_INCREMENT,DeliveryDate DATE NOT NULL,DeliveryAddress VARCHAR(200),Status VARCHAR(100),TrackingID VARCHAR(255) NOT NULL UNIQUE);")
    mycursor.execute("CREATE TABLE Orders(ID INT PRIMARY KEY AUTO_INCREMENT,CustomerID INT NOT NULL,ProductID INT NOT NULL,Date DATETIME NOT NULL,Status VARCHAR(10) NOT NULL,TrackingID INT,FOREIGN KEY (CustomerID) REFERENCES Customers(ID),FOREIGN KEY (ProductID) REFERENCES Products(ID),FOREIGN KEY (TrackingID) REFERENCES Tracking(ID));")
    mycursor.execute("CREATE TABLE Stock(ProductID INT NOT NULL,Quantity INT NOT NULL,FOREIGN KEY (ProductID) REFERENCES Products(ID));")
    mycursor.execute("CREATE TABLE Payment(OrderID INT NOT NULL,CreditCardNumber BIGINT,FOREIGN KEY (OrderID) REFERENCES Orders(ID));")
    mycursor.execute("CREATE TABLE Cart (CustomerID INT NOT NULL,ProductID INT NOT NULL,Quantity INT NOT NULL,Datetime VARCHAR(50),FOREIGN KEY (CustomerID) REFERENCES Customers(ID),FOREIGN KEY (ProductID) REFERENCES Products(ID));")

    mycursor.execute("INSERT INTO Products (Color, Size, Brand)VALUES ('Red', 'Large', 'Calvin Klein'),('Red', 'Medium', 'Calvin Klein'),('Red', 'Small', 'Calvin Klein'),('Blue', 'Large', 'Calvin Klein'),('Blue', 'Medium', 'Calvin Klein'),('Blue', 'Small', 'Calvin Klein'),('Green', 'Large', 'Calvin Klein'),('Green', 'Medium', 'Calvin Klein'),('Green', 'Small', 'Calvin Klein'),('Yellow', 'Large', 'Calvin Klein'),('Yellow', 'Medium', 'Calvin Klein'),('Yellow', 'Small', 'Calvin Klein');")
    mycursor.execute("INSERT INTO Stock (ProductID, Quantity) VALUES (1, 100),(2, 100),(3, 100),(4, 100),(5, 100),(6, 100),(7, 100),(8, 100),(9, 100),(10, 100),(11, 100),(12, 100);")

    mycursor.execute("INSERT INTO Customers (Fname, Lname, Phone, Email) VALUES ('John', 'Doe', '123-456-7890', 'john.doee@example.com');")
    mycursor.execute("INSERT INTO Customers (Fname, Lname, Phone, Email) VALUES ('John', 'Doe', '123-456-7890', 'john.doe@example.com');")
    mycursor.execute("select* from Customers;")

    print("Database Generated")


# Function to handle the purchase and generate receipt
def handle_purchase():
       
    #Generate Customer Entry
    print("Generate Customer Entry")
    mycursor.execute(f"INSERT INTO Customers (Fname, Lname, Phone, Email) VALUES ('{user_FirstName.get()}', '{user_LastName.get()}', '{user_Phone.get()}', '{user_email.get()}');")
    mycursor.execute("select* from Customers;")
    printsql()
        #Customer Keys
    mycursor.execute(f"SELECT ID FROM Customers WHERE Email = '{user_email.get()}';")
    CustomerID = ((mycursor.fetchone())[0])

    #Generate Tracking Entry
        #Date
    date = (datetime.date.today() + datetime.timedelta(days=7))
    print("Generate Tracking Entry")
    mycursor.execute(f"INSERT INTO Tracking (DeliveryDate, DeliveryAddress, Status, TrackingID) VALUES ('{date}', '{user_Address.get()}', 'In Transit', '{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))}');")
    mycursor.execute("select* from Tracking;")
    printsql()

    #Generate Order Entry
    print("Generate Order Entry")
        #Product Keys
    mycursor.execute(f"SELECT ID FROM Products WHERE Color = '{color_var.get()}' AND Size = '{size_var.get()}';")
    ProductID = ((mycursor.fetchone())[0])
    print(ProductID)
        #Tracking Keys
    mycursor.execute(f"SELECT ID FROM Tracking WHERE DeliveryAddress = '{user_Address.get()}'")
    TrackingID = ((mycursor.fetchone())[0])
    mycursor.execute(f"INSERT INTO Orders (CustomerID, ProductID, Date, Status, TrackingID) VALUES ({CustomerID}, {ProductID}, '{date}', 'Processing', {TrackingID});")
    mycursor.execute("select* from Orders;")
    printsql()

    #Generate Cart Entry
    print("Generate Cart Entry")
    Ordertime = datetime.date.today()
    mycursor.execute(f"INSERT INTO Cart (CustomerID, ProductID, Quantity, Datetime) VALUES ({CustomerID}, {ProductID}, {quantity_var.get()}, '{Ordertime}');")
    mycursor.execute("select* from Cart;")
    printsql()

    #Generate Payment Entry
    print("Generate Payment Entry")
        #Order Keys
    mycursor.execute(f"SELECT ID FROM Orders WHERE CustomerID = '{CustomerID}'")
    OrderID = ((mycursor.fetchone())[0])
    mycursor.execute(f"INSERT INTO Payment (OrderID, CreditCardNumber) VALUES ({OrderID}, {user_CreditCard.get()});")
    mycursor.execute("select* from Payment;")
    printsql()



    make_receipt()

    
    

def make_receipt():

    print("===========================================================================")
    print("Making Receipt")
    print("===========================================================================")
    print("Thank you for shopping with us! Here is your Receipt!")
    print(f"{user_FirstName.get()} {user_LastName.get()} bought {quantity_var.get()} {size_var.get()} {color_var.get()} T-Shirt(s) today ({datetime.date.today()})")
    print(f"This purchase was made with {user_CreditCard.get()} and plans to arrive at {user_Address.get()} on {str((datetime.date.today() + datetime.timedelta(days=7)))}")



    exit()

GenerateDB()

# Create the main window
root = tk.Tk()
root.title("T-Shirt Purchase")

# Email input
tk.Label(root, text="Enter your email:").pack()
user_email = tk.Entry(root)
user_email.pack()

# First Name Input
tk.Label(root, text="Enter your First Name:").pack()
user_FirstName = tk.Entry(root)
user_FirstName.pack()

# Last Name Input
tk.Label(root, text="Enter your Last Name:").pack()
user_LastName = tk.Entry(root)
user_LastName.pack()

# Phone Input
tk.Label(root, text="Enter your Phone Number:").pack()
user_Phone = tk.Entry(root)
user_Phone.pack()

# Address Input
tk.Label(root, text="Enter your Address:").pack()
user_Address = tk.Entry(root)
user_Address.pack()

# Credit Card Input

tk.Label(root, text="Enter your Credit Card:").pack()
user_CreditCard = tk.Entry(root)
user_CreditCard.pack()

# T-shirt color selection
color_var = tk.StringVar()
color_var.set("Red")
tk.Label(root, text="Choose T-shirt color:").pack()
for color in ["Red", "Blue", "Green", "Yellow"]:
    tk.Radiobutton(root, text=color, variable=color_var, value=color).pack()

# T-shirt size selection
size_var = tk.StringVar()
size_var.set("Large")
tk.Label(root, text="Choose T-shirt size:").pack()
for size in ["Large", "Medium", "Small"]:
    tk.Radiobutton(root, text=size, variable=size_var, value=size).pack()

# Quantity selection
quantity_var = tk.StringVar()
quantity_var.set("1")
tk.Label(root, text="Choose quantity:").pack()
for quantity in ["1", "5", "10"]:
    tk.Radiobutton(root, text=quantity, variable=quantity_var, value=quantity).pack()

# Submit button
submit_button = tk.Button(root, text="Purchase", command=handle_purchase)
submit_button.pack()

# Start the GUI event loop
root.mainloop()