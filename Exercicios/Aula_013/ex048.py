#Calcular a soma de todos os números ímpares múltiplos de 3 de 1 a 500.
soma = 0
for c in range (1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c
print(soma)