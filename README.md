# SE211 | Group6 | MySQL GitHub README

### Code Documentation 

**Importing the required library:**  
- The `mysql.connector` library is imported to establish a connection to the MySQL database.
- Establishing a connection to the database: The mysql.connector.connect() method is used to establish a connection to the MySQL database. The host, port, username, password, and database name are provided as parameters.
- **Creating a cursor object:** A cursor object is created using the db.cursor() method to execute SQL queries.
- **Defining the printsql() function:** The printsql() function is defined to iterate through the query results and print them.
- **Dropping the existing database (if exists):** The mycursor.execute() method is used to execute the SQL query DROP DATABASE IF EXISTS myStore;. This query drops the existing database named "myStore" if it exists.
- **Creating a new database:** The mycursor.execute() method is used to execute the SQL query CREATE DATABASE myStore;. This query creates a new database named "myStore".
- **Using the newly created database:** The mycursor.execute() method is used to execute the SQL query USE myStore;. This query sets the newly created "myStore" database as the current database.
- **Creating tables for the store management system:**
  - _The mycursor.execute() method is used to execute a series of SQL queries to create the following tables:_
    - **Customers table:** Stores information about customers, including their ID, first name, last name, phone number, and email address.
    - **Products table:** Stores details about products, such as the ID, color, size, and brand.
    - **Tracking table:** Tracks the delivery status of orders, including the delivery date, delivery address, status, and a unique tracking ID.
    - **Orders table:** Manages the orders placed by customers, including the order ID, customer ID, product ID, order date, status, and tracking ID.
    - **Stock table:** Keeps track of the stock quantity for each product.
    - **Payment table:** Handles payment information for orders, storing the order ID and credit card number.
    - **Cart table:** Tracks the items added to the cart by customers, including the customer ID, product ID, and quantity.
    - **Inserting sample data into the Products table:** The mycursor.execute() method is used to execute an SQL query to insert sample data into the Products table. The INSERT INTO statement is used to specify the columns (Color, Size, Brand) and the values for each row.
    - **Inserting sample data into the Customers table:** The mycursor.execute() method is used to execute an SQL query to insert sample data into the Customers table. The INSERT INTO statement is used to specify the columns (Fname, Lname, Phone, Email) and the values for each row.
    - **Retrieving data from the Customers table:** The mycursor.execute() method is used to execute an SQL query to select all data from the Customers table. The query is then passed to the printsql() function to print the query results.
    - **Retrieving data from the Products table:** The mycursor.execute() method is used to execute an SQL query to select all data from the Products table. The query is then passed to the printsql() function to print the query results. 

### Python Script Overview  

The provided code sets up the necessary database structure for a store management system. It creates the required tables and inserts sample data for testing purposes. The code can serve as a foundation for building a complete store management application. 

Please note that additional code and user interface implementation may be required to utilize the database effectively in a real-world scenario. 

### Code Documentation 

This code is written in Python and utilizes the tkinter library to create a graphical user interface (GUI) for handling T-shirt purchases. The code allows users to enter their personal information, select the desired T-shirt color, size, and quantity, and then generate a mock receipt. 

### Functionality 

The code consists of the following key components: 

**handle_purchase() function:** This function is called when the user clicks the "Purchase" button. It retrieves the user's email, T-shirt color, size, and quantity from the respective input fields. It then generates a mock receipt string using f-strings and prints it to the console. Finally, it clears the email input field for the next entry. 

**Main window creation:** The main window is created using the tk.Tk() method. The title of the window is set to "T-Shirt Purchase" using the title() method. 

**User input fields:** The code creates several input fields for the user to enter their personal information, including email, first name, last name, and phone number. Each input field is created using the tk.Entry() method, and a label is associated with each input field using the tk.Label() method. 

**T-shirt color selection:** The user can choose the desired T-shirt color by selecting one of the available options (Red, Blue, Green, Yellow). Radio buttons are created for each color option using the tk.Radiobutton() method. The selected color is stored in the color_var variable, which is of type tk.StringVar(). 

**T-shirt size selection:** Similar to the color selection, the user can choose the T-shirt size by selecting one of the available options (Large, Medium, Small). Radio buttons are created for each size option using the tk.Radiobutton() method. The selected size is stored in the size_var variable, which is of type tk.StringVar(). 

**Quantity selection:** The user can choose the quantity of T-shirts they want to purchase by selecting one of the available options (1, 5, 10). Radio buttons are created for each quantity option using the tk.Radiobutton() method. The selected quantity is stored in the quantity_var variable, which is of type tk.StringVar(). 

**Purchase button:** The "Purchase" button is created using the tk.Button() method. When clicked, it calls the handle_purchase() function. 

**GUI event loop:** The code enters the GUI event loop using the mainloop() method of the main window. This ensures that the GUI remains responsive and can handle user interactions. 

### Conclusion

The provided code demonstrates the use of tkinter library to create a GUI for handling T-shirt purchases. Users can enter their personal information, select the T-shirt color, size, and quantity, and generate a mock receipt. The code can serve as a basis for building a more comprehensive T-shirt purchasing system with additional features and database integration. 

Please note that further improvements, such as error handling and data validation, can be implemented to enhance the user experience and ensure data integrity.
