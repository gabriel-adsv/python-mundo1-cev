# Exercício 033
# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.

# Passo 1: Entre com o valor dos números
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

maior = 0
menor = 0

if n1 > maior:
  maior = n1
else:
  maior = maior

if n2 > maior:
  maior = n2
else:
  maior = maior

if n3 > maior:
  maior = n3
else:
  maior = maior

if n1 < menor:
  menor = menor
else:
  menor = n1

if menor < n2:
  menor = menor
else:
  menor = n2

if menor < n3:
  menor = menor
else:
  menor = n3

print('O maior número digitado foi: {}. E o menor número digitado foi: {}'.format(maior, menor))

# EXERCÍCIO FEITO EM AULA
'''a = int(input('Primeior valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é menor
menor = a
if b < a and b < c:
  menor = b
if c < a and c < b:
  menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
  maior = b
if c > a and c > b:
  maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))'''
