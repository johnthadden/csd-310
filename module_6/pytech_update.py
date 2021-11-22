from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.jiuf0.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

db.students.find()
