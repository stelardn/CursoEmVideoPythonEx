#PEDRA, PAPEL, TESOURA!
from random import randint
from time import sleep
print('Vamos jogar!\n'
      'Escolha:\n'
      '1 - pedra;\n'
      '2 - papel;\n'
      '3 - tesoura!')
player = int(input())
print('Pedra,')
sleep(0.5)
print('papel,')
sleep(0.5)
print('teSOURA!')
computer = randint(1,3)
Menu = {1 : 'Pedra!', 2 : 'Papel!',3 : 'Tesoura!'}
if player != 1 and player != 2 and player != 3:
      print('Ei! Brinca direito! Esse número não vale!')
else:
      print(f'Você: {Menu [player]}')
      print(f'Eu: {Menu [computer]}')
      if player == computer:
            print('Empatamos!')
      else:
            if player == 1:
                  if computer == 2:
                        winner = computer
                  else:
                        winner = player
            elif player == 2:
                  if computer == 1:
                        winner = player
                  else:
                        winner = computer
            elif player == 3:
                  if computer == 1:
                        winner = computer
                  else:
                        winner = player
            if winner == player:
                  print('Você ganhou!')
            elif winner == computer:
                  print('Haha! Eu ganhei!')
