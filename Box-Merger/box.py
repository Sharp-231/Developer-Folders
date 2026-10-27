import pygame
from entity import Entity

class Box(Entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.held = False

        