from my_classes import *


pg.init()

BLACK = (0, 0, 0)
WIDTH, HEIGHT = 1280, 720
FPS = 60

pg.display.set_caption('Laboratory work 5')
screen = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()

background = pg.image.load('images/background.jpg').convert()

saturn = Saturn(200, 480, 0, 'images/saturn.png')

star_1 = Star(randint(0, int(WIDTH / 2)), 30, 'images/star.png')
star_2 = Star(randint(0, int(WIDTH / 2)), 90, 'images/star.png')
star_3 = Star(randint(0, int(WIDTH / 2)), 150, 'images/star.png')
star_4 = Star(randint(0, int(WIDTH / 2)), 210, 'images/star.png')
star_5 = Star(randint(0, int(WIDTH / 2)), 270, 'images/star.png')
star_6 = Star(randint(0, int(WIDTH / 2)), 330, 'images/star.png')
star_7 = Star(randint(0, int(WIDTH / 2)), 390, 'images/star.png')
star_8 = Star(randint(0, int(WIDTH / 2)), 450, 'images/star.png')
star_10 = Star(randint(0, int(WIDTH / 2)), 570, 'images/star.png')
star_11 = Star(randint(0, int(WIDTH / 2)), 630, 'images/star.png')
star_12 = Star(randint(0, int(WIDTH / 2)), 690, 'images/star.png')

rocket_speed = 5
rocket = Rocket(WIDTH / 2, HEIGHT, rocket_speed, 'images/rocket.png')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(saturn.image, saturn.rect)
    screen.blit(star_1.image, star_1.rect)
    screen.blit(star_2.image, star_2.rect)
    screen.blit(star_3.image, star_3.rect)
    screen.blit(star_4.image, star_4.rect)
    screen.blit(star_5.image, star_5.rect)
    screen.blit(star_6.image, star_6.rect)
    screen.blit(star_7.image, star_7.rect)
    screen.blit(star_8.image, star_8.rect)
    screen.blit(star_10.image, star_10.rect)
    screen.blit(star_11.image, star_11.rect)
    screen.blit(star_12.image, star_12.rect)
    screen.blit(rocket.image, rocket.rect)

    pg.display.update()
    clock.tick(FPS)

    saturn.update(200, 480)
    star_1.update(WIDTH)
    star_2.update(WIDTH)
    star_3.update(WIDTH)
    star_4.update(WIDTH)
    star_5.update(WIDTH)
    star_6.update(WIDTH)
    star_7.update(WIDTH)
    star_8.update(WIDTH)
    star_10.update(WIDTH)
    star_11.update(WIDTH)
    star_12.update(WIDTH)
    rocket.update(HEIGHT)
