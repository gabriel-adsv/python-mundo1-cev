# Exercício 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Uma distância em metros: '))

decametro = metro / 10
hectometro = metro / 100
quilometro = metro / 1000
decimetro = metro * 10
centimetro = metro * 100
milimetro = metro * 1000


print('A medida de {}m corresponde a: \n{:.4f}dam \n{:.2f}hm \n{:.2f}km \n{:.2f}dm \n{:.2f}cm \n{:.2f}mm'.format(metro, decametro, hectometro, quilometro, decimetro, centimetro, milimetro))

# EXERCICIO FEITO EM AULA
# medida = float(input('Uma distância em metros: '))

# cm = medida * 100
# mm = medida * 1000
# print('A medida de {}m corresponde a: \n{:.0f}cm \n{:.0f}mm'.format(medida, cm, mm))
