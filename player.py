import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS


class Player(CircleShape):
    def __init__(self, x, y):
        # Call parent constructor with position and radius
        super().__init__(x, y, PLAYER_RADIUS)
        # Initialize rotation
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # Draw the player as a white triangle with line width 2
        pygame.draw.polygon(screen, "white", self.triangle(), 2)