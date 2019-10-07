# import sqlite
import sqlite3

# establish a connection with the desired database
conn = sqlite3.connect('rpg_db.sqlite3')
conn  # (optional) test the output

# create a cursor -> curs = conn.cursor() -> see loop below

# query for the total number of characters
query = 'SELECT COUNT(DISTINCT character_id) FROM charactercreator_character;'

# queries for the number of characters per subclass
query2a = 'SELECT COUNT(DISTINCT name) FROM charactercreator_character INNER JOIN charactercreator_necromancer ON character_id = mage_ptr_id'
query2b = 'SELECT COUNT(DISTINCT name) FROM charactercreator_character INNER JOIN charactercreator_mage ON character_id = character_ptr_id'
query2c = 'SELECT COUNT(DISTINCT name) FROM charactercreator_character INNER JOIN charactercreator_cleric ON character_id = character_ptr_id'
query2d = 'SELECT COUNT(DISTINCT name) FROM charactercreator_character INNER JOIN charactercreator_fighter ON character_id = character_ptr_id'
query2e = 'SELECT COUNT(DISTINCT name) FROM charactercreator_character INNER JOIN charactercreator_theif ON character_id = character_ptr_id'

# query for the total number of items
query3 = 'SELECT COUNT(item_id) FROM charactercreator_character_inventory;'

# query for the total number of weapons
query4 = 'SELECT COUNT(*) FROM armory_item INNER JOIN armory_weapon ON item_id = item_ptr_id;'

# query for the number of items held by each character
query5 = 'SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory GROUP BY character_id LIMIT 20'

# query for the number of weapons held by each character
query6 = 'SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory INNER JOIN  armory_weapon ON item_id = item_ptr_id GROUP BY character_id LIMIT 20;'

# query for the average number of items held by characters
query7 = 'SELECT AVG(count) FROM(SELECT COUNT(item_id) AS count FROM charactercreator_character_inventory GROUP BY character_id);'

# query for the average number of weapons held by characters
query8 = 'SELECT AVG(count) FROM(SELECT COUNT(item_id) AS count FROM charactercreator_character_inventory INNER JOIN  armory_weapon ON item_id = item_ptr_id GROUP BY character_id);'


# execute the queries; 'define-a-function' route show below

queries = [query, query2a, query2b,
    query2c, query2d, query2e, query3, 
    query4, query5, query6, query7, query8
    ]

def executer(list_queries):
    for i in list_queries:
        
        conn = sqlite3.connect('rpg_db.sqlite3')
        
        # make a cursor
        curs = conn.cursor()

        # print results of each query
        print(curs.execute(i))
        print(curs.execute(i).fetchall())

        # close up each query
        curs.close

        # commit each query
        conn.commit()
