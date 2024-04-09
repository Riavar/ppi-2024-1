import pygame as Pygame
import sys
from configuraciones import *


class Juego:
    
    #este metodo nos construlle la clase juego
    def __init__(self): # __ (son dos rayas al piso juntas )
        Pygame.init()
        print(ANCHO)
        # SE CREA LA PANTALLA DE JUEGO CON EL ANCHO Y EL ALTO 
        self.pantalla = Pygame.display.set_mode((ANCHO,ALTO))
        # SE PONE EL TITULOA LA VENTANA DE ESTA PANTALLA 
        Pygame.display.set_caption('ECO-GUERRA')
        # crea el reloj:
        self.reloj = Pygame.time.Clock()
        
    def iniciarJuego(self):
        while True:
            for evento in Pygame.event.get():
                #si se pulso la x para salir 
                if evento.type == Pygame.QUIT:
                    Pygame.quit()
                    sys.exit()
                    #si se pulso     la q para salir 
                elif evento.type == Pygame.KEYDOWN:
                    if evento.key == Pygame.k_q:
                        Pygame.quit()
                        sys.exit()
            #mortrar la pantalla de fondo negro
            self.pantalla.fill('black')
            #que actualice la pantalla con los cambios
            Pygame.display.update()
            # que el reloj empiece a contar
            self.reloj.tick(IPS)

if __name__ == '__main__':
    #hacer una variable que sea un juego
    jugar = Juego()
    jugar.iniciarJuego()

    