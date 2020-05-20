from config import CONFIG
import pygame
import math

class Ground:
    def __init__(self):
        self.position = (0, CONFIG["window_height"]-100)
        self.size = (CONFIG["window_width"], 200)
        self.color = (80, 180, 80)

    def draw(self, window: pygame.Surface):
        surface = pygame.Surface(self.size)
        surface.set_colorkey((0, 0, 0))
        pygame.draw.rect(surface, self.color, ((0, 0), self.size))
        center = (
            self.position[0] + self.size[0] / 2,
            self.position[1] + self.size[1] / 2,
        )
        # draw on window surface
        window.blit(surface, self.position)