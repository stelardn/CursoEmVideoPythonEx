#IMC
alt = float(input('Insira a sua altura, em m: '))
peso = float(input('Insira o seu peso, em kg: '))
IMC = peso / (alt ** 2)
if IMC < 18.5:
    print('Abaixo do peso.')
elif IMC <= 25:
    print('Peso ideal.')
elif IMC <= 30:
    print('Sobrepeso.')
elif IMC <= 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')