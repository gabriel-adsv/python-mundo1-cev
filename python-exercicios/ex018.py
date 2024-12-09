# Exercício 018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.

# FIZ A IMPORTAÇÃO ERRADA
from math import sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print('O ângulo de {} tem o SENO de {:.2f}. \nO ângulo de {} tem o COSSENO de {:.2f}. \nO ângulo de {} tem a TANGENTE de {:.2f}.'.format(angulo, seno, angulo, cosseno, angulo, tangente))

# EXERCÍCIO FEITO EM AULA
# from math import radians, sin, cos, tan
# ângulo = float(input('Digite o ângulo que você deseja: '))
# seno = sin(radians(ângulo))
# print('O ângulo de {} tem o SENO de {:.2f}.'.format(ângulo, seno))
# cosseno = cos(radians(ângulo))
# print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(ângulo, cosseno))
# tangente = tan(radians(ângulo))
# print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(ângulo, tangente))