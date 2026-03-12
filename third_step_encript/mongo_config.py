from pymongo import MongoClient
from uuid import uuid4

client = MongoClient('mongodb://localhost:27017/')


db = client['week-19-db-muazin']
collection = db['podcasts']

def get_from_mongo():
    result = collection.find({}, {'_id': 0, })
    for value in result:
        yield value