# Exercício 034
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais o aumento é de 15%.

# Passo 1: Entre com o valor do salário
salario = float(input('Digite o valor do salário: R$ '))

# Passo 2: Calcular aumento de 10% para salários acima de 1.250,00
aumento = (salario / 100) * 10

# Passo 3: Calcular aumento de 15% para salários abaixo de 1.250,00
if salario < 1250:
  aumento = (salario / 100) * 15

novo_salario = salario + aumento  

print('O salário atual é de R$ {:.2f} e receberá um aumento de R$ {:.2f}, e o novo salário será de R$ {:.2f}.'.format(salario, aumento, novo_salario))

# EXERCÍCIO FEITO EM AULA
'''salário = float(input('Qual é o salário do funcionário? R$ '))
if salário <= 1250:
  novo = salário + (salário * 15 / 100)
else:
  novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))'''