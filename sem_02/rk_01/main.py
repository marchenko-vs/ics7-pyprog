import pygame
import math

pygame.init()

SCALE = 100
RADIUS = 100
POSITION = (400, 300)
colors = [(255, 255, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
WHITE = (255, 255, 255)
WIDTH = 700
HEIGHT = 900
FPS = 30


def get_position(p, t):
    pos_x = p[0] + math.sin(t / 2) * RADIUS
    pos_y = p[1] + math.cos(t / 2) * RADIUS

    return pos_x, pos_y


def get_coordinates(p, t):
    coordinates = []
    for i in range(4):
        coordinates.append([[p[0], p[1]],
                            [p[0] + math.cos(t + math.pi * i / 2) * SCALE,
                             p[1] + math.sin(t + math.pi * i / 2) * SCALE],
                            [p[0] + math.cos(
                                t + math.pi * i / 2 + math.pi / 2) * SCALE,
                             p[1] + math.sin(
                                 t + math.pi * i / 2 + math.pi / 2) * SCALE]])

    return coordinates


def draw_square(surface, coordinates, color):
    for i in range(4):
        pygame.draw.polygon(surface, color[i], coordinates[i])


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test 01")
clock = pygame.time.Clock()
pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT))

tick = 0

clause = True
while clause:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            clause = False
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, HEIGHT))
    draw_square(screen, get_coordinates(get_position(POSITION, tick), tick),
                colors)
    pygame.display.flip()
    tick += 0.1
pygame.quit()
