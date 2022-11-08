# Crie um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

#Usando PRINT

n1 = int(input('Digite um número e veja sua tabuada: '))

print('-' * 13)
print('{} x {:2} = {}'.format(n1, 1, n1 * 1))
print('{} x {:2} = {}'.format(n1, 2, n1 * 2))
print('{} x {:2} = {}'.format(n1, 3, n1 * 3))
print('{} x {:2} = {}'.format(n1, 4, n1 * 4))
print('{} x {:2} = {}'.format(n1, 5, n1 * 5))
print('{} x {:2} = {}'.format(n1, 6, n1 * 6))
print('{} x {:2} = {}'.format(n1, 7, n1 * 7))
print('{} x {:2} = {}'.format(n1, 8, n1 * 8))
print('{} x {:2} = {}'.format(n1, 9, n1 * 9))
print('{} x {:2} = {}'.format(n1, 10, n1 * 10))
print('-' * 13)

# Usando WHILE


n1 = int(input('Digite um número e veja sua tabuada: '))
cont = 1

print('-' * 13)

while cont <11:
    print(f'{n1:2} x {cont:2} = {n1*cont}')
    cont += 1

print('-' * 13)
