
import pygame
import sys
import random as rd
from demo import pantalla_inicio

def main():
    # Obtener el nombre del jugador
    
    
    nombre_personaje = pantalla_inicio()
    list_rec = []
    for x in range(rd.randrange(15,30)):
        w = rd.randrange(15,45)
        h=rd.randrange(20,60)
        x=rd.randrange(800)
        y=rd.randrange(600)
        list_rec.append(pygame.Rect(x,y,w,h))
    
    # Inicializar Pygame
    pygame.init()

    # Dimensiones de la pantalla
    WIDTH, HEIGHT = 800, 600
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ECO-GUERRA")

    # Color de fondo
    background_color = (255, 255, 255)

    # Posición y tamaño del objeto
    objeto_x = 50
    objeto_y = 300
    objeto_ancho = 50
    objeto_alto = 50
    objeto_velocidad = 600  # Píxeles por segundo

    # Reloj para controlar el tiempo
    timer = 0
    kills = 0
    clock = pygame.time.Clock()
    r1=pygame.Rect(objeto_x,objeto_y,objeto_ancho,objeto_alto)
    r2 =pygame.Rect(400, HEIGHT/2, 80, 50)
    # Game loop
    while True:
        dt = clock.tick(60) / 1000.0  # Obtener tiempo transcurrido desde el último fotograma en segundos
        
        old_x,old_y  = r1.left,r1.top
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            r1.move_ip(-objeto_velocidad * dt, 0)
            
        if keys[pygame.K_RIGHT]:
            r1.move_ip(+objeto_velocidad * dt, 0)
            
        if keys[pygame.K_UP]:
            r1.move_ip(0, -objeto_velocidad * dt)
            
        if keys[pygame.K_DOWN]:
            r1.move_ip(0, +objeto_velocidad * dt)
        
        int(kills)
        for recs in list_rec:
                if r1.colliderect(recs):
                    (r1.left,r1.top) =  (old_x,old_y)
                    recs.width=0
                    recs.height=0
                    kills+=1
        # Limitar el movimiento del objeto dentro de la pantalla
        timer += clock.tick(60)
        # Guarda las posisicones en x e y 
        
        segundos = timer // 1000
        minutos = segundos // 60
        segundos %= 60

            
        
        # Dibujar objetos en pantalla
        pantalla.fill(background_color)
        
        
        for element in list_rec:
            pygame.draw.rect(pantalla, (255, 245, 150), element)
        pygame.draw.rect(pantalla, (255, 0, 0), r1)
        
        # Mostrar nombre del personaje en la pantalla
        font = pygame.font.Font(None, 36)
        text_surface = font.render(nombre_personaje, True, (0, 0, 0))
        timer_text = "{:02}:{:02}".format(minutos, segundos)

    # Renderizar texto
        text_surface1 = font.render(timer_text, True, (0,0,0))
        text_rect1 = text_surface1.get_rect(topright=(WIDTH - 20, 20))
        
        
        kills_surface = font.render("Kills: " + str(kills), True, (0,0,0))
        kills_rect1 = kills_surface.get_rect(topright=(WIDTH - 100, 20))
        pantalla.blit(text_surface,(20, 20))
        pantalla.blit(text_surface1,text_rect1)
        pantalla.blit(kills_surface,kills_rect1)
        pygame.display.flip()



if __name__ == "__main__":
    main()
