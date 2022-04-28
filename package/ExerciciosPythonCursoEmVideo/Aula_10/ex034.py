#Aumento condicional
sal = float(input("Qual o salário atual do funcionário? R$"))
if sal > 1250:
    aumentoPer = 10
    novoSal = 1.1 * sal
    aumento = 0.1 * sal
else:
    aumentoPer = 15
    novoSal = 1.15 * sal
    aumento = 0.15 * sal
print(f"O aumento será de {aumentoPer}%, que corresponde a R${aumento:.2f}.\nO novo salário será de R${novoSal:.2f}.")