import pygame
import random
from player import Player
from box import Box

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = Player(100, 100, 64, 64)
#randX = random.randint(1 + player.w/2, 800 - player.w/2)

#def randomPosition():
#    box1 = Box(randX, )

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