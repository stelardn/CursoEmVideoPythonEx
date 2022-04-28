#Faça um prgrama que leia um número de 0 a 9999 e mostre na tela os dígitos separados
num = int(input('Insira um número de 0 a 9999: '))
num = str(num)
if len(num)<5:
    num = num.rjust(4,'0')
    print('Milhar:', num[-4])
    print('Centena:',num[-3])
    print('Dezena:',num[-2])
    print('Unidade:',num[-1])
else:
    print('Número inválido!')

