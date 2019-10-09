#pip install psycopg2-binary #(do this before going into python)

#To connect csv data file to ElephantSQL, run the following in python
import psycopg2

#Set from a .csv file to Postgress (# titanic.csv example..)

# convert .csv to .sqlite
# import sqlite
import sqlite3

# call the dataframe
import pandas as pd
dset = pd.read_csv('titanic.csv')

#Populate the database (sqlite)
# make the engine
from sqlalchemy import create_engine
engine = create_engine('sqlite://',echo=False)

# establish a connection with the desired database
conn = sqlite3.connect('titanic.sqlite3') 
# connects the file to the database so queries can be run

# make the sqlite file; note you need to specify the connection defined above
dset.to_sql('titanic', conn)

# then cursor -> used for queries
curs = conn.cursor()

# translate pandas dataframe to sql; run in command line
query = 'SELECT COUNT(*) FROM titanic;'
engine.execute(query).fetchall() 

# commit each query
conn.commit()

# close up each query
curs.close()    


# from sqlite to Postgress(ElephantSQL)
# connect to Elephant via python 
dbname = 'nrwsotro'
user = 'nrwsotro'
password = '60bRSYbWQSq14qksj1Ip-BVpbYSMkGqb'
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)
pg_curs = pg_conn.cursor()

# upload relevant sqlite file 
wget 'https://github.com/lucguittard/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module2-sql-for-analysis/titanic.sqlite3'
mw 'titanic.sqlite3' titanic.sqlite3

# import sqlite3
sl_conn = sqlite3.connect('titanic_db.sqlite3')
sl_curs = sl_conn.cursor()

# test output
sl_curs.execute('SELECT COUNT(*) FROM titanic').fetchall() 

# check the schema
sl_curs.execute('PRAGMA table_info(titanic);').fetchall()

# make a datatable 
titanic_table = """CREATE TABLE titanic(
    index SERIAL PRIMARY KEY, 
    Survived INT, Pclass INT, 
    Name VARCHAR(30), Sex VARCHAR(10), 
    Age DECIMAL, Siblings_Spouses INT,
    Parents_Children INT, Fare DECIMAL, 
    );
    """

pg_curs.execute(titanic_table)

show_tables = """
SELECT * 
FROM pg_catalog.pg_tables 
WHERE schemaname != 'pg_catalog' 
AND schemaname != 'information_schema';
"""

pg_curs.execute(show_tables)
pg_curs.fetchall()

# populate the data to the ElephantSQL instance
for entry in entries:
    insert_entry = """INSERT INTO titanic(
        index, Survived, Pclass, Name, Sex,
        Age, Siblings_Spouses, Parents_Children,
        Far) VALUES""" + str(entry[1:]) + ';'
    pg_curs.execute(insert_entry)

# check output
spg_curs.fetchall()

# save changes
pg_curs.close()
pg_conn.commit()


# check process
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM titanic')
pg_entries = pg_curs.fetchall()

for entry, pg_entry in zip(entries, pg_entries):
    assert entry == pg_entry

