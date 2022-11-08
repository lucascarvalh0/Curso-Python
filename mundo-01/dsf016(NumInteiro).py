# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite o número 6.127 | O número 6.127 tem a parte inteira 6.

from math import trunc
n = float(input('Digite um número para saber sua porção inteira: '))
i = trunc(n)

print(f'O número {n} é representado por {i} em sua porção inteira.')
