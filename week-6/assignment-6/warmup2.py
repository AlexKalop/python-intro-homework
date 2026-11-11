def celsius_to_fahrenheit(c):
    f= (c * 9/5) + 32
    return f

def fahrenheit_to_celsius(f):
    c= (f - 32) * 5/9
    return c


new_temp = celsius_to_fahrenheit(0)
print(f"{new_temp:.1f}ºF")
new_temp = celsius_to_fahrenheit(100)
print (f"{new_temp:.1f}ºF")
new_temp = fahrenheit_to_celsius(72)
print (f"{new_temp:.1f}ºC")



