import pygame
import random
import csv
from Funciones import *
from Constantes import *

# Inicialización de Pygame
pygame.init()

# Cargar preguntas desde un archivo CSV
with open('preguntas.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    lista_preguntas = list(reader)

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

# Función para crear superficies redondeadas
def crear_superficie_redondeada(width, height, radius, color):
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    rect = pygame.Rect(0, 0, width, height)
    pygame.draw.rect(surface, color, rect, border_radius=radius)
    return surface

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
    pantalla.blit(imagen_fondo, (0, 0))
    pantalla.blit(timer, (220, 20))
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
            
        # Agregar el texto a la superficie antes de hacer hoveR
        mostrar_texto(superficie_actual, f"{pregunta_actual[f'respuesta_{i+1}']}", (20, 20), FUENTE_22, COLOR_BLANCO)
        lista_respuestas[i]["rectangulo"] = pantalla.blit(superficie_actual, pos)

    # Mostrar texto de pregunta
    mostrar_texto(cuadro_pregunta["superficie"], f"{pregunta_actual['pregunta']}", (20, 20), FUENTE_22, COLOR_BLANCO)

    # Mostrar puntuación y vidas
    mostrar_texto(pantalla, f"PUNTUACION: {datos_juego['puntuacion']}", (350, 10), FUENTE_18, COLOR_NEGRO)
    mostrar_texto(pantalla, f"VIDAS: {datos_juego['cantidad_vidas']}", (350, 40), FUENTE_18, COLOR_NEGRO)

    return retorno
