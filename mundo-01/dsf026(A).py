# Crie um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

texto = str(input('Digite um texto qualquer: ')).strip() .upper()
print('Analisando seu texto...')
print('A letra A aparece {} vezes no seu texto.'.format(texto.count('A')))
print('A letra A aparece pela primeira vez na posição {} do seu texto.'.format(texto.find('A')+1))
print('A letra A aparece pela última vez na posição {} do seu texto.'.format(texto.rfind('A')+1))
