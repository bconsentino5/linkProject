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
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (206, 7, 232)
PURPLE = (151, 7, 250)
DARKPURPLE = (90, 3, 149)
GRAY = (28, 28, 28)

# start menu stuff
game_state = 'start_menu'

# Initialize input_text
input_text = ""

def draw_start_menu():
    windowSurface.fill(BLACK) 

    # Load the PNG image
    logo = pygame.image.load('screen.png')
    logo = pygame.transform.scale(logo, (1800, 1700)) #size of image

    play = pygame.image.load('pressSPACE.png')
    play = pygame.transform.scale(play, (600, 300)) #size of image

    # Location of image
    logo_rect = logo.get_rect(topleft=(-500, -400))

    play_rect = play.get_rect(topleft=(200, 500))

    #shows stuff on screen
    windowSurface.blit(logo, logo_rect) 
    windowSurface.blit(play, play_rect) 
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                start_game()

# main game page
def start_game():
    global game_state
    game_state = "game"
    global input_text
    input_text = ""

def game():
    global input_text  # Declare input_text as global

    windowSurface.fill(BLACK) #makes screen black

    clouds = pygame.image.load('clouds.png') #import image
    clouds = pygame.transform.scale(clouds, (1800, 1200)) #size of image
    clouds_rect = clouds.get_rect(topleft=(-300, -280)) #postition of image
    windowSurface.blit(clouds, clouds_rect) #puts image on screen

    logo = pygame.image.load('LINK_logo.png') #import image
    logo = pygame.transform.scale(logo, (400, 200)) #size of image
    logo_rect = logo.get_rect(topleft=(300, 50)) #postition of image
    windowSurface.blit(logo, logo_rect) #puts image on screen
    
    # Draw rectangle
    pygame.draw.rect(windowSurface, PURPLE, pygame.Rect(120, 250, 750, 700)) #big rectangle
    pygame.draw.rect(windowSurface, DARKPURPLE, pygame.Rect(150, 280, 690, 600)) #small rectangle

    # Display typed text
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render(input_text, True, WHITE)
    text_rect = text_surface.get_rect(topleft=(200, 300))
    windowSurface.blit(text_surface, text_rect)

    pygame.display.update()

    # Handle typing
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                input_text = input_text[:-1]  # Remove last character
            elif event.key == K_RETURN:
                # Here you would handle the entered word, for now just print it
                print("Entered word:", input_text)
                input_text = ""  # Clear the input for the next word
            else:
                input_text += event.unicode  # Add the character to the input text

# Main game loop
while True:
    # Check for quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if game_state == "start_menu":  # if game is in the start menu
        draw_start_menu()

    elif game_state == "game":  # if game is in the game
        game()

    mainClock.tick(40)


# Main game loop
while True:
    # Check for quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if game_state == "start_menu": #if game is in the start menu
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]: #if space bar pressed it will take you to game
            start_game()

    elif game_state == "game": #if game is in the game
        game()
        mainClock.tick(40)