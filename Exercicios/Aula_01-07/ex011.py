#Ler a altura e a largura de uma parede, calcular sua área e quantos litros de tinta são necessários para pintá-la, sendo que 1l pinta 2m²
lar = eval(input('Insira a largura da parede, em metros: '))
alt = eval(input('Insira a altura da parede, em metros: '))
area = lar*alt
tinta = area/2
print('São necessários {:.2f}l de tinta para pintar uma parede de {:.2f}m².'.format(tinta,area))
