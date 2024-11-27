import pygame
pygame.init()

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
COLOR_AMARILLO = (239,255,0)
COLOR_VERDE_OSCURO = "#0B9827"
ANCHO = 500
ALTO = 500
VENTANA = (ANCHO,ALTO)
FPS = 60

TAMAÑO_PREGUNTA = (350,150)
TAMAÑO_RESPUESTA = (250,60)
TAMAÑO_BOTON = (250,60)
CUADRO_TEXTO = (250,60)
TAMAÑO_BOTON_VOLUMEN = (60,60)
TAMAÑO_BOTON_VOLVER = (100,40)


FUENTE_22 = pygame.font.SysFont("Arial",22)
FUENTE_25 = pygame.font.SysFont("Arial",25)
FUENTE_27 = pygame.font.SysFont("Arial",27)
FUENTE_30 = pygame.font.SysFont("Arial",30)
FUENTE_32 = pygame.font.SysFont("Arial",32)
FUENTE_50 = pygame.font.SysFont("Arial",50)

CLICK_SONIDO = pygame.mixer.Sound("assets/musica/click.mp3")
ACIERTO_SONIDO = pygame.mixer.Sound("assets/musica/correct.mp3")
ERROR_SONIDO = pygame.mixer.Sound("assets/musica/wrong.mp3")
GAME_OVER_SONIDO = pygame.mixer.Sound("assets/musica/game-over.mp3")

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25

BOTON_JUGAR = 0
BOTON_AJUSTES = 1
BOTON_RANKINGS = 2
BOTON_SALIR = 3