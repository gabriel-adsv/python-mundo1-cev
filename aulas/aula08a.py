# Aula 08 - Utilizando módulos

# import math
from math import sqrt, ceil, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# Arredondando a raiz para cima com ceil
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))

# Arredondando a raiz para baixo com floor
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

# import random
# num = random.random()
# print(num)

# import emoji
# print(emoji.emojize('Olá, Mundo :earth_americas:', use_aliases=True))
