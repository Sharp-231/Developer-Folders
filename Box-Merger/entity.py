import pygame

class Entity:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.w, self.h))