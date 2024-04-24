# import pygame
# import sys
# from pygame.locals import *

# # Set up pygame
# pygame.init()
# mainClock = pygame.time.Clock()

# # Set up window
# WINDOW_WIDTH = 1000
# WINDOW_HEIGHT = 1000
# windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
# pygame.display.set_caption("Link")

# # colors
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# PINK = (250, 195, 226)
# PURPLE = (202, 102, 242)

# # set up title of page
# font = pygame.font.SysFont('ariel', 100)
# text = font.render('Link', True, PURPLE, GREEN)
# textRect = text.get_rect()
# textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 900)

# #start menu stuff
# game_state = 'start_menu'

# def draw_start_menu():
#     windowSurface.fill(WHITE)
#     title = font.render('Link', True, PINK)
#     prompt = font.render('Press SPACE to continue', True, PURPLE)
#     windowSurface.blit(title, (WINDOW_WIDTH/2 - title.get_width()/2, WINDOW_HEIGHT/2 - title.get_height()/2))
#     windowSurface.blit(prompt, (WINDOW_WIDTH/2 - prompt.get_width()/2, WINDOW_HEIGHT/2 + title.get_height()))
#     pygame.display.update()

# def start_game():
#     global game_state
#     game_state = "game"


# # Main game loop
# while True:
#     # Check for quit
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#     if game_state == "start_menu":
#         draw_start_menu()
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_SPACE]:
#             start_game()

#     elif game_state == "game":
#         # Your game logic goes here
#         windowSurface.fill(WHITE)
#         # Draw rectangle
#         pygame.draw.rect(windowSurface, PINK, pygame.Rect(400, 50, 200, 100))
#         # Draw text
#         windowSurface.blit(text, textRect)
#         pygame.display.update()
#         mainClock.tick(40)





# ---------------------------------------------------------------#





# import pygame
# import sys

# # Initialize Pygame
# pygame.init()

# # Set up the screen
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Word Rectangles")

# # Set up colors
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# PINK = (250, 195, 226)
# PURPLE = (202, 102, 242)
# BLACK = (0, 0, 0)


# # Set up fonts
# font = pygame.font.Font(None, 48)

# def draw_word_with_rectangle(word, x, y):
#     text_surface = font.render(word, True, BLACK)
#     text_rect = text_surface.get_rect()
#     text_rect.topleft = (x, y)
#     new_rect = pygame.Rect(x - 5, y - 5, text_rect.width + 10, text_rect.height + 10)
#     pygame.draw.rect(screen, PURPLE, (new_rect.topleft, (new_rect.width, new_rect.height)), border_radius = 3)
#     pygame.draw.rect(screen, WHITE, (text_rect.topleft, (text_rect.width, text_rect.height)), border_radius = 3)
#     screen.blit(text_surface, new_rect)
#     # screen.blit(text_surface, text_rect)


# # Main loop
# def main():
#     word1 = "happapapapa"
#     word2 = "World"
    
#     # Calculate the positions for the words
#     word1_width = font.size(word1)[0]
#     word2_width = font.size(word2)[0]
#     total_width = word1_width + word2_width
#     margin = 20
#     x_start = (((screen_width - total_width) // 2) - margin)
#     # x_start = (((screen_width) // 2) - margin) - word1_width
    
#     word_y = (screen_height - font.get_height()) // 2
    
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         screen.fill(WHITE)
        
#         # Draw word1 and its rectangle
#         draw_word_with_rectangle(word1, x_start, word_y)
        
#         # Draw word2 and its rectangle
#         draw_word_with_rectangle(word2, x_start + word1_width + margin, word_y)

#         pygame.display.flip()

#     pygame.quit()
#     sys.exit()

# if __name__ == "__main__":
#     main()





# ---------------------------------------------------------------#




from nltk.corpus import wordnet
import random
import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.split()

# curr_word = random.choice(WORDS).decode('utf-8')
# synonyms = []
# syn1 = ""
# syn2 = ""

