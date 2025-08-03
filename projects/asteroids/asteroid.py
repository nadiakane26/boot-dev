import pygame
from circleshape import CircleShape  
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # Move the asteroid in a straight line at constant speed
        self.position.x += self.velocity[0] * dt
        self.position.y += self.velocity[1] * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create new asteroids at same position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = vel1*1.2

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = vel2*1.2
