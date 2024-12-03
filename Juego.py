import pygame
import random
from Comodines import *
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

# Configuracion de los botones de los comodines

comodin_x2 = {}
comodin_x2["rectangulo"] = pygame.Rect(432,262,35,35)

bomba = {}
bomba["rectangulo"] = pygame.Rect(432,225,35,35)

doble_chance = {}
doble_chance["rectangulo"] = pygame.Rect(432,314,35,35)

siguiente_pregunta = {}
siguiente_pregunta["rectangulo"] = pygame.Rect(432,380,35,35)

# Configuración del contador de tiempo
contador_timer = 25
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

# Seteo de contador para ganar una vida tras 5 rondas seguidas ganadas
contador_rondas_seguidas_ganadas = 0

# Seteo en False las banderas de los comodines
bandera_comodin_x2 = False # Esta bandera corresponde a cuando el comodin se pone en True una ronda y luego vuelve a setearse en False.
bandera_por_partida_comodin_x2 = False # Esta bandera corresponde a cuando el comodin se pone en True y queda asi toda la partida.

bandera_por_partida_comodin_pasar_pregunta = False

# Función principal para mostrar el juego
def mostrar_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    global indice, bandera_respuesta, contador_timer, bandera_por_partida_comodin_x2, bandera_comodin_x2,bandera_por_partida_comodin_pasar_pregunta, contador_rondas_seguidas_ganadas

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
                contador_timer = 25
                contador_rondas_seguidas_ganadas = 0
                if bandera_comodin_x2 == True:
                    bandera_comodin_x2 = False
                bandera_respuesta = True

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"

            elif comodin_x2["rectangulo"].collidepoint(evento.pos):
                if bandera_por_partida_comodin_x2 == False:
                    bandera_comodin_x2 = True
                    bandera_por_partida_comodin_x2 = True
                print("SOY EL COMODIN X2, ME ESTAS CLICKEANDO")

            elif siguiente_pregunta["rectangulo"].collidepoint(evento.pos):
                print("SOY EL COMODIN PASAR PREGUNTA, ME ESTAS CLICKEANDO")
                if bandera_por_partida_comodin_pasar_pregunta == False:
                    indice += 1
                    if indice == len(lista_preguntas):
                        indice = 0
                        random.shuffle(lista_preguntas)
                    contador_timer = 25
                    bandera_por_partida_comodin_pasar_pregunta = True
                    bandera_respuesta = True

            for i in range(len(lista_respuestas)):
                if lista_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = i + 1
                    if respuesta_seleccionada == pregunta_actual["respuesta_correcta"]:
                        ACIERTO_SONIDO.play()
                        lista_respuestas[i]["superficie"] = crear_superficie_redondeada(TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1], 12, COLOR_VERDE)
                        contador_rondas_seguidas_ganadas += 1
    
                        if contador_rondas_seguidas_ganadas == 5:
                            datos_juego["cantidad_vidas"] += 1
                            contador_rondas_seguidas_ganadas = 0
                            print(f"GANASTE UNA VIDA")

                        print(f"contador rondas ganadas: {contador_rondas_seguidas_ganadas}")
                        if bandera_comodin_x2 == False:
                            datos_juego["puntuacion"] += PUNTUACION_ACIERTO
                        else:
                            datos_juego["puntuacion"] += multiplicar_puntos_por_dos()
                            bandera_comodin_x2 = False

                    else:
                        ERROR_SONIDO.play()
                        contador_rondas_seguidas_ganadas = 0
                        lista_respuestas[i]["superficie"] = crear_superficie_redondeada(TAMAÑO_RESPUESTA[0], TAMAÑO_RESPUESTA[1], 12, COLOR_ROJO)
                        if datos_juego["cantidad_vidas"] == 1:
                            GAME_OVER_SONIDO.play()
                            retorno = "terminado"
                        elif datos_juego["puntuacion"] > 0:
                            datos_juego["puntuacion"] -= PUNTUACION_ERROR
                        datos_juego["cantidad_vidas"] -= 1
                        
                        if bandera_comodin_x2 == True:
                            bandera_comodin_x2 = False
                    indice += 1
                    if indice == len(lista_preguntas):
                        indice = 0
                        random.shuffle(lista_preguntas)
                    contador_timer = 25
                    bandera_respuesta = True

    # Dibujar elementos en la pantalla
    dibujar_elementos_juego(pantalla, imagen_fondo, cuadro_pregunta, lista_respuestas, pregunta_actual, datos_juego, pos_mouse)
    
    # Dibujar timer después de los otros elementos
    pantalla.blit(timer, (220, 20))

    return retorno