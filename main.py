from typing import Tuple
import customtkinter as tk
from views.menu import Menu
from views.game import Game


class Window(tk.CTk):
    _player = None

    def __init__(self):
        super().__init__()

        self.width = int(self.winfo_screenwidth() * 0.325)
        self.height = int(self.winfo_screenheight() * 0.6125)

        x = int(self.winfo_screenwidth() / 2) - (self.width / 2)
        y = int(self.winfo_screenheight() / 2) - (self.height / 2)

        print(x, y)

        self.geometry("600x400+%d+%d" % (x, y))
        self.title("TicTacToe")

        self._configure_grid()

        self.resizable(False, False)
        self.menu = Menu(self, self._set_player)
        self.set_frame()

    def _configure_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def set_frame(self):
        if not self._player:
            # self.game.grid_remove()
            self.menu.grid(row=0, column=0, sticky="snew")
        else:
            self.menu.grid_remove()
            self.game = Game(self, self._player)
            self.game.grid(row=0, column=0, sticky="snew")
            self.resizable(True, True)
            self.geometry(f"{self.width}x{self.height}")
            self.resizable(False, False)

    def _set_player(self, player):
        self._player = player
        self.set_frame()


window = Window()
window.mainloop()
