print('z ujdyjtl')


import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 720))
screen.fill((255, 255, 255))

circle(screen, (255, 255, 0), (600, 400), 200)
circle(screen, (255, 0, 0), (500, 350), 40)
circle(screen, (255, 0, 0), (700, 350), 30)
circle(screen, (0, 0, 0), (500, 350), 20)
circle(screen, (0, 0, 0), (700, 350), 15)
line(screen, (0, 0, 0), (500, 500), (700, 500), 50)
polygon(screen, (0, 0, 0), [[550,360], [560, 350], [450, 240], [440, 250]])
polygon(screen, (0, 0, 0), [[650, 350], [644, 340], [764, 270], [770, 280]])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()