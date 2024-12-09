# Exercício 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma ára de 2m².

largura = float(input('Largura da parede: ')) 
altura = float(input('Altura da parede: '))

area = largura * altura
quantidade = area / 2

print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.0f} latas de tinta.'.format(quantidade))

# EXERCÍCIO FEITO EM AULA
# larg = float(input('Largura da parede: '))
# alt = float(input('Altura da parede: '))
# área = larg * alt
# print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área))
# tinta = área / 2
# print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
