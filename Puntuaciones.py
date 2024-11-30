import pygame
import json
import os
from Constantes import *
from Funciones import *

pygame.init()

ruta_fondo = "./assets/imagenes/ranking.jpg"
imagen_fondo = pygame.image.load(ruta_fondo)
imagen_fondo = pygame.transform.scale(imagen_fondo, (500, 500))

boton_volver = {}
boton_volver["rectangulo"] = pygame.Rect(40, 25, 70, 40)

    
jugadores = {}
jugadores["superficie"] = pygame.Surface(TAMAÑO_CUADRO_RANKING)
jugadores["rectangulo"] = jugadores["superficie"].get_rect()
jugadores["superficie"].fill(COLOR_NEGRO)


# # Archivo JSON para el ranking
ranking = "partidas.json"
    

# def guardar_ranking(ranking):    
    
#     with open('partidas.json', "w") as archivo:
#         guardar_datos = json.dump(ranking, archivo, indent=4)
#     return guardar_datos

def leer_json(ranking):
    #Leer archivo JSON
    if os.path.exists(ranking):
        with open(ranking, "r") as archivo:
            lista_ranking = json.load(archivo)            
    else:
        print("La lista de ranking no existe")

    # Ordenar los datos por el puntaje en orden descendente
    ranking_ordenado = sorted(lista_ranking, key=lambda x: x['puntuacion'], reverse=True)
    
    return ranking_ordenado
    # Imprimir el ranking
    # for posicion, jugador in enumerate(ranking_ordenado, start=1):
    #     print(f"{posicion}. {jugador['nombre']} - {jugador['puntuacion']} puntos")
    #     return ranking_ordenado 




def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],ranking) -> str:
    retorno = "puntuaciones"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
                print("VUELVE AL MENU")

    
    pantalla.blit(imagen_fondo, (0, 0))    
    
    ranking_jugadores = leer_json(ranking)
    FUENTE_22.render("Ranking", True, COLOR_BLANCO)
    
    for i, jugador in enumerate(ranking_jugadores):
        texto = f"{i+1}.{jugador['nombre']} - {jugador['puntuacion']} puntos"
        texto_renderizado = FUENTE_22.render(texto, True, COLOR_NEGRO)
        
        if i <= 4:
            pantalla.blit(texto_renderizado,(50,128+i*51))
        else:  
            pantalla.blit(texto_renderizado,(268,128+i*51))
             
  
    # posicion_jugadores=[(50,128),(50,179),(50,230),(50,281),(50,332),(268,128),(268,179),(268,230),(268,281),(268,332)]
             
    return retorno


