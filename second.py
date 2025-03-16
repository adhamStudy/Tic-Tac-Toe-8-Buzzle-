import tkinter as tk
from tkinter import messagebox

# Colors
BG_COLOR = "#2C3E50"
BTN_COLOR = "#ECF0F1"
X_COLOR = "#E74C3C"
O_COLOR = "#3498DB"
WIN_COLOR = "#2ECC71"

# Game state
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = []

# Initialize window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x450")
root.configure(bg=BG_COLOR)

# Status label
status_label = tk.Label(root, text="Player X's Turn", font=("Arial", 14, "bold"), fg="white", bg=BG_COLOR)
status_label.pack(pady=10)

# Frame for board
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack()

# Button click function
def on_click(row, col):
    global current_player

    if board[row][col] == "" and not check_winner():
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, fg=X_COLOR if current_player == "X" else O_COLOR)

        winner = check_winner()
        if winner:
            highlight_winner(winner)
            status_label.config(text=f"Player {winner} Wins!")
        elif is_draw():
            status_label.config(text="It's a Draw!")
            messagebox.showinfo("Game Over", "It's a Draw!")
        else:
            current_player = "O" if current_player == "X" else "X"
            status_label.config(text=f"Player {current_player}'s Turn")

# Check for winner
def check_winner():
    # Rows & Columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

# Check for draw
def is_draw():
    return all(board[i][j] != "" for i in range(3) for j in range(3))

# Highlight winner
def highlight_winner(player):
    for row in range(3):
        for col in range(3):
            if board[row][col] == player:
                buttons[row][col].config(bg=WIN_COLOR)

    messagebox.showinfo("Game Over", f"Player {player} Wins!")

# Reset game
def reset_game():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    status_label.config(text="Player X's Turn")

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg=BTN_COLOR)

# Create buttons
for i in range(3):
    row_buttons = []
    for j in range(3):
        btn = tk.Button(frame, text="", font=("Arial", 24, "bold"), width=5, height=2, bg=BTN_COLOR,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row_buttons.append(btn)
    buttons.append(row_buttons)

# Restart button
reset_btn = tk.Button(root, text="Restart", font=("Arial", 14, "bold"), bg=O_COLOR, fg="white", command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()
