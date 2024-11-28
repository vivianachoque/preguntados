import pygame
from Constantes import * 
from Funciones import *

pygame.init()

caja_usuario = {}

caja_usuario["superficie"] = pygame.Surface(RECT_TAM)
caja_usuario["rectangulo"] = caja_usuario["superficie"].get_rect()
caja_usuario["superficie"].fill(COLOR_NEGRO)

texto_usuario = "Ingrese su nombre..."
fuente_texto_usuario = pygame.font.Font(None, 32)

input_activado = False

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
            if caja_usuario["rectangulo"].collidepoint(mouse_pos):
                input_activado = True
                if texto_usuario == "Ingrese su nombre...":
                    texto_usuario = ""
            else:
                input_activado = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                texto_usuario = texto_usuario[0:-1]
            elif len(texto_usuario) < 17:
                texto_usuario += evento.unicode

    pantalla.fill(COLOR_BLANCO)

    caja_usuario["rectangulo"] = pantalla.blit(caja_usuario["superficie"],RECT_POS)
    mostrar_texto(pantalla,"JUEGO TERMINADO",(135,20),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,f"Su puntuacion fue de: {datos_juego["puntuacion"]} puntos.",(100,100),FUENTE_25,COLOR_NEGRO)
    """ mostrar_texto(caja_usuario["superficie"],texto_usuario,(0,10),FUENTE_22,COLOR_NEGRO) """


    superficie_texto_usuario = fuente_texto_usuario.render(texto_usuario,True, COLOR_BLANCO)
    pantalla.blit(superficie_texto_usuario, (RECT_POS[0] + 15, RECT_POS[1] + 7 ))


    if input_activado == True:
        caja_usuario["superficie"].fill(COLOR_NEGRO)
    else:
        caja_usuario["superficie"].fill(COLOR_VIOLETA)

    """ for event in pygame.event.get():
        # Usar event.unicode correctamente
        if event.type == pygame.KEYDOWN:
            print(f"Tecla presionada: {sd}") """

    return retorno