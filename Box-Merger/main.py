import pygame
from player import Player

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = Player(100, 100, 64, 64)

running = True

while running:
    dt = clock.tick(75) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(dt, pygame.key.get_pressed())

    screen.fill((0, 0, 0))

    player.draw(screen)

    pygame.display.flip()


pygame.quit()