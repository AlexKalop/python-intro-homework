numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

def bubble_sort(numbers):
    sorted_numbers = list(numbers)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(sorted_numbers) - 1):
            if sorted_numbers[i] > sorted_numbers[i + 1]:
                sorted_numbers[i], sorted_numbers[i + 1] = sorted_numbers[i + 1], sorted_numbers[i]
                swapped = True
    return sorted_numbers

def find_min(numbers):
    smallest = numbers[0]
    for i in range(len(numbers)):
        if numbers [i] <smallest:
            smallest= numbers[i]
    return smallest

def find_max(numbers):
    largest = numbers[0]
    for i in range(len(numbers)):
        if numbers [i] >largest:
            largest= numbers[i]
    return largest

def show_menu():
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    option = input("Choose an option (1-5): ")
    return option
    
def main():
    while True:
        answer = show_menu()
        if answer == "1":
            print (f"The minimum is : {find_min(numbers)}")
        elif answer == "2":
            print(f"The maximum is : {find_max(numbers)}")
        elif answer == "3":
            num_check= int(input("Enter a number to check: "))
            result = search (numbers,num_check)
            if result ==-1:
                print(f'"{num_check}" was not found.')
            else:
                print(f'Found "{num_check}" at index {result}.')
        elif answer == "4":
            numbers_copy = bubble_sort(numbers)
            print(numbers_copy)
        elif answer == "5":
            print ("Goodbye!")
            break
        else:
            print("Please enter a number from 1-5.")

main()

