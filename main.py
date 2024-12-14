from tkinter import ttk
from random import shuffle
#Roles:
#JB - 
#Seth - 
#Carlo -
#Drew -
#JD -

def main(size): #main game function
    grid = [x for x in range(1, size)] + [None] #numbers that will be on the grid game + including the blank space
    shuffle(grid) 
    return print(grid)


    

if __name__ == "__main__": #will only run if the file is run directly
    status = True
    while status:
        try:
            size = int(input("Enter the size of the game (must be greater than 3): "))
            if size >=3:
                squared = size*size #size of the grid needs to be raise to the power of 2 to work
                main(squared)
                status = False #stops the game
            else:
                print("Invalid input. Please enter a number greater than 3.")
        except:
            print("Invalid input. Please enter a number.")
            continue