# Exercício 010
# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar.

cores = {
  'underline':'\033[4m',
  'vermelho':'\033[1;31m',
  'verde':'\033[1;32m',
  'amarelo':'\033[1;33m',
  'sem_cor':'\033[m'
}

real = float(input('quanto dinheiro você tem na carteira? R$'))

dolar = real / 6.01
euro = real / 6.35
iene = real * 25.20
yuan = real * 1.20
bitcoin = real / 576.130

print('Com {}R${:.2f}{} você pode comprar: '.format(cores['underline'], real, cores['sem_cor']))
print('{}USD ${:.2f}{}'.format(cores['verde'], dolar, cores['sem_cor']))
print('{}EUR €{:.2f}{}'.format(cores['vermelho'], euro, cores['sem_cor']))
print('{}JPY ¥{:.2f}{}'.format(cores['vermelho'], iene, cores['sem_cor']))
print('{}CNY ¥{:.2f}{}'.format(cores['vermelho'], yuan, cores['sem_cor']))
print('{}BTC - Bitcoin {:.7f}{}'.format(cores['amarelo'], bitcoin, cores['sem_cor']))

# EXERCÍCIO FEITO EM AULA
'''
  real = float(input('Quanto dinheiro você tem na carteira? R$'))
  dolar = real / 3.27
  print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
'''