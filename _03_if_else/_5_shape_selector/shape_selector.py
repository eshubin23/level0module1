import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    bob=turtle.Turtle()

    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title="Shapes",prompt="what shape do you want out of  triangle, square, or circle" )
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "circle":
        bob.circle(radius=100)
    elif shape == "triangle":
        bob.pendown()
        for i in range(3):
             bob.forward(100)
             bob.right(60)
    # Call the turtle .done() method
    window.mainloop()
