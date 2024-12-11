# Exercício 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

cor = {
  'negativo':'\033[7m',
  'verde':'\033[32m',
  'amarelo':'\033[33m',
  'azul':'\033[34m',
  'magenta':'\033[35m',
  'ciano':'\033[36m',
  'cinza':'\033[37m',
  'sem_cor':'\033[m'
}

metro = float(input('Uma distância em metros: '))

decametro = metro / 10
hectometro = metro / 100
quilometro = metro / 1000
decimetro = metro * 10
centimetro = metro * 100
milimetro = metro * 1000


print('A medida de {} {}m {} corresponde a: \n{}{:.4f}dam{} \n{}{:.2f}hm{} \n{}{:.2f}km{} \n{}{:.2f}dm{} \n{}{:.2f}cm{} \n{}{:.2f}mm{}'.format(cor['negativo'], metro, cor['sem_cor'], cor['verde'], decametro, cor['sem_cor'], cor['amarelo'],hectometro, cor['sem_cor'], cor['azul'], quilometro, cor['sem_cor'], cor['magenta'],decimetro, cor['sem_cor'], cor['ciano'], centimetro, cor['sem_cor'], cor['cinza'], milimetro, cor['sem_cor']))

# EXERCICIO FEITO EM AULA
'''
  medida = float(input('Uma distância em metros: '))
  cm = medida * 100
  mm = medida * 1000
  print('A medida de {}m corresponde a: \n{:.0f}cm \n{:.0f}mm'.format(medida, cm, mm))
'''
