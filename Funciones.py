from Constantes import *
import random
import pygame

pygame.mixer.init()

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height

def cambiar_volumen_musica(subir=True):
    volumen_actual = pygame.mixer.music.get_volume()
    if subir:
        nuevo_volumen = min(1.0, volumen_actual + 0.1)
    else:
        nuevo_volumen = max(0.0, volumen_actual - 0.1)
        
    pygame.mixer.music.set_volume(nuevo_volumen)

def cambiar_volumen_silencio(silencio=True):
    volumen_actual = pygame.mixer.music.get_volume()
    if silencio:
        nuevo_volumen = max(0.0, volumen_actual - 0.0)
    
    pygame.mixer.music.set_volume(nuevo_volumen)

def crear_superficie_redondeada(width, height, radius, color):
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    rect = pygame.Rect(0, 0, width, height)
    pygame.draw.rect(surface, color, rect, border_radius=radius)
    return surface

def dibujar_elementos_juego(pantalla, imagen_fondo, cuadro_pregunta, lista_respuestas, pregunta_actual, datos_juego, pos_mouse):
    pantalla.blit(imagen_fondo, (0, 0))
    cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"], (65, 70))

    # Respuestas con hover y sombras
    posiciones_respuestas = [(125, 183), (125, 253), (125, 323), (125, 393)]
    for i, pos in enumerate(posiciones_respuestas):
        # Crear sombra
        sombra = crear_superficie_redondeada(TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1], 12, COLOR_SOMBRA)
        pantalla.blit(sombra, (pos[0] + 2, pos[1] + 2))
        
        boton_rect = pygame.Rect(pos[0], pos[1], TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1])
        superficie_actual = None
        
        if boton_rect.collidepoint(pos_mouse):
            superficie_actual = crear_superficie_redondeada(TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1], 12, COLOR_BOTON_HOVER)
        else:
            superficie_actual = lista_respuestas[i]["superficie"]
            
        # Agregar el texto a la superficie antes de hacer hover
        mostrar_texto(superficie_actual, f"{pregunta_actual[f'respuesta_{i+1}']}", (20, 20), FUENTE_22, COLOR_BLANCO)
        lista_respuestas[i]["rectangulo"] = pantalla.blit(superficie_actual, pos)

    # Mostrar texto de pregunta
    mostrar_texto(cuadro_pregunta["superficie"], f"{pregunta_actual['pregunta']}", (20, 20), FUENTE_22, COLOR_BLANCO)

    # Mostrar puntuación y vidas
    mostrar_texto(pantalla, f"PUNTUACION: {datos_juego['puntuacion']}", (350, 10), FUENTE_18, COLOR_NEGRO)
    mostrar_texto(pantalla, f"VIDAS: {datos_juego['cantidad_vidas']}", (350, 40), FUENTE_18, COLOR_NEGRO)
