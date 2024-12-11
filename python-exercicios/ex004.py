# Exercício 004 - Dissecando uma Variável
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

cores = {
  'vermelho':'\033[0;0;41m ',
  'verde':'\033[0;0;42m',
  'azul':'\033[0;0;44m',
  'sem_cor':'\033[m'
}

entrada = input('Digite algo: ')
espaco = entrada.isspace()
numero = entrada.isnumeric()
alfabetico = entrada.isalpha()
alfanumerico = entrada.isalnum()
maiusculas = entrada.isupper()
minusculas = entrada.islower()
capitalizada = entrada.istitle()

print('O tipo primitivo desse valor é {} {} {}'.format(cores['azul'], type(entrada), cores['sem_cor']))

if espaco == True:
  print('Só tem espaços? {} {} {}'.format(cores['verde'], espaco, cores['sem_cor']))
else:
  print('Só tem espaços? {} {} {}'.format(cores['vermelho'], espaco, cores['sem_cor']))
  
if numero == True:
  print('É um número? {} {} {}'.format(cores['verde'], numero, cores['sem_cor']))
else:
  print('É um número? {} {} {}'.format(cores['vermelho'], numero, cores['sem_cor']))

if alfabetico == True:
  print('É alfabético? {} {} {}'.format(cores['verde'], alfabetico, cores['sem_cor']))
else:
  print('É alfabético? {} {} {}'.format(cores['vermelho'], alfabetico, cores['sem_cor']))

if alfanumerico == True:
  print('É alfanumérico?  {} {} {}'.format(cores['verde'], alfanumerico, cores['sem_cor']))
else:
  print('É alfanumérico?  {} {} {}'.format(cores['vermelho'], alfanumerico, cores['sem_cor']))

if maiusculas == True:
  print('Está em maiúsculas?  {} {} {}'.format(cores['verde'], maiusculas, cores['sem_cor']))
else:
  print('Está em maiúsculas?  {} {} {}'.format(cores['vermelho'], maiusculas, cores['sem_cor']))

if minusculas == True:
  print('Está em minúsculas? {} {} {}'.format(cores['verde'], minusculas, cores['sem_cor']))
else:
  print('Está em minúsculas? {} {} {}'.format(cores['vermelho'], minusculas, cores['sem_cor']))

if capitalizada == True:
  print('Está capitalizada? {} {} {}'.format(cores['verde'], capitalizada, cores['sem_cor']))
else:
  print('Está capitalizada? {} {} {}'.format(cores['vermelho'], capitalizada, cores['sem_cor']))
