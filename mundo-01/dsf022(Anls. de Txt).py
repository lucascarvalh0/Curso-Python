# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: ')) .strip()
#nome = nome.replace('Lucas', 'Jucas') -- Muda o nome se colocado em uma variável

print('Analisando seu nome...\n')
print(f'Seu nome em maiúsculo é: {nome.upper()}')
print(f'Seu nome em minúsculo é: {nome.lower()}')
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
#print(f'Seu nome tem {len(nome) - nome.count(' ')} letras') -- Não sei pq não deu certo
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras.')
