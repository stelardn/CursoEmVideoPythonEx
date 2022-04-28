#Ler seis números inteiros e mostrar a soma daqueles que forem pares
somaPares = 0
for c in range (1,7):
    num = int(input('Insira um número inteiro: '))
    if num % 2 == 0:
        somaPares = somaPares + num
print(f'A soma dos números pares inseridos é {somaPares}.')