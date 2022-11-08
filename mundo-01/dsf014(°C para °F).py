# Crie um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite e converta de Celsius para Fahrenheit: '))
f = (c * 9/5) + 32

print(f'{c}°C convertidos equivalem a {f:.1f}°F.')
