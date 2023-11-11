# Write a Python program that asks the user for the radius of a circle.
import math
import turtle
from tkinter import simpledialog, Tk
w = Tk()
w.withdraw()

radius=simpledialog.askinteger(title='Radius',prompt='Enter a radius for a circle')
# Next, ask the user if they would like to calculate the area or circumference of a circle.
choice=simpledialog.askstring(title='Radius',prompt='do you want to calculate the area or circumference of the circle?')
# Display the area of the circle using the radius.
bob=turtle.Turtle()

bob.circle(radius = radius)
bob.penup()
bob.goto(50, 100)

if choice== "area":
    area=math.pi*(radius**2)

    bob.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
elif choice== "circumference":
    circumference=math.pi*2*radius

    bob.write(arg="circunference = " + str(circumference), move=True, align='left', font=('Arial',8,'normal'))
#Area = πr^2
w.mainloop()
