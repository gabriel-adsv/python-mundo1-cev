# Exercício 017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = hypot(oposto, adjacente)

print('A hipotenusa vai medir {:.2f}.'.format(hipotenusa))

# EXERCÍCIO FEITO EM AULA
# calculo padrão
# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimendo do cateto adjacente: '))

# hi = (co ** 2 + ca ** 2) ** (1/2)

# print('A hipotenusa vai medir {:.2f}'.format(hi))

# usando math
# import math

# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimendo do cateto adjacente: '))
# hi = math.hypot(co, ca)
# print('A hipotenusa vai medir {:.2f}'.format(hi))