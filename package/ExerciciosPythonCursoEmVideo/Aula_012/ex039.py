#Alistamento militar
from datetime import date
anoNasc = int(input('Qual o ano do seu nascimento? '))
idade = date.today().year - anoNasc
if idade > 18:
    anosAtraso = idade - 18
    anoAlist = anoNasc + 18
    if anosAtraso == 1:
        print('O ano do seu alistamento foi ano passado.')
    else:
        print(f'O seu alistamento está atrasado em {anosAtraso} anos.')
        print(f'O ano do seu alistamento foi {anoAlist}.')
elif idade == 18:
    print('Você deve se alistar esse ano.')
else:
    anosFaltam = 18 - idade
    if anosFaltam == 1:
        print('Você deve se alistar ano que vem.')
    else:
        anoAlist = anoNasc + 18
        print(f'Faltam {anosFaltam} anos para o seu alistamento.')
        print(f'O seu ano de alistamento será {anoAlist}.')
print('\033[1;42mBrasil, um país de todes.\033[m')