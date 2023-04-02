import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" "]*9
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text=" ", font=("Helvetica", 20), width=4, height=2, command=lambda i=i: self.button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
        self.status = tk.Label(self.master, text="Player X's turn", font=("Helvetica", 16), pady=10)
        self.status.grid(row=3, column=0, columnspan=3)

    def button_click(self, index):
        if self.board[index] != " ":
            messagebox.showerror("Error", "That position is already taken. Try again.")
            return
        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)
        if self.check_win():
            self.status.config(text=f"Player {self.current_player} wins!")
            self.disable_buttons()
        elif self.board.count(" ") == 0:
            self.status.config(text="It's a tie!")
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            self.status.config(text=f"Player {self.current_player}'s turn")

    def check_win(self):
        win_combos = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        for combo in win_combos:
            if all(self.board[i] == self.current_player for i in combo):
                return True
        return False

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
