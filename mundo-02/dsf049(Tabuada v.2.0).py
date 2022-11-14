# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número para saber a tabuada: '))

print('-' * 13)
for c in range(1, 11):
    print(f'{n} x {c:2} = {n * c}')
print('-' * 13)
