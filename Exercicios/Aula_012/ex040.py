#Boletim
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
média = (n1 + n2) / 2
print(f'Média: {média:.3f}.')
if média < 5.0:
    print(f'\033[1;30;41mAluno reprovado.\033[m')
elif média >= 7.0:
    print((f'\033[1;42mParabéns! Você foi aprovado! Boas férias!\033[m'))
else:
    print('\033[41mVocê está de recuperação.\033[m')