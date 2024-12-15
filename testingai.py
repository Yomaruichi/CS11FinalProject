import tkinter as tk
import random

class SlidingPuzzle:
    def __init__(self, master):
        self.master = master
        self.master.title("Sliding Puzzle")
        self.size = 4
        self.tiles = list(range(1, self.size * self.size)) + [None]
        self.buttons = []
        self.create_widgets()
        self.shuffle_tiles()

    def create_widgets(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                button = tk.Button(self.master, width=10, height=5, command=lambda i=i, j=j: self.move_tile(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
        self.update_buttons()

    def shuffle_tiles(self):
        random.shuffle(self.tiles)
        while not self.is_solvable() or self.is_solved():
            random.shuffle(self.tiles)
        self.update_buttons()

    def is_solvable(self):
        inv_count = 0
        for i in range(len(self.tiles) - 1):
            for j in range(i + 1, len(self.tiles)):
                if self.tiles[i] and self.tiles[j] and self.tiles[i] > self.tiles[j]:
                    inv_count += 1
        return inv_count % 2 == 0

    def is_solved(self):
        return self.tiles == list(range(1, self.size * self.size)) + [None]

    def move_tile(self, i, j):
        index = i * self.size + j
        empty_index = self.tiles.index(None)
        if index in [empty_index - 1, empty_index + 1, empty_index - self.size, empty_index + self.size]:
            self.tiles[empty_index], self.tiles[index] = self.tiles[index], self.tiles[empty_index]
            self.update_buttons()
            if self.is_solved():
                self.show_victory_message()

    def update_buttons(self):
        for i in range(self.size):
            for j in range(self.size):
                tile = self.tiles[i * self.size + j]
                self.buttons[i][j].config(text=tile if tile else "")

    def show_victory_message(self):
        victory_label = tk.Label(self.master, text="You Win!", font=("Helvetica", 24))
        victory_label.grid(row=self.size, column=0, columnspan=self.size)

if __name__ == "__main__":
    root = tk.Tk()
    game = SlidingPuzzle(root)
    root.mainloop()
