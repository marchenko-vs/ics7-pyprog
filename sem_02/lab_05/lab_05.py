import pygame

pygame.init()

WIDTH = 700
HEIGHT = 500
FPS = 60
DARK_BLUE = (5, 0, 180)
WHITE = (255, 255, 255)

sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Laboratory work 5')

clock = pygame.time.Clock()

surf = pygame.Surface((WIDTH, HEIGHT))
surf.fill(DARK_BLUE)

rocket_surf = pygame.Surface((200, 100))
rocket_surf.fill(WHITE)
pygame.draw.rect(rocket_surf, WHITE, (10, 10, 75, 75), 2)

rocket_surf.blit(surf, (0, 0))
sc.blit(rocket_surf, (50, 50))

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FPS)
