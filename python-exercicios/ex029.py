# Exercício 029
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

# Passo 1: Entre com a velocidade do carro
velocidade = int(input('Digite a velocidade do carro: '))

# Passo 2: Se o carro estiver acima de 80 Km/h, o motorista foi multado
if velocidade > 80:
  # Passo 3: Somar 7,00 para cada km acima de 80
  multa = (velocidade - 80) * 7
  print('Você excedeu o limite de velocidade e vai pagar R$ {:.2f} de multa.'.format(multa))
else:
  print('Parabéns! Você não excedeu o limite de velocidade.')

# EXERCÍCIO FEITO EM AULA
# velocidade = float(input('Qual é a velocidade atual do carro? '))

# if velocidade > 80:
#   print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
#   multa = (velocidade - 80)* 7
#   print('Você deve pagar uma multa de R${:.2f}'.format(multa))
# print('Tenha um vom dia! Dirija com segurança!')