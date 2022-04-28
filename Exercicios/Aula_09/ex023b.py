import math
num = int(input('Insira um número: '))
print('Unidade:',num // 1 % 10)
print('Dezena:',num // 10 % 10)
print('Centena:',num // 100 % 10)
print('Milhar: ',num // 1000 % 10)