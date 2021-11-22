from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.jiuf0.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

print(db.students.find())

result = db.students.update_one({“student_id”: 1007}, {“$set”: {“last_name”: “Hadden II”}})

doc = db.collection_name.find_one({“student_id”: “1007”})
