# Aula 09 - Manipulando Texto

frase = 'Curso em Vídeo Python'
print(frase)

# Fatiando
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15])
print(frase[1:15:2])
print(frase[::2])

# Análise
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(frase.replace('Python', 'Android'))

# Transformação
# OBS: Uma string e seus microelementos são imutáveis, até que se use uma função de transformação de string e faça uma atribuição:
frase = frase.replace('Python', 'Android')
print(frase)
print('Curso' in frase)
print(frase.lower().find('vídeo'))
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])

# Técnica das três aspas
print("""
  Welcome! Are you completely new to programming?
	about why and how to get started with Python. Fortunately
  an experienced programmer in any programming language
  (whatever it may be) can pick up Python very quickly.
  Its also easy for beginners to use and learn, so jump in!
""")