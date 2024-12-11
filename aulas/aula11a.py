# Aula 11 (Extra) - Cores no terminal

# Padrão ANSI (Escape sequence)
# - Padrão de normalização internacional

# Sempre que uma cor for representada em Python, deve-se iniciar com:
#   \033[style; text; background m
#   \033[0;33;44m

# Código para estilo: 
print('ESTILOS')
# 0 - none
print('Cód: 0 - \033[0mnone')
# 1 - Bold
print('Cód: 1 - \033[1mbold')
# 4 - Underline
print('Cód: 4 - \033[4munderline\033[m')
# 7 - Negative
print('Cód: 7 - \033[7mnegative\033[m')
print(' ')

# Código para cores:
print('CORES')
# 30 - Branco
print('Cód: 30 - \033[0;30mBranco\033[m')  
# 31 - Vermelho
print('Cód: 31 - \033[0;31mVermelho\033[m')  
# 32 - Verde
print('Cód: 32 - \033[0;32mVerde\033[m')  
# 33 - Amarelo
print('Cód: 33 - \033[0;33mAmarelo\033[m')  
# 34 - Azul
print('Cód: 34 - \033[0;34mAzul\033[m')  
# 35 - Magenta
print('Cód: 35 - \033[0;35mMagenta\033[m')
# 36 - Ciano
print('Cód: 36 - \033[0;36mCiano\033[m')
# 37 - Cinza
print('Cód: 37 - \033[0;37mCinza\033[m')
print(' ')

# Código para background
print('BACKGROUNDS')
# 40 - Branco
print('Cód: 40 - \033[0;0;40m Branco \033[m')  
# 41 - Vermelho  
print('Cód: 41 - \033[0;0;41m Vermelho \033[m')  
# 42 - Verde
print('Cód: 42 - \033[0;0;42m Verde \033[m')  
# 43 - Amarelo  
print('Cód: 43 - \033[0;0;43m Amarelo \033[m')  
# 44 - Azul
print('Cód: 44 - \033[0;0;44m Azul \033[m')  
# 45 - Magenta
print('Cód: 45 - \033[0;0;45m Magenta \033[m')  
# 46 - Ciano
print('Cód: 46 - \033[0;0;46m Ciano \033[m')  
# 47 - Cinza
print('Cód: 47 - \033[0;0;47m Cinza \033[m')  

# print('\033[1;31;43mOlá, mundo!\033[m')
# print('\033[4;30;45mOlá, mundo!\033[m')
# print('\033[0;33;44mOlá, mundo!\033[m')

# a = 3
# b = 5
# print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

# nome = 'Gabriel'
# cores = {
#   'limpa':'\033[m', 
#   'azul':'\033[34m', 
#   'amarelo':'\033[33m', 
#   'pretoebranco':'\033[7;30m'
# }
# print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))

background = '\033[0;0;45m'
nobackground = '\033[m'
print('{}Testando a cor magenta{}'.format(background, nobackground))