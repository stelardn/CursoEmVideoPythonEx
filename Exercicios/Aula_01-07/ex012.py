#Leia o preço de um produto e mostre seu novo preço com 5% de desconto
preçoAtual = float(input('Qual o preço atual do produto, em reais? '))
preçoNovo = preçoAtual*0.95
print('5% de desconto! De {} R${:.2f} {}, por {} R${:.2f} {}!'.format('\033[1;30;41m', preçoAtual,'\033[m','\033[1;30;42m',preçoNovo,'\033[m'))
