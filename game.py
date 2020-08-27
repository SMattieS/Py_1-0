####################################################################
####################  simple array game   ##########################
####################   M.L.Souilljee     ###########################
####################################################################

# importing pygame #################################################
import pygame
import math

# Custom files
import Board
import Solve
####################################################################

# give game instructions ###########################################
print("This game is called 1&0 when playing use the left and right arrow ")
print("to move up and down. Use the up arrow to flip the rectangular bar. ")
print("Use spacebar to select a row or colum this highlights it and marks it  blue ")
print("afterwards select a spot to put the colum or row the position where ")
print("the row or colum was original there will be a new random row or colum ")
print("Use s to solve the colums and use d to solve the rows, when solving ")
print("you get one point the less points you collect during the game the ")
print("better (points are collected every s or d key press. ")
print("The game ands when all 1's and 0's are gone Use r to reset the game and escape to exit.")
print("GOOD LUCK!")
####################################################################

# define some constants ############################################
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
ROWS = COLUMS = 0
print("Give size of playing field")
ROWS = input()
COLUMS = ROWS
SCREEN_WIDTH = int(math.ceil(50 * COLUMS))
SCREEN_HEIGHT = int(math.ceil(50 * ROWS))
RESET = True

# intialize the array which saves the playing field
TABLE = [[0 for x in range(COLUMS)] for y in range(ROWS)]
LOCATION = [10,10]
SAVED_LOCATION = [10,10]
VERTICAL = False
SAME = False
SWITCHING = False
DONE = False
SOLVES = 0

#make a running variable
running = True
####################################################################

# import some key locals ###########################################
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    K_r,
    K_s,
    K_d,
    KEYDOWN,
    QUIT,
)
####################################################################

# initialize pygame ################################################
pygame.init()

# create a screen to play the game in
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('1&0')

# clock for FPS
clock = pygame.time.Clock()

# set the font
font = pygame.font.Font('freesansbold.ttf', 16)

# create the zero and ones for the game
ZERO = font.render('0', True, WHITE, BLACK)
ONE = font.render('1', True, WHITE, BLACK)

# create the squares to place the zeros and ones in
ZERORECT = ZERO.get_rect()
ONERECT = ONE.get_rect()
####################################################################

# while loop for the game ##########################################
while running:
    for event in pygame.event.get():
        #check if a key is pressed
        if event.type == KEYDOWN:
            #check if certain keys are pressed
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_r and SWITCHING == False:
                RESET = True
            elif event.key == K_RIGHT:
                if LOCATION[1] + 50 < SCREEN_HEIGHT and LOCATION[0] + 50 < SCREEN_WIDTH:
                    if VERTICAL:
                        LOCATION[1] += 50
                    else:
                        LOCATION[0] += 50
            elif event.key == K_LEFT:
                if LOCATION[1] - 50 > 0 or LOCATION[0] - 50 > 0:
                    if VERTICAL:
                        LOCATION[1] -= 50
                    else:
                        LOCATION[0] -= 50
            elif event.key == K_UP and SWITCHING == 0:
                VERTICAL = not VERTICAL
                LOCATION = [10,10]
            elif event.key == K_s:
                Board.TRANSPOSE(ROWS, COLUMS, TABLE)
                Solve.CHECK(ROWS, COLUMS, TABLE)
                Board.TRANSPOSE(ROWS, COLUMS, TABLE)
                SOLVES += 1
            elif event.key == K_d:
                Solve.CHECK(ROWS, COLUMS, TABLE)
                SOLVES += 1
            elif event.key == K_SPACE and SWITCHING == False:
                SWITCHING = True
                SAVED_VERTICAL = VERTICAL
                for i in range(2):
                    SAVED_LOCATION[i] = LOCATION[i]
                print("Saved X : ", LOCATION[0], "\n Saved Y : ", LOCATION[1])
            elif event.key == K_SPACE and SWITCHING:
                SWITCHING = False
                if VERTICAL:
                    Solve.GENERATE_ROW(ROWS, COLUMS, TABLE, SAVED_LOCATION, LOCATION)
                    print("saved location: ", SAVED_LOCATION[1])
                    print("location: ", LOCATION[1])
                else:
                    Solve.GENERATE_COLUMS(ROWS, COLUMS, TABLE, SAVED_LOCATION, LOCATION)
                    print("saved location: ", SAVED_LOCATION[0])
                    print("location: ", LOCATION[0])
        elif event.type == QUIT:
            running = False


    # make the screen black
    screen.fill(BLACK)

    if Solve.CHECK_DONE(ROWS, COLUMS, TABLE):
        print("CONGRATULATIONS WINNER")
        print("WON IN ", SOLVES, " AMOUNT OF SOLVES")
        running = False

    if RESET == True:
        print "generate new board"
        # if reset is through a board with random ones and zeros should be generated
        Board.MAKEBOARD(ROWS, COLUMS, [ZERO, ONE], [ZERORECT, ONERECT], screen, TABLE) #call the function which builds a random board
        RESET = False #reset is made false until the player pushes the r button

    else:
        Board.PRINTBOARD(ROWS, COLUMS, [ZERO, ONE], [ZERORECT, ONERECT], screen, TABLE)
        if VERTICAL:
            pygame.draw.rect(screen, WHITE, pygame.Rect(LOCATION[0], LOCATION[1], SCREEN_WIDTH-15, 35), 3)
        else:
            pygame.draw.rect(screen, WHITE, pygame.Rect(LOCATION[0], LOCATION[1], 35, SCREEN_HEIGHT-15), 3)

    if SWITCHING == True:
        Board.PRINTBOARD(ROWS, COLUMS, [ZERO, ONE], [ZERORECT, ONERECT], screen, TABLE)
        if SAVED_VERTICAL:
            pygame.draw.rect(screen, BLUE, pygame.Rect(SAVED_LOCATION[0], SAVED_LOCATION[1], SCREEN_WIDTH-15, 35), 3)
        else:
            pygame.draw.rect(screen, BLUE, pygame.Rect(SAVED_LOCATION[0], SAVED_LOCATION[1], 35, SCREEN_HEIGHT-15), 3)

    pygame.display.update()
    clock.tick(30)
####################################################################

pygame.quit()
quit()
