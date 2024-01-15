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

dino_y_pos = 0

dino_width = 37
dino_height = 75
dino_x_pos = 45
# 0 nothing, 1 jumping
Action = 0


#variables de las variables del dinosaurio ._.


cactuses_x_pos = [0, 0, 0]


dis = 200


big_width = dino_width * 2
medium_width = dino_width * 1.5
small_width = dino_width * 1

big_height = dino_height + 25
small_height = dino_height - 25  

#Variables del dinosaurio
C1_x_pos = width - dis
C2_x_pos = width - dis + (width/2)

C1_y_pos = 0
C2_y_pos = 50

C1_width = big_width
C2_width = medium_width

C1_height = big_height
C2_height = small_height


jump_t = 4


def Actualize_C_x_pos():
    global C1_x_pos, C2_x_pos, width
    C1_x_pos -= 8
    C2_x_pos -= 8

    c = random.randint(20, 50)
    if C1_x_pos < -50:
        C1_x_pos += width + c

    if C2_x_pos < -50:
        C2_x_pos += width + c



def check_Player_Action():
    global Action

    global jump_t
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] or keys[pygame.K_SPACE] or jump_t < 100:
        Action = 1
    else:
        Action = 0

def Jump():
    global dino_y_pos
    global jump_t
    global Action

    if jump_t < 100:
        dino_y_pos = -(jump_t - 50) ** 2 / 13.33333 + 187.5  # Quadratic function
        Action = 1
    else:
        dino_y_pos = 0
        jump_t = 0
        Action = 0

    jump_t += 2





Playing = True
# Bucle principal
while Playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar el fondo  
    screen.fill(black)

    # Dibujar la línea del piso
    pygame.draw.line(screen, white, (0, floor_y), (floor_width, floor_y), 2)

    #Dibujar el dinosaurio
    pygame.draw.rect(screen, white, (dino_x_pos, floor_y - dino_height - dino_y_pos, dino_width, dino_height))



    #Dibujar el cactus 1
    pygame.draw.rect(screen, white, (C1_x_pos, floor_y - C1_height - C1_y_pos, C1_width, C1_height))
    #Dibujar el cactus 2
    pygame.draw.rect(screen, (20,50,20), (C2_x_pos, floor_y - C2_height - C2_y_pos, C1_width, C1_height))

    Actualize_C_x_pos()

    check_Player_Action()

    if Action == 1:
        Jump()
    else:
        dino_y_pos = 0

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    clock.tick(60)