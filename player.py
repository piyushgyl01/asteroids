import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED


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
    
    def rotate(self, dt):
        # Add turn speed * dt to current rotation
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        # Calculate forward vector based on current rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Move in that direction
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left (negative dt for opposite direction)
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # Rotate right (positive dt)
            self.rotate(dt)
        if keys[pygame.K_w]:
            # Move forward (positive dt)
            self.move(dt)
        if keys[pygame.K_s]:
            # Move backward (negative dt for opposite direction)
            self.move(-dt)