# Exercício 003 - Somando dois números
# Crie um programa que leia dois números e mostre a soma entre eles.

cores = {
  'azul':'\033[0;34m',
  'verde':'\033[0;32m',
  'sem_cor':'\033[m'
}

n1 = input('Digite o 1º número: ')
n2 = input('Digite o 2º número: ')

soma = int(n1) + int(n2)

print('O resultado da soma entre {}{}{} e {}{}{} é igual a {}{}{}!'.format(cores['azul'], n1, cores['sem_cor'], cores['azul'], n2, cores['sem_cor'], cores['verde'], soma, cores['sem_cor']))
