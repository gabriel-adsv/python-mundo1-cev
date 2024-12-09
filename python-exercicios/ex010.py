# Exercício 010
# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('quanto dinheiro você tem na carteira? R$'))

dolar = real / 6.01
euro = real / 6.35
iene = real * 25.20
yuan = real * 1.20
bitcoin = real / 576.130

print('Com R${:.2f} você pode comprar: \nUSD ${:.2f} \nEUR €{:.2f} \nJPY ¥{:.2f} \nCNY ¥{:.2f} \nBTC - Bitcoin {:.7f}.'.format(real, dolar, euro, iene, yuan, bitcoin))

# EXERCÍCIO FEITO EM AULA
# real = float(input('Quanto dinheiro você tem na carteira? R$'))
# dolar = real / 3.27
# print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))