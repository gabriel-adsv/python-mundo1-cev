# Exercício 006 - Dobro, Triplo e Raiz Quadrada
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número: '))

print('O dobro de {} é: {}'.format(numero, (numero * 2)))
print('O triplo de {} é: {}'.format(numero, (numero * 3)))
print('E a raiz quadrada é: {:.0f}'.format(pow(numero, (1/2))))

# EXERCICIO FEITO EM AULA
# n = int(input('Digite um número: '))
# d = n * 2
# t = n * 3
# r = n ** (1/2)
# print('O dobro de {} vale {}.'.format(n, d))
# print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
