# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

#USANDO COMANDOS INTERNOS

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print(f'A raiz da hipotenusa é: {hi:.2f}')

#USANDO IMPORT

import math # Outra opção: from match import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = math.hypot(co, ca) # Outra opção: hypot(co, ca)
print(f'A raiz da hipotenusa é: {hi:.2f}')
