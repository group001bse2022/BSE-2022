num = []
while True:
    number = input("Enter a number : ")
    try:
        number = int(number)
        num.append(number)
    except:
        if number == "done":
            break
        else:
            print("invalid input")
addition = 0
for value in num:
    x = len(num)
    addition += value
print("Average", (addition/x))
print("Sum", addition)
