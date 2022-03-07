InputName = input("Enter the File name: ")
count = 0
total = 0
with open(InputName, 'r') as mainFile:
    for line in mainFile:
        if line.startswith('X-DSPAM-Confidence'):
            count = count + 1
            x = float(line[20:])
            total = total + x
average = total/count
print("average :", average)