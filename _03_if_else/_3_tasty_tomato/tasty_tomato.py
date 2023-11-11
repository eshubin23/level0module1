from tkinter import *
import tkinter as tk
from tkinter import simpledialog, Tk

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
color = simpledialog.askstring(title= 'Tomato', prompt='what kind of tomato do you want out of red, green, yellow')

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if color== "red":
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="red")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="red")
if color== "green":
    canvas.create_oval(75, 200, 400, 450, fill="green", outline="green")
    canvas.create_oval(200, 200, 525, 450, fill="green", outline="green")
if color== "yellow":
    canvas.create_oval(75, 200, 400, 450, fill="yellow", outline="yellow")
    canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="yellow")

canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")

root.mainloop()
