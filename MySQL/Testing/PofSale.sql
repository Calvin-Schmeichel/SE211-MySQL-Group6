Create Database myStore;


CREATE TABLE Customers(
ID int Primary key auto_increment,
fname varchar(40) not null,
lname varchar(40),
Phone varchar(15) not null,
email varchar(40)
);

CREATE TABLE PRODUCTS(
ID int Primary key auto_increment,
color varchar(40),
size varchar(40) not null,
Brand varchar (40)
);


CREATE TABLE Orders(
ID int Primary key auto_increment,
CustomerID int not null,
ProductID int not null,
OrderDate DATETIME not null,
OrderStatus varchar (10) not null,
tracking_id varchar(255) not null unique,
foreign key(CustomerID) references Customers(ID),
foreign key(ProductID) references Products(ID)
);

CREATE TABLE STOCK(
ProductId int not null,
Quantity int not null,
foreign key(ProductId) references Products(ID)
);

CREATE TABLE Payment(
OrderID int not null,
CREDITCARD int,
foreign key (OrderID) references Orders(ID)
);

CREATE TABLE Tracking(
ID int Primary key auto_increment,
DeliveryDate DATE not null,
DeliveryAddress varchar(200),
TrackStatus varchar (100)
);

CREATE TABLE CART (
order_id INT NOT NULL,
product_id INT NOT NULL,
quantity INT NOT NULL,
PRIMARY KEY (order_id, product_id),
FOREIGN KEY (order_id) REFERENCES orders(id),
FOREIGN KEY (product_id) REFERENCES products(id)
);