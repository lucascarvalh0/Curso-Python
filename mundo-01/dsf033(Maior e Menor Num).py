# Crie um programa que leia três números e mostre qual é o maior e qual é o menor.

print('Digite 3 números inteiros aleatórios...')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

# Verificando o maior:

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# Verificando o menor:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'O maior número é o {maior}. \nE o menor número é o {menor}.')
