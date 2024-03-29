import os
import pygame
import sys
import math
import random


# initialising the screen

# center the new window that opens
os.environ["SDL_VIDEO_CENTERED"] = "1"
# default screen values
WIDTH = 800
HEIGHT = 594
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
#pygame.mixer.music.play(loops=-1)  # disabled music since i listen to music while working
# checking if music should be paused
pause_music = False

# defining colours

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (0, 255, 255)
DARK_BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PINK = (255, 20, 147)
GREY = (128, 128, 128)

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
pause_music_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
unpause_music_font = pygame.font.SysFont("monospace", min((HEIGHT // 25), (WIDTH // 30)))
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
g_start_rect = g_start_label.get_rect(center=(WIDTH / 2, HEIGHT / 2))  # arbitrary positioning
# pause the music
pause_music_text = "[q]: Pause music"
pause_music_label = pause_music_font.render(pause_music_text, 1, WHITE)
pause_music_rect = pause_music_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))  # arbitrary positioning
# unpause the music
unpause_music_text = "[q]: Unpause music"
unpause_music_label = unpause_music_font.render(unpause_music_text, 1, WHITE)
unpause_music_rect = unpause_music_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))  # arbitrary positioning
# back to start screen
back_start_text = "[c]: Go back to the Start screen"
back_start_label = back_start_font.render(back_start_text, 1, WHITE)
back_start_rect = back_start_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 100))  # arbitrary positioning
# quit the game
quit_text = "[esc]: Quit the game"
quit_label = quit_font.render(quit_text, 1, WHITE)
quit_rect = quit_label.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 150))  # arbitrary positioning

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
# background colour
PAUSE_BACKGROUND_COLOUR = BLACK

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
# game background colour
GAME_BACKGROUND_COLOUR = BLACK
# how many blocks should make up the height of the tetris game
height_amount = 22
# how many blocks should make up the width of the tetris game
width_amount = 12
# block dimensions
block_size = math.floor(min(WIDTH / width_amount, HEIGHT / height_amount))


# creating the Block class for re-use
class Block:

    # initial properties of class
    def __init__(self, x, y, colour, block_size):
        # finding dimensions of blocks
        self.block_outer = block_size
        self.block_inner = block_size * 0.98
        self.block_diff = math.ceil(self.block_outer - self.block_inner)
        # border colour
        self.border = BLACK
        # block colour
        self.colour = colour
        # x top of the block
        self.x = x
        # y top of the block
        self.y = y

    # drawing the block with its border
    def draw(self):
        pygame.draw.rect(screen, self.border, [self.x, self.y, self.block_outer, self.block_outer])
        pygame.draw.rect(screen, self.colour, [self.x + self.block_diff, self.y + self.block_diff,
                                               self.block_outer - 2 * self.block_diff,
                                               self.block_outer - 2 * self.block_diff])


# creating the Z-block class for re-use
class Zblock:

    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.block_size = block_size
        self.colour = LIGHT_BLUE

    def left(self):
        block = Block(self.x, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 2 * self.block_size, self.y + self.block_size, self.colour, self.block_size)
        block.draw()

    def up(self):
        block = Block(self.x + self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + 2 * self.block_size, self.colour, self.block_size)
        block.draw()

    def orient(self, orientation):
        if orientation == "left" or orientation == "right":
            self.left()
        else:
            self.up()


# creating the S-block class for re-use
class Sblock:

    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.block_size = block_size
        self.colour = ORANGE

    def left(self):
        block = Block(self.x, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 2 * self.block_size, self.y, self.colour, self.block_size)
        block.draw()

    def up(self):
        block = Block(self.x, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y + 2 * self.block_size, self.colour, self.block_size)
        block.draw()

    def orient(self, orientation):
        if orientation == "left" or orientation == "right":
            self.left()
        else:
            self.up()


# creating the I-block class for re-use
class Iblock:

    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.block_size = block_size
        self.colour = RED

    def left(self):
        block = Block(self.x, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 2 * self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 3 * self.block_size, self.y, self.colour, self.block_size)
        block.draw()

    def up(self):
        block = Block(self.x, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + 2 * self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + 3 * self.block_size, self.colour, self.block_size)
        block.draw()

    def orient(self, orientation):
        if orientation == "left" or orientation == "right":
            self.left()
        elif orientation == "up" or orientation == "down":
            self.up()


