# Update Table
# You can update existing records in a table by using the "UPDATE" statement:
# Overwrite the address column from "Valley 345" to "Canyon 123":



# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# sql = "UPDATE customers SET address = 'Valley 145' WHERE address = 'Gurgaon' "
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")


# Creating a Table


# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

 
# Select from table


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



# Prevent SQL Injection


import mysql.connector
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "root@password",
	database = "mydatabase"
	)
mycursor = mydb.cursor()
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Pune 135", "Delhi")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")