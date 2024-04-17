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
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (250, 195, 226)
PURPLE = (202, 102, 242)

# set up title of page
font = pygame.font.SysFont('ariel', 100)
text = font.render('Link', True, PURPLE)
textRect = text.get_rect()
textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 900)

#start menu stuff
game_state = 'start_menu'

def draw_start_menu():
    # Load the PNG image
    # Load the PNG image
    image = pygame.image.load('Flower.png')
    image = pygame.transform.scale(image, (200, 200))
    
    # Create rects for each instance of the image and set their positions
    image_rect1 = image.get_rect(topleft=(200, 200))
    image_rect2 = image.get_rect(topleft=(500, 300))
    image_rect3 = image.get_rect(topleft=(700, 400))
     
    # 
    windowSurface.fill(WHITE)
    title = font.render('Link', True, PINK)
    prompt = font.render('Press SPACE to continue', True, PURPLE)
    windowSurface.blit(title, (WINDOW_WIDTH/2 - title.get_width()/2, WINDOW_HEIGHT/2 - title.get_height()/2))
    windowSurface.blit(prompt, (WINDOW_WIDTH/2 - prompt.get_width()/2, WINDOW_HEIGHT/2 + title.get_height()))
    windowSurface.blit(image, image_rect1)
    windowSurface.blit(image, image_rect2)
    windowSurface.blit(image, image_rect3)
    pygame.display.update()

def start_game():
    global game_state
    game_state = "game"


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
        # Your game logic goes here
        windowSurface.fill(WHITE)
        # Draw rectangle
        pygame.draw.rect(windowSurface, PINK, pygame.Rect(400, 50, 200, 100))
        # Draw text
        windowSurface.blit(text, textRect)
        pygame.display.update()
        mainClock.tick(40)
