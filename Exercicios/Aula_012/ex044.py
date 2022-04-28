#Pagamento
print('{:=^40}'.format('LOJAS SULAMERICANAS')) #centraliza o texto entre 40 espaços
print('Condições de pagamento:\n'
'1 - à vista (dinheiro/cheque): 10% de desconto;\n'
'2 - à vista no cartão (débito): 5% de desconto;\n'
'3 - cartão de crédito: \n'
    '- em até 2x: preço normal;\n'
    '- 3x ou mais: 20% de juros.\n')
try:
    preço = float(input('Insira o preço do produto: R$'))
    try:
        pagamento = int(input('Insira a forma de pagamento (1, 2 ou 3): '))
        if pagamento == 1:
            pagar = preço * 0.9
        elif pagamento == 2:
            pagar = preço * 0.95
        elif pagamento == 3:
            parcelas = int(input('Em quantas vezes? '))
            if parcelas <= 2:
                pagar = preço
            else:
                pagar = preço * 1.2
            mensalidade = pagar / parcelas
            print(f'{parcelas}x R${mensalidade:.2f} ')
        print(f'Valor total a ser pago: R${pagar:.2f}')
    except:
        print('Opção de pagamento inválida.')
except ValueError:
    print('Preço inválido. Tente novamente.')