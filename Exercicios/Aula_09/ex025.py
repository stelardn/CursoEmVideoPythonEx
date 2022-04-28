#Receber um nome e verficar se há "Silva"
nome = input('Insira seu nome: ').strip()
if 'SILVA' in nome.upper():
    print('O nome contém "Silva".')
else:
    print('O nome não contém "Silva".')