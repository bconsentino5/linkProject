import pygame, sys, time, random
from pygame.locals import *

# set up pygame
pygame.init()

# set up window
WINDOWWIDTH = 1000
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')

MOVESPEED = 4

DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

DIRLIST = [DOWNLEFT, DOWNRIGHT, UPLEFT, UPRIGHT]

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

COLORLIST = [RED, GREEN, BLUE]

# set up the box data structure
# b1 = {'rect': pygame.Rect(300, 80, 50, 100), 'color': RED, 'dir': UPRIGHT}
# b2 = {'rect': pygame.Rect(200, 20, 20, 20), 'color': GREEN, 'dir': UPLEFT}
# b3 = {'rect': pygame.Rect(100, 150, 60, 60), 'color': BLUE, 'dir': DOWNLEFT}

number = 25
boxes = []

for i in range(number):
    # random.randint(#, #)
    color = COLORLIST[random.randint(0, 2)]
    direction = DIRLIST[random.randint(0, 3)]
    top = random.randint(1, WINDOWHEIGHT - 200)
    left = random.randint(1, WINDOWWIDTH - 200)
    width = random.randint(1, 200)
    height = random.randint(1, 200)

    box = {'rect': pygame.Rect(top, left, width, height), 'color': color, 'dir': direction}

    boxes.append(box)



while True:
    # check for a QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(WHITE)

    # for b in boxes:
    #     if b['dir'] == DOWNLEFT:
    #         b['rect'].left -= MOVESPEED
    #         b['rect'].top += MOVESPEED
    #     if b['dir'] == DOWNRIGHT:
    #         b['rect'].left += MOVESPEED
    #         b['rect'].top += MOVESPEED
    #     if b['dir'] == UPLEFT:
    #         b['rect'].left -= MOVESPEED
    #         b['rect'].top -= MOVESPEED
    #     if b['dir'] == UPRIGHT:
    #         b['rect'].left += MOVESPEED
    #         b['rect'].top -= MOVESPEED
        
    #     if b['rect'].top < 0:
    #         if b['dir'] == UPLEFT:
    #             b['dir'] = DOWNLEFT
    #         if b['dir'] == UPRIGHT:
    #             b['dir'] = DOWNRIGHT
    #     if b['rect'].bottom > WINDOWHEIGHT:
    #         if b['dir'] == DOWNLEFT:
    #             b['dir'] = UPLEFT
    #         if b['dir'] == DOWNRIGHT:
    #             b['dir'] = UPRIGHT
    #     if b['rect'].left < 0:
    #         if b['dir'] == DOWNLEFT:
    #             b['dir'] = DOWNRIGHT
    #         if b['dir'] == UPLEFT:
    #             b['dir'] = UPRIGHT
    #     if b['rect'].right > WINDOWWIDTH:
    #         if b['dir'] == DOWNRIGHT:
    #             b['dir'] = DOWNLEFT
    #         if b['dir'] == UPRIGHT:
    #             b['dir'] = UPLEFT

    #     pygame.draw.rect(windowSurface, b['color'], b['rect'])
    pygame.Rect(left, top, width, height)    
    pygame.display.update()
    time.sleep(.02)