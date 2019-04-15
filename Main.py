from tkinter import *
import Heroes
import Towers



def init(data):
    data.map = [
    [1,1,1,1,1,1,0,0,0,3,3,3,3,3,3],
    [1,1,1,1,1,1,0,0,0,3,3,3,3,3,3],
    [1,1,1,1,1,0,0,0,3,3,3,3,3,3,3],
    [2,2,1,1,0,0,0,1,3,3,3,3,3,3,2],
    [2,2,1,0,0,0,1,1,1,0,0,0,3,2,2],
    [2,2,2,0,0,0,1,1,0,0,0,0,0,2,2],
    [2,2,2,0,0,0,0,0,0,0,0,0,0,2,2],
    [1,2,2,2,0,0,0,0,0,0,3,0,0,0,2],
    [1,2,2,2,2,2,2,2,3,3,3,0,0,0,2],
    [1,1,2,2,2,2,2,4,2,3,0,0,0,2,2],
    [1,1,1,1,1,2,2,2,0,0,0,0,0,2,2],
    [1,5,5,5,1,0,0,0,0,0,0,0,2,2,2],
    [1,5,5,5,0,0,0,0,0,0,1,1,2,2,2],
    [1,5,5,5,0,0,0,1,1,1,1,2,2,2,2],
    [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2]]
    
    data.mapColors = ["tan4", "olive drab", "Cadet Blue3", "brown4", "gray74", "DeepSkyBlue2"]

    data.s = data.height // 15
    
    data.level = 1
    
    data.waves = [
    [0,0,0,0],
    [1,1,1],
    [1,1,1,1],
    [2,2,2,2,2],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2],
    [3,3,3,3,3],
    [20]]
    
    data.wave = 0
    data.wavePos = 0
    
    data.heroes = []
    
    data.counter = 0
    
    data.paused = False
    data.dCost = 100
    data.cCost = 100
    data.aCost = 100
    data.gold = 500
    pass

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    if not data.paused:
        data.counter += 1
        for hero in data.heroes:
            hero.move()
        
        if data.counter % 10 == 0:
            data.heroes.append(Heroes.Villager(50, 50))
    pass

def redrawAll(canvas, data):
    drawMap(canvas,data)
    drawSidebar(canvas, data)
    drawHeroes(canvas, data)
    
    pass
    
def drawMap(canvas, data):
    for row in range(15):
        for col in range(15):
            canvas.create_rectangle(col*data.s, row*data.s, (col+1)*data.s, (row+1)*data.s, fill=data.mapColors[data.map[row][col]], outline="")

def drawSidebar(canvas, data):
    canvas.create_rectangle(data.height, 0, data.width, data.height, fill="ivory3")
    canvas.create_text((data.width + data.height)//2, data.height//3, text="Level " + str(data.level) + "   " + str(len(data.waves)) + " Waves")
    canvas.create_text((data.width + data.height)//2, data.height//2, text="Gold: " + str(data.gold))
    
    
def drawHeroes(canvas, data):
    for hero in data.heroes:
        hero.draw(canvas)


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 600)