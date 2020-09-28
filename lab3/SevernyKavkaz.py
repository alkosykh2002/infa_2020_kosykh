import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 6
screen = pygame.display.set_mode((1200, 720))
screen.fill((250, 200, 100))


# горы на заднем плане
def gornychrebet1(x=0.0, y=400.0):
    gor = [[0, 0]] * 1200
    for x in range(0, 1200):
        gor[x] = [round(x), round(y)]
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
    polygon(screen, [139, 109, 92], gor)


# горы в центре экрана
def gornychrebet2(x=0, y=510.0):
    gor = [[0, 0]] * 1200
    for x in range(x, 1200):
        gor[x] = [round(x), round(y)]
        if x < 151:
            y = y + 2 * 150 * (x - 80) / 5000
        if (x > 150) and (x < 201):
            y = y - 1.5
        if (x > 200) and (x < 261):
            y = y + 1
        if (x > 260) and (x < 301):
            y = y - 2
        if (x > 300) and (x < 431):
            y = y + 0.3
        if (x > 430) and (x < 481):
            y = y + 1.5
        if (x > 480) and (x < 601):
            y = y - 0.15
        if (x > 600) and (x < 801):
            y = y + 2 * (x - 740) / 90
        if (x > 800) and (x < 901):
            y = y - 2 * (x - 980) / 250
        if (x > 900) and (x < 1001):
            y = y - 0.8
        if (x > 1000) and (x < 1031):
            y = y + 2
        if (x > 1030) and (x < 1101):
            y = y - 1.2
        if (x > 1100) and (x < 1151):
            y = y + 0.8
        if (x > 1150) and (x < 1198):
            y = y - 3
        if x > 1197:
            y = 510
    polygon(screen, [109, 79, 62], gor)


def gornychrebet3():
    polygon(screen, [100, 50, 0],
            [[0, 800], [0, 480], [150, 600], [200, 799], [500, 750], [700, 799], [800, 799], [950, 730], [1000, 799],
             [1100, 600], [1200, 500], [1200, 800]])


# ну тут очев, солнце
def solntse(x, y, r):
    pygame.draw.circle(screen, [255, 200, 200], [x, y], r)
    for i in range(1, 200):
        corona = pygame.Surface((1000, 500), pygame.SRCALPHA)
        pygame.draw.circle(corona, (255, 0, 0, 0), (2 * r, 2 * r), 2 * r)
        pygame.draw.circle(corona, [255, 150, 0, 200 - i], [x, y], r + 2 * i, 2)
        screen.blit(corona, (0, 0))


# рандомно генерируемые деревья
def les():
    polygon(screen, [33, 110, 0], [[0, 510], [0, 390], [1200, 270], [1200, 500]])
    for i in range(1, 400):
        X = randint(0, 1200)
        Y = randint(400 - round(X / 12), 500)
        pygame.draw.line(screen, [180, 20, 0], [X + 5, Y + 20], [X + 5, Y], 3)
        pygame.draw.polygon(screen, [randint(20, 40), randint(40, 80), randint(0, 20)],
                            [[X, Y], [X + 10, Y], [X + 5, Y - randint(20, 30)]])
        pygame.draw.polygon(screen, [randint(20, 40), randint(40, 80), randint(0, 20)],
                            [[X, Y + 10], [X + 10, Y + 10],
                             [X + 5, Y + 10 - randint(20, 30)]])


# море, рисуется линиями, чтобы цвет волны менялся от координаты и от времени
def more(x, y, t):
    volna = [[0, 0]] * 130
    for i in range(0, 110):
        for j in range(0, 130):
            volna[j] = [x + 10 * j, y + i * 3 + 3 * (j % 3)]
        pygame.draw.lines(screen,
                          [60 * (i + t) % 8, 120 + 15 * ((t + i) % 8), 170 + 3 * ((i + t) % 8)],
                          0, volna, 3)


# кораблик, r - это размер, х и у координаты левой верхней точки
def korablik(x, y, r):
    pygame.draw.polygon(screen, (184, 16, 0),
                        [[x, y + 7 * r / 10], [x + 3 * r / 10, y + r], [x + r, y + r], [x + r, y + 8 * r / 10]])
    pygame.draw.polygon(screen, [255, 0, 0], [[x + 0.6 * r, y + 0.2 * r], [x + 0.6 * r, y], [x + 0.9 * r, y + 0.1 * r]])
    pygame.draw.polygon(screen, [255, 255, 255],
                        [[x + 0.6 * r, y + 0.76 * r], [x + 0.6 * r, y + 0.2 * r], [x, y + 0.7 * r],
                         [x + 0.3 * r, y + 0.65 * r]])
    pygame.draw.polygon(screen, [255, 255, 255],
                        [[x + 0.6 * r, y + 0.76 * r], [x + 0.6 * r, y + 0.2 * r], [x + r, y + 0.8 * r],
                         [x + 0.8 * r, y + 0.7 * r]])
    pygame.draw.line(screen, [184, 16, 0], [x + 0.6 * r, y], [x + 0.6 * r, y + 0.8 * r], round(r / 20))


# рисуем птицу, r - это размер, х и у координаты левой верхней точки
def ptitsa(x, y, r, t):
    pygame.draw.polygon(screen, [50, 30, 0],
                        [[x, y + 2 * (3 + t % 1) * abs(r) / 10], [x + 0.5 * r, y + 0.1 * (5 + t % 1) * abs(r)],
                         [x + 0.9 * r, y + 0.6 * abs(r)], [x + 0.8 * r, y + 0.5 * abs(r)],
                         [x + 0.9 * r, y + 0.5 * abs(r)], [x + r, y + 0.6 * abs(r)],
                         [x + 1.5 * r, y + 0.1 * (4 + t % 1) * abs(r)], [x + 2 * r, y + 2 * (2 + t % 1) * abs(r) / 10],
                         [x + 1.5 * r, y + 0.1 * (5 + t % 1) * abs(r)], [x + 1.1 * r, y + 0.7 * abs(r)],
                         [x + 1.2 * r, y + 0.8 * abs(r)], [x + r, y + 0.8 * abs(r)],
                         [x + 0.5 * r, y + 0.1 * (6 + t % 1) * abs(r)]])


# птицы поверх всего, поэтому сначала задаём расположение
# здесь k_ptits – количество, staya – массив массивов, хранит в себе координаты х, у, размер r соответственно в
# staya[i][0] staya[i][1] и staya[i][2] для i-той птицы
k_ptits = 20
staya = [0] * k_ptits
for i in range(k_ptits):
    staya[i] = [0] * 3
for i in range(k_ptits):
    staya[i][0] = randint(100, 1100)
    staya[i][1] = randint(500, 700)
    staya[i][2] = randint(-50, 50)

# основная программа
gornychrebet1()
les()
gornychrebet2()
solntse(500, 200, 30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

# анимированная вода, кораблик, птицы
time = 0
while not finished:
    clock.tick(FPS)
    more(0, 500, round(time))
    korablik(1000 + round(2 * time), 600, 90)
    for i in range(0, k_ptits - 1):
        if (staya[i][0] < 0) or (staya[i][0] > 1200):
            staya[i][2] *= -1
            staya[i][0] -= 2.1 * staya[i][2]
        staya[i][0] -= round((staya[i][2] + 1) / 10)
        ptitsa(staya[i][0], staya[i][1], staya[i][2], time)
    gornychrebet3()
    time = time - 0.5
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
