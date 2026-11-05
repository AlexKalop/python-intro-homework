numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

def bubble_sort(data):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
    return data

def find_smallest(data):
    smallest = data[0]
    for i in range(len(data)):
        if data [i] <smallest:
            smallest= data[i]
    return smallest

def find_largest(data):
    largest = data[0]
    for i in range(len(data)):
        if data [i] >largest:
            largest= data[i]
    return largest

while (True):
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    option = int(input("Choose an option (1-5): "))

    if option == 1:
        print (f"The minimum is : {find_smallest(numbers)}")
    elif option == 2:
        print(f"The maximum is : {find_largest(numbers)}")
    elif option == 3:
        num_check= int(input("Enter a number to check: "))
        result = linear_search (numbers,num_check)
        if result ==-1:
            print(f'"{num_check}" was not found in the list.')
        else:
            print(f'Found "{num_check}" at index {result}.')
    elif option ==4:
        numbers_copy= numbers[:]
        print(bubble_sort(numbers_copy))
    elif option == 5:
        print ("Goodbye")
        break