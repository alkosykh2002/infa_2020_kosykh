import pygame
from pygame.draw import *
from random import randint
import numpy

pygame.init()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

score = 0
time = 0
exp_x = 0
exp_y = 0
exp_x1 = 0
exp_y1 = 0
Ecrx = 1000
Ecry = 700
FPS = 20
cursor_pos = 0
screen = pygame.display.set_mode((Ecrx, Ecry))

pygame.font.SysFont('arial', 36)
f1 = pygame.font.Font(None, 30)


class Hero:
    x = 0
    y = 0
    fi = 0
    r = 50
    tsvet_tela = COLORS[0]
    tsvet_planseta = COLORS[3]

    def vverh(self):
        self.y -= 100 / FPS

    def vniz(self):
        self.y += 100 / FPS

    def vlevo(self):
        self.x -= 100 / FPS

    def vpravo(self):
        self.x += 100 / FPS

    def new_coord(self, dx, dy):
        return [self.x + dx * self.r * numpy.cos(self.fi) + dy * self.r * numpy.sin(self.fi),
                self.y + dx * self.r * numpy.sin(self.fi) - dy * self.r * numpy.cos(self.fi)]

    def risyi(self, cursor):
        if self.y <= cursor[1]:
            self.fi = numpy.arccos((cursor[0] - self.x) / numpy.sqrt(
                (cursor[0] - self.x) * (cursor[0] - self.x) + (cursor[1] - self.y) * (cursor[1] - self.y)))
        if self.y > cursor[1]:
            self.fi = numpy.pi + numpy.arccos(-(cursor[0] - self.x) / numpy.sqrt(
                (cursor[0] - self.x) * (cursor[0] - self.x) + (cursor[1] - self.y) * (cursor[1] - self.y)))
        polygon(screen, [255, 255, 150], [self.new_coord(0.3, 0.5), self.new_coord(0.5, 0.4), self.new_coord(0.4, 0.3)])
        polygon(screen, [255, 255, 150],
                [self.new_coord(0.3, -0.5), self.new_coord(0.5, -0.4), self.new_coord(0.4, -0.3)])
        polygon(screen, self.tsvet_tela,
                [self.new_coord(-0.2, 0.2), self.new_coord(0, 0.6), self.new_coord(0.4, 0.5), self.new_coord(0.3, 0.4),
                 self.new_coord(0.1, 0.5), self.new_coord(0.2, 0.4), self.new_coord(0.3, 0.1),
                 self.new_coord(0.3, -0.1), self.new_coord(0.2, -0.4), self.new_coord(0.1, -0.5),
                 self.new_coord(0.3, -0.4), self.new_coord(0.4, -0.5), self.new_coord(0, -0.6),
                 self.new_coord(-0.2, -0.2)])
        polygon(screen, self.tsvet_planseta,
                [self.new_coord(0.3, 0.2), self.new_coord(0.5, 0.6), self.new_coord(0.7, 0.5),
                 self.new_coord(0.5, 0.1)])
        line(screen, self.tsvet_planseta, self.new_coord(0.45, -0.3), self.new_coord(0.45, -0.6), self.r // 20)
        circle(screen, [255, 255, 150], [int(self.x), int(self.y)], int(0.2 * self.r))

    def vystrel(self):
        line(screen, [255, 200, 100], [int(self.x), int(self.y)],
             [int(self.x + 1000 * numpy.cos(self.fi)), int(self.y + 1000 * numpy.sin(self.fi))])


def explosion(x, y, t):
    for i in range(0, 1000):
        fi = randint(0, 500)
        dobavka_x = randint(-10, 10)
        dobavka_y = randint(-10, 10)
        circle(screen, [255, 255, 255],
               [int(x + 3 * t * numpy.cos(fi) + dobavka_x), int(y + 3 * t * numpy.sin(fi) + dobavka_y)], 10)
        circle(screen, [0, 0, 0],
               [int(x + 3 * t * numpy.cos(fi) + dobavka_x), int(y + 3 * t * numpy.sin(fi) + dobavka_y)], 10, 1)


class SharOdin:
    parametry = [0, 0, 0, 0, 0, 0]
    time_of_birthday = 0

    def __init__(self):
        x = randint(200, Ecrx - 200)
        y = randint(200, Ecry - 200)
        r = randint(40, 100)
        speed_x = randint(-100, 100) / FPS
        speed_y = randint(-100, 100) / FPS
        self.time_of_birthday = time
        self.parametry = [x, y, r, speed_x, speed_y, time]

    def dvizh(self):
        self.parametry[5] = time
        if self.parametry[5] - self.time_of_birthday < 200:
            self.parametry[0] += self.parametry[3]
            self.parametry[1] += self.parametry[4]
            if self.parametry[0] < 100 + self.parametry[2]:
                self.parametry[3] = -self.parametry[3]
                self.parametry[0] = self.parametry[0] + 2 * int(round(self.parametry[3]))
                self.parametry[4] = randint(-100, 100) / FPS
            if self.parametry[0] > Ecrx - 100 - self.parametry[2]:
                self.parametry[3] = -self.parametry[3]
                self.parametry[0] = self.parametry[0] + 2 * int(round(self.parametry[3]))
                self.parametry[4] = randint(-100, 100) / FPS
            if self.parametry[1] < 100 + self.parametry[2]:
                self.parametry[4] = -self.parametry[4]
                self.parametry[1] = self.parametry[1] + 2 * int(round(self.parametry[4]))
                self.parametry[3] = randint(-100, 100) / FPS
            if self.parametry[1] > Ecry - 100 - self.parametry[2]:
                self.parametry[4] = -self.parametry[4]
                self.parametry[1] = self.parametry[1] + 2 * int(round(self.parametry[4]))
                self.parametry[3] = randint(-100, 100) / FPS

    def risyi(self):
        if self.parametry[5] - self.time_of_birthday < 150:
            circle(screen, [50 + (time - self.time_of_birthday) % 150, 0, 0],
                   [int(self.parametry[0]), int(self.parametry[1])], self.parametry[2])
            circle(screen, [0, 0, 0], [int(self.parametry[0]), int(self.parametry[1])],
                   self.parametry[2] + 3, 3)
        if (self.parametry[5] - self.time_of_birthday > 150) and (
                self.parametry[5] - self.time_of_birthday < 201):
            circle(screen, [255, 255, 0], [int(self.parametry[0]), int(self.parametry[1])],
                   self.parametry[2])
            circle(screen, [0, 0, 0], [int(self.parametry[0]), int(self.parametry[1])],
                   self.parametry[2] + 3, 3)
        if self.parametry[5] - self.time_of_birthday > 200:
            explosion(int(self.parametry[0]), int(self.parametry[1]),
                      self.parametry[5] - self.time_of_birthday - 200)

    def check(self, hero, cursor):
        if abs((cursor[1] - hero[1]) * self.parametry[0] + (hero[0] - cursor[0]) * self.parametry[1] - hero[0] * (
                cursor[1] - hero[1]) + hero[1] * (cursor[0] - hero[0])) / numpy.sqrt(
            (cursor[1] - hero[1]) * (cursor[1] - hero[1]) + (cursor[0] - hero[0]) * (cursor[0] - hero[0])) < \
                self.parametry[2]:
            return 1
        else:
            return 0


clock = pygame.time.Clock()
finished = False

shar_1 = SharOdin()
print(shar_1.parametry)
shar_2 = SharOdin()
shar_3 = SharOdin()
shar_4 = SharOdin()
shar_5 = SharOdin()
player = Hero()

while not finished:
    clock.tick(FPS)
    screen.fill([0, 0, 0])
    polygon(screen, [255, 255, 255], [[100, 100], [100, 600], [900, 600], [900, 100]], 5)
    time += 1
    screen.blit(f1.render('score = ' + str(score), 1, (255, 255, 255)), (0, 0))
    shar_1.dvizh()
    shar_1.risyi()
    keys = pygame.key.get_pressed()
    # движения игрока, если нажата одна из клавиш wasd
    if keys[pygame.K_w]:
        player.vverh()
    if keys[pygame.K_a]:
        player.vlevo()
    if keys[pygame.K_s]:
        player.vniz()
    if keys[pygame.K_d]:
        player.vpravo()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEMOTION:
            cursor_pos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.button == 1) or (event.button == 3):
                cursor_pos = event.pos
                player.vystrel()
                if shar_1.check([player.x, player.y], cursor_pos):
                    score += 1
                    shar_1 = SharOdin()
    player.risyi(cursor_pos)
    pygame.display.update()
pygame.quit()
