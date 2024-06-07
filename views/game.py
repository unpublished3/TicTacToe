import customtkinter as tk


class Game(tk.CTkFrame):
    _scale_factor = None
    _text_font_size = None
    _label_text = None

    def __init__(self, parent, player):
        tk.CTkFrame.__init__(self, parent)
        self.grid()

        self._configure_grid()

        self._scale_factor = (self.winfo_screenwidth() * self.winfo_screenheight()) / (
            2560 * 1600
        )
        self._text_font_size = 25 * self._scale_factor

        self._label_text = tk.StringVar(self, f"{player}'s Turn")
        self._create_label()

    def _configure_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

    def _create_label(self):
        label = tk.CTkLabel(
            self, textvariable=self._label_text, font=("Arial", self._text_font_size)
        )
        label.grid(row=0, column=0, columnspan=5, sticky="nsew")

    def change_label_text(self, text):
        self._label_text.set(text)
