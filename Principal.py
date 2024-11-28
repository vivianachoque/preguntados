import pygame
from Funciones import *
from Constantes import *
from Menu import *
from Juego import *
from Configuraciones import *
from Puntuaciones import *

pygame.init()
pygame.display.set_caption("JUEGO 314")
pygame.mixer.init()

pantalla = pygame.display.set_mode(VENTANA)
corriendo = True
reloj = pygame.time.Clock()
datos_juego = {"puntuacion":0,"cantidad_vidas":CANTIDAD_VIDAS,"nombre":"","volumen_musica":100}
ventana_actual = "menu"
bandera_juego = False


while corriendo:
    #Gestion de Eventos -> No lo programamos aca
    #Actualizacion de estados -> No lo programamos aca
    #Imprimir en pantalla esa informacion -> No lo programamos aca
    cola_eventos = pygame.event.get()
    reloj.tick(FPS)
        
    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "juego":
        if bandera_juego == False:
            porcentaje_coma = datos_juego["volumen_musica"] / 100
            pygame.mixer.music.load("./assets/musica/musica.mp3")
            pygame.mixer.music.set_volume(porcentaje_coma)
            pygame.mixer.music.play(-1)
            bandera_juego = True
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "configuracion":
        ventana_actual = mostrar_ajustes(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "puntuaciones":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos)
    elif ventana_actual == "terminado":
        pass
    elif ventana_actual == "salir":
        corriendo = False
    
    pygame.display.flip()
    
pygame.quit()
    
    
    