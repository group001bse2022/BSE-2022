a = 'X-DSPAM-Confidence: 0.8475'
b = a[20:26]
c = float(b)
print(a.find("0.8475"))
print(c)