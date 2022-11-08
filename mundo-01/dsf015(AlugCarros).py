# Crie um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('BEM VINDO!!! \nSISTEMA PARA DEVOLUÇÃO DE VEÍCULOS...\nConsiderando R$60 por dia e R$0,15 por KM rodado.')
km = float(input('KMs percorridos com o carro: '))
dias = int(input('Dias de aluguel: '))
preco = (60 * dias) + (0.15 * km)

print(f'Total: {preco:.2f}R$')
