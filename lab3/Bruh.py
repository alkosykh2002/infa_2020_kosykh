import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 20
screen = pygame.display.set_mode((1000, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

balls = [[0, 0, 0, 0]]
kolichestvo_sharov = 0
score = 0

pygame.font.SysFont('arial', 36)
f1 = pygame.font.Font(None, 30)


def risovaniye(massiv):
    for ball in massiv:
        circle(screen, ball[3], [ball[0], ball[1]], ball[2])


def new_ball():
    """
    задает параметры для шарика в виде (х, у, радиус, цвет)

    :return: (х, у, радиус, цвет)
    """
    x = randint(100, 800)
    y = randint(100, 600)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    return [x, y, r, color]


pygame.display.update()
clock = pygame.time.Clock()
finished = False

balls[0] = new_ball()

while not finished:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    screen.blit(f1.render('score = ' + str(score), 1, (255, 255, 255)), (0, 0))
    risovaniye(balls)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                cursor_pos = event.pos
                if (int(balls[0][0]) - cursor_pos[0]) * (int(balls[0][0]) - cursor_pos[0]) + (
                        int(balls[0][1]) - cursor_pos[1]) * (int(balls[0][1]) - cursor_pos[1]) < int(balls[0][2]) * int(
                        balls[0][2]):
                    balls[kolichestvo_sharov] = new_ball()
                    score = score + 2
                if (int(balls[0][0]) - cursor_pos[0]) * (int(balls[0][0]) - cursor_pos[0]) + (
                        int(balls[0][1]) - cursor_pos[1]) * (int(balls[0][1]) - cursor_pos[1]) > int(balls[0][2]) * int(
                        balls[0][2]):
                    score = score - 1
    pygame.display.update()
pygame.quit()
