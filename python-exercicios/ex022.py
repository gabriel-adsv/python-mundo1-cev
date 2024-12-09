# Exercício 022
# Crie um programa que leia o nome completo de uma pessoa e mostre:

nome = str(input('Digite seu nome: '))

# - O nome com todas as letras maiscúlas;
print('Seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))

# - O nome com todas minúsculas;
print('Seu nome com todas as letras minúsculas: {}'.format(nome.lower()))

# - Quantas letras ao todo (sem considerar espaços);
letras = nome.split()
quantidade = ''.join(letras)
print('Seu nome tem {} letras.'.format(len(quantidade)))

# - Quantas letras tem o primeiro nome.
primeiro = nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(primeiro[0])))

# EXERCÍCIO FEITO EM AULA
# nome = str(input('Digite seu nome completo: ')).strip()
# print('Analisando seu nome...')
# print('Seu nome em maiúsculas é {}'.format(nome.upper()))
# print('Seu nome em minúsculas é {}'.format(nome.lower()))
# print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# #print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# separa = nome.split()
# print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))