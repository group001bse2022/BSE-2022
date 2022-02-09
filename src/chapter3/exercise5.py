# n = input("number of people: ")
# try:
#     n = int(n)
#     if 1 <= n <= 50:
#         print("The price is $4000")
#     elif 51 <= n <= 100:
#         print("The price is $10000")
#     elif 101 <= n <= 200:
#         print("The price is $15000")
#     elif n > 200:
#         print("the price is $20000")
#     else:
#         print("Enter a counting number")
# except:
#     print("Input figures")


guests = (input("Enter the no:"))
try:
    guests = int(guests)
    if guests <= 50:
        print("Price: $4000")
    elif guests <= 100:
        print("Price: $10000")
    elif guests <= 200:
        print("Price: $15000")
    else:
        if guests > 200:
            print("Price: $20000")
except:
    print("Error, pliz insert an interger")


