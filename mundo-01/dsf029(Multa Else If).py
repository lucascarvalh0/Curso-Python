# Crie um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

km = float(input('Km/h: '))

if km > 80:
    print('Velocidade acima da permitida!')
    print('Você recebeu uma multa de R${:.2f}'.format((km - 80) * 7))
else:
    print('Dentro do limite de velocidade, boa viagem!')
