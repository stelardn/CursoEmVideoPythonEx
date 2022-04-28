#Comparar dois números inteiros
try:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número inteiro: '))
    if n1 > n2:
        print('O primeiro valor é maior.')
    elif n2 > n1:
        print('O segundo valor é maior.')
    elif n1 == n2:
        print('Não existe valor maior! Os dois são iguais.')
except:
    print('\033[30;41mValores inválidos foram inseridos. Tente novamente.\033[m')
