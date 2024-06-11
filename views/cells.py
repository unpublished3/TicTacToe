import customtkinter as tk
import logic


class Cells(tk.CTkFrame):
    _buttons = []
    _data = []
    _turn = "X"

    def __init__(self, parent, player, cells):
        super().__init__(parent)
        self._cells = cells

        self._scale_factor = (self.winfo_screenwidth() * self.winfo_screenheight()) / (
            2560 * 1600
        )
        self._text_font_size = 50 * self._scale_factor
        self._parent = parent
        self._buttons = []

        self._player = player
        self._configure_grid()
        self._create_cells()

        if player != self._turn:
            self._computer_move()

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
            self._data.append([])

            self._buttons.append([])
            for j in range(3):
                self._data[i].append("")

                self._cells[i].append(tk.StringVar(self))
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
                        font=("Helvetica", self._text_font_size),
                        text_color_disabled=("black", "white"),
                        text_color=("black", "white"),
                    )
                )

                self._buttons[i][j].grid(row=i, column=j, sticky="nsew")

    def _click(self, i, j):
        if logic.terminal(self._data):
            self._handle_terminal()
            return

        if self._data[i][j] != "X" and self._data[i][j] != "O":
            self._data[i][j] = logic.turn(self._data)
            self._cells[i][j].set(self._data[i][j])

            self._turn = logic.turn(self._data)
            self._parent.change_label_text(
                f"{self._player}'s Turn"
                if self._player == self._turn
                else "Computer Thinking..."
            )

            if logic.terminal(self._data):
                self._handle_terminal()
                return

            if self._player != self._turn:
                self._computer_move()

    def _computer_move(self):
        i, j = logic.minimax(self._data)
        self._click(i, j)

    def _handle_terminal(self):
        for row in self._buttons:
            for button in row:
                button.configure(state="disabled")

        utility = logic.utility(self._data)

        if utility == 0:
            self._parent.change_label_text("Draw")
        elif utility == 1:
            self._parent.change_label_text("X wins")
        elif utility == -1:
            self._parent.change_label_text("O Wins")
