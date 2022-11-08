# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salário: R$'))

if salario > 1250:
    aumento = salario + (salario * 0.10)
    print(f'Você teve um aumento de 10%\nPortanto seu salário aumentou R${salario * 0.10:.2f}')
else:
    aumento = salario + (salario * 0.15)
    print(f'Você teve um aumento de 15%\nPortanto seu salário aumentou R${salario * 0.15:.2f}')

print(f'Seu novo salário será de R${aumento:.2f}')
