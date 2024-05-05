import pygame
import sys
from pygame.locals import *
from combo import Link

from nltk.corpus import wordnet
import random
import requests

mode = "easy"

class Button:
    def __init__(self, text, position, size):
        self.text = text
        self.position = position
        self.size = size
        self.rect = pygame.Rect(position, size)

    def draw(self, surface):
        if mode == "easy":
            pygame.draw.rect(surface, GREEN, self.rect)
        else:
            pygame.draw.rect(surface, RED, self.rect)
        font = pygame.font.SysFont("monospace", 25)
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
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
GREEN = (110, 230, 50)
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

# Initialize that the input is empty
incorrect = False
wrong_num = False
correct = False

# Words for the game
ans_display = ""

link = Link()
words = link.get_words()

button = Button("Easy/Hard", (800, 50), (150, 50)) 


def draw_start_menu():
    global game_state

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
                    game_state = "instructions"  # Update game_state here
                    

def draw_instructions():

    global game_state

    windowSurface.fill(BLACK)

    clouds = pygame.image.load('clouds.png')
    clouds = pygame.transform.scale(clouds, (1800, 1200))
    clouds_rect = clouds.get_rect(topleft=(-400, -280))
    windowSurface.blit(clouds, clouds_rect)

    # Draw your instructions here
    font = pygame.font.SysFont("monospace", 25)
    instruction_text = [
        "Instructions:",
        "you are given two words and you need to guess", 
        "the LINK between the two",
        "you are given 5 lives per level",
        "when you submit a guess, you are given which letters",
        "you guessed right",
        "",
        "press SPACE to continue"
    ]
    y_offset = 200
    for line in instruction_text:
        text_surface = font.render(line, True, WHITE)
        text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, y_offset))
        windowSurface.blit(text_surface, text_rect)
        y_offset += 50

    pygame.display.update()

    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    game_state = "game"  # Update game_state here
    

