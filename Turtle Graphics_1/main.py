import turtle as t
from random import randint
import colorgram
t.colormode(255)
turtle = t.Turtle()
colors = colorgram.extract(r"C:\Users\A-Team\Desktop\hirst-1.jpg", 20)
print(colors[0])


def random_color():
    color_1 = colors[randint(0,19)]
    return color_1.rgb


turtle.speed(1000)
turtle.right(225)
turtle.penup()
turtle.forward(400)
turtle.setheading(180)
turtle.forward(70)
turtle.setheading(0)


def one_line(dots):
    for _ in range(dots):
        turtle.dot(10, random_color())
        turtle.forward(22)
    turtle.right(90)
    turtle.forward(22)
    turtle.right(90)
    turtle.forward(22*dots)
    turtle.setheading(0)


for _ in range(27):
    one_line(33)

screen = t.Screen()
screen.exitonclick()

