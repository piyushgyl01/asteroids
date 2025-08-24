import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        # Call parent constructor with position and shot radius
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        # Draw the shot as a white filled circle
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        # Move in a straight line at constant speed
        self.position += self.velocity * dt