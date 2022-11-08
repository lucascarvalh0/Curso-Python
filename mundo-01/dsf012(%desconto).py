# Crie um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço para saber o valor de desconto: R$'))
desconto = preço - (preço * 0.05)

print(f'O preço deste produto com 5% de desconto é R${desconto:.2f}')
