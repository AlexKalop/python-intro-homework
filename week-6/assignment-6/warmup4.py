def is_valid_score(score):
    if score >= 0 and score <= 100:
        return True
    else:
        return False



user_score = int(input("Enter a score: "))
check = is_valid_score(user_score)

if check:
    print("Valid score.")
else:
    print ("Invalid score — must be between 0 and 100.")