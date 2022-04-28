#Aprovar um empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos irá pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou a compra será negada.
valor = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o seu salário? R$'))
anos = float(input('Em quantos anos deseja pagar a casa? '))
meses = anos * 12
prestação = valor / meses
if prestação > 0.3 * salário:
    print(f'Desculpe, não podemos conceder este empréstimo, pois a prestação de R${prestação:.2f} ',end='')
    print(f'é maior que 30% do seu salário (R${0.3 * salário:.2f}).')
else:
    print(f'Empréstimo aprovado! Sua prestação será de R${prestação}.')