import os
import pygame
import sys
import random


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

# defining colours

GREEN = (0, 204, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# defining fonts

game_name_font = pygame.font.SysFont("monospace", min((HEIGHT // 18), (WIDTH // 23)))
start_game_font = pygame.font.SysFont("monospace", min((HEIGHT // 18), (WIDTH // 23)))
go_controls_font = pygame.font.SysFont("monospace", min((HEIGHT // 18), (WIDTH // 23)))

# creating the start screen

# variable that checks what screen we are on
start_screen = True
# background colour
START_BACKGROUND_COLOUR = BLACK
# name of game
game_name_text = "Keyboard Tetris"
game_name_label = game_name_font.render(game_name_text, 1, WHITE)
game_name_rect = game_name_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))  # arbitrary positioning
# how to go to the controls screen
start_game_text = "Press [g] to start the game"
start_game_label = start_game_font.render(start_game_text, 1, WHITE)
start_game_rect = start_game_label.get_rect(center=(WIDTH / 2, HEIGHT / 2))  # arbitrary positioning
# how to start the game
go_controls_text = "Press [c] to go to the controls"
go_controls_label = go_controls_font.render(go_controls_text, 1, WHITE)
go_controls_rect = go_controls_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 100))  # arbitrary positioning

# creating the controls screen

# variable that checks what screen we are on
controls_screen = False
# background colour
CONTROLS_BACKGROUND_COLOUR = BLACK

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
                screen.fill(START_BACKGROUND_COLOUR)
                # write the name of the game
                screen.blit(game_name_label, game_name_rect)
                # write how to start the game
                screen.blit(start_game_label, start_game_rect)
                # write how to go to the controls
                screen.blit(go_controls_label, go_controls_rect)
                # update the screen
                pygame.display.update()

            # controls screen
            if controls_screen:
                screen.fill(CONTROLS_BACKGROUND_COLOUR)
                pygame.display.update()

        # actual game screen
        elif game_screen:
            screen.fill(WHITE)
            pygame.display.update()
