john = {
      "student_id": "1007",
      "first_name": "John",
      "last_name": "Hadden"
  }

tim = {
      "student_id": "1008",
      "first_name": "Tim",
      "last_name": "Jones"
  }

mary = {
      "student_id": "1009",
      "first_name": "Mary",
      "last_name": "Elizabeth"
  }

john_student_id = students.insert_one(john).inserted_id
tim_student_id = students.insert_one(tim).inserted_id
mary_student_id = students.insert_one(mary).inserted_id

print("-- Insert Statements --")
print("Inserted student record " + john["first_name"] + " " john["last_name"] + " into the students collection with document_id " + john_student_id)
print("Inserted student record " + tim["first_name"] + " " tim["last_name"] + " into the students collection with document_id " + tim_student_id)
print("Inserted student record " + mary["first_name"] + " " mary["last_name"] + " into the students collection with document_id " + mary_student_id)

input("End of program, input any key to exit...")
