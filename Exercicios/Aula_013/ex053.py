# Palíndromo?
print('Vamos brincar de palíndromo? ')
frase0 = str(input('Insira uma frase! ')).strip().upper()
frase = frase0.replace(' ', '')
isPalindromo = True
for c in range(0, len(frase) - 1):
    if frase[c] != frase[len(frase) - 1 - c]:
        isPalindromo = False
if isPalindromo:
    print(f'Sim, {frase0} é um palíndromo!')
else:
    print(f'Não, {frase0} não é palíndromo.')
