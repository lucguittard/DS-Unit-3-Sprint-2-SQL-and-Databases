#MAKE THE SQLITE FILE
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
conn = sqlite3.connect('buddymove_holidayiq2.sqlite3') 
# connects the file to the database so queries can be run

# make the sqlite file; note you need to specify the connection defined above
dset.to_sql('buddymove_holidayiq2', conn)

# then cursor -> used for queries
#curs = conn.cursor()

# close query
#curs.close()

# commit each query
#conn.commit()
 