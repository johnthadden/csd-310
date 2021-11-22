from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.jiuf0.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
print(db.students.find())

john2 = {
  “student_id”: “1010",
  "first_name": "john",
  "last_name": "hudden"
}

john2_student_id = students.insert_one(john2).inserted_id

print("-- Insert Statements --")
print("Inserted student record " + john2["first_name"] + " " john2["last_name"] + " into the students collection with document_id " + john2_student_id)

doc = db.collection_name.find_one({“student_id”: “1010”})
 
print(doc[“student_id”])

db.collection_name.remove({"student_id":"1010"})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
print(db.students.find())

input("End of program, input any character to continue...")
