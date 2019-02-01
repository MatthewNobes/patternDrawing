from graphics import *

def main():
    #collects the inputs from the user
    winSizeIn, colourList = getInputs()
    #runs the window making function
    win= makeWin(winSizeIn)
    #runs the pattern drawing function
    drawPattens(winSizeIn, win, colourList)
    
def getInputs():
    winSizeIn = (int(input("Enter size of window. 5X5, 7X7 or 9X9 (Enter either 5, 7 or 9): ")))
    colourList = ["s", "s", "s"]
    for i in range (0, 3):
        colRepeated = True
        while colRepeated == True:
            inputColour = (input(str(i+1)+" Enter a new colour: "))
            if inputColour != colourList[0]: 
                if inputColour != colourList[1]:
                    if inputColour != colourList[2]:
                        colRepeated = False
                        colourList[i]= inputColour
    return winSizeIn, colourList
    
def makeWin(winSizeIn):
    winSize = winSizeIn * 100 
    win = GraphWin("Python Courswork", winSize, winSize)
    return win
    
def drawPattens(winSizeIn, win, colourList):
    #used to establish the middle row in each circumstance
    midRow = int((winSizeIn/2)+0.5)
    
    line1 = Line(Point(0,0), Point(winSizeIn * 100, winSizeIn * 100))
    line2 = Line(Point(winSizeIn * 100,0), Point(0, winSizeIn * 100))
    
    line1.draw(win)
    line2.draw(win)
    for i in range(0, winSizeIn):
        for n in range (0, winSizeIn):
            x= 0 + (i*100)
            y= 0 + (n*100)

            
            if :
                
                clr = colourList[1]
                drawBricks(x, y, win, clr)
            #elif (x > y) :
                #clr = colourList[2]
                #drawBricks(x, y, win, clr)
            #else: 
                #clr = colourList[0]
                #drawSquares(x, y, win, clr)
#draws out the brick pattern with the start co-ordinates and colour
def drawBricks(x, y, win, clr):
    for i in range (0,4):
        for n in range (0,5):
            sqrDraw = Rectangle(Point(x +(i*25), y +(n*20)), Point(x+25 +(i *25), y+10 +(n*20)))
            sqrDraw.setFill(clr)
            sqrDraw.draw(win)
    #draws the secound row with the spaces in it
    for i in range (0,3):
        for n in range (0,5):
            sqrDraw = Rectangle(Point(x+0 +(i *40), y+10 +(n*20)), Point(x+20 +(i *40), y+20 +(n*20)))
            sqrDraw.setFill(clr)
            sqrDraw.draw(win)
#draws out the square pattern with the start co-ordinates and colour
def drawSquares(x, y, win, clr):
    for i in range(0, 10):
        squareDraw = Rectangle(Point(x+0 +(i*5), y+0 +(i*5)), Point(x+100 -(i*5), y+100 -(i*5)))
        if i % 2 == 0:
            squareDraw.setFill(clr)
        else:
            squareDraw.setFill("white")
        squareDraw.draw(win)
main()