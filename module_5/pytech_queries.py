docs = db.collection_students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
 print(doc)

doc = db.collection_students.find_one({“student_id”: “1007”})

print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --") 
print(doc[“student_id”])

input("Enf of program, input any key to continue...")
