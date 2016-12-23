#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","password","mydb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM Maquina"

# Execute the SQL command
cursor.execute(sql)
# Fetch all the rows in a list of lists.
results = cursor.fetchall()
for row in results:
	fname = row[0]
	lname = row[1]
	age = row[2]
	sex = row[3]
	income = row[4]
	# Now print fetched result
	print "fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
			(fname, lname, age, sex, income )


# disconnect from server
db.close()
