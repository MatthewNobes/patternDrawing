from graphics import *
import math

def main():
    #collects the inputs from the user
    winSizeIn, colourList = getInputs()
    #runs the window making function
    win= makeWin(winSizeIn)
    
    #runs the pattern drawing function
    drawPattens(winSizeIn, win, colourList)
    
    selectSector(win,  winSizeIn, colourList)
    
def getInputs():
    winNotValid = True
    while winNotValid == True:
        try :
            winSizeIn = (int(input("Enter size of window. 5X5, 7X7 or 9X9 (Enter either 5, 7 or 9): ")))
        except:
            print("Must be an integer value")
        else:
            if winSizeIn == 5 or winSizeIn == 7 or winSizeIn == 9:
                winNotValid = False
    acceptedColours = ["red", "green", "blue", "orange", "pink", "magenta"]
    colourList = ["r", "g", "b"]
    for i in range (0, 3):
        colRepeated = True
        while colRepeated == True:
            inputColour = (input(str(i+1)+" Enter a new colour: "))
            if inputColour in acceptedColours: 
                colRepeated = False
                colourList[i]= inputColour
                acceptedColours.remove(inputColour)
    return winSizeIn, colourList
    
def makeWin(winSizeIn):
    winSize = winSizeIn * 100 
    win = GraphWin("Python Courswork", winSize, winSize)
    return win
    
def drawPattens(winSizeIn, win, colourList):
    for i in range(0, winSizeIn):
        for n in range (0, winSizeIn):
            x= 0 + (i*100)
            y= 0 + (n*100)
            if (x < -y+ ((winSizeIn-1)*100)) and (x < y):
                clr = colourList[1]
                drawBricks(x, y, win, clr)
            elif (x > y) and (x > -y+((winSizeIn-1)*100)):
                clr = colourList[2]
                drawBricks(x, y, win, clr)
            else: 
                clr = colourList[0]
                drawSquares(x, y, win, clr)
#draws out the brick pattern with the start co-ordinates and colour
def drawBricks(x, y, win, clr):
    #draws the secound row with the spaces in it
    for i in range (0,4):
        for n in range (0,5):
            sqrDraw = Rectangle(Point(x +(i*25), y +(n*20)), Point(x+25 +(i *25), y+10 +(n*20)))
            sqrDraw.setFill(clr)
            sqrDraw.draw(win)
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

def selectSector(win, winSizeIn, colourList):
    try :
        while True: 
            click = win.getMouse()
            x = math.floor(click.getX() / 100) * 100
            y = math.floor(click.getY() / 100) * 100            
            selectSquare = drawSelect(win, x, y)           
            patternSelected(x, y, win, selectSquare, winSizeIn, colourList)
    except :
        win.close()
    
def drawSelect(win, x, y):
    selectSquare= Rectangle(Point(x, y), Point(x + 100, y + 100))
    selectSquare.setWidth(5)
    selectSquare.draw(win)
    return selectSquare
        
def coverSelected(x, y, win):
    deleteSquare= Rectangle(Point(x, y), Point(x + 100, y + 100))
    deleteSquare.setFill("white")
    deleteSquare.setOutline("white")
    deleteSquare.draw(win)
            
def patternSelected(x, y, win, selectSquare, winSizeIn, colourList):
    Selected = True
    while Selected == True:
        key = win.getKey()
        if key == "d":
            coverSelected(x, y, win)
        elif key == "Return":
            selectSquare.undraw()
            Selected = False 
            return 
        elif key == "s":
            coverSelected(x, y, win)
            if (x < -y+ ((winSizeIn-1)*100)) and (x < y):
                clr = colourList[1]
                drawSquares(x, y, win, clr)
            elif (x > y) and (x > -y+((winSizeIn-1)*100)):
                clr = colourList[2]
                drawSquares(x, y, win, clr)
            else: 
                clr = colourList[0]
                drawBricks(x, y, win, clr)
        elif key == "r" or key == "g" or key == "b" or key == "m" or key == "o" or key == "p":
            coverSelected(x, y, win)
            if key == "r":
                clr = "red"
            elif key == "g":
                clr = "green"
            elif key == "b":
                clr ="blue"
            elif key == "m":
                clr ="magenta"
            elif key == "o":
                clr ="orange"
            elif key == "p":
                clr ="purple"
            drawSquares(x, y, win, clr)            
main()