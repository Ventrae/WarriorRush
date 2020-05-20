import pygame
import math

class Character:
    def __init__(self, character_number):
        self.character_number = character_number
        self.position = (100, 300)
        self.velocity = (0, 0)
        self.acceleration = (0, 0)
        self.size = (200, 300)
        self.color = (255, 0, 0)
        self.isInMidair = False

    def update(self, deltaT):
        # Linear calculation
        pos_x, pos_y = self.position
        velocity_x, velocity_y = self.velocity
        acceleration_x, acceleration_y = self.acceleration

        self.velocity = (acceleration_x * deltaT + velocity_x, acceleration_y * deltaT + velocity_y)
        self.position = [
            pos_x + velocity_x * deltaT + 0.5 * acceleration_x * deltaT ** 2,
            pos_y + velocity_y * deltaT + 0.5 * acceleration_y * deltaT ** 2,
        ]

    def draw(self, window: pygame.Surface):
        surface = pygame.Surface(self.size)
        surface.set_colorkey((0, 0, 0))

        pygame.draw.rect(surface, self.color, ((0, 0), self.size))
        # myimage = pygame.image.load("assets\\knights\\knight-1.gif")
        # image_resized = pygame.transform.rotozoom(myimage, 0, self.size[0]/myimage.get_rect()[2])
        
        center = (
            self.position[0] + self.size[0] / 2,
            self.position[1] + self.size[1] / 2,
        )
        if self.position[1] > 300:
            self.position = (100, 300)
            self.acceleration = (0, 0)
            self.isInMidair = False

        # draw on window surface
        window.blit(surface, self.position)

    def jump(self):
        self.acceleration = (0, 900)
        self.velocity = (0, -550)
        self.isInMidair = True