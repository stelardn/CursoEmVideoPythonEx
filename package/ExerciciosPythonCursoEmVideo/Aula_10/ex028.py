#Jogo da adivinhação
from random import randint
from time import sleep
numPlayer = int(input('Adivinhe em qual número estou pensando, de 0 a 5! '))
print('Processando...')
sleep(2)
numComp = randint(0,5)
if numComp == numPlayer:
    print('\033[1;30;42mAcertou, miserávi!\033[m')
else:
    print(f'\033[1;30;41mEroooou! Era {numComp}!\033[m')