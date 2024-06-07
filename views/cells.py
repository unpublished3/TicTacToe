from typing import Any, Tuple
import customtkinter as tk


class Cells(tk.CTkFrame):
    _cells = []
    _buttons = []

    def __init__(self, parent):
        super().__init__(parent)

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
                        border_width=5,
                    )
                )

                self._buttons[i][j].grid(row=i, column=j, sticky="nsew")
