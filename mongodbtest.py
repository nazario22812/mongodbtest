import collections
from typing import Collection
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://yto4ka:nazikking@cluster0.s2mmxuy.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test-name"]
collection = db["test-collection"]

name = input("> ")

user = {
    "_id": 1,
    "name": name 
}
if name == "find":
    fin = collection.find({"_id": 1})
    for f in fin:
        print(f)
else:
    if collection.count_documents({"_id": 1}) == 0:
        collection.insert_one(user)
    else:
        print("ошибочка")


collection.update_one({
    "_id": 1    
},
{
    "$set": {"name": "bobr"}
})