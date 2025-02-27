import pygame

from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # sprite groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # class group containers
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)
    Player.containers = (drawable, updatable)


    # class instances
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame. QUIT:
                return
        screen.fill("black")
        for p in drawable:
            p.draw(screen)
        for p in updatable:
            p.update(dt)
        for a in asteroids:
            for s in shots:
                if a.hit(s):
                    a.split()
                    s.kill()

        for a in asteroids:
            if a.hit(player):
                print('Game Over')
                exit(0)


        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
