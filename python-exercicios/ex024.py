# Exercício 024
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: '))

if 'Santo' in cidade or 'SANTO' in cidade:
  print('O nome da cidade {} começa com "SANTO".'.format(cidade))
else:
  print('O nome da cidade {} não começa com "SANTO".'.format(cidade))

# EXERCÍCIO FEITO EM AULA
# cid = str(input('Em que cidade você nasceu? ')).strip()
# print(cid[:5].upper() == 'SANTO')