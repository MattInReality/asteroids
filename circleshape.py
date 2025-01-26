import pygame

from constants import HIT_CONTACT_BUFFER


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def hit(self, circle_shape):
        if self.position.distance_to(circle_shape.position) <= (circle_shape.radius + self.radius) - HIT_CONTACT_BUFFER:
            return True
        else:
            return False

