# Delete a Table

# import mysql.connector
# mydb = mysql.connector.connect(
# 	host = "localhost",
# 	user = "root",
# 	password = "root@password",
# 	database = "mydatabase"
# 	)
# mycursor = mydb.cursor()
# sql = "DROP TABLE customers"
# mycursor.execute(sql)




# Drop Only if Exist
# Delete the table "customers" if it exists:



import mysql.connector
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "root@password",
	database = "mydatabase"	
	)
mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
