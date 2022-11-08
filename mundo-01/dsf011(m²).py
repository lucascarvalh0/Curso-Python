# Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('Largura: '))
alt = float(input('Altura: '))

area = larg * alt
lt = area / 2

print(f'Parede com dimensão de {larg:.1f}m x {alt:.1f}m e área total de {area:.1f}m².')
print(f'Para essa parede você precisará utilizar {lt:.1f}l de tinta.')
