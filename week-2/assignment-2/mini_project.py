# Asked the used to give us a temperature in fahrenheit, used float inclase of decimals and made sure to transform string to float.

fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

celsius = (fahrenheit - 32 ) * 5 / 9

#print out the temperature make sure to use :.1f to use one decimal
# ///I had to learn how to enter the degree symbol using shift + option + 8///
print(f"{fahrenheit:.1f}°F is {celsius:.1f}°C.")



