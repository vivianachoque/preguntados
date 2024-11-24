import pygame 
import random
from Funciones import * 
from Preguntas import *  

pygame.init()

ruta_fondo = "./assets/imagenes/preguntas.jpg"
imagen_fondo = pygame.image.load(ruta_fondo)
imagen_fondo = pygame.transform.scale(imagen_fondo, (500, 500)) 

COLOR_PREGUNTA = (134, 23, 219)  
COLOR_RESPUESTA = (70, 130, 180)
COLOR_RESPUESTA_HOVER = (100, 149, 237, 150) #Corregir porque se rompe al hacer hover
COLOR_SOMBRA = (50, 100, 150)

def crear_superficie_redondeada(width, height, radius, color):
    surface = pygame.Surface((width, height), pygame.SRCALPHA) 
    rect = pygame.Rect(0, 0, width, height)
    pygame.draw.rect(surface, color, rect, border_radius=radius)
    return surface

cuadro_pregunta = {}
cuadro_pregunta["superficie"] = crear_superficie_redondeada(TAMAÑO_PREGUNTA[0], TAMAÑO_PREGUNTA[1], 15, COLOR_PREGUNTA)
cuadro_pregunta["rectangulo"] = cuadro_pregunta["superficie"].get_rect()

lista_respuestas = []

for i in range(3):
    cuadro_respuesta = {}
    cuadro_respuesta["superficie"] = crear_superficie_redondeada(TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1], 12, COLOR_RESPUESTA)
    cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
    cuadro_respuesta["hover"] = False
    lista_respuestas.append(cuadro_respuesta)
    
indice = 0 
bandera_respuesta = False 
random.shuffle(lista_preguntas)  

def mostrar_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    global indice
    global bandera_respuesta
    
    retorno = "juego"
    if bandera_respuesta:
        pygame.time.delay(250)
        cuadro_pregunta["superficie"] = crear_superficie_redondeada(TAMAÑO_PREGUNTA[0], TAMAÑO_PREGUNTA[1], 15, COLOR_PREGUNTA)
        for i in range(len(lista_respuestas)):
            lista_respuestas[i]["superficie"] = crear_superficie_redondeada(TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1], 12, COLOR_RESPUESTA)
        bandera_respuesta = False
    
    pregunta_actual = lista_preguntas[indice]
    pos_mouse = pygame.mouse.get_pos()
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_respuestas)):
                if lista_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = (i + 1)
                    
                    if respuesta_seleccionada == pregunta_actual["respuesta_correcta"]:
                        ACIERTO_SONIDO.play()
                        lista_respuestas[i]["superficie"] = crear_superficie_redondeada(TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1], 12, COLOR_VERDE)
                        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
                    else:
                        ERROR_SONIDO.play()
                        lista_respuestas[i]["superficie"] = crear_superficie_redondeada(TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1], 12, COLOR_ROJO)
                        if datos_juego["puntuacion"] > 0:
                            datos_juego["puntuacion"] -= PUNTUACION_ERROR
                        datos_juego["cantidad_vidas"] -= 1
                    indice += 1
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        random.shuffle(lista_preguntas)
                        
                    bandera_respuesta = True

    pantalla.blit(imagen_fondo, (0, 0))

    # Sombra y pregunta
    sombra_pregunta = crear_superficie_redondeada(TAMAÑO_PREGUNTA[0], TAMAÑO_PREGUNTA[1], 15, COLOR_SOMBRA)
    pantalla.blit(sombra_pregunta, (82, 82))
    cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"], (80, 80))

    # Respuestas con hover y sombras
    posiciones_respuestas = [(125, 245), (125, 315), (125, 385)]
    
    for i, pos in enumerate(posiciones_respuestas):
        sombra = crear_superficie_redondeada(TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1], 12, COLOR_SOMBRA)
        pantalla.blit(sombra, (pos[0] + 2, pos[1] + 2))

        boton_rect = pygame.Rect(pos[0], pos[1], TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1])
        if boton_rect.collidepoint(pos_mouse):
            superficie_hover = crear_superficie_redondeada(TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1], 12, COLOR_RESPUESTA_HOVER)
            lista_respuestas[i]["rectangulo"] = pantalla.blit(superficie_hover, pos)
        else:
            lista_respuestas[i]["rectangulo"] = pantalla.blit(lista_respuestas[i]["superficie"], pos)

    # Texto
    mostrar_texto(cuadro_pregunta["superficie"], f"{pregunta_actual['pregunta']}", (20, 20), FUENTE_27, COLOR_BLANCO)
    mostrar_texto(lista_respuestas[0]["superficie"], f"{pregunta_actual['respuesta_1']}", (20, 20), FUENTE_22, COLOR_BLANCO)
    mostrar_texto(lista_respuestas[1]["superficie"], f"{pregunta_actual['respuesta_2']}", (20, 20), FUENTE_22, COLOR_BLANCO)
    mostrar_texto(lista_respuestas[2]["superficie"], f"{pregunta_actual['respuesta_3']}", (20, 20), FUENTE_22, COLOR_BLANCO)

    # Puntuación y vidas
    mostrar_texto(pantalla, f"PUNTUACION: {datos_juego['puntuacion']}", (10, 10), FUENTE_25, COLOR_NEGRO)
    mostrar_texto(pantalla, f"VIDAS: {datos_juego['cantidad_vidas']}", (10, 40), FUENTE_25, COLOR_NEGRO)
    
    return retorno
