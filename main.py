import os
import pygame
import sys
import random

# defining colours

GREEN = (0, 204, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# initialising the screen

# center the new window that opens
os.environ["SDL_VIDEO_CENTERED"] = "1"
# default screen values
WIDTH = 800
HEIGHT = 600
# making a resizable screen
screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.RESIZABLE)
# initialise pygame
pygame.init()

# creating the start screen

# variable that checks what screen we are on
start_screen = True
# background colour
BACKGROUND_COLOUR = BLACK
# name of game
start_text = "Keyboard Tetris"
start_font = pygame.font.SysFont("monospace", min((HEIGHT // 18), (WIDTH // 23)))
start_label = start_font.render(start_text, 1, GREEN)
start_rect = start_label.get_rect(center=(WIDTH / 2, HEIGHT / 2))
#

# creating the controls screen

# variable that checks what screen we are on
controls_screen = False

# creating the game screen

# variable that checks what screen we are on
game_screen = False

# starting the game

while True:

    # pygame is an event based module
    for event in pygame.event.get():

        # exiting program if the window is closed
        if event.type == pygame.QUIT:
            sys.exit()

        # checking key presses
        if event.type == pygame.KEYDOWN:
            # exiting program is escape is pressed
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            # checking for controls screen
            if event.key == pygame.K_c:
                controls_screen = not controls_screen
            # checking to see if the actual game needs to start
            if event.key == pygame.K_g:
                start_screen = False
                game_screen = True

        if start_screen:

            # start screen
            if not controls_screen:
                # fill background
                screen.fill(BACKGROUND_COLOUR)
                # write the name of the game
                screen.blit(start_label, start_rect)
                # update the screen
                pygame.display.update()

            # controls screen
            if controls_screen:
                screen.fill(GREEN)
                pygame.display.update()

        # actual game screen
        elif game_screen:
            screen.fill(WHITE)
            pygame.display.update()
