# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual a distância da sua viagem em km? '))
print(f'Sua viagem terá uma distância de {distancia:.2f}km.')

preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45 # If simplificado

# If..Else normal:
'''if distancia <= 200:
    preço = 0.50 * distancia
else:    
    preço = 0.45 * distancia'''

print(f'O preço da sua passagem será R${preço:.2f}.')
