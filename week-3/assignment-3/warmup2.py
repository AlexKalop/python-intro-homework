age = int(input("What is your age? "))
category = "Child"


if age >=65:
    category = "Senior"
elif age >=18:
    category = "Adult"
elif age >=13:
    category = "Teen"
else:
    category = "Child"

print (f" You are a {category}")
