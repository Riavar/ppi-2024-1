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
    background_color = (218, 247, 166)

    # Fuente y tamaño del textoasdfasdf
    font = pygame.font.SysFont("arial", 56)
    # Mensaje de bienvenida
    bienvenida_text = "ECOGUERRA"
    bienvenida_surface = font.render(bienvenida_text, True, ("#1a7f11"))
    bienvenida_rect = bienvenida_surface.get_rect(center=(WIDTH/2, HEIGHT/3 - 50))
    
     # Fuente y tamaño del textoasdfasdf
    font = pygame.font.SysFont("arial", 30)
    # Mensaje de bienvenida
    bienvenida_text1 = "Bienvenido, ingresa tu nombre"
    bienvenida_surface1 = font.render(bienvenida_text1, True, (00, 00, 00))
    bienvenida_rect1 = bienvenida_surface1.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))

    # Texto de entrada
    input_rect = pygame.Rect(300, 300, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('#000000')
    color = color_inactive
    
    active = False
    text = ''
    done = False

    relor = pygame.time.Clock()
 

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
            relor.tick(20)

        pantalla.fill(background_color)
        pantalla.blit(bienvenida_surface,bienvenida_rect)
        pantalla.blit(bienvenida_surface1,bienvenida_rect1)
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_rect.w = width
        pantalla.blit(txt_surface, (input_rect.x+5, input_rect.y+1))
        pygame.draw.rect(pantalla, color, input_rect, 2)

        pygame.display.flip()

    return text

