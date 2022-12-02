## database opeterion DB password mongo atlas:  euQ7nDEBuGhdhdJ  user: admin
import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/afib_db")
DB = client["afib_db"]

def InitDB():
    print("db initialization")
    col = DB['test_colection']
    col.insert_one({"name": "test_colection"})
