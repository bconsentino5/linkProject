import pygame
import sys
from pygame.locals import *

# Set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# Set up window
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption("Link")

# colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (250, 195, 226)
PURPLE = (202, 102, 242)
purplegray = (25, 24, 26)

# set up title of page
font = pygame.font.SysFont('ariel', 100)
text = font.render('Link', True, PURPLE)
textRect = text.get_rect()
textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 900)

#start menu stuff
game_state = 'start_menu'

def draw_start_menu():
    windowSurface.fill(purplegray) 
    # Load the PNG image
    logo = pygame.image.load('LINK_logo.png')
    logo = pygame.transform.scale(logo, (800, 400)) #size of image

    # Location of image
    logo_rect = logo.get_rect(topleft=(100, 100))
     
     #shows stuff on screen
    prompt = font.render('Press SPACE to continue', True, PURPLE)
    windowSurface.blit(prompt, (WINDOW_WIDTH/2 - prompt.get_width()/2, WINDOW_HEIGHT/2 + prompt.get_height()))
    windowSurface.blit(logo, logo_rect) 
    pygame.display.update()

def start_game():
    global game_state
    game_state = "game"

def game():
    windowSurface.fill(BLACK)
    # Draw rectangle
    pygame.draw.rect(windowSurface, PINK, pygame.Rect(400, 50, 200, 100))
    # Draw text
    windowSurface.blit(text, textRect)
    pygame.display.update()
    


# Main game loop
while True:
    # Check for quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if game_state == "start_menu":
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            start_game()

    elif game_state == "game":
        game()
        mainClock.tick(40)