# Sort the Result

#Sort the result alphabetically by name: result:


# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)

# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers ORDER BY name"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
# 	print(x)



# ORDER BY DESC


# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#  	print(x)



# Delete Record
# You can delete records from an existing table by using the "DELETE FROM" statement:



# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# sql = "DELETE FROM customers WHERE address = 'Noida'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")



# Prevent SQL Injection


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root@password",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Gurgaon", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")