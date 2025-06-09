import tkinter as tk
from tkinter import messagebox

class TTTBoard:
    def __init__(self):
        self.board = [''] * 9
        self.current_turn = 'X'
        self.winner = None

    def make_move(self, index):
        if self.board[index] == '' and self.winner is None:
            self.board[index] = self.current_turn
            if self.check_winner(index):
                self.winner = self.current_turn
            elif '' not in self.board:
                self.winner = 'Hòa'
            else:
                self.current_turn = 'O' if self.current_turn == 'X' else 'X'
            return True
        return False

    def check_winner(self, index):
        row = index // 3
        col = index % 3

        # Kiểm tra hàng
        if self.board[row * 3] == self.board[row * 3 + 1] == self.board[row * 3 + 2] == self.current_turn:
            return True

        # Kiểm tra cột
        if self.board[col] == self.board[col + 3] == self.board[col + 6] == self.current_turn:
            return True

        # Kiểm tra đường chéo
        if index % 2 == 0:
            if self.board[0] == self.board[4] == self.board[8] == self.current_turn:
                return True
            if self.board[2] == self.board[4] == self.board[6] == self.current_turn:
                return True

        return False

    def reset(self):
        self.board = [''] * 9
        self.current_turn = 'X'
        self.winner = None

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe OOP")
        self.board = TTTBoard()

        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text='', font=('Arial', 32), width=5, height=2,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.label = tk.Label(root, text="Lượt: X", font=('Arial', 16))
        self.label.grid(row=3, column=0, columnspan=3)

        self.reset_button = tk.Button(root, text="Reset Game", font=('Arial', 14), command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)

    def on_click(self, index):
        if self.board.make_move(index):
            self.buttons[index].config(text=self.board.board[index], state="disabled")
            if self.board.winner:
                if self.board.winner == 'Hòa':
                    self.label.config(text="Kết quả: Hòa!")
                    messagebox.showinfo("Kết quả", "Trò chơi hòa!")
                else:
                    self.label.config(text=f"{self.board.winner} thắng!")
                    messagebox.showinfo("Kết quả", f"{self.board.winner} thắng!")
                self.disable_all_buttons()
            else:
                self.label.config(text=f"Lượt: {self.board.current_turn}")

    def disable_all_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    def reset_game(self):
        self.board.reset()
        for button in self.buttons:
            button.config(text='', state="normal")
        self.label.config(text="Lượt: X")

if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
