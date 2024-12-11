# Exercício 032
# Faça um programa que leia um ano qualquer e mostre se é BISSEXTO.

# Passo 1: Entre com o ano
ano = int(input('Digite um ano: '))

# Passo 2: Dividir o ano por 4 e por 100 para saber se é bissexto
if ano % 4 == 0 and ano % 100 != 0:
  print('O ano {} é bissexto.'.format(ano))
else:
  print ('O ano {} não é um ano bissexto.'.format(ano))

# EXERCÍCIO FEITO EM AULA
'''from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
  ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('O ano {} é BISSEXTO'.format(ano))
else:
  print('O ano {} não é BISSEXTO'.format(ano))'''