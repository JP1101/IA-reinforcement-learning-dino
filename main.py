import pygame
import sys
import random
import numpy as np

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 1024, 576
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Resolver dino chtome")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

#tiempo
clock = pygame.time.Clock()

# Posición y tamaño de la línea del piso
floor_y = height - 50
floor_width = width

jump_t = 0
t = 0

class Dino:
    def __init__(self, x, y, width, height, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.action = action
    

    def Jump(self):
        global jump_t
        
        jump_t += 2
        if self.action == 1:
            self.y = -(jump_t - 50) ** 2 / 13.33333 + 187.5

            if jump_t > 100:
                jump_t = 0

        if self.action == 3:
            jump_t += 9


    def duck(self):
        if self.action == 2:
            self.height = 37.5
            self.width = 75
        else:
            self.width = 37.5
            self.height = 75


    

    def checkAction(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_UP] or key[pygame.K_SPACE] or jump_t < 100 and jump_t != 0:
            self.action = 1
        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            self.action = 2
        else:
            self.action = 0


class cactus:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self):
        
        if self.x <= -200:
            self.x = 1024
            print("x")

        self.x -= 8


Playing = True

dino1 = Dino(45, 0, 37.5, 75, 0)
cactus1 = cactus(1024, 0, 75, 100)
cactus2 = cactus(1638.4, 0, 100, 50)
# Bucle principal
while Playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Dinosaurios:

    # Dibujar el fondo  
    screen.fill(black)

    # Dibujar la línea del piso
    pygame.draw.line(screen, white, (0, floor_y), (floor_width, floor_y), 2)

    #Dibujar el dinosaurio
    pygame.draw.rect(screen, white, (dino1.x, floor_y - dino1.height - dino1.y, dino1.width, dino1.height))

    #Dibujar los cactuses
    pygame.draw.rect(screen, white, (cactus1.x, floor_y - cactus1.height - cactus1.y, cactus1.width, cactus1.height))

    pygame.draw.rect(screen, white, (cactus2.x, floor_y - cactus2.height - cactus2.y, cactus2.width, cactus2.height))



    dino1.checkAction()

    dino1.Jump()
    dino1.duck()

    cactus1.move()
    cactus2.move()

    print(jump_t)
    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    clock.tick(60)
    t+=1
