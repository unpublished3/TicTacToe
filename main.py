import customtkinter as tk
from views.menu import create_menu

window = tk.CTk()

width = int(window.winfo_screenwidth() * 0.3125)
height = int(window.winfo_screenheight() * 0.625)


window.geometry(f"600x400")
window.title("TicTacToe")
create_menu(window)

window.mainloop()
