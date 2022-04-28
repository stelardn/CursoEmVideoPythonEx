#Tabuada
num = int(input('Qual o número inteiro cuja tabuada você quer ver? '))
print('='*20)
print(f'TABUDADA DE {num}:')
for c in range (1, 10):
    print(f'{c} x {num} = {c*num}')
print('='*20)