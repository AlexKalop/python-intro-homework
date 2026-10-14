# Error : python3 warmup4.py 
    #How old are you?4
    #Traceback (most recent call last):
        # File "/Users/alexisgarciatafoya/Downloads/CTD-repos/python-intro-homework/week-2/assignment-2/warmup4.py", line 3, in <module>
        #  next_year = age +1
        #             ~~~~^~
    #TypeError: can only concatenate str (not "int") to str

# What caused it : Input uses string and python cant add a string to a integer. 

#How I fixed it I included int in from of the input so it transforms the string to an integer

age = int(input ("How old are you?"))

next_year = age +1
print(f"Next Year you will be {next_year}")