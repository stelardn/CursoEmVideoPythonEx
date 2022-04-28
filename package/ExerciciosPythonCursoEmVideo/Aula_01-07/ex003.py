"""Faça um programa que leia algo pelo teclado e mostre
na tela o seu tipo primitivo e todas as informações possíveis"""
n = input('Digite algo: ')
print(type(n))
print('É alpha? ','\033[7;40m',n.isalpha(),'\033[m')
print('É numerico? ',n.isnumeric())
print('É alphanumerico? ',n.isalnum())
print('É minusculo? ',n.islower())
