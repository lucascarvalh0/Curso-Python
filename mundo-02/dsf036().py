# Crie um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Valor da casa: '))
salario = float(input('Salário: '))
tempo = int(input('Em quantos anos vai pagar: '))
validação = (valor/tempo)
