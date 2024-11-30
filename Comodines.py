import pygame
from Constantes import *

pygame.init()

# DIBUJAR COMODINES

comodin_x2 = {}
comodin_x2["superficie"] = pygame.Surface(100,100)
comodin_x2["rectangulo"] = comodin_x2["superficie"].get_rect()
comodin_x2["superficie"].fill(COLOR_AZUL)

# FUNCIONES DE COMODINES

def multiplicar_puntos_por_dos(puntos_obtenidos:int, bandera:bool) -> int:
    retorno_total = puntos_obtenidos * 2
    bandera = False
    return retorno_total

