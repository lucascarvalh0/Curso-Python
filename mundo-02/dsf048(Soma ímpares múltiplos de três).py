# Crie um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 1
for n in range(1, 501, 2):
    if n % 3 == 0:
        print(n, end = ' ')
        soma += n
        cont += 1

print(f'\nA soma de todos os {cont} múltiplos de 3, de 1 a 500, é = {soma}')
