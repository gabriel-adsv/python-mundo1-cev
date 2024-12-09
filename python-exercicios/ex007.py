# Exercício 007 - Média Aritmética
# Desenvolva um programa que leia as duas notas de um aluno, e leia e mostre a sua média.

n1 = input('Digite a 1ª nota: ')
n2 = input('Digite a 2ª nota: ')

media = (float(n1) + float(n2)) / 2

print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, media))
