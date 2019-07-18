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

# initialising the background music

# initialise mixer
pygame.mixer.init()
# load song
pygame.mixer.music.load("DST-TowerDefenseTheme.mp3")
# play and loop song indefinitely
pygame.mixer.music.play(loops=-1)

# defining colours

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (0, 255, 255)
DARK_BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PINK = (255, 182, 193)

# defining fonts

# start screen
game_name_font = pygame.font.SysFont("monospace", min((HEIGHT // 18), (WIDTH // 23)))
start_game_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
go_controls_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
get_credits_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
# controls screen
controls_title_font = pygame.font.SysFont("monospace", min((HEIGHT // 18), (WIDTH // 23)))
orientation_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
pause_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
restart_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
g_start_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
back_start_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
quit_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
# pause screen
unpause_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
paused_restart_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
# credits screen
credits_font = pygame.font.SysFont("monospace", min((HEIGHT // 18), (WIDTH // 23)))
developed_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
audio_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
get_start_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))

# creating the start screen

# variable that checks what screen we are on
start_screen = True
# background colour
START_BACKGROUND_COLOUR = BLACK
# name of game
game_name_text = "Keyboard Tetris"
game_name_label = game_name_font.render(game_name_text, 1, WHITE)
game_name_rect = game_name_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 200))  # arbitrary positioning
# how to go to the controls screen
start_game_text = "[g]: Start the game"
start_game_label = start_game_font.render(start_game_text, 1, WHITE)
start_game_rect = start_game_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))  # arbitrary positioning
# how to start the game
go_controls_text = "[c]: Controls"
go_controls_label = go_controls_font.render(go_controls_text, 1, WHITE)
go_controls_rect = go_controls_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))  # arbitrary positioning
# how to check credits
get_credits_text = "[x]: Credits"
get_credits_label = get_credits_font.render(get_credits_text, 1, WHITE)
get_credits_rect = get_credits_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))  # arbitrary positioning

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
pause_rect = pause_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))  # arbitrary positioning
# restart when in-game
restart_text = "[r]: Restart the game when in-game"
restart_label = restart_font.render(restart_text, 1, WHITE)
restart_rect = restart_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))  # arbitrary positioning
# start game
g_start_text = "[g]: Start the game"
g_start_label = g_start_font.render(g_start_text, 1, WHITE)
g_start_rect = g_start_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 ))  # arbitrary positioning
# back to start screen
back_start_text = "[c]: Go back to the Start screen"
back_start_label = back_start_font.render(back_start_text, 1, WHITE)
back_start_rect = back_start_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))  # arbitrary positioning
# quit the game
quit_text = "[esc]: Quit the game"
quit_label = quit_font.render(quit_text, 1, WHITE)
quit_rect = quit_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 100))  # arbitrary positioning

# creating the pause screen
# this will be almost identical to the controls screen

# unpause the game
unpause_text = "[p]: Unpause the game"
unpause_label = unpause_font.render(unpause_text, 1, WHITE)
unpause_rect = unpause_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))  # arbitrary positioning
# restart when in-game
paused_restart_text = "[r]: Restart the game"
paused_restart_label = paused_restart_font.render(paused_restart_text, 1, WHITE)
paused_restart_rect = paused_restart_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))  # arbitrary positioning
# variable that checks what screen we are on
pause_screen = False

# creating the credits screen

# variable that checks what screen we are on
credits_screen = False
# background colour
CREDITS_BACKGROUND_COLOUR = BLACK
# credits title
credits_text = "Credits"
credits_label = credits_font.render(credits_text, 1, WHITE)
credits_rect = credits_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 200))  # arbitrary positioning
# game made by Ebrahim Steenkamp
developed_text = "Developed by Ebrahim Steenkamp"
developed_label = developed_font.render(developed_text, 1, WHITE)
developed_rect = developed_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))  # arbitrary positioning
# audio produce by DST
audio_text = "Audio by DST"
audio_label = audio_font.render(audio_text, 1, WHITE)
audio_rect = audio_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))  # arbitrary positioning
# go to start screen
get_start_text = "[x]: Start screen"
get_start_label = get_start_font.render(get_start_text, 1, WHITE)
get_start_rect = get_start_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))  # arbitrary positioning

