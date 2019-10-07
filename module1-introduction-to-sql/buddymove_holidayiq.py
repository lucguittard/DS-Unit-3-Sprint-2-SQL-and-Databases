# import sqlite
import sqlite3

# establish a connection with the desired database
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')


# make queries

# query for number of rows
query = 'SELECT COUNT(*) FROM buddymove_holiday;'

# query for number of users who reviewed at least 100
# in Nature category also reviewed at least 
# 100 in the Shopping category
query2 = 'SELECT COUNT(DISTINCT(Id)) FROM buddymove_holiday WHERE Nature >= 100 AND Shopping >= 100;'

# (Stretch): avg number of reviews per category

# read in the appropiate file
import pandas as pd
dset = pd.read_csv('buddymove_holidayiq.csv')

# make an engine
from sqlalchemy import create_engine
engine = create_engine('sqlite://',echo=False)

# translate pandas dataframe to sql
dset.to_sql('buddymove_holidayiq', con=engine)
engine.execute(query).fetchall() 
engine.execute(query2).fetchall()