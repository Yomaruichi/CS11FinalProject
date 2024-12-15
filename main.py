import tkinter as tk
from tkinter import ttk as ctk
from random import shuffle


#Roles:
#JB - 
#Seth - 
#Carlo -
#Drew -
#JD -

class actualGame:
    def main(master, size): #main game function for this app
        global grid #Is needed to be able to access the grid variable from the shuffleTile() function
        global buttons #Is needed to be able to access the buttons variable from the updateButton() function
        
        grid = [x for x in range(1, size*size)] + [None] #numbers that will be on the grid game + including the blank space 
        buttons = [] #placeholder for the buttons that will be created
        for i in range(size):
            rows = [] #placeholder for the rows
            for j in range(size):
                button = tk.Button(master, font=("Arial",16), command=lambda i=i, j=j: actualGame.moveTile(i, j), bg = "yellow", activebackground="green",cursor= "dotbox") #creates the buttons, lambda is used to pass the i and j values to the moveTile function cuz command= only accepts lambda arguments
                button.grid(row=i, column=j, sticky="news") #adds it to the tkinter grid
                rows.append(button) #adds the buttons directory to the rows list
            buttons.append(rows) #adds the rows list (is a row of buttons) to the buttons list
        actualGame.updateButton() #updates the grid with the buttons
        actualGame.shuffleTile() #randomizer

        for i in range(size): #this allows the buttons to resize with the frame depending on the grid size
            master.columnconfigure(i, weight=1) 
            master.rowconfigure(i, weight=1)
        
    def moveTile(row, column):
        index = row * size + column
        emptyIndex = grid.index(None)
        empty_col = emptyIndex % size
        
        if index in [emptyIndex - 1, emptyIndex + 1, emptyIndex - size, emptyIndex + size]:
            if (empty_col == 0 and column == size - 1) or (empty_col == size - 1 and column == 0): # check if we are at the edge
                return  # prevents edging

            grid[emptyIndex], grid[index] = grid[index], grid[emptyIndex]
            actualGame.updateButton()
            if actualGame.isSolved():
                print("You Win!")

    def updateButton():
        for i in range(size):
            for j in range(size):
                ifTile = grid[i * size + j] #ifTile is the value of the grid at the index i * size + j, if it is None, it will be blank
                buttons[i][j].config(text=ifTile if ifTile else "") #adds the text in the middle of each button in the tile\
                    
    def IsSolvable():
        inversionCount = 0
        for i in range(len(grid)-1):
            for j in range(i+1, len(grid)):
                if grid[i] and grid[j] and grid[i] > grid[j]: #checks if i and j exists and i is greater than j,
                    inversionCount += 1
        return inversionCount % 2 == 0 #if inversion count is odd, it is not solvable, if it is even, it is solvable
    
    def isSolved():
        return grid == [x for x in range(1, size*size)] + [None] #checks if the grid is equal to the numbers in the grid + None

    def shuffleTile():
        shuffle(grid)
        while not actualGame.IsSolvable() or actualGame.isSolved():
            shuffle(grid)
        actualGame.updateButton()
    
    def timer():
        while currentTime <= startTime:
            currentTime -= 1
            
            



def mainMenu():

    pass

def getnativeResolution():
    baseResolution = "600x900"
    scaledResolution = 0.75

    userHeight = mainWindow.winfo_screenheight()
    userWidth = mainWindow.winfo_screenwidth()

    calculatedHeight = userHeight / (int(baseResolution.split("x")[1]))
    calculatedWidth = userWidth / (int(baseResolution.split("x")[0]))
    scaleFactor = min(calculatedHeight, calculatedWidth)

    actualHeight = round((int(baseResolution.split("x")[1]) * scaleFactor * scaledResolution)) 
    actualWidth = round((int(baseResolution.split("x")[0]) * scaleFactor * scaledResolution))

    return (actualWidth, actualHeight, scaleFactor, scaledResolution)
    
def gotoGameScreen():
    status = 1
    if status == 1:
        tlFrame = tk.Frame(mainWindow, bg ="blue")
        tlFrame.place(relx = .6, rely = .1, anchor="nw", width = 200, height = 100)

        trFrame = tk.Frame(mainWindow, bg ="green")
        trFrame.place(relx = .4, rely = .1, anchor="ne", width = 200, height = 100)

        buttonsFrame = tk.Frame(mainWindow,bg ="blue")
        buttonsFrame.place(relx=.5, rely=.55, anchor="center", width=500, height=500)
        actualGame.main(buttonsFrame, size)

if __name__ == "__main__": #will only run if the file is run directly
    mainWindow = tk.Tk()

    resolution = getnativeResolution()
    width = resolution[0]
    height = resolution[1]
    scalingRef = resolution[2] * resolution[3]
    defaultGridSize = 4
    size = defaultGridSize
    status = 0

    gotoGameScreen()

    mainWindow.title("Sliding Puzzle")
    mainWindow.geometry(f"{width}x{height}")
    mainWindow.configure(bg="brown")
    mainWindow.resizable(0,0)
    mainWindow.mainloop()
