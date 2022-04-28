#Leia o salário de um funcionário e mostre o seu novo salário, com 15% de aumento
salarioAtual = eval(input('Qual o seu salário atual, em reais? '))
salarioNovo = salarioAtual*1.15
print('Com um aumento de 15%, seu novo salário será R${:.2f}.'.format(salarioNovo))