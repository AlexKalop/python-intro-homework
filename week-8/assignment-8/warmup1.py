
while True:

    input_from_user = input("Enter a number: ")
    try:
        number = float(input_from_user)
        print (f"You entered: {number:.1f}")
        break

    except ValueError:
        print("That's not a valid number. Try again.")
