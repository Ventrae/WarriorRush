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
        self.img_s = pygame.image.load("assets\\spikes\\spikes-s.png")
        self.img_m = pygame.image.load("assets\\spikes\\spikes-m.png")
        self.img_l = pygame.image.load("assets\\spikes\\spikes-l.png")
        self.img = self.img_m

    def update(self):
        # Linear calculation
        pos_x, pos_y = self.position
        velocity_x, velocity_y = self.velocity

        self.position = (
            pos_x + velocity_x,
            pos_y + velocity_y,
        )

    def draw(self, window: pygame.Surface):
        
        center = (
            self.position[0] + self.size[0] / 2,
            self.position[1] + self.size[1] / 2,
        )
        
        if self.position[0] < -450:
            self.size = (random.randrange(200, 600), 100)

            if self.size[0] < 350:
                self.img = self.img_s
            elif self.size[0] < 450:
                self.img = self.img_m
            else:
                self.img = self.img_l
            
            self.position = (CONFIG["window_width"]+random.randrange(-100, 150), 550)
	
        window.blit(self.img, center)
        # pygame.draw.rect(window, (255, 0, 0), pygame.Rect(self.position, self.size))