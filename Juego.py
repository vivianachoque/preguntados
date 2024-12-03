import pygame
import random
import csv
from Funciones import *
from Constantes import *

# Inicialización de Pygame
pygame.init()

# Cargar preguntas desde un archivo CSV
with open('preguntas.csv', 'r', encoding='utf-8') as file: #esto es para que lea los tildes y ñ
    reader = csv.DictReader(file) #esto es para que lea el archivo como un diccionario
    lista_preguntas = list(reader) #esto es para que lo lea como una lista

# Convertir respuestas correctas a enteros
for pregunta in lista_preguntas:
    pregunta['respuesta_correcta'] = int(pregunta['respuesta_correcta'])

# Configuración de imágenes y botones
ruta_fondo = "./assets/imagenes/preguntas.jpg"
imagen_fondo = pygame.image.load(ruta_fondo)
imagen_fondo = pygame.transform.scale(imagen_fondo, (500, 500))

boton_volver = {"rectangulo": pygame.Rect(40, 25, 70, 40)}

# Configuración del contador de tiempo
contador_timer = 15
fuente = pygame.font.Font(None, 50)
timer = fuente.render(str(contador_timer), True, COLOR_NEGRO)
evento_timer = pygame.USEREVENT + 1
timer_milisegundos = 1000
pygame.time.set_timer(evento_timer, timer_milisegundos)

# Configuración de cuadros de pregunta y respuesta
cuadro_pregunta = {
    "superficie": crear_superficie_redondeada(TAMAÑO_PREGUNTA[0], TAMAÑO_PREGUNTA[1], 15, COLOR_NEGRO),
    "rectangulo": None
}

lista_respuestas = []
for i in range(4):
    cuadro_respuesta = {
        "superficie": crear_superficie_redondeada(TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1], 12, COLOR_RESPUESTA),
        "rectangulo": None,
        "hover": False
    }
    lista_respuestas.append(cuadro_respuesta)

# Variables de estado del juego
indice = 0
bandera_respuesta = False
random.shuffle(lista_preguntas)

# Función principal para mostrar el juego
def mostrar_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    global indice, bandera_respuesta, contador_timer

    # Renderizar el timer constantemente
    timer = fuente.render(str(contador_timer), True, COLOR_NEGRO)
    retorno = "juego"

    if bandera_respuesta:
        pygame.time.delay(250)
        cuadro_pregunta["superficie"] = crear_superficie_redondeada(TAMAÑO_PREGUNTA[0], TAMAÑO_PREGUNTA[1], 15, COLOR_NEGRO)
        for i in range(len(lista_respuestas)):
            lista_respuestas[i]["superficie"] = crear_superficie_redondeada(TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1], 12, COLOR_RESPUESTA)
        bandera_respuesta = False

    pregunta_actual = lista_preguntas[indice]
    pos_mouse = pygame.mouse.get_pos()

    # Manejo de eventos
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == evento_timer:
            if contador_timer > 0:
                contador_timer -= 1
            else:
                if datos_juego["cantidad_vidas"] == 1:
                    GAME_OVER_SONIDO.play()
                    retorno = "terminado"
                ERROR_SONIDO.play()
                datos_juego["cantidad_vidas"] -= 1
                indice += 1
                if indice == len(lista_preguntas):
                    indice = 0
                    random.shuffle(lista_preguntas)
                contador_timer = 16
                bandera_respuesta = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
                print("VUELVE AL MENU")
            for i in range(len(lista_respuestas)):
                if lista_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = i + 1
                    if respuesta_seleccionada == pregunta_actual["respuesta_correcta"]:
                        ACIERTO_SONIDO.play()
                        lista_respuestas[i]["superficie"] = crear_superficie_redondeada(TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1], 12, COLOR_VERDE)
                        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
                    else:
                        ERROR_SONIDO.play()
                        lista_respuestas[i]["superficie"] = crear_superficie_redondeada(TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1], 12, COLOR_ROJO)
                        if datos_juego["cantidad_vidas"] == 1:
                            GAME_OVER_SONIDO.play()
                            retorno = "terminado"
                        elif datos_juego["puntuacion"] > 0:
                            datos_juego["puntuacion"] -= PUNTUACION_ERROR
                        datos_juego["cantidad_vidas"] -= 1
                    indice += 1
                    if indice == len(lista_preguntas):
                        indice = 0
                        random.shuffle(lista_preguntas)
                    bandera_respuesta = True

    # Dibujar elementos en la pantalla
    dibujar_elementos_juego(pantalla, imagen_fondo, cuadro_pregunta, lista_respuestas, pregunta_actual, datos_juego, pos_mouse)
    
    # Dibujar timer después de los otros elementos
    pantalla.blit(timer, (220, 20))

    return retorno
