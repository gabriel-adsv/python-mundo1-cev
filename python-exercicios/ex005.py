# Exercício 005 - Antecessor e Sucessor
# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e o seu antecessor.

numero = input('Digite um número: ')

sucessor = int(numero) + 1
antecessor = int(numero) - 1

print('Você digitou o número {}. Seu sucessor é {}. E o seu antecessor é {}.'.format(numero, sucessor, antecessor))

# EXERCICIO FEITO EM AULA
# n = int(input('Digite um número: '))
# print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}.'.format(n, (n-1), (n+1)))

# ANOTAÇÕES
# - Quanto menos variáveis forem utilizadas, mais memória será economizada no dispositivo.