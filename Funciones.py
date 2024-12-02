from Constantes import *
import random
import pygame

pygame.mixer.init()


def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
    
    
        
# Volumen musica y sonidos        
def cambiar_volumen_musica(subir=True):
    volumen_actual = pygame.mixer.music.get_volume()
    if subir:
        nuevo_volumen = min(1.0,volumen_actual +0.1)
    else:
        nuevo_volumen = max(0.0, volumen_actual - 0.1)
        
    pygame.mixer.music.set_volume(nuevo_volumen)
    

    
def cambiar_volumen_silencio(silencio=True):
    volumen_actual = pygame.mixer.music.get_volume()
    if silencio:
        nuevo_volumen = max(0.0, volumen_actual - 0.0)
    
    pygame.mixer.music.set_volume(nuevo_volumen)
    
