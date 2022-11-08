# Crie um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário: R$'))
aumento = salario + (salario * 0.15)

print(f'Seu salário atual é de R${salario}')
print(f'Após aumento de 15% seu novo salário será R${aumento:.2f}.')
