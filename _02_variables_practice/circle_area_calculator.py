import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    radius=simpledialog.askinteger(title='Radius',prompt='Enter a value for radius')
    # Make a new turtle
    bob=turtle.Turtle()

    bob.circle(radius = radius)
    bob.penup()

    bob.goto(50, 100)

    area=math.pi*(radius**2)

    bob.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    # Hide your turtle

    # Call turtle.done()
