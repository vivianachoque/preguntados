import pygame
from Constantes import *

pygame.init()

# DIBUJAR COMODINES

comodin_x2 = {}
comodin_x2["superficie"] = pygame.Surface((40,40))
comodin_x2["rectangulo"] = comodin_x2["superficie"].get_rect()

# FUNCIONES DE COMODINES

def multiplicar_puntos_por_dos() -> int:
    puntuacion_doble = 100 * 2
    return puntuacion_doble

