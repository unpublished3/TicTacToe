import customtkinter as tk
from views.menu import Menu
from views.game import Game


class Window(tk.CTk):
    _player = None

    def __init__(self):
        super().__init__()

        self.width = int(self.winfo_screenwidth() * 0.325)
        self.height = int(self.winfo_screenheight() * 0.6125)
        self.x = int(self.winfo_screenwidth() / 2) - (self.width / 2)
        self.y = int(self.winfo_screenheight() / 2) - (self.height / 2)


        self.title("TicTacToe")

        self._configure_grid()

        self.menu = Menu(self, self.set_player)
        self.set_frame()

    def _configure_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def set_frame(self):
        if (hasattr(self, "menu")):
            del self.menu
        
        if (hasattr(self, "game")):
            del self.game
            
        for child in self.winfo_children():
            child.destroy()

        if not self._player:
            self.menu = Menu(self, self.set_player)
            self.menu.grid(row=0, column=0, sticky="snew")
            self.set_window_size(600, 400, self.x, self.y)

        else:
            self.game = Game(self, self._player)
            self.game.grid(row=0, column=0, sticky="snew")
            self.set_window_size(self.width, self.height, self.x, self.y)

    def set_player(self, player):
        self._player = player
        self.set_frame()

    def set_window_size(self, x, y, a, b):
        self.resizable(True, True)
        self.geometry("%dx%d+%d+%d" % (x, y, a, b))
        self.resizable(False, False)


if __name__ == "__main__":
    window = Window()
    window.mainloop()
