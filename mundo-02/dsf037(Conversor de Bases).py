# Crie um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro qualquer: '))

print('''Digite a opção que você deseja converter:
[ 1 ] Para conversão BINÁRIA.
[ 2 ] Para conversão OCTAL.
[ 3 ] Para conversão HEXADECIMAL. ''')

opção = int(input('Escolha uma opção: '))

if opção == 1:
    print(f'O número {num} convertido em BINÁRIO é = {bin(num)[2:]}')
elif opção == 2:
    print(f'O número {num} convertido em OCTAL é = {oct(num)[2:]}')
elif opção == 3:
    print(f'O número {num} convertido em HEXADECIMAL é = {hex(num)[2:]}')
else:
    print('Valor inválido, digite novamente!')
