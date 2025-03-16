import tkinter as tk
import random

class Puzzle8:
    def __init__(self, root):
        self.root = root
        self.root.title("8 Puzzle Game")
        self.tiles = []
        self.board = list(range(1, 9)) + [None]  # 1-8 numbers + empty space
        self.create_ui()  # Initialize UI first
        self.shuffle_solvable()  # Shuffle the board after UI is ready

    def create_ui(self):
        self.canvas = tk.Canvas(self.root, width=300, height=300, bg='white')
        self.canvas.grid(row=0, column=0, columnspan=3)
        self.shuffle_btn = tk.Button(self.root, text="Shuffle", command=self.shuffle_solvable)
        self.shuffle_btn.grid(row=1, column=0, sticky='ew')
        self.reset_btn = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_btn.grid(row=1, column=1, sticky='ew')
        self.exit_btn = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_btn.grid(row=1, column=2, sticky='ew')
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        self.tiles.clear()
        for i, value in enumerate(self.board):
            x, y = (i % 3) * 100, (i // 3) * 100
            if value:
                rect = self.canvas.create_rectangle(x, y, x + 100, y + 100, fill='#3498db', outline='white')
                text = self.canvas.create_text(x + 50, y + 50, text=str(value), font=("Arial", 24, "bold"), fill="white")
                self.tiles.append((rect, text))
            else:
                self.empty_spot = i

    def on_click(self, event):
        x, y = event.x // 100, event.y // 100
        clicked_index = y * 3 + x
        if self.is_valid_move(clicked_index):
            self.move_tile(clicked_index)
            self.check_win()

    def is_valid_move(self, index):
        row, col = divmod(index, 3)
        empty_row, empty_col = divmod(self.empty_spot, 3)
        return abs(row - empty_row) + abs(col - empty_col) == 1

    def move_tile(self, clicked_index):
        # Swap the clicked tile with the empty spot
        self.board[self.empty_spot], self.board[clicked_index] = self.board[clicked_index], self.board[self.empty_spot]
        self.empty_spot = clicked_index
        self.draw_board()

    def shuffle_solvable(self):
        # Shuffle until a solvable board is found
        while True:
            random.shuffle(self.board)
            if self.is_solvable():
                break
        self.draw_board()

    def is_solvable(self):
        # Count inversions to determine if the puzzle is solvable
        inversions = 0
        flat_board = [tile for tile in self.board if tile is not None]
        for i in range(len(flat_board)):
            for j in range(i + 1, len(flat_board)):
                if flat_board[i] > flat_board[j]:
                    inversions += 1
        # For a 3x3 puzzle, it's solvable if the number of inversions is even
        return inversions % 2 == 0

    def reset(self):
        self.board = list(range(1, 9)) + [None]
        self.draw_board()

    def check_win(self):
        if self.board == list(range(1, 9)) + [None]:
            self.canvas.create_text(150, 150, text="You Win!", font=("Arial", 30, "bold"), fill="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = Puzzle8(root)
    root.mainloop()