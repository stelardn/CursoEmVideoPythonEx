#Número primo
num = int(input('Insira um número inteiro e vamos verificar se ele é primo ou não! '))
éPrimo = True
for c in range (2, 11):
    if num % c == 0 and num != c:
        éPrimo = False
if éPrimo == True:
    print(f'Sim, {num} é um número primo.')
else:
    print(f'Não, {num} não é um número primo.')