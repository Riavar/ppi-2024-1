import pygame
import sys

# Función para la pantalla de inicio
def pantalla_inicio():
    # Inicializar Pygame
    pygame.init()

    # Dimensiones de la pantalla
    WIDTH, HEIGHT = 800, 600
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ECO-GUERRA ")

    # Color de fondo
    background_color = (255, 30, 30)

    # Fuente y tamaño del textoasdfasdf
    font = pygame.font.Font(None, 36)
    # Mensaje de bienvenida
    bienvenida_text = "\nECOGUERRA\nBienvenido, ingresa tu nombre"
    bienvenida_surface = font.render(bienvenida_text, True, (00, 00, 00))
    bienvenida_rect = bienvenida_surface.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))

    # Texto de entrada
    input_rect = pygame.Rect(300, 300, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    
 

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        pantalla.fill(background_color)
        pantalla.blit(bienvenida_surface,bienvenida_rect)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_rect.w = width
        pantalla.blit(txt_surface, (input_rect.x+5, input_rect.y+5))
        pygame.draw.rect(pantalla, color, input_rect, 2)

        pygame.display.flip()

    return text

# Función principal del juego
def main():
    # Obtener el nombre del jugador
    nombre_personaje = pantalla_inicio()

    # Inicializar Pygame
    pygame.init()

    # Dimensiones de la pantalla
    WIDTH, HEIGHT = 800, 600
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego de Aventuras")

    # Color de fondo
    background_color = (255, 255, 255)

    # Posición y tamaño del objeto
    objeto_x = 50
    objeto_y = 300
    objeto_ancho = 50
    objeto_alto = 50
    objeto_velocidad = 200  # Píxeles por segundo

    # Reloj para controlar el tiempo
    clock = pygame.time.Clock()

    # Game loop
    while True:
        dt = clock.tick(60) / 1000.0  # Obtener tiempo transcurrido desde el último fotograma en segundos

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

        # Limitar el movimiento del objeto dentro de la pantalla
        objeto_x = max(0, min(objeto_x, WIDTH - objeto_ancho))
        objeto_y = max(0, min(objeto_y, HEIGHT - objeto_alto))

        # Dibujar objetos en pantalla
        pantalla.fill(background_color)
        pygame.draw.rect(pantalla, (255, 0, 0), (objeto_x, objeto_y, objeto_ancho, objeto_alto))
        
        # Mostrar nombre del personaje en la pantalla
        font = pygame.font.Font(None, 36)
        text_surface = font.render(nombre_personaje, True, (0, 0, 0))
        pantalla.blit(text_surface, (20, 20))
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
