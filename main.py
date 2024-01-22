import pygame
import sys
import random

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

class Dino:
    def __init__(self, x, y, width, height, action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.action = action
    

    def Jump(self):
        global jump_t
        
        jump_t += 1
        if self.action == 1:
            self.y = -(jump_t - 50) ** 2 / 13.33333 + 187.5
            if jump_t > 100:
                jump_t = 0
    def checkAction(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_UP] or key[pygame.K_SPACE] or jump_t < 100 and jump_t != 0:
            self.action = 1
        else:
            self.action = 0


class cactus:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def functionalities(self):
        self.x -= 5
        if self.x < -self.width + width-50:
            self.x += width + random.randint(50, 60)
            self.height = random.randint(75, 125)
            self.width = random.randint(50, 200)


Playing = True

dino1 = Dino(45, 0, 37.5, 75, 0)
cactus1 = cactus(width, 0, 75, 100)
cactus2 = cactus(width*1.5, 0, 100, 50)
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

    cactus1.functionalities()
    cactus2.functionalities()

    print(jump_t)
    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    clock.tick(60)
