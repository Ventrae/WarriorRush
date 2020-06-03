import pygame
from timeit import default_timer as time
from time import sleep

from config import CONFIG
from utils import CheckIfCollision

from Character import Character
from Ground import Ground
from Obstacle import Obstacle
from Background import Background

character = Character(input("Wybierz bohatera [1-3]:"))
background = Background()
ground = Ground()
obstacle = Obstacle()

pygame.init()

window = pygame.display.set_mode((CONFIG["window_width"], CONFIG["window_height"]))
pygame.display.set_caption("Warrior Rush")

game_on = True
running = False
last = 0

while game_on:

    now = time()
    deltaT = now - last

    # === Event Loop ===

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_on = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False

        if event.type == pygame.KEYDOWN:
            if not running:
                running = True
            else:
                if event.key == pygame.K_SPACE:
                    if not character.isInMidair:
                        character.jump()

    if running:
        # === Physics ===
        character.update(deltaT)
        obstacle.update()

        # === Graphics ===
        window.fill((0, 0, 0))

        background.draw(window)
        ground.draw(window)
        obstacle.draw(window)
        character.draw(window)

        pygame.display.update()

        limiter_wait = True
        while limiter_wait:
            sleep(1 / 480)
            if time() - now >= 1 / int(CONFIG["fps_target"]):
                limiter_wait = False

        last = now

        if CheckIfCollision(character, obstacle):
            game_on = False
    else:
        window.fill((0, 0, 0))
        background.drawWelcome(window)
        pygame.display.update()

print("Koniec gry! Przebiegłeś {} stóp.".format(background.highscore()))