import pygame, os, sys
from pygame.locals import*

pygame.init()   #initialize pygame
fpsClock = pygame.time.Clock()
brick = None
mainSurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bricks')
black = pygame.Color(0, 0, 0)


#bat init


bat = pygame.image.load('bat.png')
playerY = 540  #the be should always be at (x,540)
batRect = bat.get_rect() # the return (0,0,widthbat,heightbat)
mousex, mousey = (0, playerY) #the mouse starts at the position (0,540)


#ball init


ball = pygame.image.load('ball.png')
ballRect = ball.get_rect()
ballStartY = 200
ballSpeed =3
ballServed = False

bx, by = (24, ballStartY)
sx, sy = (ballSpeed,ballSpeed)
ballRect.topleft = (bx, by)

#brick init

def createBricks(pathToImg, rows, cols):
    global brick
    brick =pygame.image.load(pathToImg) 
    bricks = []
    for y in range(rows):
        brickY = (y*16) +100
        for x in range(cols):
            brickX = (x*31) + 245
            bricks.append(Rect(brickX,brickY,brick.get_width(),brick.get_height()))
    return bricks


bricks = createBricks('brick.png',5,10)

#main loop
while True:
    
    
    mainSurface.fill(black)
   

    # brick draw
    for b in bricks:
        mainSurface.blit(brick,b)
        

    # bat and ball draw
    mainSurface.blit(bat, batRect)
    mainSurface.blit(ball, ballRect)

    # events

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.event =quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            if (mousex < 800-55):
                batRect.topleft = (mousex,playerY)
            else:
                batRect.topleft =(800-55,playerY)
        elif event.type == MOUSEBUTTONUP:
            if not ballServed:
                ballServed = True

    # main game logic

    if ballServed:
        bx +=sx
        by +=sy
        ballRect.topleft = (bx, by)

    #borders
    if by<= 0: #top screen
        by=0
        sy *= -1
    
    if (by >= 600- 8): # if not hit the ball
        ballServed =False
        bx, by =(24,200)
        ballRect.topleft = (bx, by)

    if bx >= (800-8):
        bx =800-8
        sx *=-1

    if bx <= 0:
        bx =0
        sx *=-1

    
    #colision with the bat
    if ballRect.colliderect(batRect):
        by =playerY-8
        sy *= -1

    # # collision detection
    brickHitIndex = ballRect.collidelist(bricks)
    if brickHitIndex >= 0:
        hb = bricks[brickHitIndex]
        mx = bx + 4
        my = by + 4
        if mx > hb.x + hb.width or mx< hb.x:
            sx *=-1
        else:
            sy *=-1
        del (bricks[brickHitIndex])

    pygame.display.update()
    fpsClock.tick(30)
    
    



 


