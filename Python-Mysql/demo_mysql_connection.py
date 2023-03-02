  # Create Connection


# import mysql.connector

# mydb = mysql.connector.connect(
# 	host="localhost",
# 	user="root",
# 	password="root@password"
# 	)
# print(mydb)


# Creating a database

# import mysql.connector

# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password"
# 	)
# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")



#Check if Database Exists


# import mysql.connector

# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	)

# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
# 	print(x)



#Try connecting to the database "mydatabase":

# import mysql.connector

# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)



# Creating a Table
#Create a table named "customers":

# import mysql.connector

# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")



#Return a list of your system's databases:


# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
# for x  in mycursor:
# 	print(x)



# Create primary key when creating the table:

# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")



# Create primary key on an existing table:
# If the table already exists, use the ALTER TABLE keyword:


# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)

# mycusror = mydb.cursor()
# mycusror.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")




# Insert Into Table
# To fill a table in MySQL, use the "INSERT INTO" statement.


# import mysql.connector
# mydb = mysql.connector.connect(
# 	host= "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")




# Insert Multiple Rows
# To insert multiple rows into a table, use the executemany() method.
# The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:



# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
# 	('Ajay', 'Noida'),
# 	('Vijay', 'Delhi'),
# 	('Rahul', 'Gurgaon'),
# 	('Vineet', 'Dehradun'),
# 	('Vinay', 'Hardoi'),
# 	('Vivek', 'Noida'),
# 	('Susan', 'One way 98'),
# 	('Richard', 'Sky st 331'),
# 	('Vicky', 'Yellow Garden'),
# 	('William', 'Central st 954'),
#     ('Chuck', 'Main Road 989'),
#     ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)
# mydb.commit()

# print(mycursor.rowcount, "Data Successfully Inserted.")



# Get Inserted ID
# Insert one row, and return the ID:


# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)
# mydb.commit()
# print("1 record inserted, ID:", mycursor.lastrowid)



# Select From a Table
# To select from a table in MySQL, use the "SELECT" statement:


# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
# 	print(x)




# Selecting Columns
# Select only the name and address columns:


# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)

# mycursor = mydb.cursor()
# mycursor.execute("SELECT name, address FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
# 	print(x)



# Using the fetchone() Method
# The fetchone() method will return the first row of the result:



import mysql.connector
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "root@password",
	database = "mydatabase"
	)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)