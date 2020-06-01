from config import CONFIG
import pygame
import random
import math

class Obstacle:
    def __init__(self):
        self.position = (CONFIG["window_width"], 550)
        self.size = (450, 100)
        self.velocity = (-100, 0)
        self.color = (100, 100, 100)
        self.variant = "M"

    def update(self):
        # Linear calculation
        pos_x, pos_y = self.position
        velocity_x, velocity_y = self.velocity

        self.position = (
            pos_x + velocity_x,
            pos_y + velocity_y,
        )

    def draw(self, window: pygame.Surface):
        surface = pygame.Surface(self.size)
        surface.set_colorkey((0, 0, 0))

        pygame.draw.rect(surface, self.color, ((0, 0), self.size))

        center = (
            self.position[0] + self.size[0] / 2,
            self.position[1] + self.size[1] / 2,
        )
        
        if self.position[0] < -450:
            self.size = (random.randrange(200, 600), 100)

            if self.size[0] < 350:
                self.variant = "S"
            elif self.size[0] < 450:
                self.variant = "M"
            else:
                self.variant = "L"

            self.position = (CONFIG["window_width"]+random.randrange(-50, 150), 550)
        # draw on window surface
        window.blit(surface, self.position)