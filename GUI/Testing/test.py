import mysql.connector


db = mysql.connector.connect(
    host="127.0.0.1",
    port="3307",
    user="se211",
    passwd="se211",
    database="testdatabase"
)

mycursor = db. cursor()

#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
mycursor.execute("DESCRIBE Person")

for x in mycursor:
    print(x)