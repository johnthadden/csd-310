#John Hadden
# 11/17/2021
#Assignment 5.2
#Linking empty collection from MongoDB Atlas to python file
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.jiuf0.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

print("-- Pytech Collection List --")
print(db.list_collection_names())

input("End of Program. Input any key to exit...")