# creating the O-block class for re-use
class Oblock:

    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.block_size = block_size
        self.colour = GREEN

    def left(self):
        block = Block(self.x, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y + self.block_size, self.colour, self.block_size)
        block.draw()

    def orient(self, orientation):
        if orientation == "left" or orientation == "right" or orientation == "up" or orientation == "down":
            self.left()


# creating the L-block class for re-use
class Lblock:

    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.block_size = block_size
        self.colour = PINK

    def left(self):
        block = Block(self.x, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 2 * self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 3 * self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 3 * self.block_size, self.y - self.block_size, self.colour, self.block_size)
        block.draw()

    def up(self):
        block = Block(self.x, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + 2 * self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + 3 * self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y + 3 * self.block_size, self.colour, self.block_size)
        block.draw()

    def right(self):
        block = Block(self.x, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 2 * self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 3 * self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + self.block_size, self.colour, self.block_size)
        block.draw()

    def down(self):
        block = Block(self.x, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + 2 * self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + 3 * self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x - self.block_size, self.y, self.colour, self.block_size)
        block.draw()

    def orient(self, orientation):
        if orientation == "left":
            self.left()
        elif orientation == "right":
            self.right()
        elif orientation == "up":
            self.up()
        elif orientation == "down":
            self.down()


# creating the J-block class for re-use
class Jblock:

    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.block_size = block_size
        self.colour = YELLOW

    def left(self):
        block = Block(self.x, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 2 * self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 3 * self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 3 * self.block_size, self.y + self.block_size, self.colour, self.block_size)
        block.draw()

    def up(self):
        block = Block(self.x, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + 2 * self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + 3 * self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x - self.block_size, self.y + 3 * self.block_size, self.colour, self.block_size)
        block.draw()

    def right(self):
        block = Block(self.x, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 2 * self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 3 * self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y - self.block_size, self.colour, self.block_size)
        block.draw()

    def down(self):
        block = Block(self.x, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + 2 * self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x, self.y + 3 * self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y, self.colour, self.block_size)
        block.draw()

    def orient(self, orientation):
        if orientation == "left":
            self.left()
        elif orientation == "right":
            self.right()
        elif orientation == "up":
            self.up()
        elif orientation == "down":
            self.down()


# creating the T-block class for re-use
class Tblock:

    def __init__(self, x, y, block_size):
        self.x = x
        self.y = y
        self.block_size = block_size
        self.colour = DARK_BLUE

    def left(self):
        block = Block(self.x, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y + 2 * self.block_size, self.colour, self.block_size)
        block.draw()

    def up(self):
        block = Block(self.x, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 2 * self.block_size, self.y + self.block_size, self.colour, self.block_size)
        block.draw()

    def right(self):
        block = Block(self.x + 2 * self.block_size, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y + 2 * self.block_size, self.colour, self.block_size)
        block.draw()

    def down(self):
        block = Block(self.x, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y + 2 * self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + self.block_size, self.y + self.block_size, self.colour, self.block_size)
        block.draw()
        block = Block(self.x + 2 * self.block_size, self.y + self.block_size, self.colour, self.block_size)
        block.draw()

    def orient(self, orientation):
        if orientation == "left":
            self.left()
        elif orientation == "right":
            self.right()
        elif orientation == "up":
            self.up()
        elif orientation == "down":
            self.down()


# drawing the border of the game
def draw_border(width_amount, height_amount, block_size):
    # for each row in the border besides the last
    for row in range(height_amount - 1):
        # for each side of the border
        for col in [0, width_amount - 1]:
            # create the block
            block = Block(col * block_size, row * block_size, GREY, block_size)
            # draw the block
            block.draw()
    # for the last row in the border
    else:
        # for every block in the last row
        for col in range(width_amount):
            # create the block
            block = Block(col * block_size, (height_amount - 1) * block_size, GREY, block_size)
            # draw the block
            block.draw()


