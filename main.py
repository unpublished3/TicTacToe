import customtkinter as tk

window = tk.CTk()

width = int(window.winfo_screenwidth() * 0.3125)
height = int(window.winfo_screenheight() * 0.625)

window.geometry(f"{width}x{height}")
window.title("TicTacToe")

window.mainloop()