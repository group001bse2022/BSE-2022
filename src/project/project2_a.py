with open('measles.txt', 'r') as readFile:
    inputName = input('Enter the input file name : ')
    fileName = inputName.lower()
    if fileName == 'measles.txt' or fileName == 'project2_a.py' or fileName == 'project2_b.py':
        exit()
    else:
        inputYear = input('Enter the year : ').lower()
        with open(fileName, 'w') as writeFile:
            for line in readFile:
                if inputYear == 'all' or inputYear == '' or inputYear == line[88] or inputYear == line[88:89] or inputYear == line[88:90]:
                    writeFile.write(line)

        with open(fileName, 'r') as outputFile:
            for link in outputFile:
                print(link, end='')
