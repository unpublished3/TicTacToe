import customtkinter as tk


class Cells(tk.CTkFrame):
    _cells = []
    _buttons = []

    def __init__(self, parent, player):
        super().__init__(parent)

        self._scale_factor = (self.winfo_screenwidth() * self.winfo_screenheight()) / (
            2560 * 1600
        )
        self._text_font_size = 50 * self._scale_factor

        self._player = player
        self._configure_grid()
        self._create_cells()

    def _configure_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def _create_cells(self):
        for i in range(3):
            self._cells.append([])
            self._buttons.append([])
            for j in range(3):
                self._cells[i].append(tk.StringVar(self, ""))
                self._buttons[i].append(
                    tk.CTkButton(
                        self,
                        textvariable=self._cells[i][j],
                        border_color=("black", "white"),
                        border_width=2,
                        fg_color="transparent",
                        hover=False,
                        anchor="center",
                        cursor="hand2",
                        corner_radius=0,
                        command=lambda i=i, j=j: self._click(i, j),
                        font=("Arial", self._text_font_size)
                    )
                )

                self._buttons[i][j].grid(row=i, column=j, sticky="nsew")

    def _click(self, i, j):
        self._cells[i][j].set(self._player)
