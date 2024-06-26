import customtkinter as tk
from .cells import Cells


class Game(tk.CTkFrame):
    _scale_factor = None
    _text_font_size = None
    _label_text = None
    _cells = []
    _play_again_button = None

    def __init__(self, parent, player):
        tk.CTkFrame.__init__(self, parent)
        self.grid()

        self._configure_grid()
        self._player = player
        self._parent = parent

        self._scale_factor = (self.winfo_screenwidth() * self.winfo_screenheight()) / (
            2560 * 1600
        )
        self._text_font_size = 25 * self._scale_factor

        self._label_text = tk.StringVar(
            self, f"{player}'s Turn" if player == "X" else "Computer Thinking..."
        )

        self._cells = []

        self.cells = Cells(self, player, self._cells)

        self._create_label()
        self.arrange_cells()
        self.add_play_again()

    def _configure_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)
        self.grid_rowconfigure(9, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

    def _create_label(self):
        label = tk.CTkLabel(
            self,
            textvariable=self._label_text,
            font=("Helvetica", self._text_font_size),
        )
        label.grid(row=0, column=0, columnspan=5, sticky="nsew")

    def change_label_text(self, text):
        self._label_text.set(text)

    def arrange_cells(self):
        self.cells.grid(row=2, column=1, rowspan=6, columnspan=3, sticky="nsew")

    def add_play_again(self):
        self._play_again_button = tk.CTkButton(
            self,
            text="Play Again",
            font=("Helvetica", self._text_font_size),
            fg_color=("#2B2B2B", "#DBDBDB"),
            text_color=("#DBDBDB", "#2B2B2B"),
            border_spacing=10,
            corner_radius=10,
            anchor="center",
            cursor="hand2",
            hover_color=("#444546", "#e0e0e1"),
            command=self._new_game,
        )
        self._play_again_button.grid(row=9, column=0, columnspan=5, sticky="n")

    def _new_game(self):
        del self.cells
        for child in self.winfo_children():
            child.destroy()

        self._parent.set_player(None)
