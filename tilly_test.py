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

# Start menu stuff
game_state = 'start_menu'

# Initialize input_text
input_text = ""

# Words for the game
word1 = "apple"
word2 = "pie"

def draw_start_menu():
    windowSurface.fill(BLACK)

    # Load the PNG image
    logo = pygame.image.load('screen.png')
    logo = pygame.transform.scale(logo, (1800, 1700))  # Size of image

    play = pygame.image.load('pressSPACE.png')
    play = pygame.transform.scale(play, (600, 300))  # Size of image

    # Location of image
    logo_rect = logo.get_rect(topleft=(-500, -400))

    play_rect = play.get_rect(topleft=(200, 500))

    # Shows stuff on screen
    windowSurface.blit(logo, logo_rect)
    windowSurface.blit(play, play_rect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                start_game()

def start_game():
    global game_state
    game_state = "game"
    global input_text
    input_text = ""

def game():
    global input_text  # Declare input_text as global

    windowSurface.fill(BLACK)

    clouds = pygame.image.load('clouds.png')
    clouds = pygame.transform.scale(clouds, (1800, 1200))
    clouds_rect = clouds.get_rect(topleft=(-300, -280))
    windowSurface.blit(clouds, clouds_rect)

    logo = pygame.image.load('LINK_logo.png')
    logo = pygame.transform.scale(logo, (400, 200))
    logo_rect = logo.get_rect(topleft=(300, 50))
    windowSurface.blit(logo, logo_rect)

    # Draw rectangle
    pygame.draw.rect(windowSurface, PURPLE, pygame.Rect(120, 250, 750, 700))
    pygame.draw.rect(windowSurface, DARKPURPLE, pygame.Rect(150, 280, 690, 600))

    # Display the two words to the player
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render("Word 1: " + word1, True, WHITE)
    text_rect = text_surface.get_rect(topleft=(200, 300))
    windowSurface.blit(text_surface, text_rect)

    text_surface2 = font.render("Word 2: " + word2, True, WHITE)
    text_rect2 = text_surface2.get_rect(topleft=(200, 350))
    windowSurface.blit(text_surface2, text_rect2)

    # Display typed text
    text_surface3 = font.render("Your Guess: " + input_text, True, WHITE)
    text_rect3 = text_surface3.get_rect(topleft=(200, 400))
    windowSurface.blit(text_surface3, text_rect3)

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
                # Here you would check the entered guess against the link
                check_guess(input_text)
                input_text = ""  # Clear the input for the next guess
            else:
                input_text += event.unicode  # Add the character to the input text

def check_guess(guess):
    # Here you would check the guess against the link between word1 and word2
    # For now, let's just print the guess
    print("Your guess:", guess)

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
