
# Join Two or More Tables
# You can combine rows from two or more tables, based on a related column between them, by using a JOIN statement.

# Consider you have a "users" table and a "products" table:


# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
# 	print(x)

# mycursor.execute("SELECT * FROM users")
# myresult = mycursor.fetchall()
# for x in myresult:
# 	print(x)

# sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
# val = [
# 	('John', '154'),
# 	('Peter', '154'),
# 	('Amy', '155'),
# 	('Hannah', ''),
# 	('Michael', '')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "Data Successfully Inserted.")


# Creating Second Table

# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE products(id INT(11), name VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
# 	print(x)

# sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
# val = [
# 	('154', 'Chocolate Heaven'),
#  	('155', 'Tasty Lemons'),
# 	('156', 'Vanilla Dreams')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "Data Inserted Successfully.")

# mycursor.execute("SELECT * FROM products")
# for x in mycursor:
# 	print(x)




# Joining Two Tables
#Join users and products to see the name of the users favorite product:



import mysql.connector
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "root@password",
	database = "mydatabase"
	)
mycursor = mydb.cursor()
# sql = "SELECT \
# 	users.name AS user, \
# 	products.name AS favourite \
# 	FROM users \
# 	INNER JOIN products ON users.fav = products.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
# 	print(x)

# Note: We can use JOIN instead of INNER JOIN. They will both give you the same result.


 # LEFT JOIN

# sql = "SELECT \
#  	users.name AS user, \
#  	products.name as favourite \
#  	FROM users \
#  	LEFT JOIN products ON users.fav = products.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
# 	print(x)


# RIGHT JOIN

sql = "SELECT \
	users.name AS user, \
	products.name AS favourite \
	FROM users \
	RIGHT JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
	print(x)
