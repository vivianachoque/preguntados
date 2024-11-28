import pygame
# import json
# import os
from Constantes import *
from Funciones import *

pygame.init()

ruta_fondo = "./assets/imagenes/ranking.jpg"
imagen_fondo = pygame.image.load(ruta_fondo)
imagen_fondo = pygame.transform.scale(imagen_fondo, (500, 500))

boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
# boton_volver["superficie"].fill(COLOR_AZUL)

jugadores = {}
jugadores["superficie"] = pygame.Surface(TAMAÑO_CUADRO_RANKING)
jugadores["rectangulo"] = jugadores["superficie"].get_rect()
jugadores["superficie"].fill(COLOR_NEGRO)


# # Archivo JSON para el ranking
# ranking = "partidas.json"
        


# def guardar_ranking(ranking):    
    
#     with open('partidas.json', "w") as archivo:
#         guardar_datos = json.dump(ranking, archivo, indent=4)
#     return guardar_datos




def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "puntuaciones"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
            
            
    # # Mostrando el ranking
    # #Leer archivo JSON
    # if os.path.exists(ranking):
    #     with open(ranking, "r") as archivo:
    #         lista_ranking = json.load(archivo)
    # else:
    #     print("La lista de ranking no existe")


    # # Ordenar los datos por el puntaje en orden descendente
    # ranking_ordenado = sorted(lista_ranking, key=lambda x: x['puntuacion'], reverse=True)

    # # Imprimir el ranking
    # for posicion, jugador in enumerate(ranking_ordenado, start=1):
    #     print(f"{posicion}. {jugador['nombre']} - {jugador['puntuacion']} puntos")

    #     return ranking_ordenado 
    
    
    # pantalla.blit(imagen_fondo, (0, 0))
    # boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(40,25))
    
        

    #Columna izquierda
    jugadores["rectangulo"] = pantalla.blit(jugadores["superficie"],(50,128))
    jugadores["rectangulo"] = pantalla.blit(jugadores["superficie"],(50,179))
    jugadores["rectangulo"] = pantalla.blit(jugadores["superficie"],(50,230))
    jugadores["rectangulo"] = pantalla.blit(jugadores["superficie"],(50,281))
    jugadores["rectangulo"] = pantalla.blit(jugadores["superficie"],(50,332))

    #Columna derecha
    jugadores["rectangulo"] = pantalla.blit(jugadores["superficie"],(268,128))
    jugadores["rectangulo"] = pantalla.blit(jugadores["superficie"],(268,179))
    jugadores["rectangulo"] = pantalla.blit(jugadores["superficie"],(268,230))
    jugadores["rectangulo"] = pantalla.blit(jugadores["superficie"],(268,281))
    jugadores["rectangulo"] = pantalla.blit(jugadores["superficie"],(268,332))
    
    mostrar_texto(jugadores["superficie"], "PATO",(70,10), FUENTE_18, COLOR_BLANCO)
    

    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_22,COLOR_BLANCO)
        
    return retorno