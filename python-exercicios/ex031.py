# Exercício 031
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

# Passo 1: Entre com a distância da viagem
distancia = float(input('Qual a distância em Km da viagem? '))

# Passo 2: Calcular o preço da passagem até 200km
valor = distancia * 0.50

# Passo 3: Calcular o preço da passagem acima de 200km
if distancia > 200:
  valor = distancia * 0.45

# Passo 4: Exibir o custo total da viagem
print('A distancia da viagem é de {} Km e o valor da passagem é R$ {:.2f}.'. format(distancia, valor))

# EXERCÍCIO FEITO EM AULA
'''distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
if distância <= 200:
  preço = distância * 0.50
else:
  preço = distância * 0.45
print('E o preço da sua passagem será de R${}'.format(preço))'''

# condição simplificada
'''distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${}'.format(preço))'''