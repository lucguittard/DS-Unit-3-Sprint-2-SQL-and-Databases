# Import necessary packages
import sqlite3 

# Establish a connection to specified sqlite file and make a cursor
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Query: What are the ten most expensive items (per unit price) in the database?
query1 = """SELECT UnitPrice, ProductName FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;"""

# Query: What is the average age of an employee at the time of their hiring?
query2 = """SELECT AVG(HireDate - BirthDate) AS Average_emp_age_when_hired
FROM Employee;"""

# (Stretch) How does the average age of employees at hire vary by city?
query3 = """SELECT City, AVG(HireDate - BirthDate) AS Average_emp_age_when_hired
FROM Employee
GROUP BY City"""

# Query: What are the ten most expensive items (per unit price) 
# in the database *and* their suppliers?
query4 = """SELECT UnitPrice, ProductName, CompanyName
FROM Product
JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;"""

# Query: What is the largest category (by number of unique products in it)?
query5 = """SELECT CategoryId, COUNT(DISTINCT Product.Id) AS Num_products
FROM Category
Join Product ON Category.Id = Product.CategoryId
GROUP BY CategoryId 
ORDER BY Num_products DESC
LIMIT 1;"""

# (Stretch) - Which employee is assigned the most territories?
query6 = """SELECT Employee.LastName, Employee.FirstName, 
Employee.Id AS Employee_ID, COUNT(Territory.Id) AS Num_territories
FROM Territory
JOIN EmployeeTerritory ON Territory.Id = EmployeeTerritory.TerritoryId
JOIN Employee ON EmployeeTerritory.EmployeeId = Employee.Id
GROUP BY Employee.Id
ORDER BY Num_territories DESC
LIMIT 1;""" 
# Only the King merits 10.

queries = [query1, query2, query3, query4, query5, query6]

def executer(list_queries):
    for i in list_queries:
        
        conn = sqlite3.connect('northwind_small.sqlite3')
        
        # make a cursor
        curs = conn.cursor()

        # print results of each query
        print(curs.execute(i).fetchall())

executer(queries)