#Radar semafórico
vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    print(f'\033[1;30;41mLimite de velocidade ultrapassado! Você receberá uma multa de R${(vel-80)*7:.2f}.\033[m')
else:
    print('\033[30;42mVelocidade dentro do limite.\033[m')