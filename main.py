from typing import Tuple
import customtkinter as tk
from views.menu import Menu
from views.game import Game


class Window(tk.CTk):
    def __init__(self):
        super().__init__()

        width = int(self.winfo_screenwidth() * 0.3125)
        height = int(self.winfo_screenheight() * 0.625)

        self.geometry(f"600x400")
        self.title("TicTacToe")

        self._configure_grid()

        self.menu = Menu(self)
        self.game = Game(self, "X")
        self.switch_frame(0)

    def _configure_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def switch_frame(self, n):
        print(self.menu)
        print(self.game)
        if n == 0:
            self.game.grid_remove()
            self.menu.grid(row=0, column=0, sticky="snew")
        else:
            self.menu.grid_remove()
            self.game.grid(row=0, column=0, sticky="snew")


window = Window()
window.mainloop()
