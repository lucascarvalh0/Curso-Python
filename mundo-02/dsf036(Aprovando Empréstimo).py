# Crie um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = int(input('Em quantos anos vai pagar: '))

prestação = casa / (anos * 12)
mínimo = salario * 0.30

if prestação <= mínimo:
    print(f'PARABÉNS! Sua prestação será de R${prestação:.2f}, atendendo a menos de 30% do seu salário! Equivalente a R${mínimo:.2f}!')
    print('EMPRÉSTIMO APROVADO!!!')
else:
    print(f'QUE PENA! Sua prestação será de R${prestação:.2f}, excedendo o mínimo de 30% do seu salário! Equivalente a R${mínimo:.2f}!')
    print('EMPRÉSTIMO NEGADO!!!')
