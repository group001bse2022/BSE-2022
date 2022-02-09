age = input("Enter your age : ")
try:
    age = int(age)
    if age >= 18:
        print("You can vote")
    elif 0 < age <= 17:
        print("You are still young")

    else:
        print("you are a time traveller")
except:
    print("Error, please enter valid datatype(integer)")
