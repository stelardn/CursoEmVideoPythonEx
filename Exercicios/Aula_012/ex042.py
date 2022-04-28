#Formando um triângulo
a = float(input('Digite o valor da reta a: '))
b = float(input('Digite o valor da reta b: '))
c = float(input('Digite o valor da reta c: '))
if a + b > c and a + c > b and b + c > a:
    print('\033[1;32mAs retas podem formar um triângulo!')
    if a == b == c:
        print('Um triângulo equilátero!')
    elif a == b or a == c or b == c:
        print('Um triângulo isósceles!')
    else:
        print('Um triângulo escaleno!')
else:
    print('\033[1;31mAs retas informadas não podem formar um triângulo...')