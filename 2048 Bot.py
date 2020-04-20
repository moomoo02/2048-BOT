import pyautogui
import time
from PIL import ImageGrab,ImageOps


currentGrid = [0,0,0,0,
               0,0,0,0,
               0,0,0,0,
               0,0,0,0]

scoreGrid = [50,30,15,5,
             30,-10,0,0,
             15,  0,0,0,
             5,   0,0,0]
def getGrid():
    image = ImageGrab.grab()
    grayImage = ImageOps.grayscale(image)
    for index,cord in enumerate(Cords.cordArray):
        pixel = grayImage.getpixel(cord)
        pos = Values.valueArray.index(pixel)
        if pos == 0:
            currentGrid[index] = 0
        else:
            currentGrid[index] = pow(2,pos)
def printGrid(grid):
    for i in range(16):
        if i%4 == 0:
            print("[" + str(grid[i]) + " " + str(grid[i+1]) + " " +
                  str(grid[i+2]) + " " + str(grid[i+3]))
class Cords:
    topLeft = (1,29)
    bottomRight = (753,747)
    cord11 = (476,714)
    cord12 = (2*348,2*357)
    cord13 = (2*457,2*357)
    cord14 = (2*567,2*357)
    cord21 = (2*238,2*469)
    cord22 = (2*348,2*469)
    cord23 = (2*457,2*469)
    cord24 = (2*567,2*469)
    cord31 = (2*238,2*576)
    cord32 = (2*348,2*576)
    cord33 = (2*457,2*576)
    cord34 = (2*567,2*576)
    cord41 = (2*238,2*684)
    cord42 = (2*348,2*684)
    cord43 = (2*457,2*684)
    cord44 = (2*567,2*684)

    cordArray = [cord11,cord12,cord13,cord14,
                 cord21,cord22,cord23,cord24,
                 cord31,cord32,cord33,cord34,
                 cord41,cord42,cord43,cord44]
class Values:
    zero = 195
    two = 230 or 228
    four = 225 or 224
    eight = 190
    sixteen = 172
    thirtyTwo = 157 or 159 or 158
    sixtyFour = 136 or 139
    oneTwentyEight = 205
    twoFiftySix = 202
    fiveOneTwo = 198
    OneZeroTwoFour = 193
    TwoZeroFourEight = 189
    valueArray = [zero,two,four,eight,sixteen,thirtyTwo,sixtyFour,oneTwentyEight,twoFiftySix,
                  fiveOneTwo,OneZeroTwoFour,TwoZeroFourEight]

def swipeRow(row):
    prev = -1 #previous non-zero element
    i = 0
    temp = [0,0,0,0]

    for element in row:
        if element != 0:
            if prev == -1:
               prev = element
               temp[i] = element
               i += 1
            elif prev == element:
                temp[i-1] = 2*prev
                prev = -1
            else:
                prev = element
                temp[i] = element
                i += 1
    return temp

UP = 100
LEFT = 101
DOWN = 102
RIGHT = 103
def getNextGrid(grid,move):
    temp = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]
    if move == UP:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[i + 4*j])
            row = swipeRow(row)
            for j,val in enumerate(row):
                temp[i+4*j] = val
        return temp
    if move == LEFT:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[4*i+j])
            row = swipeRow(row)
            for j,val in enumerate(row):
                temp[4*i+j] = val
        return temp
    if move == RIGHT:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[4*i+(3-j)])
            row = swipeRow(row)
            for j,val in enumerate(row):
                temp[4*i+(3-j)] = val
        return temp
    if move == DOWN:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[i + (12-4*j)])
            row = swipeRow(row)
            for j,val in enumerate(row):
                temp[i + (12-4*j)] = val
        return temp
def getScore(grid):
    score = 0
    for i in range(4):
        for j in range(4):
            score += grid[4*i+j]*scoreGrid[4*i+j]
    return score

def getBestMove(grid):
    scoreUp = getScore(getNextGrid(grid,UP))
    scoreDown = getScore(getNextGrid(grid,DOWN))
    scoreRight = getScore(getNextGrid(grid,RIGHT))
    scoreLeft = getScore(getNextGrid(grid,LEFT))
    
    if not isMoveValid(grid,UP):
        scoreUp = 0
    if not isMoveValid(grid,DOWN):
        scoreDown = 0
    if not isMoveValid(grid,RIGHT):
        scoreRight = 0
    if not isMoveValid(grid,LEFT):
        scoreLeft = 0
    maxScore = max(scoreUp, scoreDown,scoreRight,scoreLeft)
    if maxScore == scoreUp:
        return UP
    elif maxScore == scoreDown:
        return DOWN
    elif maxScore == scoreRight:
        return RIGHT
    elif maxScore == scoreLeft:
        return LEFT
def isMoveValid(grid,move):
    if getNextGrid(grid,move) == currentGrid:
        return False
    else:
        return True;
def performMove(move):
    if move == UP:
        pyautogui.keyDown('up')
        print("UP")
        time.sleep(0.05)
        pyautogui.keyUp('up')
    elif move == DOWN:
        pyautogui.keyDown('down')
        print("DOWN")
        time.sleep(0.05)
        pyautogui.keyUp('down')
    elif move == RIGHT:
        pyautogui.keyDown('right')
        print("RIGHT")
        time.sleep(0.05)
        pyautogui.keyUp('right')
    elif move == LEFT:
        pyautogui.keyDown('left')
        print("LEFT")
        time.sleep(0.05)
        pyautogui.keyUp('left')

def main():
    time.sleep(3)
    while True:
        getGrid()
        performMove(getBestMove(currentGrid))
        
main()
#0 195
#2 230
#4 225
#8 190,191
#16 172,173
#32 160,159,158
#64 139
#128 205
#256 202
#512 198
