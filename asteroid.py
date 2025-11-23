import random
import pygame
from logger import log_event
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Larger asteroids split into smaller, faster asteroids
        # Small asteroids just die
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        # Create new vectors representing the first new asteroids movement
        random_angle = random.uniform(20, 50)
        new_vector_1 = self.velocity.rotate(random_angle)
        new_vector_2 = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius)
        asteroid.velocity = new_vector_1 * 1.2
        asteroid = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius)
        asteroid.velocity = new_vector_2 * 1.2