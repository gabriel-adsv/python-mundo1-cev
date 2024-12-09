# Aula 10 - Condições simples e compostas

# IMPORTANTE
# TODO comando que estiver colado do lado esquerdo da tela, será executado sempre
# TODO comando que estiver aninhado, pode ser executado ou não

nome = str(input('Qual é seu nome: '))

if nome == 'Gabriel':
  print('Que nome lindo você tem!')
else:
  print('Seu nome é tão nomral!')
print('Bom dia, {}!'.format(nome))
# if: estrutura condicional simples
# if/else: estrutura condicional composta

# EXEMPLO: VERIFICAÇÃO DE NOTA
n1 = float(input('Digita a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi: {:.1f}'.format(m))
# if m >= 6.0:
#   print('Sua média foi boa! PARABÉNS!')
# else:
#   print('Sua média foi ruim! ESTUDE MAIS!')
print('PARABÉNS' if m >= 6 else 'ESTUDE MAIS!') #Exemplo de condição simplificada