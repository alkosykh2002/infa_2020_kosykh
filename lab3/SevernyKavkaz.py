print('z ujdyjtl')

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 720))
screen.fill((250, 200, 100))


def gornychrebet1():
    x = 0.0
    y = 400.0
    Gor = [[0, 0]] * 1200
    for x in range(0, 1200):
        Gor[x] = [round(x), round(y)]
        if x < 161:
            y = 350 - 100 * (x / 100) * (x / 100)
        if (x > 160) and (x < 201):
            y = y + 1
        if (x > 200) and (x < 211):
            y = y + 5
        if (x > 210) and (x < 401):
            y = y + (375 - y) / 200
        if (x > 400) and (x < 501):
            y = y - 0.5
        if (x > 500) and (x < 541):
            y = y + 0.75
        if (x > 540) and (x < 601):
            y = y - 1 / 3
        if (x > 600) and (x < 801):
            y = y - 2 * (x - 633.3333) / 300
        if (x > 800) and (x < 1001):
            y = y + 2 * (x - 870) / 125
        if (x > 1000) and (x < 1100):
            y = y + (x - 1151) / 100
        if (x > 1100) and (x < 1197):
            y = y + (x - 1200) / 200
        if x > 1197:
            y = y + 150

    print(x, y)
    polygon(screen, [139, 109, 92], Gor)


def solntse(x, y, r):
    pygame.draw.circle(screen, [255, 255, 200], [x, y], r)
    for i in range(1, 200):
        corona = pygame.Surface((1000, 500), pygame.SRCALPHA)
        pygame.draw.circle(corona, (255, 0, 0, 0), (2 * r, 2 * r), 2 * r)
        pygame.draw.circle(corona, [255, 255, 0, 200 - i], [x, y], r + 2 * i, 2)
        screen.blit(corona, (0, 0))


def more(x, y, t):
    volna = [[0, 0]] * 130
    for i in range(0, 110):
        for j in range(0, 130):
            volna[j] = [x + 10 * j, y + i * 3 + 3 * (j % 3)]
        pygame.draw.lines(screen,
                          [120 * (i + t) % 3, 120 + 30 * ((t + i) % 3) * ((i + t) % 3), 170 + 5 * ((i + t) % 3)],
                          0, volna, 3)


def korablik(x, y, r):
    pygame.draw.polygon(screen, (184, 16, 0),
                        [[x, y + 7 * r / 10], [x + 3 * r / 10, y + r], [x + r, y + r], [x + r, y + 8 * r / 10]])
    pygame.draw.polygon(screen, [255, 0, 0], [[x + 0.6 * r, y + 0.2 * r], [x + 0.6 * r, y], [x + 0.9 * r, y + 0.1 * r]])
    pygame.draw.polygon(screen, [255, 255, 255],
                        [[x + 0.6 * r, y + 0.76 * r], [x + 0.6 * r, y + 0.2 * r], [x, y + 0.7 * r],
                         [x + 0.3 * r, y + 0.65 * r]])
    pygame.draw.polygon(screen, [255, 255, 255],
                        [[x + 0.6 * r, y + 0.76 * r], [x + 0.6 * r, y + 0.2 * r], [x + r, y + 0.8 * r],
                         [x + r, y + 0.7 * r]])
    pygame.draw.line(screen, [184, 16, 0], [x + 0.6 * r, y], [x + 0.6 * r, y + 0.8 * r], round(r/20))


# main programm
gornychrebet1()

solntse(500, 100, 30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

time = 0
while not finished:
    clock.tick(FPS)
    more(0, 400, round(time))
    korablik(1000 + round(2 * time), 600, 50)
    time = time - 0.1
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
