import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        newV1 = self.velocity.rotate(angle)
        newV2 = self.velocity.rotate(angle * -1)
        newR = self.radius - ASTEROID_MIN_RADIUS
        newA1 = Asteroid(self.position.x, self.position.y, newR)
        newA2 = Asteroid(self.position.x, self.position.y, newR)
        newA1.velocity = newV1 * 1.2
        newA2.velocity = newV2 * 1.2