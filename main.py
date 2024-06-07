import customtkinter as tk
from views.menu import Menu
from views.game import Game

window = tk.CTk()

width = int(window.winfo_screenwidth() * 0.3125)
height = int(window.winfo_screenheight() * 0.625)


window.geometry(f"600x400")
window.title("TicTacToe")

menu = Menu(window)
# game = Game(window, "X")


window.mainloop()
