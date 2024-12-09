# Exercício 014
# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

celsius = float(input('Informe a temperatura em °C: '))

fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + 273.15

print('A temperatura de {}°C corresponde a {}°F e {}°K!'.format(celsius, fahrenheit, kelvin))

# EXERCICIO FEITO EM AULA
# c = float(input('Informe a temperatura em °C: '))
# f = ((9 * c) / 5) + 32

# print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))
