def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

names = ["Marco","David","Juan","Alexis","Maria","Tanya" ]
name_check = input("Enter a name to search for: ")
result = linear_search(names, name_check)
if result ==-1:
    print(f'"{name_check}" was not found in the list.')
else:
    print(f'Found "{name_check}" at index {result}.')
