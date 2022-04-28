#Categoria de natação
from datetime import date
print('\033[1;42m=' * 40)
print('CNN: Confederação Nacional de Natação')
print('=' * 40)
anoNasc = int(input('\033[mInsira o ano de nascimento do atleta: '))
idade = date.today().year - anoNasc
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')