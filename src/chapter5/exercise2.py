num = []
while True:
    try:
        number = input("ENTER NUMBER: ").lower()
        number = int(number)
        num.append(number)
        
    except:
        if number == "done":
           break
        else:
            print("wrong input")

for x in num:
    x = max(num)
print("maximum number is: ", x)
for y in num:
    y = min(num)
print("minimum value is: ", y)
