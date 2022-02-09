hours = input("Enter the hours : ")
rate = input("Enter the rate : ")
try:
    hours = int(hours)
    rate = float(rate)
    if hours > 40:
        eh = (hours - 40)
        er = rate * 1.5
        ep = (eh * er)

        pay = (40 * rate) + ep
        print(pay)
    else:
        pay = hours * rate
        print(pay)
except:
    print("Error, please enter numeric input")


