from config import CONFIG
import pygame
import math



class Background:
    def __init__(self):
        self.position = (0, 0)
        self.size = (CONFIG["window_width"], CONFIG["window_height"])
        self.color = (80, 80, 180)
        self.distance = 0
        self.laps = 0

    def highscore(self):
        return 500*self.laps+self.distance

    def draw(self, window: pygame.Surface):
        surface = pygame.Surface(self.size)
        surface.set_colorkey((0, 0, 0))

        self.distance += 1
        print("Przebyta odległość: {}".format(self.highscore()))
        
        if self.distance < 500:
            myimage = pygame.image.load("assets\\background\\background-1.png")
        elif self.distance < 1000:
            myimage = pygame.image.load("assets\\background\\background-2.png")
        elif self.distance < 1500:
            myimage = pygame.image.load("assets\\background\\background-3.png")
        else:
            myimage = pygame.image.load("assets\\background\\background-4.png")
            if self.distance == 2000:
                self.laps += 1
                self.distance = 0

        image_resized = pygame.transform.rotozoom(myimage, 0, CONFIG["window_width"]/myimage.get_rect()[2])
        pygame.draw.rect(surface, self.color, ((0, 0), self.size))
        
        center = (
            self.position[0] + self.size[0] / 2,
            self.position[1] + self.size[1] / 2,
        )
        # draw on window surface 
        window.blit(image_resized, self.position)

    def drawWelcome(self, window: pygame.Surface):
        surface = pygame.Surface(self.size)
        surface.set_colorkey((0, 0, 0))
        myimage = pygame.image.load("assets\\background\\welcome.png")
        image_resized = pygame.transform.rotozoom(myimage, 0, CONFIG["window_width"]/myimage.get_rect()[2])
        pygame.draw.rect(surface, self.color, ((0, 0), self.size))
        center = (
            self.position[0] + self.size[0] / 2,
            self.position[1] + self.size[1] / 2,
        )
        window.blit(image_resized, self.position)