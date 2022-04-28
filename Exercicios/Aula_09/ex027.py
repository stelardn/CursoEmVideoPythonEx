#Leia o nome de uma pessoa e retorne o primeiro e o último nome
nome = str(input('Insira seu nome completo: ')).strip()
nome = nome.split()
print('Olá, {} {}!'.format(nome[0],nome[-1])) #ou [len(nome) - 1]
