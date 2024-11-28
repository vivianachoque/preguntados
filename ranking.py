import pygame
import json
import os
from Constantes import *
from Funciones import *
from Juego import *  


# Archivo JSON para el ranking
ranking = "partidas.json"
        

# Función para guardar el ranking
def guardar_ranking(ranking):    
    
    with open('partidas.json', "w") as archivo:
        guardar_datos = json.dump(ranking, archivo, indent=4)
    return guardar_datos
 
# print(guardar_ranking({"nombre": "Pato", "puntuacion": 132}))





def ordenar_ranking(ranking):
    
    #Leer archivo JSON
    if os.path.exists(ranking):
        with open(ranking, "r") as archivo:
            lista_ranking = json.load(archivo)
    else:
        print("La lista de ranking no existe")


    # Ordenar los datos por el puntaje en orden descendente
    ranking_ordenado = sorted(lista_ranking, key=lambda x: x['puntuacion'], reverse=True)

    # Imprimir el ranking
    print("Ranking:")
    for posicion, jugador in enumerate(ranking_ordenado, start=1):
        print(f"{posicion}. {jugador['nombre']} - {jugador['puntuacion']} puntos")

        return ranking_ordenado

print(ordenar_ranking(ranking))


        




# Función para mostrar el ranking en pantalla
# def mostrar_ranking(pantalla, ranking):
#     pantalla.fill(COLOR_NEGRO)

#     for i, entrada in enumerate(ranking[:10]):  # Mostrar los primeros 10
#         texto = f"{i + 1}. {entrada['nombre']} - {entrada['puntaje']}"
#         linea = fuente.render(texto, True, COLOR_BLANCO)
#         pantalla.blit(linea, (100, 100 + i * 30))

#     pygame.display.flip()
    
# def calcular_maximo(numero_uno:int,numero_dos:int) -> int:
#     if numero_uno>numero_dos:
#         return numero_uno
#     else:
#         return numero_dos

# # # Función para agregar una nueva entrada al ranking
# # def agregar_puntaje(nombre, puntaje):
# #     ranking = cargar_ranking()
# #     ranking.append({"Nombre": nombre, "Puntaje": puntaje})
# #     ranking = sorted(ranking, key=lambda x: x["puntaje"], reverse=True)  # Ordenar por puntaje
# #     guardar_ranking(ranking)


# # Variables del juego
# puntaje = 0
# jugador = ""  # Nombre del jugador, se podría pedir al usuario en otro momento

# # Bucle principal del juego
# clock = pygame.time.Clock()
# corriendo = True
# mostrar_pantalla_ranking = False

# while corriendo:

#     if mostrar_pantalla_ranking:
#         ranking = cargar_ranking()
#         mostrar_ranking(pantalla, ranking)
#     else:
#         # Dibujar el juego (pantalla principal)
#         pantalla.fill(NEGRO)
#         texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
#         instrucciones = fuente.render("Presiona ESPACIO para sumar puntos, S para guardar, R para ranking", True, VERDE)
#         pantalla.blit(texto_puntaje, (50, 50))
#         pantalla.blit(instrucciones, (50, 100))
#         pygame.display.flip()

#     clock.tick(30)
#     mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_22,COLOR_BLANCO)
