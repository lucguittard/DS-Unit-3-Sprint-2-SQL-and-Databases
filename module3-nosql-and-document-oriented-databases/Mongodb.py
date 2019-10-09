# retrieve current IP; whitelist it at mongodb.com
#curl ipecho.net/plain

# get version for specification on mongodb.com; using terminal..
#python --version 

# install and import package for mongodb access from python
#pip install pymongo
import pymongo

# call driver from mongodb.com
client = pymongo.MongoClient("mongodb://admin:421fhKfvIZI0qDix@cluster0-shard-00-00-pjqtz.mongodb.net:27017,cluster0-shard-00-01-pjqtz.mongodb.net:27017,cluster0-shard-00-02-pjqtz.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
print(db) #to check ouput
print(client.nodes) #to check number of machines(shards) running 

# insert a document
db.test.insert_one({'x':1})

# count how many documents
db.test.count_documents({'x':1})

# insert a document again
db.test.insert_one({'x':1})

# count how many documents there are again - now should be 2
db.test.count_documents({'x':1})

# pull a document matching dictionary condition
db.test.find_one({'x':1})

# cursor for all matching dictionary condition
curs = db.test.find({'x:1'})
print(list(curs)) #to list them out

# define more documents
anthony_doc = {
    'favorite_animal' : ['leafy sea dragon', 'dragon']
}

rudy_doc = {
    'favorite_animal' : 'Koala',
    'favorite_color' : 'Blue'
}

coop_doc = {
    'favorite_animal' : 'Pangolin'
}

# insert each of the specified documents 
db.test.insert_many([anthony_doc, rudy_doc, coop_doc])
print(list(db.test.find())) #to list all created documents

# Make more documents; via looping:
more_docs = []
for i in range(10):
    doc = {'even': i % 2 == 0}
    doc['value'] = i
    more_docs.append(doc)

print(more_docs) #to check output

# insert more_docs via insert_many and check output
db.test.insert_many(more_docs)

print(db.test.find({'even':False}))
print(list(db.test.find({'favorite_animal':'Pangolin'})))

# test the update_one function
db.test.update_one({'value':3},
                   {'$inc': {'value':5}})

print(list(db.test.find()))

# test the update_many function
db.test.update_many({'even': True},
                   {'$inc': {'value':100}})

print(list(db.test.find({'even':True})))

# test the delete_many function
db.test.delete_many({'even':False})
print(list(db.test.find()))

# insert a new document/object
rpg_character = (1, "King Bob", 10, 3, 0, 0, 0)
db.test.insert_one(
    {'rpg_character': rpg_character}) 
    #must be wrapped in a dictionary

# another object
db.test.insert_one({
    'sql_id': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]})
print(list(db.test.find()))
