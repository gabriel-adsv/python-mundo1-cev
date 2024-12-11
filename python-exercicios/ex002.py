# Exercício 002 - Respondendo ao Usuário
# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

cor_letra = '\033[0;32m'
sem_cor= '\033[m'
nome = input('\033[0;31mDigite o seu nome:\033[m ')
msg = 'Olá {}{}{}, seja muito bem-vindo(a)!'.format(cor_letra, nome, sem_cor)

print(msg)
