# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('-=-' * 11)
print(' /_\ Analista de triângulos /_\ ')
print('-=-' * 11)

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM formar um triângulo!')
    if s1 == s2 == s3:
        print('O triângulo é EQUILÁTERO.')
    elif s1 != s2 != s3 != s1:
        print('O triângulo é ESCALENO.')
    else:
        print('O triângulo é ISÓSCELES.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
