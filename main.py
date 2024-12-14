import tkinter as tk
from random import shuffle
#Roles:
#JB - 
#Seth - 
#Carlo -
#Drew -
#JD -

def main(master, size): #main game function
    global grid #Is needed to be able to access the grid variable from the shuffleTile() function
    global buttons #Is needed to be able to access the buttons variable from the updateButton() function
    
    grid = [x for x in range(1, size*size)] + [None] #numbers that will be on the grid game + including the blank space 
    buttons = [] #placeholder for the buttons that will be created
    for i in range(size):
        rows = [] #placeholder for the rows
        for j in range(size):
            button = tk.Button(master, width=5, command=lambda i=i, j=j: moveTile(i, j)) #creates the buttons, lambda is used to pass the i and j values to the moveTile function cuz command= only accepts lambda arguments
            button.grid(row=i, column=j) #adds it to the tkinter grid
            rows.append(button) #adds the buttons directory to the rows list
        buttons.append(rows) #adds the rows list (is a row of buttons) to the buttons list
    updateButton() #updates the grid with the buttons
    shuffleTile() #randomizer
    
def moveTile(row, column):
    index = row * size + column 
    emptyIndex = grid.index(None) 
    if index in [emptyIndex - 1, emptyIndex + 1, emptyIndex - size, emptyIndex + size]: #checks if the tile is adjacent to the empty tile
        grid[emptyIndex], grid[index] = grid[index], grid[emptyIndex] #swaps the empty tile with the tile
        updateButton()

def updateButton():
    for i in range(size):
        for j in range(size):
            ifTile = grid[i * size + j] #ifTile is the value of the grid at the index i * size + j, if it is None, it will be blank
            buttons[i][j].config(text=ifTile if ifTile else "") #adds the text in the middle of each button in the tile
            
def shuffleTile():
    shuffle(grid)
    updateButton()

if __name__ == "__main__": #will only run if the file is run directly
    status = True
    while status:
        try:
            size = int(input("Enter the size of the game (must be greater than 3): "))
            if size >=3:
                root = tk.Tk()
                main(root, size)
                root.mainloop()
                status = False #stops the game
            else:
                print("Invalid input. Please enter a number greater than 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
