####################################################################
####################  simple array game   ##########################
####################   M.L.Souilljee     ###########################
####################################################################

#importing pygame
import math
import random

def CHECK(ROWS, COLUMS, TABLE):
    for i in range(0,ROWS):
            SAME = True
            First = True
            for j in range(0,COLUMS):
                if TABLE[i][j] != None:
                    if First == True:
                        TEMP = TABLE[i][j]
                        First = False
                    elif SAME == True:
                        if TEMP != TABLE[i][j]:
                            SAME = False
            if SAME == True:
                for j in range(0,COLUMS):
                    TABLE[i][j] = None

def GENERATE_ROW(ROWS, COLUMS, TABLE, SAVED_LOCATION, LOCATION):
    for i in range(0,COLUMS):
        TABLE[(LOCATION[1]-10)/50][i] = TABLE[(SAVED_LOCATION[1]-10)/50][i]    
        TABLE[(SAVED_LOCATION[1]-10)/50][i] = random.randint(0, 1)

def GENERATE_COLUMS(ROWS, COLUMS, TABLE, SAVED_LOCATION, LOCATION):
    for i in range(0, ROWS):
        TABLE[i][(LOCATION[0]-10)/50] = TABLE[i][(SAVED_LOCATION[0]-10)/50]
        TABLE[i][(SAVED_LOCATION[0]-10)/50] = random.randint(0, 1)

def CHECK_DONE(ROWS, COLUMS, TABLE):
    DONE = True
    for i in range(0,ROWS): #loop for the y values
        for j in range(0,COLUMS): #loop for the x values
            if TABLE[i][j] == None and DONE == True:
                DONE = True
            else:
                DONE = False
    return(DONE) 
    