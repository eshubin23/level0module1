# Write a Python program that asks the user for the radius of a circle.
from tkinter import simpledialog

radius=simpledialog.askinteger(title='Radius',prompt='Enter a radius for a circle')
# Next, ask the user if they would like to calculate the area or circumference of a circle.
messagebox=simpledialog.askinteger(title='Radius',prompt='do you want to calculate the area of the circle?')
# Display the area of the circle using the radius.
bob=turtle.Turtle()

    bob.circle(radius = radius)
    bob.penup()
    bob.goto(50, 100)
    area=math.pi*(radius**2)

    bob.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))

#Area = πr^2
