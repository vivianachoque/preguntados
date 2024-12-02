import pygame
from Constantes import * 
from Funciones import *
from Puntuaciones import *

pygame.init()

ruta_fondo = "./assets/imagenes/terminado.jpg"
imagen_fondo = pygame.image.load(ruta_fondo)
imagen_fondo = pygame.transform.scale(imagen_fondo, (500, 500))

boton_volver = {}
boton_volver["rectangulo"] = pygame.Rect(40, 25, 70, 40)

caja_usuario = {}
caja_usuario["rectangulo"] = pygame.Rect(237, 47, 132, 245)

boton_enviar_usuario = {}
boton_enviar_usuario["rectangulo"] = pygame.Rect(222,315, 55,20)

texto_usuario = "Ingrese su nombre"
fuente_texto_usuario = pygame.font.Font(None, 32)

input_activado = False

ranking = []

def mostrar_terminado(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict):
    global texto_usuario
    global input_activado

    retorno = "terminado"

    pygame.display.set_caption("GAME-OVER")

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"

        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
                print("VUELVE AL MENU")
                
            if caja_usuario["rectangulo"].collidepoint(mouse_pos):
                input_activado = True
                if texto_usuario == "Ingrese su nombre":
                    texto_usuario = ""
            else:
                input_activado = False

            if boton_enviar_usuario["rectangulo"].collidepoint(evento.pos):
                ranking = leer_json()
                nuevo_jugador = {"nombre": texto_usuario,"puntuacion": datos_juego["puntuacion"]}
                ranking.append(nuevo_jugador)
                guardar_ranking(ranking)
                print("Se guardo el jugador")
                mostrar_texto(pantalla,f"Puntuacion guardada",(170,360),FUENTE_20,COLOR_NEGRO) 
            else:
                print("No se guardo el jugador")
                
                
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                texto_usuario = texto_usuario[0:-1]
            elif len(texto_usuario) < 17:
                texto_usuario += evento.unicode

    pantalla.blit(imagen_fondo, (0, 0)) 

    mostrar_texto(pantalla,f"Su puntuacion fue de: {datos_juego["puntuacion"]} puntos",(125,152),FUENTE_22,COLOR_NEGRO)

    superficie_texto_usuario = fuente_texto_usuario.render(texto_usuario,True, COLOR_NEGRO)
    pantalla.blit(superficie_texto_usuario, (150,260))

    #Comentado porque esta la imagen de fondo 
    # if input_activado == True:
    #     caja_usuario["rectangulo"].fill(COLOR_NEGRO)
    # else:
    #     caja_usuario["rectangulo"].fill(COLOR_VIOLETA)

    """ for event in pygame.event.get():
        # Usar event.unicode correctamente
        if event.type == pygame.KEYDOWN:
            print(f"Tecla presionada: {sd}") """


    return retorno
