"""Receba a qauntidade de km rodados por um carro alugado e quantidade de dias de aluguel. Calcule o preço a pagar,
sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado."""
km = eval(input('Km rodados durante o aluguel: '))
dias = eval(input('Quantidade de dias de aluguel: '))
preço = 60*dias + 0.15*km
print(f'O valor a pagar é R${preço:.2f} por {dias} dias e {km}km rodados.')