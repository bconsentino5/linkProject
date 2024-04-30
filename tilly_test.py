import pygame
import sys
from pygame.locals import *
from combo import Link

from nltk.corpus import wordnet
import random
import requests


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
RED = (255, 0, 0)

# Start menu stuff
game_state = 'start_menu'

# Initialize input_text
input_text = ""

# Words for the game
word1 = "mom"
word2 = "dad"
ans_display = ""

link = Link()
words = link.get_words()


def draw_start_menu():
    windowSurface.fill(BLACK)

    clouds = pygame.image.load('clouds.png')
    clouds = pygame.transform.scale(clouds, (1800, 1200))
    clouds_rect = clouds.get_rect(topleft=(-400, -280))
    windowSurface.blit(clouds, clouds_rect)

    # Load the PNG image
    logo = pygame.image.load('LINK_logo.png')
    logo = pygame.transform.scale(logo, (1000, 900))  # Size of image

    play = pygame.image.load('pressSPACE.png')
    play = pygame.transform.scale(play, (600, 300))  # Size of image

    # Location of image
    logo_rect = logo.get_rect(topleft=(-10, -150))

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
    global input_text  # Declare input_text as global variable
    global input_text  # Declare input_text as global
    global words
    global ans_display
    global game_state

    windowSurface.fill(BLACK)

    # background of game screen
    clouds = pygame.image.load('clouds.png')
    clouds = pygame.transform.scale(clouds, (1800, 1200))
    clouds_rect = clouds.get_rect(topleft=(-300, -280))
    windowSurface.blit(clouds, clouds_rect)

    #logo at the top of the game screen
    logo = pygame.image.load('LINK_logo.png')
    logo = pygame.transform.scale(logo, (400, 200))
    logo_rect = logo.get_rect(topleft=(300, 50))
    windowSurface.blit(logo, logo_rect)

    # Draw rectangle
    pygame.draw.rect(windowSurface, PURPLE, pygame.Rect(120, 250, 750, 700))
    pygame.draw.rect(windowSurface, DARKPURPLE, pygame.Rect(150, 280, 690, 600))

    # Display the two words to the player
    
    font = pygame.font.SysFont(None, 36)
    text_surface5 = font.render("Level " + str(link.get_curr_level()), True, WHITE)
    text_rect5 = text_surface5.get_rect(topleft=(700, 252))
    windowSurface.blit(text_surface5, text_rect5)

    font = pygame.font.SysFont(None, 36)
    text_surface6 = font.render("Lives: " + str(link.get_lives()), True, WHITE)
    text_rect6 = text_surface6.get_rect(topleft=(200, 252))
    windowSurface.blit(text_surface6, text_rect6)

    text_surface = font.render("Word 1: " + words[0], True, WHITE)
    text_rect = text_surface.get_rect(topleft=(200, 300))
    windowSurface.blit(text_surface, text_rect)

    text_surface2 = font.render("Word 2: " + words[1], True, WHITE)
    text_rect2 = text_surface2.get_rect(topleft=(200, 350))
    windowSurface.blit(text_surface2, text_rect2)

    # Display typed text
    text_surface3 = font.render("Your Guess: " + input_text, True, WHITE)
    text_rect3 = text_surface3.get_rect(topleft=(200, 400))
    windowSurface.blit(text_surface3, text_rect3)

    
    text_surface4 = font.render("Answer (" + str(len(link.get_ans())) + " letters long): " + ans_display, True, WHITE)
    text_rect4 = text_surface4.get_rect(topleft=(200, 450))
    windowSurface.blit(text_surface4, text_rect4)

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
                # check the entered guess against the link
                if link.check_guess(input_text):
                    print('correct')
                    # Display "Correct" on the screen
                    ans_display = ""
                    for i in range(link.ans_len()):
                            ans_display += input_text[i]
                    # text_surface4 = font.render("Answer (" + str(len(link.get_ans())) + " letters long): " + ans_display, True, WHITE)
                    # text_rect4 = text_surface4.get_rect(topleft=(200, 450))
                    # windowSurface.blit(text_surface4, text_rect4)

                    correct_text = font.render("Correct! press any key to continue", True, GREEN)
                    correct_rect = correct_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
                    windowSurface.blit(correct_text, correct_rect)
                    pygame.display.update()

                    # Wait for space bar to continue
                    waiting = True
                    while waiting:
                        ans_display = link.get_ans()
                        for event in pygame.event.get():
                            if event.type == KEYDOWN:
                                waiting = False
                                ans_display = ""
                    input_text = ""  
                    words = link.get_words()
                else:
                    print('incorrect')
                    link.set_lives(1)
                    if link.get_lives() == 0:
                        game_state = "gameover"
                    else:
                        ans_display = ""
                        if link.ans_len() == len(input_text):
                            for i in range(link.ans_len()):
                                if input_text[i] == link.get_ans()[i]:
                                    ans_display += input_text[i]
                                else:
                                    ans_display += "_"
                        else:
                            incorrect_text = font.render("Incorrect number of characters. Press any key to try again.", True, RED)
                            incorrect_rect = incorrect_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
                            windowSurface.blit(incorrect_text, incorrect_rect)
                            pygame.display.update()
                            waiting = True
                            while waiting:
                                for event in pygame.event.get():
                                    if event.type == KEYDOWN:
                                        waiting = False
                        input_text = ""  # Clear the input for the next guess

                
            else:
                if len(input_text) < link.ans_len():
                    input_text += event.unicode  # Add the character to the input text

def gameover():
    global input_text  # Declare input_text as global variable
    global input_text  # Declare input_text as global
    global words
    global ans_display

    windowSurface.fill(BLACK)

    # background of game screen
    clouds = pygame.image.load('clouds.png')
    clouds = pygame.transform.scale(clouds, (1800, 1200))
    clouds_rect = clouds.get_rect(topleft=(-300, -280))
    windowSurface.blit(clouds, clouds_rect)

    #logo at the top of the game screen
    logo = pygame.image.load('LINK_logo.png')
    logo = pygame.transform.scale(logo, (400, 200))
    logo_rect = logo.get_rect(topleft=(300, 50))
    windowSurface.blit(logo, logo_rect)

    # Draw rectangle
    pygame.draw.rect(windowSurface, PURPLE, pygame.Rect(120, 250, 750, 700))
    pygame.draw.rect(windowSurface, DARKPURPLE, pygame.Rect(150, 280, 690, 600))

    # Display the two words to the player
    
    font = pygame.font.SysFont(None, 36)
    text_surface4 = font.render("gameover.", True, WHITE)
    text_rect4 = text_surface4.get_rect(topleft=(200, 450))
    windowSurface.blit(text_surface4, text_rect4)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        


# Main game loop
while True:
    # Check for quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if game_state == "start_menu":  # if game is in the start menu
        draw_start_menu()
        # words = link.get_words()

    elif game_state == "game":  # if game is in the game
        # words = link.get_words()
        # word1 = words[0]
        # word2 = words[1]
        game()

    elif game_state == "gameover":
        gameover()

    mainClock.tick(40)


'''
to do:
- instruction screen
- hard/easy mode
- randomize first 20 levels
- polish font/colors
- fix incorrect state for randomized words
- fix underscore part 
'''