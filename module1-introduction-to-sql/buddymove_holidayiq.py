#DONE IN TERMINAL
# import sqlite
import sqlite3

# calling the dataframe
import pandas as pd
dset = pd.read_csv('buddymove_holidayiq.csv')

#Populate the database (sqlite)
# make the engine
from sqlalchemy import create_engine
engine = create_engine('sqlite://',echo=False)

# establish a connection with the desired database
conn = sqlite3.connect('buddymove_holidayiq.sqlite3') 
# connects the file to the database so queries can be run

# make the sqlite file; note you need to specify the connection defined above
dset.to_sql('buddymove_holidayiq', conn)

# then cursor -> used for queries
curs = conn.cursor()

#DONE USING .py FILE
# make queries (only part of this process that can be run from .py file)

# query for number of rows
query = 'SELECT COUNT(*) FROM buddymove_holiday;'

# query for number of users who reviewed at least 100
# in Nature category also reviewed at least 
# 100 in the Shopping category
query2 = 'SELECT COUNT(DISTINCT(Id)) FROM buddymove_holiday WHERE Nature >= 100 AND Shopping >= 100;'

# (Stretch): avg number of reviews per category

# translate pandas dataframe to sql; run in command line
engine.execute(query).fetchall() 
engine.execute(query2).fetchall()

# close up each query
curs.close

# commit each query
conn.commit()
