# Crie um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJÃO DO LUCÃO - AQUI VOCÊ ACHA TUDÃO ')) # Deu ruim aqui e no IDLE

produto = input('Produto: ')
preço = float(input('Valor do produto: R$'))
pagamento = int(input('''Digite a opção da forma de pagamento:
[ 1 ] - À vista dinheiro/cheque - [10% desconto]
[ 2 ] - À vista no cartão       - [5% desconto]
[ 3 ] - Em até 2x no cartão     - [Preço formal]
[ 4 ] - 3x ou mais no cartão    - [20% de juros]
Escolha sua opção: '''))

if pagamento == 1:
    desconto = preço - (preço * 10 / 100)
    print('Você escolheu a opção [ 1 ] - À vista dinheiro/cheque - [10% desconto]')
    print(f'O valor a ser pago com desconto será R${desconto:.2f}')
elif pagamento == 2:
    desconto = preço - (preço * 5 / 100)
    print('Você escolheu a opção [ 2 ] - À vista no cartão - [5% desconto]')
    print(f'O valor a ser pago com desconto será R${desconto:.2f}')
elif pagamento == 3:
    print('Você escolheu a opção [ 3 ] - Em até 2x no cartão - [Preço formal]')
    print(f'Sua compra será parcelada em 2x de R${preço/2:.2f} Somando um total de {preço:.2f} (Valor formal).')
elif pagamento == 4:
    juros = preço + (preço * 20 / 100)
    print('Você escolheu a opção [ 4 ] - 3x ou mais no cartão - [20% de juros]')
    parcelas = int(input('Número de parcelas: '))
    print(f'Sua compra sera parcelada em {parcelas}x de R${juros/parcelas:.2f} Somando um total de R${juros:.2f} com juros.')
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO!')

print(f'Parabéns!!! Você acabou de adquirir: {produto}.\nObrigado e volte sempre!!!')
