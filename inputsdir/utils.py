from pymongo import MongoClient

from eventsinput.settings import CONNECTION_STRING_MONGO_SECRET


connectionstr = CONNECTION_STRING_MONGO_SECRET 

print(connectionstr)
# raise ValueError(f'value: {MongoClient(connectionstr)}')
try:
    client = MongoClient(connectionstr)
except:
    print('Connection error')
db = client['events']
# print(db.collection_names())
print(db.list_collection_names())
events_collection = db['eventinfo']