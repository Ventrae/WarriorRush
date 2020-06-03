import pygame
import math
from config import CONFIG
from time import sleep

class Character:
    def __init__(self, character_number):
        self.character_number = character_number
        self.position = (-250, 300)
        self.velocity = (0, 0)
        self.acceleration = (0, 0)
        self.size = (50, 100)
        self.color = (255, 0, 0)
        self.isInMidair = False
        self.img_r = pygame.transform.rotozoom(
            pygame.image.load("assets\\characters\\{}\\ss_running.png".format(self.character_number)),
        0, 0.5)
        self.img_j = pygame.transform.rotozoom(
            pygame.image.load("assets\\characters\\{}\\ss_jumping.png".format(self.character_number)),
        0, 0.5)
        self.img = self.img_r
        self.frame_nr_r = 0
        self.frame_nr_j = 0
        self.deltaTCounter = 0

    def update(self, deltaT):
        # Linear calculation
        pos_x, pos_y = self.position
        velocity_x, velocity_y = self.velocity
        acceleration_x, acceleration_y = self.acceleration

        self.velocity = (acceleration_x * deltaT + velocity_x, acceleration_y * deltaT + velocity_y)
        self.position = (
            pos_x + velocity_x * deltaT + 0.5 * acceleration_x * deltaT ** 2,
            pos_y + velocity_y * deltaT + 0.5 * acceleration_y * deltaT ** 2,
        )

        if self.img == self.img_r:
            self.frame_nr_r = self.frame_nr_r + 1
            if self.frame_nr_r > 9:
                self.frame_nr_r = 0
        else:
            self.deltaTCounter += deltaT
            if self.deltaTCounter > 1/15:
                self.frame_nr_j = self.frame_nr_j + 1
                if self.frame_nr_j > 9:
                    self.frame_nr_j = 0
                self.deltaTCounter = 0

    def draw(self, window: pygame.Surface):

        if self.position[1] > 300:
            self.position = (-250, 300)
            self.acceleration = (0, 0)
            self.isInMidair = False
            self.img = self.img_r;

        if not self.isInMidair:
            self.renderFrame(window, self.calculate_frame(self.frame_nr_r)[0], self.calculate_frame(self.frame_nr_r)[1])
        else:
            self.renderFrame(window, self.calculate_frame(self.frame_nr_j)[0], self.calculate_frame(self.frame_nr_j)[1])
        

    def jump(self):

        self.img = self.img_j
        self.frame_nr_j = 0
        self.acceleration = (0, 2000)
        self.velocity = (0, -850)
        self.isInMidair = True

    def renderFrame(self, window, x, y):

        width, height = int(self.img.get_width()/3), int(self.img.get_height()/4)
        origin = 0 + width, 0

        center = (
            self.position[0] - self.size[0] / 2,
            self.position[1] - self.size[1] / 2,
        )

        source_area = pygame.Rect((x*width, y*height), (width, height))
        
        window.blit(self.img, center, source_area)

    def calculate_frame(self, frame_nr):
        if frame_nr == 0:
            return (0, 0)
        elif frame_nr == 1:
            return (0, 1)
        elif frame_nr == 2:
            return (0, 2)
        elif frame_nr == 3:
            return (0, 3)
        elif frame_nr == 4:
            return (1, 0)
        elif frame_nr == 5:
            return (1, 1)
        elif frame_nr == 6:
            return (1, 2)
        elif frame_nr == 7:
            return (1, 3)
        elif frame_nr == 8:
            return (2, 0)
        elif frame_nr == 9:
            return (2, 1)
        else:
            return (0, 0)
        