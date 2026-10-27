day_week = input("What day is it? ").lower()
time_day = input("What time of day? ").lower()



if day_week == "tuesday" and time_day == "morning":
    print ("Morning Python class - great time to focus! " )
elif day_week == "tuesday" and time_day == "afternoon":
    print ("Afternoon, Time to double check our weeks work! ")
elif day_week == "tuesday" and time_day == "evening":
    print("The Evening is the deadline to submit our assignments - let's end strong!")
elif day_week == "saturday" and time_day == "morning":
    print("Saturday morning is a great yime to get some excercise!")
elif day_week == "saturday" and time_day == "afternoon":
    print("Saturday afternoons are great time to do events! ")
elif day_week == "saturday" and time_day == "evening":
    print("Perfect time for watching a movie! ")
elif day_week == "friday" and time_day == "morning":
    print("It's Friday we're almost at the weekend!")
elif day_week == "friday" and time_day == "afternoon":
    print(" Hey! It's time to get ready for our Python Class with Eduardo!")
elif day_week == "friday" and time_day == "evening":
    print("The Weekend begins!")
else:
    print("Sorry, I don't recognize that day or time. Try: Monday, Tuesday, Wednesday or Morning, Evening, Afternoon...")
