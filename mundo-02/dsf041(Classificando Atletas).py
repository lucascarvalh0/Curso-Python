# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

atual = date.today().year
nasc = int(input('Data de nascimento do atleta: '))
idade = (atual - nasc)

if idade <= 9:
    print(f'O atleta tem {idade} anos: MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos: INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anos: JÚNIOR')
elif idade <= 25:
    print(f'O atleta tem {idade} anos: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos: MASTER')
