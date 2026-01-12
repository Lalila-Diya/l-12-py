#Spiral pattern
import turtle
wind=turtle.Screen()
wind.bgcolor("yellow")
p= turtle.Turtle()
s=0
while True: 
    for i in range(8):
        p.forward(s+1)
        p.left(45)
        s=s-5
    s=s+1