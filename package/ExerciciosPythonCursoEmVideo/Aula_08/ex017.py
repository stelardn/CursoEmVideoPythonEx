from math import hypot
cAd = eval(input('Cateto adjacente: '))
cOp = eval(input('Cateto oposto: '))
hip = hypot(cAd,cOp)
print(f'O valor da hipotenusa é {hip}.')