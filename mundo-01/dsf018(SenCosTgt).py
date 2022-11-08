# Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input("Digite o ângulo: "))

se = sin(radians(angulo))
co = cos(radians(angulo))
tgt = tan(radians(angulo))

print(f'Ângulo de {angulo:.0f}° \nSeno: {se:.2f} \nCosseno: {co:.2f} \nTangente: {tgt:.2f}')
