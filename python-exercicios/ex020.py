# Exercício 020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import sample

primeiro = str(input('Digite o nome do primeiro aluno: '))
segundo = str(input('Digite o nome do segundo aluno: '))
terceiro = str(input('Digite o nome do terceiro aluno: '))
quarto = str(input('Digite o nome do quarto aluno: '))

alunos = [primeiro, segundo, terceiro, quarto]
sorteio = sample(alunos, len(alunos))

print('A ordem sorteada foi: {}'.format(sorteio))

# EXERCÍCIO FEITO EM AULA
# from random import shuffle
# n1 = str(input('Primeiro aluno: '))
# n2 = str(input('Segundo aluno: '))
# n3 = str(input('Terceiro aluno: '))
# n4 = str(input('Quarto aluno: '))
# lista = [n1, n2, n3, n4]
# shuffle(lista)
# print('A ordem de apresentação será:')
# print(lista)
