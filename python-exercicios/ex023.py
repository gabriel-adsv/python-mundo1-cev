# Exercício 023
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# 	Ex:
# 	- Digite um número: 1834
# 	- Unidade: 4
# 	- Dezena: 3
# 	- Centena: 8
# 	- Milhar: 1

numero = str(input('Digite um número: '))
print('Analisando o número...')

print('Unidade: {}'.format(numero[3:4]))
print('Dezena: {}'.format(numero[2:3]))
print('Centena: {}'.format(numero[1:2]))
print('Milhar: {}'.format(numero[0:1]))

# EXERCÍCIO FEITO EM AULA
# num = int(input('Informe um número: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print('Analisando o número {}'.format(num))
# print('Unidade: {}'.format(u))
# print('Dezena: {}'.format(d))
# print('Centena: {}'.format(c))
# print('Milhar: {}'.format(m))