# creating the player block for re-use
class PlayerBlock:

    def __init__(self, block_size):
        self.choice = random.choice(["Z", "S", "I", "O", "L", "J", "T"])
        self.orientation = "left"
        self.block = None
        self.block_size = block_size

    def assign_block(self):
        if self.choice == "Z":
            x = random.randint(1, 8)
            self.block = Zblock(x * block_size, 0, self.block_size)
        if self.choice == "S":
            x = random.randint(1, 8)
            self.block = Sblock(x * block_size, 0, self.block_size)
        if self.choice == "I":
            x = random.randint(1, 7)
            self.block = Iblock(x * block_size, 0, self.block_size)
        if self.choice == "O":
            x = random.randint(1, 9)
            self.block = Oblock(x * block_size, 0, self.block_size)
        if self.choice == "L":
            x = random.randint(1, 7)
            self.block = Lblock(x * block_size, block_size, self.block_size)
        if self.choice == "J":
            x = random.randint(1, 7)
            self.block = Jblock(x * block_size, 0, self.block_size)
        if self.choice == "T":
            x = random.randint(1, 9)
            self.block = Tblock(x * block_size, 0, self.block_size)
        return self.block

    def draw(self):
        block = self.assign_block()
        block.orient(self.orientation)





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
            # pausing the music
            if event.key == pygame.K_q:
                pause_music = not pause_music
                if pause_music:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            # checking for controls screen
            if event.key == pygame.K_c:
                if start_screen:
                    if not credits_screen:
                        controls_screen = not controls_screen
            # checking for credits screen
            if event.key == pygame.K_x:
                if start_screen:
                    if not controls_screen:
                        credits_screen = not credits_screen
            # checking to see if the actual game needs to start
            if event.key == pygame.K_g:
                start_screen = False
                game_screen = True
            # checking to see if the game should be paused
            if event.key == pygame.K_p:
                if game_screen:
                    pause_screen = not pause_screen

            if game_screen and not pause_screen:
                # checking directional arrows
                if event.key == pygame.K_UP:
                    print("up")
                if event.key == pygame.K_DOWN:
                    print("down")
                if event.key == pygame.K_LEFT:
                    print("left")
                if event.key == pygame.K_RIGHT:
                    print("right")

    if start_screen:

        # start screen
        if not controls_screen and not credits_screen:
            # fill background
            screen.fill(START_BACKGROUND_COLOUR)
            # writing text
            for i, j in [[game_name_label, game_name_rect], [start_game_label, start_game_rect],
                         [go_controls_label, go_controls_rect], [get_credits_label, get_credits_rect]]:
                screen.blit(i, j)

        # credits screen
        if not controls_screen and credits_screen:
            # fill background
            screen.fill(CREDITS_BACKGROUND_COLOUR)
            # writing text to screen
            for i, j in [[credits_label, credits_rect], [developed_label, developed_rect], [audio_label, audio_rect],
                         [get_start_label, get_start_rect]]:
                screen.blit(i, j)

        # controls screen
        if controls_screen:
            # fill background
            screen.fill(CONTROLS_BACKGROUND_COLOUR)
            # writing text
            for i, j in [[controls_title_label, controls_title_rect], [orientation_label, orientation_rect],
                         [pause_label, pause_rect], [restart_label, restart_rect], [g_start_label, g_start_rect],
                         [back_start_label, back_start_rect], [quit_label, quit_rect]]:
                screen.blit(i, j)

            if not pause_music:
                # pause music text
                screen.blit(pause_music_label, pause_music_rect)
            else:
                # unpause music text
                screen.blit(unpause_music_label, unpause_music_rect)

    # actually playing the game
    elif game_screen:

        # game screen
        if not pause_screen:
            screen.fill(GAME_BACKGROUND_COLOUR)

            draw_border(width_amount, height_amount, block_size)

            if random.random() < 0.05:
                PlayerBlock(block_size).draw()


        # pause screen
        if pause_screen:
            # fill background
            screen.fill(PAUSE_BACKGROUND_COLOUR)
            # writing text
            for i, j in [[controls_title_label, controls_title_rect], [orientation_label, orientation_rect],
                         [unpause_label, unpause_rect], [paused_restart_label, paused_restart_rect],
                         [quit_label, quit_rect]]:
                screen.blit(i, j)

            if not pause_music:
                # pause music text
                screen.blit(pause_music_label, pause_music_rect)
            else:
                # unpause music text
                screen.blit(unpause_music_label, unpause_music_rect)

    # update the screen
    pygame.display.update()
