# Crie um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Digite o ano em que nasceu: '))

atual = date.today().year
idade = (atual - ano)
limite = 18

if idade < 18:
    print(f'Você tem {idade} anos e ainda vai se alistar no serviço militar.')
    print(f'Faltam {limite - idade} anos para seu alistamento.')
elif idade > 18:
    print(f'Você tem {idade} anos e já pode se alistar no serviço militar.')
    print(f'Já passaram {idade - limite} anos do prazo para você se alistar.')
else: print('Você tem 18 anos, este é o momento para se alistar no serviço militar.')
