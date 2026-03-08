from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')


db = client['week-19-db-muazin']
collection = db['podcasts']
