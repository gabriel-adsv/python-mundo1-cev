# Exercício 021
# Faça um programa em Python que abra e reproduza um áudio de um arquivo MP3.
import pygame
import time

pygame.mixer.init()

audio = "ex021.mp3"
pygame.mixer.music.load(audio)

pygame.mixer.music.play()
print('Reproduzindo áudio...')

while pygame.mixer.music.get_busy():
    time.sleep(1)

print('Fim da reprodução!')

# EXERCÍCIO FEITO EM AULA
# import pygame
# pygame.init()
# pygame.mixer.music.load('ex021.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()