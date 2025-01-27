import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, width=2)

    def update(self, dt):
        vel = self.velocity
        self.position += vel * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vec_one = self.velocity.rotate(angle)
        vec_two = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        left = Asteroid(self.position.x, self.position.y, radius)
        left.velocity = vec_one * 1.2
        right = Asteroid(self.position.x, self.position.y, radius)
        right.velocity = vec_two * 1.2

