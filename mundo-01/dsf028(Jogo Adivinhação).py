# Crie um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa devera escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 17)
print('Vou pensar em um número de 0 à 5, tente adivinhar!')
print('-=-' * 17)
jogador = int(input('Escolha seu número: '))
print('Seráaaa...')
sleep(3)

if computador == jogador:
    print(f'EU ESTAVA PENSANDO NO {computador} MESMO MEOOO!!!')
    print('PARABÉNS VOCÊ GANHOU!!! HIHIHIHHIHI')
else:
    print(f'Eu não estava pensando no {jogador}... Pensei no {computador}!!!')
    print('VOCÊ PERDEU SEU MERDA!!! HAHAHAHAH')
