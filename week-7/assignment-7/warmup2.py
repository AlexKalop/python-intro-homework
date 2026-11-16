import csv

with open('../data/students.csv','r') as file:
    reader = csv.DictReader(file)

    next(reader)
    for row in reader:
        print(f"{row['name']}: {row['score']}")

