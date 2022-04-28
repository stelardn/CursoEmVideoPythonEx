#Passagem de ônibus
dist = float(input('Qual a distância da sua viagem, em km? '))
"""if dist <= 200:
    preço = 0.50 * dist
else:
    preço = 0.45 * dist"""
preço = dist * 0.5 if dist <= 20 else dist * 0.45 #operador ternário
print(f'Sua passagem custará R${preço:.2f}.')