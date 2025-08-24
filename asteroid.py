import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call parent constructor with position and radius
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        # Draw the asteroid as a white circle with line width 2
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        # Move in a straight line at constant speed
        self.position += self.velocity * dt