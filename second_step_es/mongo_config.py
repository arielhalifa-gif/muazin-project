from pymongo import MongoClient
from uuid import uuid4

client = MongoClient('mongodb://localhost:27017/')


db = client['week-19-db-muazin']
collection = db['podcasts']

def send_to_mongo(stt_file: str):
    data = {
        "id": uuid4,
        "text": stt_file
    }
    result = collection.insert_one(data)