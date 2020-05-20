import pygame
from timeit import default_timer as time
from time import sleep

from config import CONFIG

from Character import Character
from Ground import Ground
from Background import Background

character = Character(input("Wybierz bohatera:"))
background = Background()
ground = Ground()

pygame.init()

window = pygame.display.set_mode((CONFIG["window_width"], CONFIG["window_height"]))
pygame.display.set_caption("Warrior Rush")

running = True
last = 0

while running:

    now = time()
    deltaT = now - last

    # === Event Loop ===

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                character.start()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not character.isInMidair:
                    character.jump()


    # === Physics ===
    character.update(deltaT)

    # === Graphics ===
    window.fill((0, 0, 0))

    background.draw(window)
    ground.draw(window)
    character.draw(window)

    pygame.display.update()

    limiter_wait = True
    while limiter_wait:
        sleep(1 / 480)
        if time() - now >= 1 / int(CONFIG["fps_target"]):
            limiter_wait = False

    last = now
