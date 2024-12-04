import pygame
from Constantes import *
from Funciones import *

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Botón Invisible")

ruta_fondo = "./assets/imagenes/ajustes.jpg"
imagen_fondo = pygame.image.load(ruta_fondo)
imagen_fondo = pygame.transform.scale(imagen_fondo, (500, 500))

boton_suma_musica = {}
boton_suma_musica["rectangulo"] = pygame.Rect(410, 142, 30, 30)


boton_resta_musica = {}
boton_resta_musica["rectangulo"] = pygame.Rect(360, 142, 30, 30)

boton_silenciar = {}
boton_silenciar["rectangulo"] = pygame.Rect(310, 142, 30, 30)

boton_volver = {}
boton_volver["rectangulo"] = pygame.Rect(40, 25, 70, 40)


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
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
    
    pantalla.blit(imagen_fondo, (0, 0))
    
    
    mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]} %",(150,145),FUENTE_22,COLOR_NEGRO) #volumen musica

    
    return retorno