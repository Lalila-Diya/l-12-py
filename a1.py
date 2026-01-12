import turtle
turtle.Screen().bgcolor("purple")
turtle.Screen().setup(500,500)
poly=turtle.Turtle()
side=6
len=100
a=360/side
for i in range(side):
    poly.forward(len)
    poly.right(a)

turtle.done()