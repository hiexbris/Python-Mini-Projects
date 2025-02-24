import pandas
from turtle import *

writer = Turtle()
writer.penup()
writer.hideturtle()
screen = Screen()
bg_image = 'blank_states_img.gif'
screen.bgpic(bg_image)
t = 0
data = pandas.read_csv('50_states.csv')

while t < 50:
    input_state = screen.textinput(title='us states', prompt='tell a state name')

    for states in data.state:
        if input_state.lower() == states.lower():
            row = data[data.state == states]
            xcor = int(row.x)
            ycor = int(row.y)
            writer.goto(x=xcor, y=ycor)
            writer.write(f"{input_state}", align="center")
            t += 1

screen.exitonclick()
