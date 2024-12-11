# Exercício 009
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input('Digite um número: '))

n0 = numero * 0
n1 = numero * 1
n2 = numero * 2
n3 = numero * 3
n4 = numero * 4
n5 = numero * 5
n6 = numero * 6
n7 = numero * 7
n8 = numero * 8
n9 = numero * 9
n10 = numero * 10

borda = '-----' * 5

print('{}{}'.format('\033[32m', borda))
print(' {} x 0 = {}'.format(numero, n0))
print(' {} x 1 = {}'.format(numero, n1))
print(' {} x 2 = {}'.format(numero, n2))
print(' {} x 3 = {}'.format(numero, n3))
print(' {} x 4 = {}'.format(numero, n4))
print(' {} x 5 = {}'.format(numero, n5))
print(' {} x 6 = {}'.format(numero, n6))
print(' {} x 7 = {}'.format(numero, n7))
print(' {} x 8 = {}'.format(numero, n8))
print(' {} x 9 = {}'.format(numero, n9))
print(' {} x 10 = {}'.format(numero, n10))
print('{}{}'.format(borda, '\033[m'))

# EXERCICIO FEITO EM AULA
'''
  num = int(input('Digite um número para ver sua tabuada: '))
  print('-' * 12)
  print(' {} x {:2} = {}'.format(num, 0, num * 0))
  print(' {} x {:2} = {}'.format(num, 1, num * 1))
  print(' {} x {:2} = {}'.format(num, 2, num * 2))
  print(' {} x {:2} = {}'.format(num, 3, num * 3))
  print(' {} x {:2} = {}'.format(num, 4, num * 4))
  print(' {} x {:2} = {}'.format(num, 5, num * 5))
  print(' {} x {:2} = {}'.format(num, 6, num * 6))
  print(' {} x {:2} = {}'.format(num, 7, num * 7))
  print(' {} x {:2} = {}'.format(num, 8, num * 8))
  print(' {} x {:2} = {}'.format(num, 9, num * 9))
  print(' {} x {:2} = {}'.format(num, 10, num * 10))
  print('-' * 12)
'''