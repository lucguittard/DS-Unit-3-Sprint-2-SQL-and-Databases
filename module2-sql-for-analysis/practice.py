# Working with sqlite   
# insert a table 

# import the needed modules
import sqlite3
import pandas as pd 

# connect to a database
connection = sqlite3.connect("myTable.db")

# make a cursor
curs = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE emp (staff_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(30),
gender CHAR(1),
joining DATE);"""

# execute the statement
curs.execute(sql_command)

# SQL command to insert the data in the table
sql_command = """INSERT INTO emp VALUE (23, "Joe", "Walker", "M", "2015-04-11");"""
curs.execute(sql_command)

# another data insertion command 
sql_command = """INSERT INTO emp VALUE (40, "Kam", "Greene", "F", "2004-07-23");"""
curs.execute(sql_command)

# save the changes made to the database file
connection.commit()

# close the connection
connection.close()

# may now run SQL queries on the populated database (continue to part 2)
