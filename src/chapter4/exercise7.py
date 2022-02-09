hours = int(input("Enter the number of hours worked : "))
rate = float(input("Enter the hourly working rate : "))

def computepay(hours, rate):
    if hours > 40:
        eh = (hours - 40)
        er = rate * 1.5
        ep = (eh * er)

        pay = (40 * rate) + ep
        print(pay)
    else:
        pay = hours * rate
        print(pay)

computepay(hours, rate)