# for ss in wordnet.synsets(curr_word):
#     for sim in ss.similar_tos():
#         synonyms.append(format(sim)[8:-7])

# while len(synonyms) < 2:
#     curr_word = random.choice(WORDS).decode('utf-8')
#     for ss in wordnet.synsets(curr_word):
#         for sim in ss.similar_tos():
#             synonyms.append(format(sim)[8:-7])

# while (syn1 == "") or (syn1 == curr_word):
#     syn1 = random.choice(synonyms)
# while (syn2 == "") or (syn2 == curr_word) or (syn2 == syn1):
#     syn2 = random.choice(synonyms)

# print(curr_word) 
# print(syn1)
# print(syn2)       


levels = {'1': ['mom', 'dad', 'parents'], 
          '2': ['bird', 'plane', 'fly'], 
          '3': ['heel', 'bark', 'dog'],
          '4': ['tree', 'glue', 'stick'],
          '5': ['theme', 'swing', 'park'],
          '6': ['football', 'smartphone', 'screen'],
          '7': ['computer', 'door', 'key'],
          '8': ['technology', 'fruit', 'apple'],
          '9': ['trust', 'religion', 'faith'],
          '10': ['animal', 'pooper', 'party'],
          '11': ['wind', 'string', 'instrument'],
          '12': ['bowtie', 'wheel', 'pasta'],
          '13': ['dog', 'chair', 'sit'],
          '14': ['pumpkin', 'slipper', 'cinderella'],
          '15': ['cheese', 'color', 'wheel'],
          '16': ['shoe', 'spirit', 'soul'],
          '17': ['leap', 'amphibian', 'frog'],
          '18': ['slice', 'italy', 'pizza'],
          '19': ['heart', 'music', 'beat'],
          '20': ['dairy', 'nut', 'butter']}

curr_level = 1
lives = 5

while lives != 0:
  if lives <= 0:
    break
  else:
    # initialize level
    lives = 5
    print(f'-- LEVEL {curr_level} --')
    print()
    words = levels.get(str(curr_level))
    print(f'{words[0]}     {words[1]}')
    print()
    print(f'LINK is {len(words[2])} characters long:')
    print()
    ans = input()

    # incorrect
    while ans != words[2]:
      if len(ans) != len(words[2]):
         print(f'answer is the wrong length. LINK is {len(words[2])} characters long. try again:')
         ans = input()
      else:
        lives -= 1
        for i in range(len(words[2])):
          if words[2][i] == ans[i]:
              print(words[2][i], end="")
          else:
              print("_", end="")
        print()
        print(f'incorrect. you have {lives} lives left.')
        print()
        # checking if they can continue to play
        if lives == 0:
          print(f'>> the LINK was {words[2]} <<')
          print('*** game over ***')
          break
        else:
          ans = input()

    # correct   
    if ans == words[2]:
      print()
      print("*** correct! onto the next level ***")
      print()
      curr_level += 1
      temp = 0
      if curr_level > 20:
        while temp == 0:
            curr_word = random.choice(WORDS).decode('utf-8')
            if len(curr_word) < 8:
               temp = 1
        synonyms = []
        syn1 = ""
        syn2 = ""

        for ss in wordnet.synsets(curr_word):
            for sim in ss.similar_tos():
                synonyms.append(format(sim)[8:-7])

        while len(synonyms) < 2:
            temp = 0
            while temp == 0:
                curr_word = random.choice(WORDS).decode('utf-8')
                if len(curr_word) < 8:
                    temp = 1
            for ss in wordnet.synsets(curr_word):
                for sim in ss.similar_tos():
                    synonyms.append(format(sim)[8:-7])

        while (syn1 == "") or (syn1 == curr_word):
            syn1 = random.choice(synonyms)
        while (syn2 == "") or (syn2 == curr_word) or (syn2 == syn1):
            syn2 = random.choice(synonyms)

        levels.update({str(curr_level): [str(syn1), str(syn2), str(curr_word)]})
          

    