import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 6
screen = pygame.display.set_mode((1200, 720))
screen.fill((250, 200, 100))


def gorny_chrebet1(x, y):
    """
    Выводит изображение гор на задний экран
    :param x: Координаты по горизонтальной оси
    :param y: Координаты по вертикальной оси
    :return: None
    """
    gor = [[0, 0]] * 1200
    for x in range(0, 1200):
        gor[x] = [round(x), round(y)]
        if x < 161:
            y = 350 - 100 * (x // 100) * (x // 100)
        if (x > 160) and (x < 201):
            y = y + 1
        if (x > 200) and (x < 211):
            y = y + 5
        if (x > 210) and (x < 401):
            y = y + (375 - y) // 200
        if (x > 400) and (x < 501):
            y = y - 0.3
        if (x > 500) and (x < 541):
            y = y + 0.75
        if (x > 540) and (x < 601):
            y = y - 1 // 3
        if (x > 600) and (x < 801):
            y = y - 2 * (x - 633.3333) // 300
        if (x > 800) and (x < 1001):
            y = y + 2 * (x - 870) // 125
        if (x > 1000) and (x < 1100):
            y = y + (x - 1151) // 100
        if (x > 1100) and (x < 1197):
            y = y + (x - 1200) // 200
        if x > 1197:
            y = y + 150

    print(x, y)
    polygon(screen, [139, 109, 92], gor)


def gorny_chrebet_2(x, y):
    """
    Выводит изображение гор в центр экрана
    :param x: Координаты по горизонтальной оси
    :param y: Координаты по вертикальной оси
    :return: None
    """
    gor = [[0, 0]] * 1200
    for x in range(x, 1200):
        gor[x] = [round(x), round(y)]
        if x < 152:
            y = y + 2 * 150 * (x - 80) // 5000
        if (x > 152) and (x < 201):
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
            y = y + 2 * (x - 740) // 90
        if (x > 800) and (x < 901):
            y = y - 2 * (x - 980) // 250
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


def gorny_chrebet_3():
    """
    Выводит изображение гор по краям экрана
    :return: None
    """
    polygon(screen, [100, 50, 0],
            [[0, 800], [0, 480], [150, 600], [200, 799], [500, 750], [700, 799], [800, 799], [950, 730], [1000, 799],
             [1100, 600], [1200, 500], [1200, 800]])


def solntse(x, y, r):
    """
    Выводит изображение солнца на экран
    :param x: Координата по горизонтальной оси
    :param y: Координата по вертикальной оси
    :param r: Радиус окружности
    :return: None
    """
    pygame.draw.circle(screen, [255, 200, 200], [x, y], r)
    for shag in range(1, 200):
        corona = pygame.Surface((1000, 500), pygame.SRCALPHA)
        pygame.draw.circle(corona, [255, 150, 0, 200 - shag], [x, y], r + 2 * shag, 2)
        screen.blit(corona, (0, 0))


def les():
    """
    Выводит изображение леса на экран, используя случайную генерацию
    :return: None
    """
    polygon(screen, [33, 110, 0], [[0, 510], [0, 390], [1200, 270], [1200, 500]])
    for derevo in range(1, 400):
        x = randint(0, 1200)
        y = randint(400 - round(x // 12), 500)
        pygame.draw.line(screen, [180, 20, 0], [x + 5, y + 20], [x + 5, y], 3)
        pygame.draw.polygon(screen, [randint(20, 40), randint(40, 80), randint(0, 20)],
                            [[x, y], [x + 10, y], [x + 5, y - randint(20, 30)]])
        pygame.draw.polygon(screen, [randint(20, 40), randint(40, 80), randint(0, 20)],
                            [[x, y + 10], [x + 10, y + 10],
                             [x + 5, y + 10 - randint(20, 30)]])


def more(x, y, t):
    """
    Выводит на экран изображение моря, отрисовывая его полосками волн, цвет и координата которых зависит от
    момента времени отрисовки
    :param x: Координата по горизонтальной оси
    :param y: Координата по вертикальной оси
    :param t: Счётчик времени
    :return:  None
    """
    volna = [[0, 0]] * 130
    for k in range(0, 110):
        for j in range(0, 130):
            volna[j] = [x + 10 * j, y + k * 3 + 3 * (j % 3)]
        pygame.draw.lines(screen,
                          [60 * (k + t) % 8, 120 + 15 * ((t + k) % 8), 170 + 3 * ((k + t) % 8)],
                          0, volna, 3)


def korablik(x, y, r):
    """
    Выводит на экран изображение кораблика
    :param x: Координата левой верхней точки по горизонтальной оси
    :param y: Координата левой верхней точки по вертикальной оси
    :param r: Коэффициент гомотетии, определяющий размер корабля
    :return: None
    """
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


def parohod(x, y, r):
    """
    Выводит на экран изображение парохода
    :param x: Координата левой верхней точки по горизонтальной оси
    :param y: Координата левой верхней точки по вертикальной оси
    :param r: Коэффициент гомотетии, определяющий размер парохода
    :return: None
    """
    pygame.draw.polygon(screen, (128, 128, 128),
                        [[x, y + 7 * r / 10], [x + 3 * r / 10, y + r], [x + r, y + r],
                         [x + 15 * r / 10, y + 7 * r / 10]])
    pygame.draw.polygon(screen, [255, 0, 0],
                        [[x, y + 7 * r / 10], [x, y + 6 * r / 10], [x + 15 * r / 10, y + 6 * r / 10],
                         [x + 15 * r / 10, y + 7 * r / 10]])
    pygame.draw.polygon(screen, [255, 255, 255],
                        [[x, y + 6 * r / 10], [x, y + 4 * r / 10], [x + 15 * r / 10, y + 4 * r / 10],
                         [x + 15 * r / 10, y + 6 * r / 10]])
    pygame.draw.polygon(screen, [128, 128, 128],
                        [[x + 3 * r / 10, y + 4 * r / 10], [x + 3 * r / 10, y + 1 * r / 10],
                         [x + 12 * r / 10, y + 1 * r / 10], [x + 12 * r / 10, y + 4 * r / 10]])
    pygame.draw.circle(screen, [0, 0, 0], [round(x + 5 * r / 10), round(y + 2.5 * r / 10)], 7)
    pygame.draw.circle(screen, [0, 0, 0], [round(x + 8 * r / 10), round(y + 2.5 * r / 10)], 7)
    pygame.draw.circle(screen, [0, 0, 0], [round(x + 11 * r / 10), round(y + 2.5 * r / 10)], 7)
    pygame.draw.polygon(screen, [0, 0, 0],
                        [[x + 4 * r / 10, y + 1 * r / 10], [x + 4 * r / 10, y - 4 * r / 10],
                         [x + 6 * r / 10, y - 4 * r / 10], [x + 6 * r / 10, y + 1 * r / 10]])


def dim(x, y, r, t):
    """
    Выводит на экран изображение дыма
    :param x: Координата левой верхней точки по горизонтальной оси
    :param y: Координата левой верхней точки по вертикальной оси
    :param r: Коэффициент гомотетии, определяющий размер дыма
    :param t: Счётчик времени
    :return: None
    """
    pygame.draw.circle(screen, [119, 136, 153], [round(x + 5 * r / 10 + round(2 * t)), round(y + -5 * r / 10 + 3 * t)],
                       30,5)
    pygame.draw.circle(screen, [119, 136, 153], [round(x -12 + 5 * r / 10 + round(2 * t)), round(y +15  + -5 * r / 10 + 3 * t)],
                       30,5)
    pygame.draw.circle(screen, [119, 136, 153], [round(x -9+ 5 * r / 10 + round(2 * t)), round(y -8+ -5 * r / 10 + 3 * t)],
                       30,5)
    pygame.draw.circle(screen, [119, 136, 153], [round(x+10 + 5 * r / 10 + round(2 * t)), round(y-10 + -5 * r / 10 + 3 * t)],
                       30,5)


def ptitsa(x, y, r, t):
    """
    Выводит на экран изображение птицы, конфигурация которого зависит от момента времени
    :param x: Координата левой верхней точки по горизонтальной оси
    :param y: Координата левой верхней точки по вертикальной оси
    :param r: Коэффициент гомотетии, определяющий размер птицы
    :param t: Счётчик времени
    :return: None
    """
    pygame.draw.polygon(screen, [50, 30, 0],
                        [[x, y + 2 * (3 + t % 1) * abs(r) // 10], [x + 0.5 * r, y + 0.1 * (5 + t % 1) * abs(r)],
                         [x + 0.9 * r, y + 0.6 * abs(r)], [x + 0.8 * r, y + 0.5 * abs(r)],
                         [x + 0.9 * r, y + 0.5 * abs(r)], [x + r, y + 0.6 * abs(r)],
                         [x + 1.5 * r, y + 0.1 * (4 + t % 1) * abs(r)], [x + 2 * r, y + 2 * (2 + t % 1) * abs(r) // 10],
                         [x + 1.5 * r, y + 0.1 * (5 + t % 1) * abs(r)], [x + 1.1 * r, y + 0.7 * abs(r)],
                         [x + 1.2 * r, y + 0.8 * abs(r)], [x + r, y + 0.8 * abs(r)],
                         [x + 0.5 * r, y + 0.1 * (6 + t % 1) * abs(r)]])


k_ptits = 20  # определяет количество птиц на экране
staya = [0] * k_ptits  # хранит информацию о параметрах изображения каждой птицы
for i in range(k_ptits):
    staya[i] = [0] * 3
for i in range(k_ptits):  # описание для i-той птицы
    staya[i][0] = randint(100, 1100)  # координата по горизонтальной оси
    staya[i][1] = randint(500, 700)  # координата по вертикальной оси
    staya[i][2] = randint(-50, 50)  # размер

# Вывод общего изображения заднего фона
gorny_chrebet1(0, 400)
les()
solntse(500, 200, 30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

# Создание анимации для объктов экрана
time = 0
while not finished:
    gorny_chrebet_2(0, 510)
    clock.tick(FPS)
    more(0, 500, round(time))
    korablik(1000 + round(2 * time), 450, 90)
    parohod(200 - round(2 * time), 600, 90)

    # Работа с таймером для дыма
    if (time >-20)and (time<0):
        dim(200 - round(2 * time), 600, 90, time)
    if (time >-40)and (time<-20):
        dim(200 - round(2 * time), 600, 90, time+20)
    if (time >-60)and (time<-40):
        dim(200 - round(2 * time), 600, 90, time+40)
    if (time >-80)and (time<-60):
        dim(200 - round(2 * time), 600, 90, time+60)
    if (time >-100)and (time<-80):
        dim(200 - round(2 * time), 600, 90, time+80)

    for i in range(0, k_ptits - 1):
        if (staya[i][0] < 0) or (staya[i][0] > 1200):
            # разворот на 180 градусов
            staya[i][2] *= -1
            staya[i][0] -= 2.1 * staya[i][2]
        staya[i][0] -= round((staya[i][2] + 1) // 10)
        ptitsa(staya[i][0], staya[i][1], staya[i][2], time)
    gorny_chrebet_3()
    time -= 0.5
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
