#Programa que receba um valor em metros e o converta em centímetros e milímetros:
metros = eval(input('Insira o valor, em metros: '))
print('{}m equivalem a {:.3f}cm, ou {:.3f}mm.'.format(metros,(metros*100),(metros*1000)))