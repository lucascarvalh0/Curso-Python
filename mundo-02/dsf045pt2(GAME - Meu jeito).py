# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

computador = randint(0, 2)
opções = int(input('''Suas opções:

[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA
Qual é a sua jogada? '''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

if opções == 0 and computador == 1:
    print('-=-' * 10)
    print('Você jogou PEDRA')
    print('Computador jogou PAPEL')
    print('-=-' * 10)
    print('COMPUTADOR VENCEU!!!')
elif opções == 0 and computador == 2:
    print('-=-' * 10)
    print('Você jogou PEDRA')
    print('Computador jogou TESOURA')
    print('-=-' * 10)
    print('JOGADOR VENCEU!!!')

elif opções == 1 and computador == 0:
    print('-=-' * 10)
    print('Você jogou PAPEL')
    print('Computador jogou PEDRA')
    print('-=-' * 10)
    print('JOGADOR VENCEU!!!')
elif opções == 1 and computador == 2:
    print('-=-' * 10)
    print('Você jogou PAPEL')
    print('Computador jogou TESOURA')
    print('-=-' * 10)
    print('COMPUTADOR VENCEU!!!')

elif opções == 2 and computador == 0:
    print('-=-' * 10)
    print('Você jogou TESOURA')
    print('Computador jogou PEDRA')
    print('-=-' * 10)
    print('COMPUTADOR VENCEU!!!')
elif opções == 2 and computador == 1:
    print('-=-' * 10)
    print('Você jogou TESOURA')
    print('Computador jogou PAPEL')
    print('-=-' * 10)
    print('JOGADOR VENCEU!!!')
    
elif opções == computador:
    print('-=-' * 10)
    print('Vocês escolheram a mesma opção')
    print('-=-' * 10)
    print('EMPATOU, JOGUEM DE NOVO!!!')
