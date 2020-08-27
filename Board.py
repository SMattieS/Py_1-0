####################################################################
####################  simple array game   ##########################
####################   M.L.Souilljee     ###########################
####################################################################

#importing pygame
import pygame
import random
import math

def DEF_BIN(x, y, NUM, RECT, screen):
    RECT.center = (x, y)
    screen.blit(NUM, RECT)

def MAKEBOARD(ROWS, COLUMS, NUM, RECT, screen, TABLE):
    for i in range(0,ROWS): #loop for the y values
        for j in range(0,COLUMS): #loop for the x values
            TABLE[i][j] = random.randint(0, 1)

def PRINTBOARD(ROWS, COLUMS, NUM, RECT, screen, TABLE):
    for i in range(0,ROWS):
        for j in range(0,COLUMS):
            if TABLE[i][j] != None:
                DEF_BIN(j*50+25, i*50+25, NUM[TABLE[i][j]], RECT[TABLE[i][j]], screen)

def TRANSPOSE(ROWS, COLUMS, TABLE):
    TABLE_TRANS = [[0 for x in range(COLUMS)] for y in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLUMS):
            TABLE_TRANS[i][j] = TABLE[j][i]
    for i in range(ROWS):
        for j in range(COLUMS):
            TABLE[i][j] = TABLE_TRANS[i][j]
    