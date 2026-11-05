while(True):
    number = input("Enter a positive integer: ")
    try:
        positive_number=int(number)
        if positive_number>0:
            print(f"Got it: {positive_number}")
            break
        else:
            print("That is not a postive integer")
    except ValueError:
        print("That is not a integer")
        

    


