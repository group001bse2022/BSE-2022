c = float(input('enter initial amount of investment:'))
r = float(input('enter yearly rate of interest:'))
n = float(input('enter the number of times the interest is to be compounded:'))
t = float(input('enter number of years until maturation:'))

p = c*(1+r/n)**(t*n)
print(round(p, 2))