import pygame

# Inicializa Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((800, 600))  # Tamaño de la ventana
pygame.display.set_caption("Preguntados")

# Colores
blanco = (255, 255, 255)
rojo = (255, 0, 0)

# Bucle principal del juego
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Cierra la ventana
            corriendo = False

    # Rellena la pantalla de blanco
    screen.fill(blanco)

    # Dibuja un rectángulo rojo
    pygame.draw.rect(screen, rojo, (300, 200, 200, 150))

    # Actualiza la pantalla
    pygame.display.flip()

# Cierra Pygame
pygame.quit()
