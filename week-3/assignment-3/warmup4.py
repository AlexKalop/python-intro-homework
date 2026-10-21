number = int(input("Enter a number: "))
sign = "odd"
is_negative = "Negative"




if number < 0:
    is_negative = " Negative"
elif number == 0:
    is_negative = " Zero."
else:
    is_negative = " Positive."

if number/2 == 0:
    sign = " Even."
else:
    sign = " Odd."

print(f"{number} is {is_negative}")
print(f"{number} is {sign}")
