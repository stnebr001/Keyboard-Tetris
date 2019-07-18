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

# start screen
game_name_font = pygame.font.SysFont("monospace", min((HEIGHT // 18), (WIDTH // 23)))
start_game_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
go_controls_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
# controls screen
controls_title_font = pygame.font.SysFont("monospace", min((HEIGHT // 18), (WIDTH // 23)))
orientation_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
pause_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
g_start_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
back_start_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
quit_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
# pause screen
unpause_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))

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
start_game_text = "[g]: Start the game"
start_game_label = start_game_font.render(start_game_text, 1, WHITE)
start_game_rect = start_game_label.get_rect(center=(WIDTH / 2, HEIGHT / 2))  # arbitrary positioning
# how to start the game
go_controls_text = "[c]: Controls"
go_controls_label = go_controls_font.render(go_controls_text, 1, WHITE)
go_controls_rect = go_controls_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 100))  # arbitrary positioning

# creating the controls screen

# variable that checks what screen we are on
controls_screen = False
# background colour
CONTROLS_BACKGROUND_COLOUR = BLACK
# title of the screen
controls_title_text = "Controls"
controls_title_label = controls_title_font.render(controls_title_text, 1, WHITE)
controls_title_rect = controls_title_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 250))  # arbitrary positioning
# changing orientation of object
orientation_text = "[arrows]: Change orientation of object"
orientation_label = orientation_font.render(orientation_text, 1, WHITE)
orientation_rect = orientation_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 150))  # arbitrary positioning
# pause when in-game
pause_text = "[p]: Pause when in-game"
pause_label = pause_font.render(pause_text, 1, WHITE)
pause_rect = pause_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))  # arbitrary positioning
# start game
g_start_text = "[g]: Start the game"
g_start_label = g_start_font.render(g_start_text, 1, WHITE)
g_start_rect = g_start_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))  # arbitrary positioning
# back to start screen
back_start_text = "[c]: Go back to the Start screen"
back_start_label = back_start_font.render(back_start_text, 1, WHITE)
back_start_rect = back_start_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 150))  # arbitrary positioning
# quit the game
quit_text = "[esc]: Quit the game"
quit_label = quit_font.render(quit_text, 1, WHITE)
quit_rect = quit_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 250))  # arbitrary positioning

# creating the pause screen
# this will be almost identical to the controls screen
# quit the game
unpause_text = "[p]: Unpause the game"
unpause_label = unpause_font.render(unpause_text, 1, WHITE)
unpause_rect = unpause_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))  # arbitrary positioning

# variable that checks what screen we are on
pause_screen = False

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
            # checking to see if the game should be paused
            if event.key == pygame.K_p:
                if game_screen:
                    pause_screen = not pause_screen

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
            # fill background
            screen.fill(CONTROLS_BACKGROUND_COLOUR)
            # write the controls title
            screen.blit(controls_title_label, controls_title_rect)
            # write the orientation text
            screen.blit(orientation_label, orientation_rect)
            # write the pause text
            screen.blit(pause_label, pause_rect)
            # write start game text
            screen.blit(g_start_label, g_start_rect)
            # write back to the start text
            screen.blit(back_start_label, back_start_rect)
            # write the quit text
            screen.blit(quit_label, quit_rect)
            # update the screen
            pygame.display.update()

    # actually playing the game
    elif game_screen:

        # game screen
        if not pause_screen:
            screen.fill(WHITE)
            pygame.display.update()

        # pause screen
        if pause_screen:
            # fill background
            screen.fill(CONTROLS_BACKGROUND_COLOUR)
            # write the controls title
            screen.blit(controls_title_label, controls_title_rect)
            # write the orientation text
            screen.blit(orientation_label, orientation_rect)
            # write the unpause text
            screen.blit(unpause_label, unpause_rect)
            # write the quit text
            screen.blit(quit_label, quit_rect)
            # update the screen
            pygame.display.update()
