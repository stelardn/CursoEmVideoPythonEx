"""Ler o nome completo de uma pessoa e mostrar:
- o nome com todas as letras minúsculas;
- o nome com todas as letras maiúsculas;
- quantas letras ao todo, sem considerar espaços;
- quantas letras tem o primeiro nome."""
nome = input('Digite seu nome completo: ').strip()
print(nome.lower())
print(nome.upper())
espaços = nome.count(' ')
print(len(nome) - espaços)
nomes = nome.split()
print(len(nomes[0]))