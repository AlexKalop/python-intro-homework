student = { "name": "Alex", "grade": "B", "subjects": ["CompSci"]}

for  key, value in student.items():
    print(f"{key}: {value}")


student["graduated"] = False

for key, value in student.items():
    print(f"{key}: {value}")