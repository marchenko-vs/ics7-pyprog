import pygame

pygame.init()

NULL = 0
WIDTH = 900
HEIGHT = 660
FPS = 60
SPACE_COLOR = (3, 2, 57)
STAR_COLOR = (217, 196, 16)
WHITE = (255, 255, 255)

sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc.fill(SPACE_COLOR)
pygame.display.set_caption('Laboratory work 5')

clock = pygame.time.Clock()

star_surface_1 = pygame.Surface((100, 100))
star_surface_1.fill(WHITE)
star_surface_1.set_colorkey(WHITE)

pygame.draw.polygon(star_surface_1, STAR_COLOR,
                    [(50, 20), (60, 40), (85, 40), (60, 55), (70, 80), (50, 65),
                     (30, 80), (40, 55), (15, 40), (40, 40)])

star_surface_2 = pygame.Surface((100, 100))
star_surface_2.fill(WHITE)
star_surface_2.set_colorkey(WHITE)

pygame.draw.polygon(star_surface_2, STAR_COLOR,
                    [(50, 20), (60, 40), (85, 40), (60, 55), (70, 80), (50, 65),
                     (30, 80), (40, 55), (15, 40), (40, 40)])

x1, y1 = NULL, NULL
x2, y2 = 150, 80

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FPS)
