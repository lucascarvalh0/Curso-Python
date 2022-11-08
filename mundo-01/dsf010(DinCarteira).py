# Crie um programa que leia o quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Digite quanto você tem em R$: '))
dolar = 5.17

print(f'Com {real:.2f} R$, você consegue comprar {real/dolar:.2f} US$!')
