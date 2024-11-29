import pygame
from Constantes import *
from Funciones import *

pygame.init()
pygame.mixer.init()

ruta_fondo = "./assets/imagenes/ajustes.jpg"
imagen_fondo = pygame.image.load(ruta_fondo)
imagen_fondo = pygame.transform.scale(imagen_fondo, (500, 500))

boton_suma = {}
boton_suma_musica = {}
boton_suma["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_suma["rectangulo"] = boton_suma["superficie"].get_rect()
boton_suma_musica["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_suma_musica["rectangulo"] = boton_suma_musica["superficie"].get_rect()
# boton_suma["superficie"].fill((0,0,0,0))


boton_resta = {}
boton_resta_musica = {}
boton_resta["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_resta["rectangulo"] = boton_resta["superficie"].get_rect()
boton_resta_musica["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_resta_musica["rectangulo"] = boton_resta_musica["superficie"].get_rect()
# boton_resta["superficie"].fill(COLOR_ROJO)

boton_silenciar = {}
boton_silenciar["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_silenciar["rectangulo"] = boton_silenciar["superficie"].get_rect()

boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
# boton_volver["superficie"].fill(COLOR_AZUL)


screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Mostrar clic del mouse")


def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "configuracion"
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:            
            if boton_suma_musica["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                if datos_juego["volumen_musica"] < 100:
                    cambiar_volumen_musica(subir=True)
                    datos_juego["volumen_musica"] += 10
            elif boton_resta_musica["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                if datos_juego["volumen_musica"] > 0:
                    cambiar_volumen_musica(subir=False)
                    datos_juego["volumen_musica"] -= 10
            elif boton_silenciar["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                if datos_juego["volumen_musica"] > 0:
                    pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(0.0)                     
                    datos_juego["volumen_musica"] = 0
                    print("SILENCIA VOLUMEN MUSICA")
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
                print("VUELVE AL MENU")
    
    pantalla.blit(imagen_fondo, (0, 0))
    
    # boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(360,205)) #volumen general
    # boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(410,205))  #volumen general 
    
    boton_resta_musica["rectangulo"] = pantalla.blit(boton_resta_musica["superficie"],(360,142)) #musica
    boton_suma_musica["rectangulo"] = pantalla.blit(boton_suma_musica["superficie"],(410,142))  #musica
    boton_silenciar["rectangulo"] = pantalla.blit(boton_silenciar["superficie"],(310,142))

    
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(40,25))
    
    mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]} %",(140,142),FUENTE_27,COLOR_NEGRO) #volumen musica

    # mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]} %",(240,202),FUENTE_27,COLOR_NEGRO) #volumen general
    
    return retorno