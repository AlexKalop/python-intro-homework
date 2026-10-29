student = { "name": "Alex", "grade": "B", "subject": "CompSci"}

for  key, value in student.items():
    print(f"{key}: {value}")


student["graduated"] = False

for key, value in student.items():
    print(f"{key}: {value}")