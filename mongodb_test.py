from pymongo import MongoClient



# connection string
client = MongoClient("mongodb://localhost:27017")
database = client['own_db']

coll = database['test_col']

# insert - adatlétrehozás
my_dict = {"kulcs": "érték"}

# coll.insert_one(my_dict)

my_dict = [{"kulcs": "érték"}, {"kulcs": "érték"}, {"kulcs": "érték"}, {"kulcs": "érték"},{"kulcs": "érték"}]
# coll.insert_many(my_dict)
# delete - törlünk adatot

query = {"kulcs": "érték"}

# coll.delete_one(query)
# coll.delete_many(query)

# update - módosítunk adatot

query = {"color": "black"}

coll.update_one(query, {"$set": {"kulcs": "valami"}}, upsert=True)
# coll.update_many(query, {"$set": {"kulcs": "valami"}})

# find - selectálunk adatot

query = {"color": "black", "kulcs": "valami"}

data = coll.find(query)

for item in data:
    print(item)