location = str(input("Enter the job location : ")).lower()
pay = input(" Enter the job pay : ")

try:
    pay = int(pay)
    if location == "kampala":
        if pay > 8000000:
            print("I will take the job")
        else:
            print("No thanks")

    elif location == "mbarara":
        if pay > 4000000:
            print("i will take the job")
        else:
            print("I have better options")

    elif location == "space":
        if pay > 0:
            print("Without doubt , i will take it")
        else:
            print("without a chance, i will still take it.")

    else:
        if pay > 6000000:
            print("sure,I can work with this")
        else:
            print("No thanks, i can find something better")

except:
    print("not a value , enter a number")
