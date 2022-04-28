#Criar um programa que leia o nome de uma cidade e escreva se ela começa ou não com "SANTO"
nome = input('Insira o nome da cidade: ').strip().upper()
primeiroNome = nome.split()
primeiroNome = primeiroNome[0]
if primeiroNome == 'SANTO' and len(primeiroNome) == 5:
    print('A primeira palavra do nome da cidade é "Santo".')
else:
    print('A primeira palavra do nome da cidade não é "Santo".')