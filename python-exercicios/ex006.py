# Exercício 006 - Dobro, Triplo e Raiz Quadrada
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

cores = {
  'amarelo':'\033[1;33m',
  'verde':'\033[1;34m',
  'sem_cor':'\033[m'
}

numero = int(input('Digite um número: '))

print('O dobro de {}{}{} é: {}{}{}'.format(cores['amarelo'], numero, cores['sem_cor'], cores['verde'], (numero * 2), cores['sem_cor']))
print('O triplo de {}{}{} é: {}{}{}'.format(cores['amarelo'], numero, cores['sem_cor'], cores['verde'], (numero * 3), cores['sem_cor']))
print('E a raiz quadrada de {}{}{} é: {}{:.0f}{}'.format(cores['amarelo'], numero, cores['sem_cor'], cores['verde'], pow(numero, (1/2)), cores['sem_cor']))

# EXERCICIO FEITO EM AULA
'''
  n = int(input('Digite um número: '))
  d = n * 2
  t = n * 3
  r = n ** (1/2)
  print('O dobro de {} vale {}.'.format(n, d))
  print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
'''
