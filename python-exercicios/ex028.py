# Exercício 028
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint

numero_aleatorio = randint(0,5)
print('Jogo da adivinhação')
numero_usuario = int(input('Digite um número entre 0 e 5: '))

if numero_usuario == numero_aleatorio:
  print('Parabéns, você acertou! O número é {}'.format(numero_aleatorio))
else:
  print('Você errou! O número que o computador escolheu é {}'.format(numero_aleatorio))