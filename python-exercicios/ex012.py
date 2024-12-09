# Exercício 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$'))
porcentagem = float(input('Quantos % de desconto o produto irá receber? '))

desconto = (preco * porcentagem) / 100 
valor = preco - desconto

print('O produto que custava R${:.2f}, na promoção com desconto de {:.0f}% vai custar R${:.2f}.'.format(preco, porcentagem, valor))

# EXERCÍCIO FEITO EM AULA
# preco = float(input('Qual é o preço do produto? R$'))
# novo = preco - (preco * 5 / 100)
# print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(preco, novo))