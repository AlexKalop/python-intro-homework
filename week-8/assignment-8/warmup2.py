try:
    numerator_from_user = float(input("Enter the numerator: "))
    denominator_from_user = float(input("Enter the denominator: "))
    answer = numerator_from_user/denominator_from_user
    print (f"{numerator_from_user} ÷ {denominator_from_user} = {answer} ")
except ZeroDivisionError:
    print("Can't divide by zero - please try a non-zero denominator.")
