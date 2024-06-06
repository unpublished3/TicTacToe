import customtkinter as tk


def create_menu(parent):
    menu = tk.CTkFrame(parent)
    menu.pack(fill="both", expand=True)

    scale_factor = (menu.winfo_screenwidth() * menu.winfo_screenheight()) / (
        2560 * 1600
    )
    text_font_size = 25 * scale_factor

    # Configure Columns
    menu.columnconfigure(0, weight=1)
    menu.columnconfigure(1, weight=1)

    # Confifure Rows
    menu.rowconfigure(0, weight=1)
    menu.rowconfigure(1, weight=1)
    menu.rowconfigure(2, weight=2)
    menu.rowconfigure(3, weight=1)

    label = tk.CTkLabel(menu, text="Play", font=("Arial", text_font_size))
    label.grid(row=0, column=0, columnspan=2, sticky="nsew")

    x_buttom = tk.CTkButton(
        menu,
        text="Play as X",
        font=("Arial", text_font_size),
        border_color=("black", "white"),
        border_width=5,
        fg_color=("black", "white"),
        text_color=("white", "black"),
        border_spacing=10,
        corner_radius=10,
        anchor="center",
        cursor="hand2",
        hover=False,
    )
    o_buttom = tk.CTkButton(
        menu,
        text="Play as O",
        font=("Arial", text_font_size),
        border_color=("black", "white"),
        border_width=5,
        fg_color=("black", "white"),
        text_color=("white", "black"),
        border_spacing=10,
        corner_radius=10,
        anchor="center",
        cursor="hand2",
        hover=False,
    )

    x_buttom.grid(row=2, column=0, sticky="n")
    o_buttom.grid(row=2, column=1, sticky="n")
