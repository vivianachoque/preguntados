import pygame 
import random
from Funciones import * 
from Preguntas import *  

pygame.init()

# Ruta de la imagen de fondo
ruta_fondo = "./assets/imagenes/preguntas.jpg"
imagen_fondo = pygame.image.load(ruta_fondo)
imagen_fondo = pygame.transform.scale(imagen_fondo, (500, 500)) 

# Configuración de preguntas y respuestas
cuadro_pregunta = {}
cuadro_pregunta["superficie"] = pygame.Surface(TAMAÑO_PREGUNTA)
cuadro_pregunta["rectangulo"] = cuadro_pregunta["superficie"].get_rect()
cuadro_pregunta["superficie"].fill(COLOR_ROJO)

lista_respuestas = []

for i in range(3):
    cuadro_respuesta = {}
    cuadro_respuesta["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
    cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
    cuadro_respuesta["superficie"].fill(COLOR_AZUL)
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
        cuadro_pregunta["superficie"].fill(COLOR_ROJO)
        for i in range(len(lista_respuestas)):
            lista_respuestas[i]["superficie"].fill(COLOR_AZUL)
        bandera_respuesta = False
    
    pregunta_actual = lista_preguntas[indice]
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_respuestas)):
                if lista_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = (i + 1)
                    
                    if respuesta_seleccionada == pregunta_actual["respuesta_correcta"]:
                        ACIERTO_SONIDO.play()
                        print("RESPUESTA CORRECTA")
                        lista_respuestas[i]["superficie"].fill(COLOR_VERDE_OSCURO)
                        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
                    else:
                        ERROR_SONIDO.play()
                        lista_respuestas[i]["superficie"].fill(COLOR_ROJO)
                        if datos_juego["puntuacion"] > 0:
                            datos_juego["puntuacion"] -= PUNTUACION_ERROR
                        datos_juego["cantidad_vidas"] -= 1
                        print("RESPUESTA INCORRECTA")
                    indice += 1
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        random.shuffle(lista_preguntas)
                        
                    bandera_respuesta = True

    # Dibuja la imagen de fondo
    pantalla.blit(imagen_fondo, (0, 0)) 

    # Renderizado de preguntas y respuestas
    mostrar_texto(cuadro_pregunta["superficie"], f"{pregunta_actual['pregunta']}", (20, 20), FUENTE_27, COLOR_NEGRO)
    mostrar_texto(lista_respuestas[0]["superficie"], f"{pregunta_actual['respuesta_1']}", (20, 20), FUENTE_22, COLOR_BLANCO)
    mostrar_texto(lista_respuestas[1]["superficie"], f"{pregunta_actual['respuesta_2']}", (20, 20), FUENTE_22, COLOR_BLANCO)
    mostrar_texto(lista_respuestas[2]["superficie"], f"{pregunta_actual['respuesta_3']}", (20, 20), FUENTE_22, COLOR_BLANCO)
    
    cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"], (80, 80))
    lista_respuestas[0]["rectangulo"] = pantalla.blit(lista_respuestas[0]["superficie"], (125, 245))  # Respuesta 1
    lista_respuestas[1]["rectangulo"] = pantalla.blit(lista_respuestas[1]["superficie"], (125, 315))  # Respuesta 2
    lista_respuestas[2]["rectangulo"] = pantalla.blit(lista_respuestas[2]["superficie"], (125, 385))  # Respuesta 3

    # Dibuja bordes
    pygame.draw.rect(pantalla, COLOR_NEGRO, cuadro_pregunta["rectangulo"], 2)
    pygame.draw.rect(pantalla, COLOR_BLANCO, lista_respuestas[0]["rectangulo"], 2)
    pygame.draw.rect(pantalla, COLOR_BLANCO, lista_respuestas[1]["rectangulo"], 2)
    pygame.draw.rect(pantalla, COLOR_BLANCO, lista_respuestas[2]["rectangulo"], 2)

    # Muestra puntuación y vidas
    mostrar_texto(pantalla, f"PUNTUACION: {datos_juego['puntuacion']}", (10, 10), FUENTE_25, COLOR_NEGRO)
    mostrar_texto(pantalla, f"VIDAS: {datos_juego['cantidad_vidas']}", (10, 40), FUENTE_25, COLOR_NEGRO)
    
    return retorno
