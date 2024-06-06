import customtkinter as tk

window = tk.CTk()

width = int(window.winfo_screenwidth() * 0.3125)
height = int(window.winfo_screenheight() * 0.625)
scale_factor = (window.winfo_screenwidth() * window.winfo_screenheight()) / (
    2560 * 1600
)
text_font_size = 25 * scale_factor


window.geometry(f"600x400")
window.title("TicTacToe")

# Configure Columns
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# Confifure Rows
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=2)
window.rowconfigure(3, weight=1)


label = tk.CTkLabel(window, text="Play", font=("Arial", text_font_size))
label.grid(row=0, column=0, columnspan=2, sticky="nsew")

x_buttom = tk.CTkButton(
    window,
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
    hover=False
)
o_buttom = tk.CTkButton(
    window,
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
    hover=False
)

x_buttom.grid(row=2, column=0, sticky="n")
o_buttom.grid(row=2, column=1, sticky="n")

window.mainloop()
