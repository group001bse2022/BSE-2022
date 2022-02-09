hours = int(input("Enter hours :  "))
rate = float(input("Enter rate :  "))
if hours > 40:
    eh = (hours - 40)
    er = rate * 1.5
    ep = (eh * er)

    pay = (40 * rate) + ep
    print(pay)
else:
    pay = hours * rate
    print(pay)