def game():

    global input_text  # Declare input_text as global
    global words
    global ans_display
    global game_state
    global game_state
    global incorrect
    global wrong_num
    global correct
    global mode
    global prev_ans

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
    
    font = pygame.font.SysFont("monospace", 25)
    text_surface5 = font.render("Level " + str(link.get_curr_level()), True, WHITE)
    text_rect5 = text_surface5.get_rect(topleft=(700, 252))
    windowSurface.blit(text_surface5, text_rect5)

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
    text_rect3 = text_surface3.get_rect(topleft=(200, 450))
    windowSurface.blit(text_surface3, text_rect3)
        
    if mode == "easy":
        text_surface4 = font.render("LINK (" + str(len(link.get_ans())) + " letters long): " + ans_display, True, WHITE)
        text_rect4 = text_surface4.get_rect(topleft=(200, 550))
        windowSurface.blit(text_surface4, text_rect4)
    else:
        text_surface4 = font.render("LINK (" + str(len(link.get_ans())) + " letters long): ", True, WHITE)
        text_rect4 = text_surface4.get_rect(topleft=(200, 550))
        windowSurface.blit(text_surface4, text_rect4)

    text_surface5 = font.render("enter '1' to get a hint, lose one life", True, WHITE)
    text_rect5 = text_surface5.get_rect(topleft=(210, 700))
    windowSurface.blit(text_surface5, text_rect5)

    if correct == True:
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
        
        correct_text = font.render("Correct! LINK was: " + prev_ans, True, GREEN)
        correct_rect = correct_text.get_rect(center=(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2)))
        windowSurface.blit(correct_text, correct_rect)

        correct_text = font.render("Press any key to continue.", True, GREEN)
        correct_rect = correct_text.get_rect(center=(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 50))
        windowSurface.blit(correct_text, correct_rect)

    if incorrect == True:
        incorrect_text = font.render("Incorrect. Try again.", True, RED)
        incorrect_rect = incorrect_text.get_rect(center=(WINDOW_WIDTH // 2, 650))
        windowSurface.blit(incorrect_text, incorrect_rect)
    
    incorrect_number_text = [
        "Incorrect number of characters.",
        "Press any key to try again."
    ]

    if wrong_num == True:
        y_offset = 620
        for line in incorrect_number_text:
            text_surface = font.render(line, True, RED)
            text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, y_offset))
            windowSurface.blit(text_surface, text_rect)
            y_offset += 50

    button.draw(windowSurface)

    pygame.display.update()

    # Handle typing
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if (x >= 800 and x <= 950) and (y >= 50 and y <= 100):
                if mode == "easy":  
                    mode = "hard"
                else:
                    mode = "easy"
                print(f'game mode: {mode}')
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            incorrect = False
            wrong_num = False
            if event.key == K_BACKSPACE:
                input_text = input_text[:-1]  # Remove last character
            elif event.key == K_RETURN:
                # check if they want a hint
                if link.get_lives() < 0:
                    game_state = "gameover"
                elif (input_text == '1') and (link.get_lives() >= 0):
                    input_text = ""
                    link.set_lives(link.get_lives() - 1)
                    ans_display = link.get_hint(ans_display)
                    if link.check_guess(ans_display):
                        prev_ans = link.get_ans()
                        link.set_lives(5)
                        words = link.get_words()
                        ans_display = ""
                        correct = True
                    elif link.get_lives() < 0:
                        game_state = "gameover"

                # check the entered guess against the link
                elif link.check_guess(input_text):
                    print('correct')
                    correct = True
                    prev_ans = link.get_ans()
                    input_text = ""  
                    link.set_lives(5)
                    words = link.get_words()
                    ans_display = ""

                else:
                    print('incorrect')
                    if link.get_lives() == 0:
                        game_state = "gameover"
                    else:
                        if link.ans_len() == len(input_text):
                            link.set_lives((link.get_lives())-1)
                            incorrect = True
                            if mode == "easy":
                                if len(ans_display) == link.ans_len():
                                    for i in range(link.ans_len()):
                                        ans_display = list(ans_display)
                                        if input_text[i] == link.get_ans()[i]:
                                            ans_display[i] = link.get_ans()[i]
                                        else:
                                            ans_display[i] = '_'
                                    ans_display = "".join(ans_display)
                                else:           
                                    for i in range(link.ans_len()):
                                        if input_text[i] == link.get_ans()[i]:
                                            ans_display += input_text[i]
                                        else:
                                            ans_display += "_"
                        else:
                            wrong_num = True
                    
                        input_text = ""  # Clear the input for the next guess
                        

            else:
                if len(input_text) < link.ans_len():
                    input_text += event.unicode  # Add the character to the input text
                if correct == True:
                    input_text = input_text[:-1]
                    correct = False

def gameover():
    global input_text  # Declare input_text as global variable
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
    
    font = pygame.font.SysFont("monospace", 25)
    text_surface4 = font.render("Gameover.", True, WHITE)
    text_rect4 = text_surface4.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    windowSurface.blit(text_surface4, text_rect4)

    text_surface4 = font.render("LINK was: " + link.get_ans(), True, WHITE)
    text_rect4 = text_surface4.get_rect(center=(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 30))
    windowSurface.blit(text_surface4, text_rect4)

    text_surface4 = font.render("Press SPACE to start over", True, WHITE)
    text_rect4 = text_surface4.get_rect(center=(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) + 80 ))
    windowSurface.blit(text_surface4, text_rect4)



    pygame.display.update()

    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    link.set_lives(5)
                    link.set_level(1)
                    link.clear_called_levels()
                    words = link.get_words()
                    input_text = ""
                    ans_display = ""
                    game_state = "instructions"
        

# Main game loop
while True:
    # Check for quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if game_state == "start_menu":
        draw_start_menu()
    elif game_state == "instructions":
        draw_instructions()
    elif game_state == "game":
        game()
    elif game_state == "gameover":
        gameover()

    mainClock.tick(40)
