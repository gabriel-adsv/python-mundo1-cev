# Exercício 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$'))
porcentagem = float(input('Quantos % de aumento o funcionário irá receber? '))

aumento = (salario * porcentagem) / 100
novoSalario = salario + aumento

print('Um funcionário que ganha R${:.2f}, com {:.0f}% de aumento, passa a receber R${:.2f}.'.format(salario, porcentagem, novoSalario))

# EXERCICIO FEITO EM AULA
# salario = float(input('Qual é o salário do Funcionário? R$'))
# novo = salario + (salario * 15 / 100)
# print('Um funcionário que ganha R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario, novo))