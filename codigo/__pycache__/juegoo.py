import pygame
import sys
from demo import pantalla_inicio

def juegoo():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego de Aventuras")
    background_color = (255, 255, 255)
    objeto_x = 50
    objeto_y = 300
    objeto_ancho = 50
    objeto_alto = 50
    objeto_velocidad = 200
    clock = pygame.time.Clock()
    nombre_personaje = pantalla_inicio()

    while True:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            objeto_x -= objeto_velocidad * dt
        if keys[pygame.K_RIGHT]:
            objeto_x += objeto_velocidad * dt
        if keys[pygame.K_UP]:
            objeto_y -= objeto_velocidad * dt
        if keys[pygame.K_DOWN]:
            objeto_y += objeto_velocidad * dt

        objeto_x = max(0, min(objeto_x, WIDTH - objeto_ancho))
        objeto_y = max(0, min(objeto_y, HEIGHT - objeto_alto))

        pantalla.fill(background_color)
        pygame.draw.rect(pantalla, (255, 0, 0), (objeto_x, objeto_y, objeto_ancho, objeto_alto))
        font = pygame.font.Font(None, 36)
        text_surface = font.render(nombre_personaje, True, (0, 0, 0))
        pantalla.blit(text_surface, (20, 20))
        pygame.display.flip()

if __name__ == "__main__":
    juegoo()
