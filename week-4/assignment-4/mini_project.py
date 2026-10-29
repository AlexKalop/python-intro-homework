students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

top_scorer = ""
top_grade = 0
for student in students:
    if student["score"] > top_grade:
        top_scorer = (student["name"])
        top_grade = (student["score"])
print(f"Top Scorer: {top_scorer} ({top_grade})")


total = 0
for student in students:
    total += student["score"]
class_average = total / len(students)
print(f"Class average: {class_average}")

subjects = set()
for student in students:
   subjects.add(student["subject"])
print(f"Subjects offered: {subjects}")

high_scorers = []
for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])
print(f"High scorers: {high_scorers}")