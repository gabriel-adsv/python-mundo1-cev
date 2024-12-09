# Exercício 027
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#   Ex:
#     Ana Maria de Souza
#     Primeiro: Ana
#     Último: Souza

completo = str(input('Digite o nome completo: ')).strip()
nome = completo.split()
print('O primeiro nome é: {}'.format(nome[0]))
print('O último nome é: {}'.format(nome[-1]))

# EXERCÍCIO FEITO EM AULA
# n = str(input('Digite seu nome completo: ')).strip()
# nome = n.split()
# print('Muito prazer em te conhecer!')
# print('Seu primeiro nome é {}'.format(nome[0]))
# print('Seu último nome é {}'.format(nome[len(nome) - 1]))