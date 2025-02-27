import pygame.draw

from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, SHOT_RADIUS, width=2)

    def update(self, dt):
        vel = self.velocity
        self.position += vel * dt
