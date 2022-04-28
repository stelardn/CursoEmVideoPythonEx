import math
angDeg = eval(input('Digite o ângulo: '))
angRad = math.radians(angDeg)
seno = math.sin(angRad)
coss = math.cos(angRad)
tang = math.tan(angRad)
print(f'Ângulo de {angDeg}° tem:\n seno: {seno}, cosseno: {coss}, tangente: {tang}')