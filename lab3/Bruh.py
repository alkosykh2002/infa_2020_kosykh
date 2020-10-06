import pygame
from pygame.draw import *
from random import randint
import numpy

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

balls = [[-1000, -1000, 0, 0, 0, 0]] * 5
kolichestvo_sharov = 0
score = 0
time = 0
shar = 0
exp_x = 0
exp_y = 0
exp_x1 = 0
exp_y1 = 0

pygame.font.SysFont('arial', 36)
f1 = pygame.font.Font(None, 30)


def risovaniye(massiv):
    for i in massiv:
        circle(screen, [50 + i[5] % 150, 255 * (i[5] // 120), 0], [i[0], i[1]], i[2])
        circle(screen, [0, 0, 0], [i[0], i[1]], i[2] + 3, 3)


def new_ball():
    """
    задает параметры для шарика в виде (х, у, радиус, скорость х, скорость у, время жизни)

    :return: (х, у, радиус, скорость х, скорость у, время жизни)
    """
    x = randint(100, 800)
    y = randint(100, 600)
    r = randint(40, 100)
    speed_x = randint(-5, 5)
    speed_y = randint(-5, 5)
    return [x, y, r, speed_x, speed_y, 0]


def explosion(x, y, t):
    for i in range(0, 1000):
        fi = randint(0, 500)
        dobavka_x = randint(-10, 10)
        dobavka_y = randint(-10, 10)
        circle(screen, [255, 255, 255],
               [int(x + 3 * t * numpy.cos(fi) + dobavka_x), int(y + 3 * t * numpy.sin(fi) + dobavka_y)], 10)
        circle(screen, [0, 0, 0],
               [int(x + 3 * t * numpy.cos(fi) + dobavka_x), int(y + 3 * t * numpy.sin(fi) + dobavka_y)], 10, 1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

balls[0] = new_ball()

while not finished:
    clock.tick(FPS)
    screen.fill([0, 0, 0])
    polygon(screen, [255, 255, 255], [[100, 100], [100, 600], [900, 600], [900, 100]], 5)
    screen.blit(f1.render('score = ' + str(score), 1, (255, 255, 255)), (0, 0))
    if exp_x1 > 0:
        time = time + 1
        explosion(exp_x1, exp_y1, time)
        score = -255
    risovaniye(balls)
    for ball in balls:
        ball[5] = ball[5] + 1
        ball[0] = ball[0] + int(ball[3])
        ball[1] = ball[1] + int(ball[4])
        if ball[0] < 100:
            ball[3] = -ball[3]
            ball[0] = ball[0] + 2 * int(round(ball[3]))
            ball[4] = randint(-5, 5)
        if ball[0] > 900:
            ball[3] = -ball[3]
            ball[0] = ball[0] + 2 * int(round(ball[3]))
            ball[4] = randint(-5, 5)
        if ball[1] < 100:
            ball[4] = -ball[4]
            ball[1] = ball[1] + 2 * int(round(ball[4]))
            ball[3] = randint(-5, 5)
        if ball[1] > 600:
            ball[4] = -ball[4]
            ball[1] = ball[1] + 2 * int(round(ball[4]))
            ball[3] = randint(-5, 5)
        if ball[5] > 148:
            ball[5] = 0
            exp_x = ball[0]
            exp_y = ball[1]
            if (exp_x > 0) and (exp_y > 0):
                exp_x1 = exp_x
                exp_y1 = exp_y
                time = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.button == 1) or (event.button == 3):
                cursor_pos = event.pos
                for ball in balls:
                    if (int(ball[0]) - cursor_pos[0]) * (int(ball[0]) - cursor_pos[0]) + (
                            int(ball[1]) - cursor_pos[1]) * (int(ball[1]) - cursor_pos[1]) < int(ball[2]) * int(
                            ball[2]):
                        balls[shar] = new_ball()
                        score = score + 5
                        break
                    if (int(ball[0]) - cursor_pos[0]) * (int(ball[0]) - cursor_pos[0]) + (
                            int(ball[1]) - cursor_pos[1]) * (int(ball[1]) - cursor_pos[1]) > int(ball[2]) * int(
                            ball[2]) and (ball[2] > 0):
                        score = score - 1
                        shar = shar + 1
                balls[shar % 5] = new_ball()
                shar = 0
        if event.type == pygame.MOUSEMOTION:
            cursor_pos = event.pos
            print(cursor_pos)
            for ball in balls:
                if (ball[0] - cursor_pos[0]) * (ball[0] - cursor_pos[0]) + (ball[1] - cursor_pos[1]) * (
                        ball[1] - cursor_pos[1]) < 4 * ball[2] * ball[2]:
                    ball[3] = 7 * (ball[0] - cursor_pos[0]) * abs(ball[0] - cursor_pos[0]) / (
                            (ball[0] - cursor_pos[0]) * (
                                ball[0] - cursor_pos[0]) + (ball[1] - cursor_pos[1]) * (ball[1] - cursor_pos[1]) + 1)
                    ball[4] = 7 * (ball[1] - cursor_pos[1]) * abs(ball[1] - cursor_pos[1]) / (
                            (ball[1] - cursor_pos[1]) * (
                                ball[1] - cursor_pos[1]) + (ball[1] - cursor_pos[1]) * (ball[1] - cursor_pos[1]) + 1)
    pygame.display.update()
pygame.quit()
