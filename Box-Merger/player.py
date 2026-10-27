import pygame
from entity import Entity

class Player(Entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.speed = 250

    def update(self, dt, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed * dt
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed * dt
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed * dt