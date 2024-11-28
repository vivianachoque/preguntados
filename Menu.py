import pygame 
from Constantes import *
from Funciones import *

pygame.init()

ruta_fondo = "./assets/imagenes/menu.jpg"
imagen_fondo = pygame.image.load(ruta_fondo)
imagen_fondo = pygame.transform.scale(imagen_fondo, (500, 500))

COLOR_BOTON = (70, 130, 180)  
COLOR_BOTON_HOVER = (100, 149, 237)
COLOR_TEXTO = (255, 255, 255)
COLOR_SOMBRA = (50, 100, 150)

lista_botones = []

def crear_boton_redondeado(width, height, radius):
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    rect = pygame.Rect(0, 0, width, height)
    pygame.draw.rect(surface, COLOR_BOTON, rect, border_radius=radius)
    return surface

for i in range(4):
    boton = {}
    boton["superficie"] = crear_boton_redondeado(250, 45, 12)
    boton["rectangulo"] = boton["superficie"].get_rect()
    boton["hover"] = False
    lista_botones.append(boton)

def mostrar_menu(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]) -> str:
    retorno = "menu"
    pygame.display.set_caption("MENU")
    
    pos_mouse = pygame.mouse.get_pos()

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if lista_botones[BOTON_JUGAR]["rectangulo"].collidepoint(evento.pos):
                retorno = "juego"
                CLICK_SONIDO.play()
            elif lista_botones[BOTON_AJUSTES]["rectangulo"].collidepoint(evento.pos):
                retorno = "configuracion"
                CLICK_SONIDO.play()
            elif lista_botones[BOTON_RANKINGS]["rectangulo"].collidepoint(evento.pos):
                retorno = "puntuaciones"
                CLICK_SONIDO.play()
            elif lista_botones[BOTON_SALIR]["rectangulo"].collidepoint(evento.pos):
                retorno = "salir"
                CLICK_SONIDO.play()

    pantalla.blit(imagen_fondo, (0, 0))

    posiciones_botones = [(125, 165), (125, 235), (125, 305), (125, 375)]
    textos_botones = ["JUGAR", "AJUSTES", "RANKINGS", "SALIR"]
    
    for i, (pos, texto) in enumerate(zip(posiciones_botones, textos_botones)):
        sombra = crear_boton_redondeado(250, 45, 12)
        pygame.draw.rect(sombra, COLOR_SOMBRA, sombra.get_rect(), border_radius=12)
        pantalla.blit(sombra, (pos[0] + 2, pos[1] + 2))

        boton_rect = pygame.Rect(pos[0], pos[1], 250, 45)
        if boton_rect.collidepoint(pos_mouse):
            superficie_hover = crear_boton_redondeado(250, 45, 12)
            pygame.draw.rect(superficie_hover, COLOR_BOTON_HOVER, superficie_hover.get_rect(), border_radius=12)
            lista_botones[i]["rectangulo"] = pantalla.blit(superficie_hover, pos)
        else:
            lista_botones[i]["rectangulo"] = pantalla.blit(lista_botones[i]["superficie"], pos)

        texto_surface = FUENTE_30.render(texto, True, COLOR_TEXTO)
        texto_rect = texto_surface.get_rect(center=(pos[0] + 125, pos[1] + 22))
        pantalla.blit(texto_surface, texto_rect)

    return retorno