"""Converter bases numéricas:
- 1 para binário;
- 2 para octal;
- 3 para hexadecimal."""

number = int(input('Qual o número a ser convertido? '))
base = int(input('''Escolha a base de conversão:
                 1: decimal
                 2: octal
                 3: hexadecimal '''))
if base == 1:
    number = bin(number)
elif base == 2:
    number = oct(number)
elif base == 3:
    number = hex(number)
else:
    print('Número ou base inválida. Tente novamente...')
print(number[2:])
