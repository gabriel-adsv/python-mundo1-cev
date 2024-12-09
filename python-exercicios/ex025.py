# Exercício 025
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o nome completo da pessoa: '))

if 'Silva' in nome or 'SILVA' in nome:
  print('O nome completo {} contém "SILVA"'.format(nome))
else:
  print('O nome completo {} não contém "SILVA"'.format(nome))

# EXERCÍCIO FEITO EM AULA
# nome = str(input('Qual é seu nome completo? ')).strip()
# print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))