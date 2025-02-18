import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x400")
        self.window.configure(bg="#d4f1f4")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        self.window.mainloop()

    def create_board(self):
        # Create a label for the current player's turn
        self.label = tk.Label(self.window, text=f"Player {self.current_player}'s Turn", font=('Arial', 16, 'bold'), bg="#d4f1f4", fg="#05445e")
        self.label.pack(pady=10)

        # Create a grid for the board
        self.frame = tk.Frame(self.window, bg="#d4f1f4")
        self.frame.pack()

        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.frame, text=' ', font=('Arial', 24), width=5, height=2,
                    bg="#189ab4", fg="#ffffff", activebackground="#75e6da",
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, bg="#05445e" if self.current_player == 'X' else "#189ab4", fg="#ffffff")
            self.buttons[row][col].config(state=tk.DISABLED)
            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self, row, col):
        # Check row
        if all(self.board[row][c] == self.current_player for c in range(3)):
            return True
        # Check column
        if all(self.board[r][col] == self.current_player for r in range(3)):
            return True
        # Check main diagonal
        if row == col and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        # Check secondary diagonal
        if row + col == 2 and all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.board[row][col] != ' ' for row in range(3) for col in range(3))

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.label.config(text=f"Player {self.current_player}'s Turn")
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=' ', state=tk.NORMAL, bg="#189ab4", fg="#ffffff")

if __name__ == "__main__":
    TicTacToe()