# creating the game screen

# variable that checks what screen we are on
game_screen = False

# how many blocks should make up the height of the tetris game
height_amount = 22
# how many blocks should make up the width of the tetris game
width_amount = 12
# block dimensions
block_size = int(min(WIDTH / width_amount, HEIGHT / height_amount))


# creating the Block class for re-use
class Block:

    # initial properties of class
    def __init__(self, x, y, colour, block_size):
        # finding dimensions of blocks
        self.block_outer = block_size
        self.block_inner = int(block_size * 0.98)
        self.block_diff = self.block_outer - self.block_inner
        # border colour
        self.border = WHITE
        # block colour
        self.colour = colour
        # x top of the block
        self.x = x
        # y top of the block
        self.y = y

    # drawing the block with its border
    def draw(self):
        pygame.draw.rect(screen, self.border, [self.x, self.y, self.x + self.block_outer, self.y + self.block_outer])
        pygame.draw.rect(screen, self.colour, [self.x + self.block_diff, self.y + self.block_diff,
                                               self.x + self.block_outer - self.block_diff,
                                               self.y + self.block_outer - self.block_diff])


# drawing the border of the game
def draw_border(width_amount, height_amount, block_size):
    for idx_1 in range(height_amount - 1):
        for idx_2 in [0, 11]:
            block = Block(idx_2 * block_size, idx_1 * block_size, BLACK, block_size)
            block.draw()
    else:
        for idx_2 in range(width_amount):
            block = Block(idx_2 * block_size, idx_1 * block_size, BLACK, block_size)
            block.draw()


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
            # checking for credits screen
            if event.key == pygame.K_x:
                credits_screen = not credits_screen
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
        if not controls_screen and not credits_screen:
            # fill background
            screen.fill(START_BACKGROUND_COLOUR)
            # write the name of the game
            screen.blit(game_name_label, game_name_rect)
            # write how to start the game
            screen.blit(start_game_label, start_game_rect)
            # write how to go to the controls
            screen.blit(go_controls_label, go_controls_rect)
            # write how to go to the credits screen
            screen.blit(get_credits_label, get_credits_rect)
            # update the screen
            pygame.display.update()

        # credits screen
        if not controls_screen and credits_screen:
            # fill background
            screen.fill(CREDITS_BACKGROUND_COLOUR)
            # write credits text
            screen.blit(credits_label, credits_rect)
            # write developed text
            screen.blit(developed_label, developed_rect)
            # write audio text
            screen.blit(audio_label, audio_rect)
            # write how to get to start text
            screen.blit(get_start_label, get_start_rect)
            # update the screen
            pygame.display.update()

        # controls screen
        if controls_screen:
            # fill background
            screen.fill(CONTROLS_BACKGROUND_COLOUR)
            # write controls title
            screen.blit(controls_title_label, controls_title_rect)
            # write orientation text
            screen.blit(orientation_label, orientation_rect)
            # write pause text
            screen.blit(pause_label, pause_rect)
            # write restart text
            screen.blit(restart_label, restart_rect)
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
            screen.fill(BLACK)

            draw_border(width_amount, height_amount, block_size)
            pygame.display.update()

        # pause screen
        if pause_screen:
            # fill background
            screen.fill(CONTROLS_BACKGROUND_COLOUR)
            # write controls title
            screen.blit(controls_title_label, controls_title_rect)
            # write orientation text
            screen.blit(orientation_label, orientation_rect)
            # write unpause text
            screen.blit(unpause_label, unpause_rect)
            # write restart text
            screen.blit(paused_restart_label, paused_restart_rect)
            # write quit text
            screen.blit(quit_label, quit_rect)
            # update the screen
            pygame.display.update()
