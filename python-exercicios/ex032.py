# Exercício 032
# Faça um programa que leia um ano qualquer e mostre se é BISSEXTO.

# Passo 1: Entre com o ano
ano = int(input('Digite um ano: '))

# Passo 2: Dividir o ano por 4 e por 100 para saber se é bissexto
if ano % 4 == 0 and ano % 100 != 0:
  print('O ano {} é bissexto.'.format(ano))
else:
  print ('O ano {} não é um ano bissexto.'.format(ano))