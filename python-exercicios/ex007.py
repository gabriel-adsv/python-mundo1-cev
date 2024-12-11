# Exercício 007 - Média Aritmética
# Desenvolva um programa que leia as duas notas de um aluno, e leia e mostre a sua média.

cores = {
  'vermelho':'\033[1;31m',
  'verde':'\033[1;32m',
  'amarelo':'\033[1;33m',
  'sem_cor':'\033[m'
}

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))

media = (n1 + n2) / 2

print('A média entre {}{:.1f}{} e {}{:.1f}{} é igual a {:.1f}'.format(cores['amarelo'], n1, cores['sem_cor'], cores['amarelo'], n2, cores['sem_cor'], media))

if media >= 7.5:
  print('Parabéns, você está {}APROVADO!{}'.format(cores['verde'], cores['sem_cor']))
else:
  print('Você está {}REPROVADO{}, estude mais!'.format(cores['vermelho'], cores['sem_cor']))
