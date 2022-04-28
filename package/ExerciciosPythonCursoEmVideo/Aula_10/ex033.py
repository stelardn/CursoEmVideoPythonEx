#Maior e menor de 3 números
n1 = float(input('Informe o primeiro número: '))
maior = n1
menor = n1
n2 = float(input('Informe o segundo número: '))
if n2 == n1:
    print('Primeiro e segundo número informados são iguais.')
elif n2 > maior:
    maior = n2
else:
    menor = n2
n3 = float(input('Informe o terceiro número: '))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
if n3 == n2 == n1:
    print('Os três números informados são iguais.')
elif n3 == n2:
    print('Segundo e terceiro número iguais.')
    print(f'O maior número informado foi {maior} e o menor foi {menor}.')
elif n3 == n1:
    print('Primeiro e terceiro número iguais.')
    print(f'O maior número informado foi {maior} e o menor foi {menor}.')
else:
    print(f'O maior número informado foi {maior} e o menor foi {menor}.')

