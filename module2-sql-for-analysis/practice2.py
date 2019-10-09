# Practice (contd.)
# may now run SQL queries on the populated database 
import sqlite3

connection = sqlite3.connect("myTable.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM emp")

# store fetched data in a variable
ans = cursor.fetchall()

# loop to print all data
for i in ans:
    print(i)
