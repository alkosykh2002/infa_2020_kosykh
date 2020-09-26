import pygame

pygame.init()
wndsize = (400, 400)
window = pygame.display.set_mode(wndsize)
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(0)
    pygame.draw.rect(window, (0, 0, 255), (0, 0, 200, 400))

    radius = 100
    circle = pygame.Surface((200, 200), pygame.SRCALPHA)
    pygame.draw.circle(circle, (255, 0, 0, 128), (radius, radius), radius)
    window.blit(circle, (100, 100))

    pygame.display.flip()