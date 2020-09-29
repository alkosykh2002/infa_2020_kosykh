import pygame
import numpy

pygame.init()
wndsize = (400, 400)
window = pygame.display.set_mode(wndsize)
clock = pygame.time.Clock()

koord1 = [0] * 314
koord2 = [0] * 314
for i in range(0, 314):
    koord1[i] = [50 + i, 300 - int(round(300*numpy.sin(i/99.99)))]
    koord2[i] = [50 + i, 300 - int(round(50 * numpy.sin(i/33.333333333333333)))]
koord = koord1 + koord2
print(koord2)

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    pygame.draw.rect(window, (0, 0, 255), (0, 0, 200, 400))

    radius = 100
    circle = pygame.Surface((400, 400), pygame.SRCALPHA)
    pygame.draw.polygon(circle, [255, 255, 255, 100], koord)
    window.blit(circle, (0, 0))

    pygame.display.flip()