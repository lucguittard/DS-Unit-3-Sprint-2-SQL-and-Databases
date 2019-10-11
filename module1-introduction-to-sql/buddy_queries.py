# import sqlite
import sqlite3

# establish a connection with the desired database
conn = sqlite3.connect('buddymove_holidayiq2.sqlite3')

# create a cursor -> curs = conn.cursor() -> see loop below

# query for number of rows
query = """SELECT COUNT(*) FROM buddymove_holidayiq2;"""

# query for number of users who reviewed at least 100
# in Nature category also reviewed at least 100 in the Shopping category
query2 = """SELECT COUNT(*) FROM buddymove_holidayiq2 WHERE Nature >= 100 AND Shopping >= 100;"""

# execute the queries; 'define-a-function' route show below

queries = [query, query2]

def executer(list_queries):
    for i in list_queries:
        
        conn = sqlite3.connect('buddymove_holidayiq2.sqlite3')
        
        # make a cursor
        curs = conn.cursor()

        # print results of each query
        print(curs.execute(i).fetchall())

# close up curs after finished querying
# curs.close

# commit updated instance
# conn.commit()
 
executer(queries)
