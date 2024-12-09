# Exercício 035
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Desigualdade triângular
# - A soma de dois lados deve ser maior que a medida do terceiro
# - Não é necessário fazer as três somas para verificar a possibilidade de um triângulo existir. Basta fazer a soma entre os dois lados menores. "

# Passo 1: Entre com o valor do primeiro lado
reta1 = float(input('Digite o valor da 1º reta: '))

# Passo 2: Entre com o valor do segundo lado
reta2 = float(input('Digite o valor da 2º reta: '))

# Passo 3: Entre com o valor do terceiro lado
reta3 = float(input('Digite o valor da 3º reta: '))

medida1 = reta1 + reta2
medida2 = reta2 + reta3
medida3 = reta1 + reta3

if medida1 > reta3 and medida2 > reta1 and medida3 > reta2:
  print('A 1ª reta mede: {:.0f} \nA 2º reta mede: {:.0f} \nA 3º reta mede: {:.0f} \nÉ possível formar um triângulo.'.format(reta1, reta2, reta3))
else:
  print('A 1ª reta mede: {:.0f} \nA 2º reta mede: {:.0f} \nA 3º reta mede: {:.0f} \nNÃO é possível formar um triângulo.'.format(reta1, reta2, reta3))
