# Exercício 030
# Crie um programa que leia um número inteiro e mostre na tela se é PAR ou ÍMPAR.

# Passo 1: Leia um número inteiro
# numero = int(input('Digite um número inteiro: '))

# # Passo 2: Verificar se o número é PAR ou ÍMPAR
# if numero % 2 == 0:
#   print('O número {} é PAR.'.format(numero))
# else:
#   print('O número {} é ÍMPAR.'.format(numero))

# EXERCÍCIO FEITO EM AULA
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
  print('O número {} é PAR'.format(número))
else:
  print('O número {} é ÍMPAR'.format(número))