inputName = input("Enter the file path and name : ")
try:
    with open(inputName, 'r') as readFile:
        print("na na boo boo")
        for line in readFile:
            if line.startswith('X-DSPAM-Confidence'):
                print(line, end='')
except:
    print("Invalid file name")