# Select With a Filter

# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers WHERE name = 'Rahul'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for x in myresult:
# 	print(x)


	# OR

# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers WHERE address = 'Gurgaon'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for x in myresult:
# 	print(x)




# Wildcard Characters
# Use the %  to represent wildcard characters:


# Select records where the address contains the word "way":

# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database= "mydatabase"
# 	)
# mycursor = mydb.cursor()
# sql = "SELECT * FROM customers WHERE address Like '%a%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
# 	print(x)




# Prevent SQL Injection
# Escape query values by using the placholder %s method:


import mysql.connector
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "root@password",
	database = "mydatabase"
	)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Hardoi",)
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
	print(x)