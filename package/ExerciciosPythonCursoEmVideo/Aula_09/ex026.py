"""Leia uma frase pelo teclado e mostre:
- quantas vezes a letra 'A' aparece;
- em que posição aparece o primeiro 'A';
- em que posição aparece o último 'A'."""
frase = input('Insira uma frase: ').strip().upper()
fraseInv = frase[::-1]
print(frase.count('A'),'letras "a" foram inseridas.')
print(frase.find('A'),'é a posição do primeiro "a".')
print(frase.rfind('A'),'é a posição do último "a".')
print(fraseInv.find('A'),'é a posição do último "a", de trás para frente.')
print(len(frase))
