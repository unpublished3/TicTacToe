import customtkinter as tk


class Menu(tk.CTkFrame):
    _scale_factor = None
    _text_font_size = None

    def __init__(self, parent, set_player):
        tk.CTkFrame.__init__(self, parent)
        self.grid()
        self.set_player = set_player

        self._configure_grid()
        self._scale_factor = (self.winfo_screenwidth() * self.winfo_screenheight()) / (
            2560 * 1600
        )
        self._text_font_size = 25 * self._scale_factor
        self._create_label()
        self._create_buttons()

    def _configure_grid(self):
        # Configure Columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Confifure Rows
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=1)

    def _create_label(self):
        label = tk.CTkLabel(self, text="Play", font=("Arial", self._text_font_size))
        label.grid(row=0, column=0, columnspan=2, sticky="nsew")

    def _create_buttons(self):
        x_buttom = tk.CTkButton(
            self,
            text="Play as X",
            font=("Arial", self._text_font_size),
            fg_color=("black", "white"),
            text_color=("white", "black"),
            border_spacing=10,
            corner_radius=10,
            anchor="center",
            cursor="hand2",
            hover_color=("#444546", "#b5b4b5"),
            command=lambda: self.set_player("X")
        )

        o_buttom = tk.CTkButton(
            self,
            text="Play as O",
            font=("Arial", self._text_font_size),
            fg_color=("black", "white"),
            text_color=("white", "black"),
            border_spacing=10,
            corner_radius=10,
            anchor="center",
            cursor="hand2",
            hover_color=("#444546", "#b5b4b5"),
            command=lambda: self.set_player("X")

        )

        x_buttom.grid(row=2, column=0, sticky="n")
        o_buttom.grid(row=2, column=1, sticky="n")
