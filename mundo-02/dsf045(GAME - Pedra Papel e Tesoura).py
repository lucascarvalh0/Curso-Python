# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('''Suas opções:

[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')

jogador = int(input('Qual sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=-' * 8)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=-' * 8)

if computador == 0:
    if jogador == 0:
        print('EMPATOU! JOGUEM NOVAMENTE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!!!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!!!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 1:
        print('EMPATOU! JOGUEM NOVAMENTE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!!!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!!!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 2:
        print('EMPATOU! JOGUEM NOVAMENTE!')
    else:
        print('JOGADA INVÁLIDA!')
