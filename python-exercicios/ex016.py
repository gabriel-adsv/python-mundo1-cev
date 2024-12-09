# Exercício 016
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

from math import trunc

numero = float(input('Digite um número: '))

print('O número {} tem a parte inteira {}.'.format(numero, trunc(numero)))

# EXERCÍCIO FEITO EM AULA

# 1ª maneira
# from math import trun
# num = float(input('Digite um valor: '))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

# 2ª maneira
# num = float(input('Digite um valor: '))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))