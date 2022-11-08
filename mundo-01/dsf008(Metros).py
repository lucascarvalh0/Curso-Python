# Crie um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n1 = float(input('Digite um valor em metros:'))
cm = n1 * 100
mm = n1 * 1000

print(f'{n1} metros equivalem a {cm:.0f} centímetros.')
print(f'{n1} metros equivalem a {mm:.0f} milímetros.')
