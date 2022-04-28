#Ler o valor que uma pessoa tem em sua carteira e mostra quantos dólares ela pode comprar
reais = eval(input('Quantos reais você tem? '))
print('Você pode comprar {:.3f} doláres com {} reais.'.format((reais/5.68),reais))